from parser import SeleniumParser


def main():
    url = "https://krisha.kz/prodazha/kvartiry/astana/?das[live.rooms]=1"
    proxy_list = 'proxy/proxy_list.json'
    dirname = 'pages/'
    max_page = 2
    i = 1

    while i <= max_page:
        filename = f'page_' + str(i) + '.html'
        if i == 1:
            SeleniumParser(url, dirname, filename, proxy_list).download_page()
        else:
            url_param = url + '&page=' + str(i)
            SeleniumParser(url_param, dirname, filename, proxy_list).download_page()
        i += 1

if __name__ == '__main__':
    main()