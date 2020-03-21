# disthw

Web server for **ONLINE STORE**. The project is created as homework at the course of distributed computing at HSE faculty of computer science.

Service architecture:
* Python Django - web framework.
* PostgreSQL - database.

Instruction for setting up server **WITH DOCKER COMPOSE**.

Run server with docker-compose `sudo docker-compose build && sudo docker-compose up`.

Instruction for setting up server **WITH LOCAL POSTGRESQL**.

1. Set environment variables DJANGO_PG_USER, DJANGO_PG_PASSWORD, DJANGO_PG_HOST, DJANGO_PG_PORT, DJANGO_SECRET_KEY or pass them to docker run command futher.

2. Run server with local (from another host) postgresql `sudo docker image build -t estore:1.0 -f estore/Dockerfile . && sudo docker run -d --network=host -p 8080:8080 disthw:1.0`. If you whant to connect to postgresql from another host remove `-d --network=host` option from `run` command.

**SWAGGER DOCS** - you can see doc by url `http://<IP>:<PORT>/docs/`.
