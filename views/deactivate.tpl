% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/deactivate">
	<p>{{message}}</p>
	<input type="submit" name="deactivate" value="Yes">
	<a href="{{!current_user.path()}}">No</a>
</form>