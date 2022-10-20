from parser import SeleniumParser

def download_page_of_offers():
    url = "https://krisha.kz/prodazha/kvartiry/astana/?das[live.rooms]=1"
    proxy_list = '../proxy/proxy_list.json'
    dirname = '../pages/'
    driver_path = 'drivers/chromedriver_windows.exe'
    max_page = 1
    i = 1

    while i <= max_page:
        filename = f'pages_' + str(i) + '.html'
        print("Waiting for download page with list of offers...")
        if i == 1:
            SeleniumParser(url, dirname, filename, proxy_list, driver_path).download_page()
        else:
            url_param = url + '&page=' + str(i)
            SeleniumParser(url_param, dirname, filename, proxy_list, driver_path).download_page()
        i += 1
        print(f'{filename} is downloaded to {dirname}')