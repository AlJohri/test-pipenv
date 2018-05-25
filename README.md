# test-pipenv

Note how Step 10/11 of the build below has `--system` in there but it still says `Creating a virtualenv for this project…`.

```
$ cd apps/myapp
$ docker-compose up --build

Building app
Step 1/11 : FROM python:3.6
 ---> d69bc9d9b016
Step 2/11 : RUN pip install --upgrade pipenv
 ---> Using cache
 ---> 5e5c5f3ae5b7
Step 3/11 : ARG APP=myapp
 ---> Using cache
 ---> 16e255bbaa20
Step 4/11 : RUN mkdir /code
 ---> Using cache
 ---> 12995844cedc
Step 5/11 : WORKDIR /code
 ---> Using cache
 ---> 7b793b5e959d
Step 6/11 : COPY lib/python lib/python
 ---> Using cache
 ---> 416dba984876
Step 7/11 : COPY apps/$APP/Pipfile apps/$APP/Pipfile
 ---> Using cache
 ---> f8cc7a81de9d
Step 8/11 : COPY apps/$APP/Pipfile.lock apps/$APP/Pipfile.lock
 ---> Using cache
 ---> 9c32d392d2af
Step 9/11 : WORKDIR /code/apps/$APP
 ---> Using cache
 ---> a608dc0b7b0f
Step 10/11 : RUN pipenv install --system --deploy
 ---> Running in 3a39e00a895e
Installing -e ../../lib/python…
Looking in indexes: https://pypi.python.org/simple
Obtaining file:///code/lib/python
Installing collected packages: mypackage
  Running setup.py develop for mypackage
Successfully installed mypackage

Adding -e ../../lib/python to Pipfile's [packages]…
Installing -e ./../../lib/python…
Looking in indexes: https://pypi.python.org/simple
Obtaining file:///code/lib/python
Installing collected packages: mypackage
  Found existing installation: mypackage 0.0.1
    Uninstalling mypackage-0.0.1:
      Successfully uninstalled mypackage-0.0.1
  Running setup.py develop for mypackage
Successfully installed mypackage

Adding -e ./../../lib/python to Pipfile's [packages]…
Creating a virtualenv for this project…
Using /usr/local/bin/python (3.6.5) to create virtualenv…
Already using interpreter /usr/local/bin/python
Using base prefix '/usr/local'
New python executable in /root/.local/share/virtualenvs/myapp-HQwuOUlF/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /root/.local/share/virtualenvs/myapp-HQwuOUlF
Installing dependencies from Pipfile.lock (e81229)…
Removing intermediate container 3a39e00a895e
 ---> f858a6730b49
Step 11/11 : COPY apps/$APP .
 ---> e78cdd2b1d2f
Successfully built e78cdd2b1d2f
Successfully tagged myapp_app:latest
Recreating myapp_app_1 ... done
Attaching to myapp_app_1
app_1  |  * Serving Flask app "app" (lazy loading)
app_1  |  * Environment: production
app_1  |    WARNING: Do not use the development server in a production environment.
app_1  |    Use a production WSGI server instead.
app_1  |  * Debug mode: on
app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
app_1  |  * Restarting with stat
app_1  |  * Debugger is active!
app_1  |  * Debugger PIN: 139-845-864
```