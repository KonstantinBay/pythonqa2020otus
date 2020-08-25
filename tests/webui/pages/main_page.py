from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    tabs = (By.CLASS_NAME, 'rt-tabs-navigation__item-name')
    card_price = (By.XPATH, '/html/body/div[2]/div/div/main/div/div/div/div/div[3]/div/div/div/div[3]/article/div/div/'
                            'div/div/div/noindex/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/'
                            'div[1]/div/div/div[2]/div/div/div/div/div[2]')
    tariff_cards = 'rt-carousel__inner rt-container'
    fast_offer_form = (By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > '
                                              'div > div > div.v--modal-box.v--modal > div > div')

    def get_cards(self, driver):
        js = 'document.getElementsByClassName("{}")'.format(self.tariff_cards)
        return driver.execute_script(js)

    def scroll_to_form(self, driver):
        js = "window.scrollTo(0, document.getElementsByClassName('rt-button rt-button-with-ripple  " \
             "rt-button-purple full-width')[0].offsetTop)"
        driver.execute_script(js)
