<html>
	<head>
	</head>
	<body>
		<h1>{{title}}</h1>
		% if t_name == 'Stranger':
    		<h2>Hello {{t_name}}!</h2>
    		<p>This is a test.</p>
		% else:
    		<h2>Hello {{t_name.title()}}!</h2>
    		<p>How are you, today?</p>
		% end
	</body>
</html>