% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/deactivate">
	<p>{{message}}</p>
	<input type="submit" name="deactivate" value="Yes">
	<a href="/profile">No</a>
</form>