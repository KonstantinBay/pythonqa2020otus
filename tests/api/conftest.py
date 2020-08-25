import os
import logging
import pytest

import settings
from tests.api.clients.base_client import APIClient

logger = logging.getLogger('api')
logging.basicConfig(level=logging.INFO, filename=os.getcwd() + r'\logs\run_logs.txt')


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://{}.rt.ru'.format(settings.REGIONS[settings.DEFAULT_REGION]),
        help='request url, default - "https://{}.rt.ru"'.format(settings.REGIONS[settings.DEFAULT_REGION])
    )
    parser.addoption(
        '--base_path',
        default='{}'.format(settings.REQUEST_PATH),
        help='api request base path, default - "{}"'.format(settings.REQUEST_PATH)
    )
    parser.addoption(
        '--status_code',
        default=200,
        choices=[200, 400, 404, 500, 502, 503, 504],
        # для числовых значений нужно указывать type int, т.к по умолчанию string
        type=int,
        help='request status code, default - 200'
    )


@pytest.fixture(scope='session')
def get_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def get_path(request):
    return request.config.getoption('--base_path')


@pytest.fixture
def get_status_code(request, get_url):
    return request.config.getoption('--status_code')


@pytest.fixture(scope="session")
def api_client(get_path):
    return APIClient(base_path=get_path)
