% rebase('base.tpl')
<h2>All Posts</h2>
% if len(posts) == 0:
	% if not current_user:
		<p>There are no posts so far. Be the first <a href="/registration">one</a>!</p>
	% else:
		<p>There are no posts so far. Be the first <a href="{{!current_user.path()}}/newpost">one</a>!</p>
	% end
% else:
	% for post in posts:
		<h3>{{post.title}}</h3>
		<p>Author: {{post.user.username}}</p>
    	<p>Created at: {{post.created_at}}</p>
		{{!post.get_abstract()}}<a href="{{!post.path()}}">...read more.</a>
    	<p>------------------------------------------------</p>
	% end
% end