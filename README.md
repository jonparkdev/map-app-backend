## Set Up

After cloning the repo, in your terminal (NOTE - I am using virtualenv for my python virtual env):

```bash
$ cd map-app-backend
$ virtualenv --python=python3 venv
```

### POSTGRES configuration

Create your own congifuratiolsn or copy the one that is in settings.py. Either option you will need to go about the option
of creating a db and user with permissions.

Installing postgreSQL
```bash
$ sudo apt-get install libpq-dev python-dev
$ sudo apt-get install postgresql postgresql-contrib
```

```bash
$ sudo -i -u postgres
```

```bash
postgres@server~$ createdb mydb
postgres@server~$ psql
```

```bash
$ CREATE ROLE username NOINHERIT LOGIN PASSWORD 'password';
$ GRANT ALL PRIVILEGES ON DATABASE mydb TO username;
$ \q
```

Go back to bash shell

Let's get the server running
```bash
$ source ./venv/bin/activate # activate virtual env
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

The server should be up and running on localhost:8000
