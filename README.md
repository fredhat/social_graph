# Django Social Graph API

A simple Django Python-based social graph api for representing follower connections between users.

## Duplicating My Dev Environment

Clone this repository to an empty directory of your choice and cd to the project root.

Execute the following commands to install dependencies and migrate the database:

```
pip install django

pip install djangorestframework

python manage.py makemigrations

python manage.py migrate
```

Execute the following commands to run a local dev server hosting the Social Graph API:

```
python manage.py runserver
```

Execute the following commands to create a superuser cappable of logging into Django's admin console:

```
python manage.py createsuperuser
```

### Available Endpoints

The following API endpoints can be accessed while the dev server is running:

```
127.0.0.1:8000/admin/

Allows access to Django's admin console, which provides tools for examining and updating the database.
```

```
127.0.0.1:8000/api/users/

GET: Returns a json formatted list of all the users in the database.
Returns a HTTP_200_OK status.

POST: Creates a new user in the database. Consumes a json string such as:
{
	"name":"{insert_name}",
	"username":"{insert_username}"
}
Returns a HTTP_200_OK status and a user object json on success.
Returns a HTTP_422_UNPROCESSABLE_ENTITY error on failure due to malformed json or non-unique user name.
```

```
127.0.0.1:8000/api/users/{user_id}/
{user_id} = target user's primary key

GET: Returns the specified json formatted user from the database.
Returns a HTTP_200_OK status on success.
Returns an HTTP_404_NOT_FOUND status on not finding the specified user.
```

```
127.0.0.1:8000/api/users/{user_id}/followers/
{user_id} = target user's primary key

GET: Returns a json formatted list of all the users in the database following the specified user.
Can return an empty json formatted list.
Returns a HTTP_200_OK status on success.
Returns an HTTP_404_NOT_FOUND status on not finding the specified user.
```

```
127.0.0.1:8000/api/users/{user_id}/follow/{target_user_id}
{user_id} = target user's primary key
{target_user_id} = target user to follow's primary key

POST: Makes the target user follow another target user.
Returns a HTTP_200_OK status on success.
Returns an HTTP_404_NOT_FOUND status on not finding either specified user.
Returns a HTTP_422_UNPROCESSABLE_ENTITY error on failure due to an existing follows relationship.
```

```
127.0.0.1:8000/api/users/{user_id}/unfollow/{target_user_id}
{user_id} = target user's primary key
{target_user_id} = target user to unfollow's primary key

POST: Makes the target user unfollow another target user.
Returns a HTTP_200_OK status on success.
Returns an HTTP_404_NOT_FOUND status on not finding either specified user.
Returns a HTTP_422_UNPROCESSABLE_ENTITY error on failure due to not finding an existing follows relationship.
Note: Also returns a HTTP_422_UNPROCESSABLE_ENTITY error if user_id = target_user_id.
```