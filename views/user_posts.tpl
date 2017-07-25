% rebase('base.tpl')
<h2>All posts of {{user.username}}</h2>
% include('posts.tpl')
<br>
<br>
% from blog_classes import User
<a href="{{!User.index_path()}}">Back</a>