<html>
	<head>
	</head>
	<body>
		<h1>{{title}}</h1>
		% if t_name == 'Stranger':
    		<h2>Hello {{t_name}}!</h2>
		% else:
    		<h2>Hello {{t_name.title()}}!</h2>
    		<p>How are you, today?</p>
		% end
		<div>
			% for post in posts:
			<p>{{post['author']}} says: 
			<b></b>
			{{post['body']}}</p>	
			% end		
		</div>
	</body>
</html>