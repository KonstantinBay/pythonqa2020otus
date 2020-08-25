import logging
import allure
import pytest
import requests
import cerberus

import settings

headers = {"Content-type": "application/json; charset=UTF-8"}

FEATURE = 'Проверка api запросов'
STORY_PAGE = 'Проверка доступности страниц'
STORY_SERV = 'Функциональная проверка микросервисов'
TITLE_TEXT = 'Проверка кода ответа'
REQ_TEXT = 'Отправить запрос для '

logger = logging.getLogger('API requests')


@allure.feature(FEATURE)
@allure.story(STORY_PAGE)
@allure.title('{}: Landing Page'.format(TITLE_TEXT))
@pytest.mark.api
@pytest.mark.xfail
@pytest.mark.parametrize('lp', ['/books', '/smarthome', '/lightplus', '/videocontrol', '/zakompaniyu', '/cometous'])
@pytest.mark.parametrize('reg', range(1))
def test_access_lp(get_url, get_status_code, lp, reg):
    respcode = requests.get(get_url + lp).status_code
    logger.info('Access LP')
    logger.info('Got respcode {} from LP {} in region {}'.format(respcode, lp, settings.REGIONS[reg]))
    with allure.step('Код ответа {} LP {} в регионе {}'.format(respcode, lp, settings.REGIONS[reg])):
        assert respcode == get_status_code


@allure.feature(FEATURE)
@allure.story(STORY_SERV)
@allure.title('{}'.format(TITLE_TEXT))
@pytest.mark.api
@pytest.mark.parametrize('service, method', [(settings.SERVICES[0], settings.METHODS[0]),
                                             (settings.SERVICES[1], settings.METHODS[1]),
                                             (settings.SERVICES[2], settings.METHODS[2])])
def test_get_region(api_client, get_status_code, service, method):
    logger.info('Get region')
    if service == settings.SERVICES[2]:
        with allure.step('Для сервиса {} отправить запрос с доп. параметрами'.format(settings.SERVICES[2])):
            resp = api_client.get(path='/'.join([service, settings.API_VERSION, method]),
                                  params={'r12': 524613, 'apikey': settings.APIKEY})
    else:
        with allure.step('Для сервиса {} отправить запрос без доп. параметров'.format(service)):
            resp = api_client.get(path='/'.join([service, settings.API_VERSION, method]),
                                  params={'apikey': settings.APIKEY})
    logger.info('Got respcode {} from {}/{}'.format(resp.status_code, service, method))
    with allure.step('Код ответа {} от {}/{}'.format(resp.status_code, service, method)):
        assert resp.status_code == get_status_code


@allure.feature(FEATURE)
@allure.story(STORY_SERV)
@allure.title('Проверка полученных данных при параметризации запроса')
@pytest.mark.api
@pytest.mark.xfail
@pytest.mark.parametrize('service, method', [(settings.SERVICES[0], settings.METHODS[3])])
@pytest.mark.parametrize('locality', ['Краснодар', 'краснодар', 'КРАСНОДАР', 'Krasnodar', 'qwerty'])
def test_get_locality(api_client, service, method, locality):
    logger.info('Get locality')
    json_data = {"region_id": "23", "search_str": locality}
    with allure.step('{}{}/{}'.format(REQ_TEXT, service, method)):
        resp = api_client.post(path='/'.join([service, settings.API_VERSION, method]), headers=headers, json=json_data,
                               params={'apikey': settings.APIKEY}).json()
    logger.info('Got response from {}/{} and locality {}'.format(service, method, locality))
    with allure.step('Ответ от {}/{} не пустой'.format(service, method)):
        assert len(resp) != 0


