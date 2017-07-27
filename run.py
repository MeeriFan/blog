from bottle import template, Bottle, debug, run, request, response
from bottle import redirect, static_file
from uuid import uuid4
from blog_classes import User, Post, Comment
from datetime import datetime

app = Bottle()


def set_app_cookie(user_id):
    key = uuid4().hex
    response.set_cookie('session_id', key, secret=SECRET)
    session_dict[key] = user_id


def delete_app_cookie(deactivate_user=False):
    session_key = get_key()
    if deactivate_user:
        User.deactivate_user(session_dict[session_key])
    del session_dict[session_key]
    response.delete_cookie('session_id', secret=SECRET)


def get_key():
    return request.get_cookie('session_id', secret=SECRET)


def logged_in():
    session_key = get_key()
    if session_key:
        return User.get_by_id(session_dict[session_key])
    return None


@app.route('/')
@app.route('/index')
def index():
    info = {
        'current_user': logged_in(),
        'posts': Post.select().order_by(Post.created_at.desc())
    }
    return template('index.tpl', info)


session_dict = {}

SECRET = 'dogcatmouse'


@app.route('/users/<username>/editprofile')
def edit_profile(username):
    current_user = logged_in()
    if not current_user:
        info = {
            'message': 'You must be logged in.',
            'current_user': current_user,
            'href': 'index'
        }
        return template('error.tpl', info)
    else:
        info = {
            'current_user': current_user,
            'profile_text': current_user.profile_text
        }
        return template('edit_profile.tpl', info)


@app.post('/users/<username>/editprofile')
def save_profile_description(username):
    current_user = logged_in()
    current_user.save_profile_text(request.forms.profile_text)
    return redirect(current_user.path())


@app.route('/users')
def list_users():
    list_users = User.get_all()
    info = {
        'title': 'List of all Users',
        'current_user': logged_in(),
        'users': list_users
    }
    return template('users.tpl', info)


@app.route('/users/<username>')
def specific_user(username):
    user = User.slug(username)
    current_user = logged_in()
    if current_user and current_user.id == user.id:
        message = 'Hello ' + current_user.first_name + ' ' \
                            + current_user.last_name + '!'
        info = {
            'title': message,
            'current_user': current_user,
            'posts': current_user.posts.order_by(Post.created_at.desc()),
            'user': current_user
        }
        return template('profile.tpl', info)
    else:
        info = {
            'user': user,
            'title': 'Profile of %s' % user.username,
            'current_user': current_user,
            'posts': user.posts.order_by(Post.created_at.desc())
        }
        return template('profile.tpl', info)


@app.route('/login')
def login_form():
    info = {
        'title': 'Login',
        'message': 'Please log in.',
        'current_user': logged_in()
    }
    return template('login.tpl', info)


@app.route('/login/failed')
def login_form_failed():
    info = {
        'title': 'Login',
        'message': 'Login failed. Please try again.',
        'current_user': logged_in()
    }
    return template('login.tpl', info)


@app.post('/login')
@app.post('/login/failed')
def do_login():
    # TO DO allow username or email for registration
    user_input = request.forms.get('verification')
    user = User(password=request.forms.get('pw'))
    if '@' in user_input:
        user.email = user_input
    else:
        user.username = user_input
    if user.verify_login():
        if user.email != '':
            user = User.by_email(user.email)
        elif user.username != '':
            user = User.slug(user.username)
        set_app_cookie(user.id)
        return redirect(user.path())
    else:
        return redirect('/login/failed')


@app.post('/logout')
def do_logout():
    delete_app_cookie()
    return redirect('/')


@app.route('/registration')
def registration(message='Please fill out the form completely for \
                registration.', user=User()):
    info = {
        'title': 'Registration',
        'message': message,
        'current_user': logged_in(),
        'u_f_name': user.first_name,
        'u_l_name': user.last_name,
        'u_name': user.username,
        'u_email': user.email
    }
    return template('registration.tpl', info)


