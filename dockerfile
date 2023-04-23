FROM ubuntu:20.04

ENV TZ=UTC

RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get install -y python3.10

# RUN apt-get install python3.10-dev 




# RUN apt-get update && apt-get install -y python3.10 python3.10-dev

RUN apt-get -y install python3-pip
WORKDIR /app
COPY requirement.txt requirement.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirement.txt
RUN apt-get update

RUN python3 -m spacy download en_core_web_sm

RUN apt-get install wget


# RUN wget en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz


COPY . /app


EXPOSE 5000