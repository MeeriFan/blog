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
				<li><a href="/">Mainpage</a></li>
				% if not current_user:
					<li><a href="/login">Login</a></li>
					<li><a href="/registration">Registration</a></li>
				% else:
					<li><a href="{{!current_user.path()}}/newpost">Write a new Post</a></li>
					<li><a href="{{!current_user.path()}}">Your Profile</a></li>
					<li><a id="logout" href="/logout">Logout</a></li>
				% end
				<li><a href="{{!User.index_path()}}">Users</a></li>
			</ul>
			% include('search.tpl', search_term='')
		</nav>
		{{!base}}
	</body>
</html>