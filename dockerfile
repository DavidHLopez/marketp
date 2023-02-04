FROM alpine:3.16

RUN apk add --no-cache python3 py3-pip

WORKDIR /marketp

COPY . /marketp

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 3000

CMD [ "python3", "run.py" ]