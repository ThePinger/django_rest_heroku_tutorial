release: export DEVELOPMENT=True
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn django_rest_heroku_tutorial.wsgi