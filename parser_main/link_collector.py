from bs4 import BeautifulSoup
import glob
from parser import SeleniumParser


def get_pages() -> list:
    return glob.glob('pages/*.html')


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


def main():
    proxy_list = 'proxy/proxy_list.json'
    dirname = 'pages/flats/'
    i = 1
    link_list = collect_links(get_pages())
    for link in link_list:
        filename = f'flat_' + str(i) + '.html'
        SeleniumParser(link, dirname, filename, proxy_list).download_page()
        i += 1


if __name__ == '__main__':
    main()