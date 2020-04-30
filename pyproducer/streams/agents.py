import uuid
from pyproducer import config


def create_producer(app):
    # create topics
    stream_in_topic = app.topic(config['topic']['to'], key_type=str, value_type=str)

    # create a periodic task to send a message to the stream.in topic every 2
    # seconds. message contains a randomly generated UUID for its ID.
    @app.timer(interval=2.0)
    async def producer_timer():
        await stream_in_topic.send(key=str(uuid.uuid4()), value={'key': str(uuid.uuid4()), 'value': ['python-kafka-producer']})
