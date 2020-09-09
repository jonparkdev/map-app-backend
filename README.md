## Set Up

After cloning the repo, in your terminal (NOTE - I am using virtualenv for my python virtual env):

```bash
$ cd map-app-backend
$ virtualenv --python=python3 venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

## POSTGRES configuration

Create your own congifuration or copy the one that is in settings.py. Either option you will need to go about the option
of creating a db and user with permissions.

(assuming postgres is installed)
```bash
$ sudo -i -u postgres
```
```bash
postgres@server~$ createuser --interactive
postgres@server~$ createdb mydb
postgres@server~$ psql
```
```bash
$ CREATE ROLE username NOINHERIT LOGIN PASSWORD password;
$ GRANT ALL PRIVILEGES ON DATABASE mydb TO username;
```

Let's get the server running
```bash
$ python manage.py migrate
$ python manage.py runserver
```

The server should be up and running on localhost:8000
