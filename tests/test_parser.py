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
    res2 = 'Check that file with proxies is exist'
    res3 = 'Check structure of the file with proxy. It should be json.'
    with open(data1['proxy_list'], 'r', encoding='UTF-8') as g:
        expected_res = json.load(g)[0]
    assert res1 == expected_res
    with pytest.raises(FileNotFoundError) as e1:
        SeleniumParser(**data2).get_proxy_user()
        assert str(e1.value) == res2
    with pytest.raises(json.decoder.JSONDecodeError) as e2:
        SeleniumParser(**data3).get_proxy_user()
        assert str(e2.value) == res3


def test_set_webdriver():
    data1 = get_data()
    data2 = get_data(driver_path='test_wrong_path')
    exp_res = 'Главная'
    driver = SeleniumParser(**data1).set_webdriver()
    driver.get(data1['url'])
    res1 = driver.title
    res2 = 'Message: Webdriver not found.' \
           'Check that path to webdriver is correct\n'
    assert res1 == exp_res

    with pytest.raises(WebDriverException) as e:
        SeleniumParser(**data2).set_webdriver()
        assert str(e.value) == res2


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
    res1 = 'This directory not exist. Check the path to download'
    res2 = 'Message: Proxy is not working. Please use another proxy\n'
    with tempfile.TemporaryDirectory() as tmpdirname:
        data1 = get_data(dirname=f'{tmpdirname}/')
        SeleniumParser(**data1).download_page()
        assert os.path.exists(os.path.join(tmpdirname, data1['filename']))

        with pytest.raises(FileNotFoundError) as e1:
            data2 = get_data(dirname='wrong_path/')
            SeleniumParser(**data2).download_page()
        assert str(e1.value) == res1

        with pytest.raises(WebDriverException) as e2:
            data3 = get_data(proxy_list='fixtures/test_wrong_proxy.json')
            SeleniumParser(**data3).download_page()
        assert str(e2.value) == res2

        with open(
                f'{tmpdirname}/{data1["filename"]}',
                'r', encoding='UTF-8'
        ) as f:
            res3 = f.read()
    with open('fixtures/test_html.html', 'r', encoding='UTF-8') as g:
        expected_res = g.read()
    assert res3 == expected_res
