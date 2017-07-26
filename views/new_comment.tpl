<form action="{{!post.path()}}/comments" method="post">
	<fieldset>
		<legend>Leave a Comment</legend>
		<br>
		<textarea name="body" rows="10" cols="100"></textarea>
		<br>
		<input type="submit" name="save" value="Save">
	</fieldset>
</form>