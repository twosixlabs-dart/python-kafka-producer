import warnings
import asynctest
import pytest
from pyproducer.app import app, producer_timer
from pyproducer.messages.stream_message import StreamMessage
from pyproducer.streams.agents import stream_in_topic


@pytest.fixture()
def basic_stream_processor(event_loop):
    """passing in event_loop helps avoid 'attached to a different loop' error"""
    app.finalize()
    app.conf.store = 'memory://'
    app.flow_control.resume()
    return app


@pytest.fixture()
def sample_messages(event_loop):
    sample_message_1 = StreamMessage(id='test1', breadcrumbs=[])
    sample_message_2 = StreamMessage(id='test1', breadcrumbs=['python-kafka-producer'])
    return {'empty': sample_message_1, 'full': sample_message_2}


@pytest.mark.asyncio()
@pytest.mark.usefixtures('basic_stream_processor', 'sample_messages')
async def test_event_update(mocker, basic_stream_processor, sample_messages):
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    assert True

