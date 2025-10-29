# How to start the development server
1. If it is the first time, copy blog_api/config.py.example and rename it to config.py. Update the settings in config.py to actual values.
2. In windows, `set FLASK_ENV=development`


# How to run development server
# TODO dockerize this application both frontend and backend
flask --app blog_api run --debug


# Datebase update
## Revision
`alembic revision --autogenerate -m "some comments"`

## Migrate
`alembic upgrade head`


## Docker
