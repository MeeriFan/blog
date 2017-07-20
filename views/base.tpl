<html>
	<head>
		<meta charset="utf-8">
		<title>Blog</title>

		<script type="application/javascript" src="/static/jquery.js"></script>
		<script type="application/javascript">
			$(document).ready(function() {
				$('#logout').click(function(e) {
					e.preventDefault(); // do not follow the actual href of the anchor tag

					$.post('/logout', function(data) {
						document.location.href = '/';
					});
				});
			});
		</script>
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
					<li><a id="logout" href="/logout">Logout</a></li>
				% end
				<li><a href="/users">Users</a></li>
			</ul>
		</nav>
		{{!base}}
	</body>
</html>