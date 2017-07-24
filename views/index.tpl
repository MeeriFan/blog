% rebase('base.tpl')
<h2>All Posts</h2>
% for post in posts:
	<h3>{{post.title}}</h3>
	<p>Author: {{post.user.username}}</p>
    <p>Created at: {{post.created_at}}</p>
	{{!post.get_abstract()}}<a href="/users/{{post.user.id}}/posts/{{post.id}}">...read more.</a>
    <p>------------------------------------------------</p>
% end