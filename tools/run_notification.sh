#!/usr/bin/env bash

celery worker -A notification --loglevel=info && python manage.py migrate && python manage.py runserver 0.0.0.0:8080