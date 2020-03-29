FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD notification/req.txt /app/
RUN pip install -r req.txt
ADD notification/ /app/
ADD tools/ /app/

CMD run_notification.sh
