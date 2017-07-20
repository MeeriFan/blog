% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/login">
	<fieldset>
		<p>{{message}}</p>
		% if link:
			<br>
			<a href="/reactivate">{{link}}</a>
		% end
		<ul>
			<li>Email: <input type="email" name="email"></li>
			<li>Password: <input type="password" name="pw"></li>
		</ul>
		<input type="submit" name="Submit form">
	</fieldset>
</form>
<a href="/index">Back to mainpage</a>