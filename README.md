# python-kafka-producer

[![Build Status](https://github.com/twosixlabs-dart/python-kafka-producer/workflows/Build/badge.svg)](https://github.com/twosixlabs-dart/python-kafka-producer/actions)

## What Is This?

This project is a part of a collection of Python examples for working with kafka Streams via the [`Faust`](https://faust.readthedocs.io) library. This particular project contains a simple producer implementation. The full suite of projects are the following:

- [Producer](https://github.com/twosixlabs-dart/python-kafka-producer) (this project)
- [Stream Processor](https://github.com/twosixlabs-dart/python-kafka-streams)
- [Consumer](https://github.com/twosixlabs-dart/python-kafka-consumer)
- [Environment](https://github.com/twosixlabs-dart/kafka-examples-docker)

The *producer* in this example is a task that publishes to some topic on a periodic. That is it!

## Getting Started

Getting started with this example requires a complete Kafka environment. [This project](https://github.com/twosixlabs-dart/kafka-examples-docker) contains a docker-compose file for setting up everything. You can use the configuration inputs to connect to a preexisting infrastructure if you have one already.

If you do not have a Python installation ready, you can configure the input and then build the Dockerfile and run the resulting image with:

```shell
docker build -t python-kafka-producer-local .
docker run --env PROGRAM_ARGS=wm-sasl-example -it python-kafka-producer-local:latest 
```


### Configuration File & SASL/SSL

The code here is configured to use JSON resources found at the subpackage `pyproducer.resources.env`. Your configuration must be found within the [pyproducer/resources/env](pyproducer/resources/env) directory. When specifying your own you may omit the `.json` extension; it will attempt to load it as it and if that fails will attempt to load it assuming a `.json` extension. The default is to point to the [wm-sasl-example](/pyproducer/resources/env/wm-sasl-example.json) configuration (which contains mostly nothing). Here is the expected format of the input file:

```json
{
    "broker": "",
    "auth": {
        "username": "",
        "password": ""
    },
    "app": {
        "id": ""
    },
    "topic": {
        "to": ""
    },
}
```

* `broker` - the hostname + port of the Kafka broker
* `auth`
  * `username` - username for SASL authentication
  * `password` - password for SASL authentication
* `app`
  * `id` - unique identifier for your application/group
* `topic`
  * `to` - topic to publish to; currently only a single topic may be specified

These options are subject to change/refinement, and others may be introduced in the future.
