% rebase('base.tpl')
<h2>{{post.title}}</h2>
<p>Author: {{post.user.username}}</p>
<p>created at: {{!post.nice_date()}}</p>
{{!post.render_body()}}
<br>
<% 	
if current_user:
	include('new_comment.tpl')
end
if len(post.comments) !=0:
	include('comments.tpl')
end
%>
<a href="/">Back to mainpage</a>