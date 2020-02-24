# disthw

Instruction for setting up server

1. Create `secdist.json` file with secrects of your app. Use `secdist_example.json` schema.
2.1 Run server with local (from another host) postgresql `sudo docker image build -t disthw:1.0 . && sudo docker run -d --network=host -p 8080:8080 disthw:1.0`. If you whant to connect to postgresql from another host remove `-d --network=host` option from `run` command.
2.2 Run server with docker-compose `sudo docker-compose build && sudo docker-compose up`.
