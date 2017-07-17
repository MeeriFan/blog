<html>
	<head>
		<meta charset="utf-8">
		<title>Blog</title>
	</head>
	<body>
		<h1>Blog</h1>
		<nav>
			<ul>
				% if logged_in == 'no':
					<li><a href="/login">Login</a></li>
					<li><a href="/registration">Registration</a></li>
				% else:
					<li><a href="/profile">Your Profile</a></li>
					<li><a href="/logout">Logout</a></li>
				% end
			</ul>
		</nav>
		{{!base}}
	</body>
</html>