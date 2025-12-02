import pytest
import logging
import pathlib

@pytest.fixture
def api_url():
    return "http://jsonplaceholder.typicode.com"


path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)

logging.basicConfig(filename=path_dir / 'historial.log', level=logging.INFO)
format='%(asctime)s %(levelname)s %(name)s – %(message)s',
datefmt='%H:%M:%S'
logger = logging.getLogger()

