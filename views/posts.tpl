% if len(posts) == 0:
    % if current_user == user:
        <p><p>Write your first <a href="{{!current_user.path()}}/newpost">post.</a></p></p>
    % else:
        <p>{{user.username}} didn't post anything, yet.</p>
    % end
% else:
    % for post in posts:
        <h3>{{post.title}}</h3>
        <p>Created at: {{post.nice_date()}}</p>
        {{!post.get_abstract()}}<a href="{{!post.detail_path()}}">...read more.</a>
    % end
% end