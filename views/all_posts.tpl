% rebase('base.tpl')
<h2>All posts of {{user.username}}</h2>
% include('post_loop.tpl')
<br>
<br>
<a href="/users">Back</a>