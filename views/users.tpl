% rebase('base.tpl')
<h2>{{title}}</h2>
% if len(users) == 0:
	<p>There are no users registered to this blog.</p>
	<p><a href="/registration">Be the first one!</a></p>
% else:
	<table>
		<tr>
			<th>Firstname</th>
			<th>Lastname</th>
			<th>Link to Profile</th>
		</tr>
		% for user in users:
			<tr>
				<td>{{user.first_name}}</td>
				<td>{{user.last_name}}</td>
				<td><a href="/users/{{user.id}}">{{user.username}}'s Profile</a></td>
			</tr>
		% end
	</table>
% end