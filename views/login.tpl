% rebase('base.tpl')
<h1>{{title}}</h1>
<form method="post" action="/login">
	<fieldset>
		<legend>
			LOGIN
		</legend>
		<p>{{message}}</p>
		<ul>
			<li>Email: <input type="email" name="email"></li>
			<li>Password: <input type="password" name="pw"></li>
		</ul>
		<input type="submit" name="Submit form">
	</fieldset>
</form>