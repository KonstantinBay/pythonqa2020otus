import logging
import time
from selenium.webdriver.common.by import By

import settings
from helpers import locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        self.apply_region_btn = (By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div > header > '
                                                  'div.region-notification.rt-dark-theme.ui_is-scrolled > div > div > '
                                                  'div > div > '
                                                  'div.notification-content__buttons.rt-space-top05.d-flex.flex-md-start > '
                                                  'button.rt-button.rt-button-orange.text-center.rt-button.rt-button-with-ripple')
        self.change_region_btn = (By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div > header > '
                                                   'div.region-notification.rt-dark-theme.ui_is-scrolled > div > div > '
                                                   'div > div > div.notification-content__buttons.rt-space-top05.d-flex.flex-md-start > '
                                                   'button.rt-button.rt-button-white.text-center.color-white.rt-button.rt-button-with-ripple')
        # при начальной загрузке страницы закрываем дефолтный поп-ап смены региона
        self.close_region_popup(driver)

    def close_region_popup(self, driver):
        btn = locators.element_is_clickable(driver, self.apply_region_btn)
        btn.click()
        time.sleep(settings.PAUSE_TIME)

    def scroll_to_form(self, driver):
        pass
