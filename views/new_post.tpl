% rebase('base.tpl')
<form action="/users/{{current_user.id}}/newpost" method="post">
    <fieldset>
        <legend>New Post</legend>
        Title: <input type="text" name="title" placeholder="Title of your post">
        <br>
        <br>
        <textarea rows="30" cols="100" placeholder="Please write your post here...."></textarea>
        <br>
        <input type="submit" name="save" value="Save">
    </fieldset>
</form>