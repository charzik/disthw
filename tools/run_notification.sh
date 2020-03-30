#!/usr/bin/env bash

python manage.py migrate && python manage.py runserver 0.0.0.0:8080 && celery worker -A notification --loglevel=info
