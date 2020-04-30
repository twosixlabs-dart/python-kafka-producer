import ssl
import faust
from pyproducer import config
from pyproducer.streams.agents import create_producer


app = None


def create_app():
    broker = None
    if config.get('broker'):
        broker = f'kafka://{config["broker"]}',

    broker_credentials = None
    if 'auth' in config:
        broker_credentials = faust.SASLCredentials(
            username=config['auth']['username'],
            password=config['auth']['password'],
            ssl_context=ssl.create_default_context()
        )

    # create your application
    global app
    app = faust.App(
        config['app']['id'],
        autodiscover=True,
        origin='pyproducer',
        broker=broker,
        broker_credentials=broker_credentials,
        topic_disable_leader=True
    )

    create_producer(app)

    return app


# used for a main entrypoint
def main() -> None:
    app.main()
