import os
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

import settings
from tests.webui.pages.base_page import BasePage
from tests.webui.pages.main_page import MainPage
from tests.webui.forms.order_form import OrderForm

logger = logging.getLogger('driver')
logging.basicConfig(level=logging.INFO, filename=os.getcwd() + r'\logs\run_logs.txt')


def pytest_addoption(parser):
    parser.addoption(
        '--page',
        default='main',
        choices=['main', 'package', 'internet', 'wink', 'mobile', 'video', 'phone']
    )
    parser.addoption(
        '--region',
        default=settings.REGIONS[settings.DEFAULT_REGION],
        type=int,
        choices=range(6)
    )


class MyListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.info('Navigate to {}'.format(url))

    def after_navigate_to(self, url, driver):
        logging.info('The current URL is {}'.format(url))

    def before_quit(self, driver):
        logging.info('Browser is ready to quit {}'.format(driver))


@pytest.fixture(scope='session')
def get_page(request):
    return request.config.getoption('--page')


@pytest.fixture(scope='session')
def get_region(request):
    return request.config.getoption('--region')


@pytest.fixture(scope='session')
def driver(get_page, get_region):
    base_url = 'https://{}.rt.ru'.format(settings.REGIONS[get_region])
    logger.info('Start test')
    caps = DesiredCapabilities.CHROME
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    options.add_experimental_option('w3c', False)
    caps['loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL'}
    wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=caps,
                                               options=options), MyListener())
    if get_page == 'package':
        wd.get(url='{}/packages/tariffs'.format(base_url))
    elif get_page == 'internet':
        wd.get(url='{}]/homeinternet/order_internet'.format(base_url))
    elif get_page == 'wink':
        wd.get(url='{}/hometv'.format(base_url))
    elif get_page == 'mobile':
        wd.get(url='{}/mobile/mobile_tariff'.format(base_url))
    elif get_page == 'video':
        wd.get(url='{}/videocontrol'.format(base_url))
    elif get_page == 'phone':
        wd.get(url='{}/hometel'.format(base_url))
    else:
        wd.get(base_url)

    def driver_quit():
        wd.quit()
        logger.info('Chrome browser driver quit')
        logger.info('End test')

    # request.addfinalizer(driver_quit())
    return wd


@pytest.fixture(scope='session')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='session')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='session')
def order_form(driver):
    return OrderForm(driver)
