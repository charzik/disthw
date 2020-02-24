FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD req.txt /app/
RUN pip install -r req.txt
ADD . /app/

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8080