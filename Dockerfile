FROM lnk2past/centos-python3:latest

LABEL maintainer="nicholas.sanchirico@twosixlabs.com"

USER root

ADD requirements.txt /

RUN python -m pip install -r requirements.txt

ADD pyproducer /pyproducer

ENTRYPOINT python -m pyproducer worker -l info
