def get_data(
    url: str = "https://rocky-plateau-42258.herokuapp.com/ru/",
    dirname: str = 'fixtures/',
    filename: str = 'test_file.html',
    proxy_list: str = 'fixtures/test_proxy_list.json',
    driver_path: str = 'drivers/chromedriver_windows.exe'
) -> dict:
    return {
        'url': url,
        'dirname': dirname,
        'filename': filename,
        'proxy_list': proxy_list,
        'driver_path': driver_path
    }