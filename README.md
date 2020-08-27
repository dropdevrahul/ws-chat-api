# A django project which uses `django-channels` to support websocket connections.

## Intro
A default user is also provided for token based authorization using django-rest-framework present in the
   "user_app" app. So instead of usign django's default User class we will use this ApiUser class.


Default url for login is which uses a default POST request which you are free to override:

    /api/login/

which returns the username and token for the user.

Once we have the token we can add the following header to requests to auth:

    Authorization: "token {newly_generated_token}"

Replace the newly_generated_token with your token


### Running the project

Run this command

```
./setup.bash
```
