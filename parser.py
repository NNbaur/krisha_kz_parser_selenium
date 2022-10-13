from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
import json


class SeleniumParser:
    def __init__(self, url: str, filename: str, proxy_list: str):
        self.url = url
        self.filename = filename
        self.proxy_list = proxy_list

    def save_page(self):
        proxy_data = self.get_proxy_user(self.proxy_list)
        proxy = proxy_data['proxy']
        user_agent = proxy_data['user-agent']
        options = webdriver.ChromeOptions()
        # Set proxy settings for Chrome
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "proxyType": "MANUAL",
        }
        # Accept all SSL certificates by default
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
        options.add_argument("user-agent="+user_agent)
        # Disable webdriver mode, so our requests won't be blocked, imitate default user
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Disable the launch of the browser on PC
        options.add_argument("--headless")
        s = Service(executable_path="drivers/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=s)

        try:
            driver.get(self.url)
            time.sleep(3)
            html = driver.page_source
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        finally:
            # Check that session runs with our proxy data
            user_agent_check = driver.execute_script("return navigator.userAgent;")
            print(user_agent_check)

    def get_proxy_user(self, path):
        try:
            with open(path, 'r') as f:
                proxy_list = json.load(f)
                proxy_data = random.choice(proxy_list)
                return proxy_data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print('Check that file with proxies is exist or not empty')


