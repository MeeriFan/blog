% rebase('base.tpl')
<h2>{{post.title}}</h2>
<p>Author: {{post.user.username}}		created at: {{post.nice_date()}}</p>
{{!post.render_body()}}
<br>
<a href="/">Back to mainpage</a>