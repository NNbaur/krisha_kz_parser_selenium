from parser import SeleniumParser


def download_page_of_offers():
    url = make_url_to_parse()
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


def make_url_to_parse():
    gorod = {'Алмата': 'almaty', 'Астана': 'astana'}
    intro = 'Введите название одного из перечисленных городов,' \
            'в точности, как прописано ниже:\nАстана\nАлмата\n'
    try:
        n_flats = [int(i) for i in input(
            'Введите комнатность квартиры:'
            '\n1 = однокомнатная'
            '\n2 = двукомнатная'
            '\n3 = трехкомнатная'
            '\n4 = четырехкомнатная'
            '\n5 = пятикомнатная и выше'
            '\n\nЕсли хотите выбрать несколько вариантов, запишите через пробел в одну строку:'
            '\n1 2 4'
            '\nПокажет все одно-,двух- и четырехкомнатные квартиры\nВвод:\n').split(' ')]
    except ValueError:
        raise ValueError('Пожалуйста, попробуйте снова. Введите комнатность из представленного выше списка.')
    try:
        g1 = gorod[input(intro).strip()]
        url = f'https://krisha.kz/prodazha/kvartiry/{g1}/'
    except KeyError:
        raise KeyError('К сожалению, вы ввели неверное название города.')
    else:
        lst = [i for i in n_flats if i in range(1, 6)]
        lst.sort()
        for n, i in enumerate(lst):
            if i == 5:
                i = '5.100'
            if n == 0:
                url += f'?das[live.rooms][]={i}'
            else:
                url += f'&das[live.rooms][]={i}'
        return url
