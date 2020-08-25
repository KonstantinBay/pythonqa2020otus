import logging
import random
import time

import allure
import pytest

import settings
from helpers import locators

FEATURE = 'Проверка формы быстрой заявки'
STORY_TEXT = 'Проверка соответствия текстов'
STORY_FUNC = 'Функциональная проверка элементов формы'
VALID_TEST = 'Проверка валидации'
STREET_TITLE = 'поле Улица'
NAME_TITLE = 'поле ФИО'
HOUSE_TITLE = 'поле Дом'
FLAT_TITLE = 'поле Квартира'
PHONE_TITLE = 'поле Телефон'
FORM_TITLE = 'Быстрая заявка'
CLEAR_FIELD = 'Очистить'
VALID_DATA_TEXT = 'валидные данные'
APPLY_BTN_TEXT = 'Отправить заявку'

logger = logging.getLogger('Quick order')


@allure.feature(FEATURE)
@allure.story(STORY_TEXT)
@allure.title('Сравнение цены на карточке тарифа и на форме быстрой заявки')
@pytest.mark.webui
@pytest.mark.negative
@pytest.mark.positive
def test_price_card(driver, main_page, order_form):
    logger.info('Offer price')
    with allure.step('Получение цены на карточке тарифа'):
        card_price = locators.element_is_visible(driver, main_page.card_price).text
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка отображения формы'):
        locators.element_is_visible(driver, order_form.fast_order_form)
    with allure.step('Получение цены на форме быстрой заявки'):
        form_price = locators.element_is_visible(driver, order_form.form_price).text
    logger.info('Compare offer and form prices')
    with allure.step('Сравнение цены карточки тарифа и формы быстрой заявки'):
        assert card_price == form_price


