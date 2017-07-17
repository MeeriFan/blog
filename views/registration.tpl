% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/registration">
	<fieldset>
	<p>{{message}}</p>
		<ul>
			<li>First name: <input type="text" name="first_name" value="{{u_f_name}}"></li>
			<li>Last name: <input type="text" name="last_name" value="{{u_l_name}}"></li>
			<li>Nickname: <input type="text" name="nickname" value="{{u_name}}"></li>
			<li>Email: <input type="email" name="email" value="{{u_email}}"></li>
			<li>Password: <input type="password" name="pw" value="{{u_pw}}"></li>
			<li>Repeat password: <input type="password" name="r_pw" value="{{u_pw_r}}"></li>
		</ul>
		<input type="submit" name="registration">
	</fieldset>
</form>
<a href="/index">Back to mainpage</a>