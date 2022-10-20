from load_data import download_page_of_offers
from link_collector import save_page_by_links
from data_collector import save_to_excel

def main():
    download_page_of_offers()
    save_page_by_links()
    save_to_excel()

if __name__ == '__main__':
    main()