@allure.feature(FEATURE)
@allure.story(STORY_TEXT)
@allure.title('Сравнение текста кнопки для отправки заявки')
@pytest.mark.webui
@pytest.mark.positive
def test_text_apply_btn(driver, main_page, order_form):
    logger.info('Apply button')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    logger.info('Button text is equal to {}'.format(APPLY_BTN_TEXT))
    with allure.step('Текст на кнопке формы равен {}'.format(APPLY_BTN_TEXT)):
        assert locators.element_is_visible(driver, order_form.apply_btn).text == APPLY_BTN_TEXT


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title('Проверка интерактивности элементов и закрытия формы')
@pytest.mark.webui
@pytest.mark.positive
def test_form_elements(driver, main_page, order_form):
    logger.info('Form elements')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных для поля Улица'):
        locators.element_is_clickable(driver, order_form.street)
    with allure.step('Проверка возможности ввода данных для поля Дом'):
        locators.element_is_clickable(driver, order_form.house)
    with allure.step('Проверка возможности ввода данных для поля Квартира'):
        locators.element_is_clickable(driver, order_form.flat)
    with allure.step('Проверка возможности ввода данных для поля ФИО'):
        locators.element_is_clickable(driver, order_form.name)
    with allure.step('Проверка возможности ввода данных для поля Телефон'):
        locators.element_is_clickable(driver, order_form.phone)
    with allure.step('Проверка интерактивности чек-бокса "Обработка персональных данных"'):
        locators.element_is_clickable(driver, order_form.chk_box)
    with allure.step('Проверка интерактивности иконки смены региона'):
        locators.element_is_clickable(driver, order_form.change_region_btn)
    with allure.step('Проверка интерактивности иконки закрытия формы'):
        btn = locators.element_is_clickable(driver, order_form.close_btn)
    with allure.step('Закрыть форму быстрой заявки'):
        btn.click()
    logger.info('Closed form is not present')
    with allure.step('Проверка, что закрытая форма не отображается'):
        assert locators.element_is_not_found(driver, order_form.fast_order_form)


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title(VALID_TEST + ', ' + STREET_TITLE + ', негативный сценарий')
@pytest.mark.webui
@pytest.mark.negative
@pytest.mark.parametrize('street_param', ['street', '!@#$%', '     '])
def test_street_validation_neg(driver, main_page, order_form, street_param):
    logger.info('Negative validation street field')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных, {}'.format(STREET_TITLE)):
        street = locators.element_is_clickable(driver, order_form.street)
    with allure.step('Очистить {}'.format(STREET_TITLE)):
        street.clear()
    with allure.step('Ввод, {}, не{}'.format(STREET_TITLE, VALID_DATA_TEXT)):
        street.send_keys(street_param)
    logger.info('Validation text is present' + ', ' + STREET_TITLE + ', input data: ' + street_param)
    with allure.step('Проверка отображения сообщения, не{}'.format(VALID_DATA_TEXT)):
        assert locators.element_is_visible(driver, order_form.street_error_msg)


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title(VALID_TEST + ', ' + STREET_TITLE + ', позитивный сценарий')
@pytest.mark.webui
@pytest.mark.positive
@pytest.mark.parametrize('street_param', ['Тест', 'Тест-Тест', '12345'])
def test_street_validation_pos(driver, main_page, order_form, street_param):
    logger.info('Positive validation street field')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных, {}'.format(STREET_TITLE)):
        street = locators.element_is_clickable(driver, order_form.street)
    with allure.step('Очистить {}'.format(STREET_TITLE)):
        street.clear()
    with allure.step('Ввод, {}, {}'.format(STREET_TITLE, VALID_DATA_TEXT)):
        street.send_keys(street_param)
    logger.info('Validation text is not present' + ', ' + STREET_TITLE + ', input data: ' + street_param)
    with allure.step('Проверка, что валидация не отображается'):
        assert locators.element_is_not_found(driver, order_form.street_error_msg)


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.story(STORY_TEXT)
@allure.title(VALID_TEST + ', ' + STREET_TITLE + ', проверка текстов валидации')
@pytest.mark.webui
@pytest.mark.negative
def test_street_validation_msg(driver, main_page, order_form):
    logger.info('Check validation text for street field')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных, {}'.format(STREET_TITLE)):
        street = locators.element_is_clickable(driver, order_form.street)
    with allure.step('Очистить {}'.format(STREET_TITLE)):
        street.clear()
    with allure.step('Ввод, {}, не{}'.format(STREET_TITLE, VALID_DATA_TEXT)):
        street.send_keys('street')
    with allure.step('Получить текст валидации при вводе невалидных данных'):
        text1 = locators.element_is_visible(driver, order_form.street_error_msg).text
    with allure.step('Проверка отображения иконки очистки, {}'.format(STREET_TITLE)):
        btn = locators.element_is_visible(driver, order_form.street_clear_btn)
    with allure.step('Нажать иконку очистки поля'):
        btn.click()
    with allure.step('Получить текст валидации при пустом поле'):
        text2 = locators.element_is_visible(driver, order_form.street_error_msg).text
    logger.info('Validation texts are correct' + ', ' + STREET_TITLE + ', 1: ' + text1 + ', 2: ' + text2)
    with allure.step('Проверка текстов валидации для невалидных данных и для пустого поля'):
        assert (text1 == 'введите на русском языке') & (text2 == 'необходимо заполнить')


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title(VALID_TEST + ', ' + NAME_TITLE + ', негативный сценарий')
@pytest.mark.webui
@pytest.mark.negative
@pytest.mark.parametrize('name_param', ['test', 'Тест-Test', '12345'])
def test_name_validation_neg(driver, main_page, order_form, name_param):
    logger.info('Negative validation name field')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных, {}'.format(NAME_TITLE)):
        name = locators.element_is_clickable(driver, order_form.name)
    with allure.step('Очистить {}'.format(NAME_TITLE)):
        name.clear()
    with allure.step('Ввод, {}, не{}'.format(NAME_TITLE, VALID_DATA_TEXT)):
        name.send_keys(name_param)
    logger.info('Validation text is present' + ', ' + NAME_TITLE + ', input data: ' + name_param)
    with allure.step('Проверка отображения сообщения, не{}'.format(VALID_DATA_TEXT)):
        assert locators.element_is_visible(driver, order_form.name_error_msg)


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title(VALID_TEST + ', ' + NAME_TITLE + ', позитивный сценарий')
@pytest.mark.webui
@pytest.mark.positive
@pytest.mark.parametrize('name_param', ['Тест', 'Тест-Тест', 'Тестов Тест', 'тест'])
def test_name_validation_pos(driver, main_page, order_form, name_param):
    logger.info('Positive validation name field')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Проверка возможности ввода данных, {}'.format(NAME_TITLE)):
        name = locators.element_is_clickable(driver, order_form.name)
    with allure.step('Очистить {}'.format(NAME_TITLE)):
        name.clear()
    with allure.step('Ввод, {}, {}'.format(NAME_TITLE, VALID_DATA_TEXT)):
        name.send_keys(name_param)
    logger.info('Validation text is not present' + ', ' + NAME_TITLE + ', input data: ' + name_param)
    with allure.step('Проверка, что валидация не отображается'):
        assert locators.element_is_not_found(driver, order_form.name_error_msg)


