% rebase('base.tpl')
% if not current_user:
% include('login_error.tpl')
% else:
<form action="{{!current_user.path()}}/newpost" method="post">
    <fieldset>
        <legend>New Post</legend>
        <label for="title">Title of your post: </label>
        <input id="title" type="text" name="title">
        <br>
        <br>
        <textarea name="body" rows="30" cols="100" placeholder="Please write your post here...."></textarea>
        <br>
        <input type="submit" name="save" value="Save">
    </fieldset>
</form>
% end