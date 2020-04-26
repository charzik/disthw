FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD loader/req.txt /app/
RUN pip install -r req.txt
ADD loader/ /app/
ADD tools/ /app/

CMD ./run.sh
