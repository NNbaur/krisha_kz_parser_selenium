from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time
import random
import json
import os


class SeleniumParser:
    def __init__(
            self, url: str, dirname: str,
            filename: str, proxy_list: str,
            driver_path: str
    ):
        self.url = url
        self.filename = filename
        self.proxy_list = proxy_list
        self.dirname = dirname
        self.driver_path = driver_path

    def download_page(self):
        driver = self.set_webdriver()
        try:
            driver.get(self.url)
            time.sleep(3)
            html = driver.page_source
            with open(self.dirname + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        except FileNotFoundError:
            raise FileNotFoundError('This directory not exist. Check the path to download')
        except WebDriverException:
            raise WebDriverException('Proxy is not working. Please use another proxy')
        finally:
            # Check that session runs with our proxy data
            user_agent_check = driver.execute_script("return navigator.userAgent;")
            print(user_agent_check)
            driver.quit()

    def get_webdriver_options(self, user_agent: str):
        options = webdriver.ChromeOptions()
        # Added custom user-agent
        options.add_argument("user-agent=" + user_agent)
        # Disable webdriver mode, so our requests won't be blocked, imitate default user
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Disable the launch of the browser on PC
        options.add_argument("--headless")
        return options

    def set_webdriver(self):
        proxy_data = self.get_proxy_user()
        proxy = proxy_data['proxy']
        user_agent = proxy_data['user-agent']

        options_proxy = {
            'proxy': {
                'https': proxy,
                'no_proxy': 'localhost,127.0.0.1:8080'
            }
        }
        options = self.get_webdriver_options(user_agent)
        dr_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                os.path.pardir,
                self.driver_path)
        )
        s = Service(executable_path=dr_path)
        try:
            driver = webdriver.Chrome(options=options, service=s, seleniumwire_options=options_proxy)
            return driver
        except WebDriverException:
            raise WebDriverException('Webdriver not found. Check that path to webdriver is correct')


    def get_proxy_user(self):
        try:
            with open(self.proxy_list, 'r') as f:
                proxy_list = json.load(f)
                proxy_data = random.choice(proxy_list)
                return proxy_data
        except FileNotFoundError:
            raise FileNotFoundError('Check that file with proxies is exist')
        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError('Check structure of the file with proxy. It should be json.', "\n\n", 1)



