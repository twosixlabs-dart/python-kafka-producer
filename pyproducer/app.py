import uuid
import faust
from pyproducer.messages.stream_message import StreamMessage


app = faust.App('pyproducer',
                broker='kafka://kafka-broker-1:19092',
                autodiscover=True,
                origin='pyproducer')


from pyproducer.streams.agents import stream_in_topic


@app.timer(interval=2.0)
async def producer_timer():
    value = StreamMessage(str(uuid.uuid4()), ['python-kafka-producer'])
    await stream_in_topic.send(value=value)


def main() -> None:
    app.main()
