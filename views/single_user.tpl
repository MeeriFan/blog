% rebase('base.tpl')
<h2>{{title}}</h2>
<p>Hi! I am {{user.first_name}} {{user.last_name}}.</p>
<p>What I can tell you about myself:</p>
<p>{{user.profile_text}}</p>
<h2>{{user.username}}'s posts</h2>
% if len(posts) == 0:
	<p>{{user.username}} didn't post anything, yet.</p>
% else:
	% for post in posts:
		<h3>{{post.title}}</h3>
		<p>Created at: {{post.created_at}}</p>
		<p>{{post.body}}</p>
	% end
% end

