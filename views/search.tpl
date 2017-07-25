<form method="get" action="/search">
    <fieldset>
        <input type="text" name="q"><input type="submit" value="Search">
    </fieldset>
</form>
<a href="/index">Back to mainpage</a>
% if not word == '':
	% if len(posts) == 0:
		<p>We couldn't find any post containing your searchword. Please try again with a different word.</p>
	% else:
		% for post in posts:
    		<h3>{{post.title}}</h3>
    		<p>Author: {{post.user.username}}</p>
    		<p>Created at: {{post.nice_date()}}</p>
    		{{!post.get_abstract()}}<a href="/users/{{post.user.id}}/posts/{{post.id}}">...read more.</a>
    		<p>-----------------------------------------</p>
		% end
	% end
% end