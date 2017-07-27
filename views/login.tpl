% rebase('base.tpl')
<h2>{{title}}</h2>
<form method="post" action="/login">
    <fieldset>
        <p>{{message}}</p>
        <ul>
            <li>Email or Username: <input type="text" name="username_or_email"></li>
            <li>Password: <input type="password" name="pw"></li>
        </ul>
        <input type="submit" name="Submit form">
    </fieldset>
</form>
<a href="/index">Back to mainpage</a>