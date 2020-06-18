import ssl
import faust
from pyproducer import config
from pyproducer.streams.agents import create_producer


app = None


def create_app():
    broker = None
    if config.get('kafka.bootstrap.servers'):
        broker = f'kafka://{config["kafka.bootstrap.servers"]}',

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
        broker_credentials=broker_credentials
    )

    create_producer(app)

    return app


# used for a main entrypoint
def main() -> None:
    app.main()
