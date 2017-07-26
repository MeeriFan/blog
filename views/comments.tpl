<h4>Comments</h4>
% for comment in post.comments:
	<p>Author: {{comment.user.username}}</p>
	<p>Created at: {{!comment.nice_date()}}</p>
	{{!comment.render_body()}}
	<p>-------------------------------</p>
% end