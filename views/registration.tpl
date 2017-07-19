% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/registration">
	<fieldset>
	<p>{{message}}</p>
		<ul>
			<li>First name: <input type="text" name="first_name"></li>
			<li>Last name: <input type="text" name="last_name"></li>
			<li>Nickname: <input type="text" name="nickname"></li>
			<li>Email: <input type="email" name="email"></li>
			<li>Password: <input type="password" name="pw"></li>
		</ul>
		<input type="submit" name="registration">
	</fieldset>
</form>
<a href="/index">Back to mainpage</a>