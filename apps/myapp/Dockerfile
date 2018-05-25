FROM python:3.6
RUN pip install --upgrade pipenv

ARG APP=myapp

RUN mkdir /code
WORKDIR /code

COPY lib/python lib/python
COPY apps/$APP/Pipfile apps/$APP/Pipfile
COPY apps/$APP/Pipfile.lock apps/$APP/Pipfile.lock

WORKDIR /code/apps/$APP
# RUN python -m pipenv.help
RUN pipenv install --system --deploy
# --verbose

COPY apps/$APP .