@app.post('/registration')
def do_registration():
    new_user = User(
        username=request.forms.get('nickname'),
        email=request.forms.get('email'),
        first_name=request.forms.get('first_name'),
        last_name=request.forms.get('last_name'),
        password=request.forms.get('pw')
    )
    if not new_user.is_already_in_db():
        repeated_password = request.forms.get('r_pw')
        valid, error = new_user.is_valid(repeated_password)
        if valid:
            new_user.generate_salt()
            new_user.password = new_user.hash_password()
            new_user.save()
            set_app_cookie(new_user.id)
            info = {
                'f_name': new_user.first_name,
                'l_name': new_user.last_name,
                'current_user': new_user,
                'message': 'Thank you for registrating to this microblog!'
            }
            return template('thank_you.tpl', info)
        else:
            return registration(message=error, user=new_user)
    else:
        info = {
            'message': 'You are already registered.',
            'href': 'registration',
            'current_user': logged_in()
        }
        return template('error.tpl', info)


@app.route('/deactivate')
def deactivate_user():
    info = {
        'title': 'Good Bye?',
        'message': 'You really want to deactivate you profile? This means you \
        have to register again to reactivate your profile. \
        All your data will be kept.',
        'current_user': logged_in()
    }
    return template('deactivate.tpl', info)


@app.post('/deactivate')
def do_deactivate():
    delete_app_cookie(deactivate_user=True)
    info = {
        'current_user': logged_in(),
        'specification': 'deactivated'
    }
    return template('sorry.tpl', info)


@app.route('/users/<username>/delete')
def delete_account(username):
    info = {
        'title': 'Good Bye?',
        'message': 'You really want to delete your account? This means that your \
        whole profile will be deleted and there is no way back. Are you sure? \
        You should consider to deactivate your profile',
        'current_user': logged_in()
    }
    return template('delete.tpl', info)


@app.post('/users/<username>/delete')
def do_delete(username):
    User.delete_user(username)
    delete_app_cookie()
    info = {
        'current_user': logged_in(),
        'specification': 'deleted'
    }
    return template('sorry.tpl', info)


@app.route('/users/<username>/newpost')
def new_post(username):
    current_user = logged_in()
    return template('new_post.tpl', current_user=current_user)


@app.post('/users/<username>/newpost')
def save_post(username):
    current_user = logged_in()
    new_post = Post(
        title=request.forms.title,
        body=request.forms.body,
        user=current_user,
        created_at=datetime.now()
    )
    new_post.save()
    return redirect(current_user.path())


@app.route('/users/<username>/posts')
def user_posts(username):
    user = User.slug(username)
    info = {
        'current_user': logged_in(),
        'user': user,
        'posts': user.posts.order_by(Post.created_at.desc())
    }
    return template('user_posts.tpl', info)


@app.route('/users/<username>/posts/<post_id:int>')
def one_post(username, post_id):
    # Using title instead of post id?
    info = {
        'current_user': logged_in(),
        'post': Post.get_post(post_id)
    }
    return template('single_post.tpl', info)


@app.post('/users/<username>/posts/<post_id:int>/comments')
def save_comment(username, post_id):
    new_comment = Comment(
        body=request.forms.body,
        created_at=datetime.now(),
        user=logged_in(),
        post=Post.get_post(post_id)
    )
    new_comment.save()
    return redirect('/users/%s/posts/%d' % (username, post_id))


@app.route('/search')
def search_post():
    searchword = request.query.q
    info = {
        'current_user': logged_in(),
        'posts': Post.matching_posts(searchword),
        'search_term': searchword
    }
    return template('search.tpl', info)


@app.route('/static/<path:path>')
def static_files(path):
    return static_file(path, 'static/')

if __name__ == '__main__':
    debug(True)
    run(app, host='localhost', port=8080, reloader=True)
