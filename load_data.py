from parser import SeleniumParser


def main():
    url = "https://krisha.kz/prodazha/kvartiry/astana/?das[live.rooms]=1"
    proxy_list = 'proxy/proxy_list1.json'
    MAX_PAGE = 2
    i = 1

    while i <= MAX_PAGE:
        filename = f'page_' + str(i) + '.html'
        if i == 1:
            SeleniumParser(url, filename, proxy_list).save_page()
        else:
            url_param = url + '&page=' + str(i)
            SeleniumParser(url_param, filename, proxy_list).save_page()
        i += 1

if __name__ == '__main__':
    main()