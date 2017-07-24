% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/delete">
	<p>{{message}}</p>
	<input type="submit" name="delete" value="Yes">
	<a href="/users/{{current_user.id}}">No</a>
</form>