#!/usr/bin/env bash

set -e

cmd="$@"

RETRIES=5
until psql -h $DJANGO_PG_HOST -U $DJANGO_PG_USER -d $WAIT_PG_DB -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

