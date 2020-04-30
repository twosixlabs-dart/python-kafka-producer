import os
os.environ['PROGRAM_ARGS'] = 'test.json'
import warnings
import pytest
from pyproducer.app import create_app


app = create_app()


SAMPLE_MESSAGE = {"key": "test1", "value": ["python-kafka-producer"]}


@pytest.fixture()
def basic_stream_processor(event_loop):
    """passing in event_loop helps avoid 'attached to a different loop' error"""
    app.finalize()
    app.conf.store = 'memory://'
    app.flow_control.resume()
    return app


@pytest.mark.asyncio()
@pytest.mark.usefixtures('basic_stream_processor')
async def test_event_update(mocker, basic_stream_processor):
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    warnings.warn('THIS TEST DOES NOTHING. JUST A STUB')
    assert True
