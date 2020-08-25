import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger('Test locators')


def element_is_clickable(driver, locator, time=1):
    try:
        return WebDriverWait(driver, time).until(ec.element_to_be_clickable(locator))
    except TimeoutException:
        logger.exception('Элемент {} не кликабелен'.format(locator))
        allure.attach(body=driver.get_screenshot_as_png(),
                      name='element_not_clickable_image',
                      attachment_type=allure.attachment_type.PNG)
        raise TimeoutException


def element_is_visible(driver, locator, time=1):
    try:
        return WebDriverWait(driver, time).until(ec.visibility_of_element_located(locator))
    except TimeoutException:
        logger.exception('Элемент {} не отображается на странице'.format(locator))
        allure.attach(body=driver.get_screenshot_as_png(),
                      name='element_not_visible_image',
                      attachment_type=allure.attachment_type.PNG)
        raise TimeoutException


def element_is_present(driver, locator, time=1):
    try:
        return WebDriverWait(driver, time).until(ec.presence_of_all_elements_located(locator))
    except TimeoutException:
        logger.exception('Элемент {} не найден на странице'.format())
        allure.attach(body=driver.get_screenshot_as_png(),
                      name='element_not_present_image',
                      attachment_type=allure.attachment_type.PNG)
        raise TimeoutException


def element_is_not_found(driver, locator,  time=1):
    try:
        return WebDriverWait(driver, time).until_not(ec.presence_of_element_located(locator))
    except TimeoutException:
        logger.exception('Закрытый элемент {} отображается на странице'.format(locator))
        allure.attach(body=driver.get_screenshot_as_png(),
                      name='element_is_visible_image',
                      attachment_type=allure.attachment_type.PNG)
        raise TimeoutException