@allure.feature(FEATURE)
@allure.story(STORY_SERV)
@allure.title('Проверка кода ответа при параметризации запроса')
@pytest.mark.api
@pytest.mark.parametrize('service, method', [(settings.SERVICES[3], settings.METHODS[4])])
@pytest.mark.parametrize('locality', ['5203074', 5203074, -5203074, 'something', '5203074520307452030745', True])
def test_get_banners(api_client, get_status_code, service, method, locality):
    logger.info('Get banners')
    json_data = {"segment": "b2c", "bgroup": "b2c_main", "region": "5200035", "locality": locality,
                 "services": ["noclient"]}
    with allure.step('{}{}/{} и locality code {} ({})'.format(REQ_TEXT, service, method, locality, type(locality))):
        resp = api_client.post(path='/'.join([service, settings.API_VERSION, method]), headers=headers, json=json_data,
                               params={'apikey': settings.APIKEY})
    logger.info(
        'Got respcode {} from {}/{} and locality code {} ({})'.format(resp.status_code, service, method, locality,
                                                                      type(locality)))
    with allure.step(
            'Код ответа {} от {}/{} и locality code {} ({})'.format(resp.status_code, service, method, locality,
                                                                    type(locality))):
        if type(locality) is str:
            assert resp.status_code == get_status_code
        else:
            assert resp.status_code == 400


@allure.feature(FEATURE)
@allure.story(STORY_SERV)
@allure.title('Проверка создания заявки при параметризации запроса')
@pytest.mark.api
@pytest.mark.xfail
@pytest.mark.parametrize('service, method', [(settings.SERVICES[4], settings.METHODS[5])])
@pytest.mark.parametrize('city', [3092902, '3092902', '-1', '309290230929023092902', 'city_id', True])
def test_create_order(api_client, city, service, method):
    logger.info('Create order')
    json_data = {"hash_key": "6326017180118839f98fb0f10aceed9e0952b41b", "offer_id": "414603496970",
                 "address": {"city_id": city, "city_name": "Краснодар", "street_name": "тестовая",
                             "house_num": "78787", "flat": "878978"}, "client": {"last_name": "автотест"},
                 "phone_num": "9999999999", "region_id": "23", "region_name": "Краснодарский край"}
    with allure.step('{}{}/{} и city code {} ({})'.format(REQ_TEXT, service, method, city, type(city))):
        resp = api_client.post(path='/'.join([service, settings.API_VERSION, method]), headers=headers, json=json_data,
                               params={'apikey': settings.APIKEY}).json()
    logger.info('Got order from {}/{} and city code {} ({}). Order #{}'.format(service, method, city, type(city), resp["order_id"]))
    with allure.step('Проверка полученного order_id. Номер заявки {}'.format(resp["order_id"])):
        assert isinstance(resp['order_id'], int)


@allure.feature(FEATURE)
@allure.story(STORY_SERV)
@allure.title('Валидация структуры ответа')
@pytest.mark.api
@pytest.mark.parametrize('service, method', [(settings.SERVICES[4], settings.METHODS[5])])
def test_validation_schema(api_client, service, method):
    logger.info('Validate order create response schema')
    json_data = {"hash_key": "6326017180118839f98fb0f10aceed9e0952b41b", "offer_id": "414603496970",
                 "address": {"city_id": "3092902", "city_name": "Краснодар", "street_name": "тестовая",
                             "house_num": "78787", "flat": "878978"}, "client": {"last_name": "автотест"},
                 "phone_num": "9999999999", "region_id": "23", "region_name": "Краснодарский край"}
    with allure.step('{}{}/{}'.format(REQ_TEXT, service, method)):
        resp = api_client.post(path='/'.join([service, settings.API_VERSION, method]), headers=headers, json=json_data,
                               params={'apikey': settings.APIKEY}).json()
    logger.info('Got response from {}/{}'.format(service, method))
    logger.info('Define validation schema')
    schema = {
        'order_id': {'type': 'integer'},
        'status': {'type': 'string'}
    }
    logger.info('Create cerberus validator')
    with allure.step('Создание валидатора cerberus'):
        valid = cerberus.Validator()
    logger.info('Check schema and structure response from {}/{}'.format(service, method))
    with allure.step('Проверка валидности полученного ответа от {}/{}'.format(service, method)):
        assert valid.validate(resp, schema)
