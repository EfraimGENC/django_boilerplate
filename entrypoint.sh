#!/bin/sh
echo "ENTRYPOINT SCRIPT RAN ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "$DEBUG"
echo "$BUILD_ENV"
echo "$DJANGO_SETTINGS_MODULE"
echo "$APP_PORT"

python3 manage.py wait_for_db
python3 manage.py migrate

if [ "$BUILD_ENV" = "dev" ]
then
  python3 manage.py runserver 0.0.0.0:8000
else
  python3 manage.py collectstatic --no-input --clear --settings="${DJANGO_SETTINGS_MODULE}"
  gunicorn --bind 0.0.0.0:8000 src.asgi:application -k uvicorn.workers.UvicornWorker --log-level debug
fi
