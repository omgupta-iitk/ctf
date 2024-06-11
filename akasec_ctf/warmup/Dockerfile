FROM ubuntu:latest

RUN apt-get update
RUN apt-get install socat -y

EXPOSE 1338

RUN useradd ctf

WORKDIR /chal
COPY warmup /chal
COPY flag.txt /chal

USER ctf

CMD ["socat", "127.0.0.1:1338,reuseaddr,fork", "EXEC:./warmup"]
