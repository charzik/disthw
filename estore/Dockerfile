FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD estore/req.txt /app/
RUN pip install -r req.txt
ADD estore/ /app/
ADD tools/ /app/

CMD python run.sh
