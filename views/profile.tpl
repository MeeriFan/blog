%rebase('base.tpl')
<p>{{message}}</p>
% if current_user:
	<form method="post" action="/profile">
		<textarea placeholder="Describe yourself..." name='profile_text' rows="30" cols="100">
% if not current_user.profile_text == '':
{{current_user.profile_text}}
% end
</textarea>
		<br>
		<input type="submit" name="submit" value="Save">
	</form>
% end
<a href="/delete">Delete my profile</a>
<br>
<a href="/index">Back to main page</a>
<br>
% if current_user:
    <h2>List of your posts</h2>
    % include('user_posts.tpl')
% end