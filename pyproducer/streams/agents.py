from pyproducer.app import app
from pyproducer.messages.stream_message import StreamMessage


stream_in_topic = app.topic('stream.in', value_type=StreamMessage)
