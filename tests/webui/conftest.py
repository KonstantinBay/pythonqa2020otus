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
        logging.info(f"Navigate to {url}")

    def after_navigate_to(self, url, driver):
        logging.info(f"The current URL is {url}")

    def before_quit(self, driver):
        logging.info(f"Browser is ready to quit {driver}")


@pytest.fixture(scope='session')
def get_page(request):
    return request.config.getoption('--page')


@pytest.fixture(scope='session')
def get_region(request):
    return request.config.getoption('--region')


@pytest.fixture(scope='session')
def driver(get_page, get_region):
    base_url = f'https://{settings.REGIONS[get_region]}.rt.ru'
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
        wd.get(url=f'{base_url}/packages/tariffs')
    elif get_page == 'internet':
        wd.get(url=f'{base_url}]/homeinternet/order_internet')
    elif get_page == 'wink':
        wd.get(url=f'{base_url}/hometv')
    elif get_page == 'mobile':
        wd.get(url=f'{base_url}/mobile/mobile_tariff')
    elif get_page == 'video':
        wd.get(url=f'{base_url}/videocontrol')
    elif get_page == 'phone':
        wd.get(url=f'{base_url}/hometel')
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
