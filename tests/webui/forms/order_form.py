import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class OrderForm:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    fast_order_form = (By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > '
                                        'div > div > div.v--modal-box.v--modal > div > div')
    street = (By.CSS_SELECTOR,
              'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
              'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
              'div > div.row.no-padding > div.rt-col-8.rt-col-td-4.rt-col-md-3 > div > div.input-wrapper > div > input')
    house = (By.CSS_SELECTOR,
             'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
             'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
             'div > div.row.no-padding > div:nth-child(2) > div > div.input-wrapper > div > input')
    flat = (By.CSS_SELECTOR,
            'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
            'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
            'div > div.row.no-padding > div:nth-child(3) > div > div > div > input')
    name = (By.CSS_SELECTOR,
            'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
            'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
            'div > div:nth-child(3) > div.rt-col-8.rt-col-td-3.rt-col-md-3.rt-space-top > div > div > input')
    phone = (By.CSS_SELECTOR,
             'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
             'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
             'div > div:nth-child(3) > div.rt-col-4.rt-col-td-3.rt-col-md-3.rt-space-top > div > input')
    chk_box = (By.CSS_SELECTOR,
               'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
               'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > '
               'div > div.row.rt-col-12.rt-col-td-6.rt-col-md-3.rt-space-top.rt-space-bottom > label')
    apply_btn = (By.CSS_SELECTOR,
                 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
                 'div > div > div > div.rt-col-3.rt-col-td-6.rt-col-md-3.cart-custom-border.d-flex.price-block-space-horizontal.block-space-vertical > '
                 'div > div:nth-child(3) > button')
    close_btn = (By.CSS_SELECTOR,
                 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
                 'a > i > svg')
    change_region_btn = (By.CSS_SELECTOR,
                         'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > div.v--modal-box.v--modal > '
                         'div > div > div > div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > '
                         'form > div > div:nth-child(1) > div')
    street_clear_btn = (
        By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > '
                         'div > div.v--modal-box.v--modal > div > div > div > '
                         'div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > '
                         'form > div > div.row.no-padding > div.rt-col-8.rt-col-td-4.rt-col-md-3 > div > '
                         'div.input-wrapper > div > div.input-clear')
    name_clear_btn = (By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > '
                                       'div > div.v--modal-box.v--modal > div > div > div > '
                                       'div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > '
                                       'form > div > div:nth-child(3) > '
                                       'div.rt-col-8.rt-col-td-3.rt-col-md-3.rt-space-top > div > div > div.input-clear')
    street_error_msg = (By.CSS_SELECTOR,
                        'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > '
                        'div.v--modal-box.v--modal > div > div > div > '
                        'div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > div > '
                        'div.row.no-padding > div.rt-col-8.rt-col-td-4.rt-col-md-3 > div > div.input-wrapper > div > '
                        'div.text-field__error-message.rtb-text-field__error-message--on-the-right')
    name_error_msg = (By.CSS_SELECTOR,
                      'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > '
                      'div.v--modal-box.v--modal > div > div > div > '
                      'div.rt-col-9.rt-col-td-6.rt-col-md-3.form-space-horizontal.block-space-vertical > form > div > '
                      'div:nth-child(3) > div.rt-col-8.rt-col-td-3.rt-col-md-3.rt-space-top > div > div > '
                      'div.text-field__error-message.rtb-text-field__error-message--on-the-right')
    form_price = (
        By.CSS_SELECTOR, 'body > div.dialog-off-canvas-main-canvas > div > div.app-dialog_global > div > div > '
                         'div.v--modal-box.v--modal > div > div > div > '
                         'div.rt-col-3.rt-col-td-6.rt-col-md-3.cart-custom-border.d-flex.price-block-space-horizontal.block-space-vertical > '
                         'div > div.rt-col-12.rt-col-td-3.rt-col-md-3.rt-space-top.d-flex > div > '
                         'div.rt-price__option-value.rt-price__value')

    def open_form(self, driver):
        try:
            driver.find_element_by_css_selector(self.fast_order_form[1])
        except NoSuchElementException:
            js = "document.getElementsByClassName('rt-button rt-button-with-ripple  " \
                 "rt-button-purple full-width')[0].click()"
            driver.execute_script(js)
