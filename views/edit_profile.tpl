% rebase('base.tpl')
% if not current_user:
% include('login_error.tpl')
% else:
<form action="/users/{{current_user.id}}/editprofile" method="post">
    <fieldset>
        <legend>My Profile Description</legend>
        <textarea name="profile_text" rows="30" cols="100">{{profile_text}}</textarea>
        <br>
        <input type="submit" name="save" value="Save">
    </fieldset>
</form>
% end