#!/usr/bin/env bash

set -e
set -u

celery worker -A $CELERY_SERVICE_NAME --loglevel=info