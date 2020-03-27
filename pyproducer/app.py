import uuid
import faust
from pyproducer.messages.stream_message import StreamMessage


# create your application. here we give it a name and broker. the other two
# arguments allow faust to find everything else neeeded
app = faust.App('pyproducer',
                broker='kafka://kafka-broker-1:19092',
                autodiscover=True,
                origin='pyproducer')


# this import seems weird, but we simply need to ensure that the agents (and
# topics) are loaded explicitly after our app is created. faust's autodiscovery
# takes care of the rest. in a more complex project this could be done more
# cleanly
from pyproducer.streams.agents import stream_in_topic  # noqa: E402, F401


# create a periodic task to send a message to the stream.in topic every 2
# seconds. message contains a randomly generated UUID for its ID.
@app.timer(interval=2.0)
async def producer_timer():
    value = StreamMessage(str(uuid.uuid4()), ['python-kafka-producer'])
    await stream_in_topic.send(value=value)


# used for a main entrypoint
def main() -> None:
    app.main()