@allure.feature(FEATURE)
@allure.story(STORY_FUNC)
@allure.title(FORM_TITLE + ', позитивный сценарий')
@pytest.mark.webui
@pytest.mark.positive
@pytest.mark.order
def test_create_quick_order(driver, main_page, order_form):
    logger.info('Create quick order')
    with allure.step('Открыть форму быстрой заявки, если она не отображается'):
        order_form.open_form(driver)
    with allure.step('Очистить поля формы'):
        with allure.step('Очистить {}'.format(STREET_TITLE)):
            locators.element_is_clickable(driver, order_form.street).clear()
        with allure.step('Очистить {}'.format(HOUSE_TITLE)):
            locators.element_is_clickable(driver, order_form.house).clear()
        with allure.step('Очистить {}'.format(FLAT_TITLE)):
            locators.element_is_clickable(driver, order_form.flat).clear()
        with allure.step('Очистить {}'.format(NAME_TITLE)):
            locators.element_is_clickable(driver, order_form.name).clear()
        with allure.step('Очистить {}'.format(PHONE_TITLE)):
            locators.element_is_clickable(driver, order_form.phone).clear()
    with allure.step('Ввод данных, {}'.format(STREET_TITLE)):
        locators.element_is_clickable(driver, order_form.street).send_keys('Тестовая')
    with allure.step('Время для подгрузки js-скрипта'):
        time.sleep(settings.PAUSE_TIME)
    with allure.step('Ввод данных, {}'.format(HOUSE_TITLE)):
        locators.element_is_clickable(driver, order_form.house).send_keys(random.randint(1, 999))
    with allure.step('Время для подгрузки js-скрипта'):
        time.sleep(settings.PAUSE_TIME)
    with allure.step('Ввод данных, {}'.format(FLAT_TITLE)):
        locators.element_is_clickable(driver, order_form.flat).send_keys(random.randint(1, 999))
    with allure.step('Ввод данных, {}'.format(NAME_TITLE)):
        locators.element_is_clickable(driver, order_form.name).send_keys('автотест')
    with allure.step('Ввод данных, {}'.format(PHONE_TITLE)):
        locators.element_is_clickable(driver, order_form.phone).send_keys('9998887766')
    with allure.step('Проверка отображения кнопки отправки заявки'):
        apl = locators.element_is_clickable(driver, order_form.apply_btn)
    with allure.step('Получить текущий URL до отправки заявки'):
        url_before = driver.current_url
    logger.info('Send quick order')
    with allure.step('Нажать кнопку отправки заявки'):
        apl.click()
    with allure.step('Проверка ,что форма быстрой заявки не отображается'):
        locators.element_is_not_found(driver, order_form.fast_order_form, time=settings.PAUSE_TIME + 7)
    with allure.step('Получить текущий URL после отправки заявки'):
        url_after = driver.current_url
    logger.info('URLs not equal')
    with allure.step('Проверка, что URL до и после отправки заявки не совпадают'):
        assert url_after != url_before
