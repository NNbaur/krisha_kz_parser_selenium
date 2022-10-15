


# def test_download_page():
#     url = "https://rocky-plateau-42258.herokuapp.com/ru/"
#     proxy_list = 'fixtures/test_proxy_list.json'
#     filename = 'test_file.html'
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         SeleniumParser(url, tmpdirname, filename, proxy_list).download_page()
#         assert os.path.exists(tmpdirname)
#         print(os.listdir(tmpdirname))

url = "https://rocky-plateau-42258.herokuapp.com/ru/"
proxy_list = 'fixtures/test_proxy_list.json'
filename = 'test_file.html'
dirname = 'tests/'

# SeleniumParser(url, dirname, filename, proxy_list).download_page()




# with tempfile.TemporaryDirectory() as tmpdirname:
#     SeleniumParser(url, tmpdirname, filename, proxy_list).download_page()
#     print(tmpdirname)