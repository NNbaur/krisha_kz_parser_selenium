from bs4 import BeautifulSoup
import glob
from parser import SeleniumParser


def get_pages() -> list:
    return glob.glob('../pages/*.html')


def collect_links(pages_path: str) -> list:
    url = 'https://krisha.kz/'
    link_list = []
    for page in pages_path:
        with open(page, 'r', encoding='UTF-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', class_='a-card__title')
            for link in links:
                link_list.append(url + link.get('href'))
    return link_list


def save_page_by_links():
    proxy_list = '../proxy/proxy_list.json'
    dirname = '../pages/flats/'
    driver_path = 'drivers/chromedriver_windows.exe'
    i = 1
    link_list = collect_links(get_pages())
    for link in link_list:
        filename = f'flat_{i}.html'
        print("Waiting for download page with flat...")
        SeleniumParser(
            link, dirname, filename,
            proxy_list, driver_path
        ).download_page()
        i += 1
        print(f"{filename} is downloaded to {dirname}")
