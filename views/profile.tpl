%rebase('base.tpl')
<h2>{{title}}</h2>
<br>
% if current_user == user:
    <a href="{{!current_user.path()}}/delete">Delete my profile</a>
    <br>
    <a href="{{!current_user.path()}}/editprofile">Edit my Profiletext</a>
    <br>
    <h5>What I say about myself:</h5>
    % if current_user.profile_text == '':
        <p>Describe <a href="{{!current_user.path()}}/editprofile">yourself</a>.</p>
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

% include('posts.tpl')
<br>
<br>
<a href="{{!User.index_path()}}">Back</a>


