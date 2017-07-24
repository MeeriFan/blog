%rebase('base.tpl')
<h2>{{title}}</h2>
<br>
% if current_user == user:
    <a href="/delete">Delete my profile</a>
    <br>
    <a href="/users/{{current_user.id}}/editprofile">Edit my Profiletext</a>
    <br>
    <h5>What I say about myself:</h5>
    % if current_user.profile_text == '':
        <p>Describe <a href="/users/{{current_user.id}}/editprofile">yourself</a>.</p>
    % else:
        <p>{{current_user.profile_text}}</p>
    % end
    <h5>My Posts:</h5>
% else:
    <h5>What I can tell you about myself:</h5>
    % if user.profile_text == '':
        <p>{{user.username}} can't tell you anything...</p>
    % else:
        <p>{{user.profile_text}}</p>      
    % end
    <h5>{{user.username}}'s Posts</h5>  
% end

% if len(posts) == 0:
    % if current_user == user:
        <p><p>Write your first <a href="/users/{{current_user.id}}/newpost">post.</a></p></p>
    % else:
        <p>{{user.username}} didn't post anything, yet.</p>
    % end
% else:
    % for post in posts:
        <h3>{{post.title}}</h3>
        <p>Created at: {{post.created_at}}</p>
        {{!post.render_body()}}
    % end
% end
<a href="/index">Back to main page</a>


