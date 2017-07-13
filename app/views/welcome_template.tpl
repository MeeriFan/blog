<html>
	<head>
	</head>
	<body>
		% if t_name == 'Stranger':
    		<h1>Hello {{t_name}}!</h1>
    		<p>This is a test.</p>
		% else:
    		<h1>Hello {{t_name.title()}}!</h1>
    		<p>How are you?</p>
		% end
	</body>
</html>