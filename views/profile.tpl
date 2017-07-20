%rebase('base.tpl')
<p>{{message}}</p>
<a href="/deactivate">Deactivate my profile</a>
<br>
<a href="/delete">Delete my Profile</a>
<br>
% if current_user:
	<form method="post" action="/profile">
		<textarea name='profile_text' rows="30" cols="100">
		% if current_user.profile_text == '':
Describe yourself....
			% else:
{{current_user.profile_text}}
			% end
		</textarea>
		<br>
		<input type="submit" name="submit" value="Save">
	</form>
% end
<a href="/delete">Delete my profile</a>
<a href="/index">Back to main page</a>