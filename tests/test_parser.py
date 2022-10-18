import pytest
from parser_main.parser import SeleniumParser
import os
import json
import tempfile
from selenium.common.exceptions import WebDriverException
from tests.get_data_for_test import get_data


def test_get_proxy():
    data1 = get_data()
    data2 = get_data(proxy_list='wrong_path_proxy')
    data3 = get_data(proxy_list='fixtures/empty_proxy.json')
    res1 = SeleniumParser(**data1).get_proxy_user()
    with open(data1['proxy_list'], 'r', encoding='UTF-8') as g:
        expected_res = json.load(g)[0]
    assert res1 == expected_res
    with pytest.raises(FileNotFoundError) as e1:
        SeleniumParser(**data2).get_proxy_user()
        assert str(e1.value) == 'Check that file with proxies is exist'
    with pytest.raises(json.decoder.JSONDecodeError) as e2:
        SeleniumParser(**data3).get_proxy_user()
        assert str(e2.value) == 'Check structure of the file with proxy. It should be json.'


def test_set_webdriver():
    data1 = get_data()
    data2 = get_data(driver_path='test_wrong_path')
    exp_res = 'Главная'
    driver = SeleniumParser(**data1).set_webdriver()
    driver.get(data1['url'])
    res = driver.title
    assert res == exp_res

    with pytest.raises(WebDriverException) as e:
        SeleniumParser(**data2).set_webdriver()
        assert str(e.value) == 'Message: Webdriver not found. Check that path to webdriver is correct\n'


def test_webdriver_options():
    data = get_data()
    parser = SeleniumParser(**data)
    options = parser.get_webdriver_options('test_user_agent1').arguments
    expected_res = [
        'user-agent=test_user_agent1',
        '--disable-blink-features=AutomationControlled',
        '--headless'
    ]
    assert options == expected_res


def test_download_page():
    with tempfile.TemporaryDirectory() as tmpdirname:
        data1 = get_data(dirname=f'{tmpdirname}/')
        SeleniumParser(**data1).download_page()
        assert os.path.exists(os.path.join(tmpdirname, data1['filename']))

        with pytest.raises(FileNotFoundError) as e1:
            data2 = get_data(dirname='wrong_path/')
            SeleniumParser(**data2).download_page()
        assert str(e1.value) == 'This directory not exist. Check the path to download'

        with pytest.raises(WebDriverException) as e2:
            data3 = get_data(proxy_list='fixtures/test_wrong_proxy.json')
            SeleniumParser(**data3).download_page()
        assert str(e2.value) == 'Message: Proxy is not working. Please use another proxy\n'

        with open(f'{tmpdirname}/{data1["filename"]}', 'r', encoding='UTF-8') as f:
            res = f.read()
    with open('fixtures/test_html.html', 'r', encoding='UTF-8') as g:
        expected_res = g.read()
    assert res == expected_res
