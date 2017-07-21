% if len(posts) == 0:
	<p>Write your first <a href="/users/{{current_user.id}}/newpost">post.</a></p>
% else:
	% for post in posts:
		<h3>{{post.title}}</h3>
		% if current_user.id != post.user.id:
			<p>Author: {{post.user.username}}</p>
		% end	
		<p>Created at: {{post.created_at}}</p>
		<p>{{post.body}}</p>
	% end
% end