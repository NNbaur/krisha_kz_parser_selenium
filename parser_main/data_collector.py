import bs4
from typing import Type
from bs4 import BeautifulSoup
import glob


def get_characteristics(soup: Type[bs4.BeautifulSoup]) -> list:
    list_of_chars = []
    chars = [
        'flat.building',
        'flat.floor',
        'live.square',
        'map.complex',
        'house.year'
    ]
    for char in chars:
        result = None
        char_block = soup.find('div', {
            'class': 'offer__info-item',
            'data-name': char
        })
        if char_block:
            result = char_block.find(
                'div',
                class_="offer__advert-short-info"
            ).get_text(strip=True)
        list_of_chars.append(result)
    return list_of_chars


def get_main_info(soup: Type[bs4.BeautifulSoup]) -> list:
    main_info = []
    classes = ["offer__location offer__advert-short-info", "offer__advert-title", "offer__price", "text"]
    for i in classes:
        if i.startswith("offer__location"):
            info = soup.find(('p', 'div'), class_=i).span.get_text(strip=True)
        else:
            info = soup.find(('p', 'div'), class_=i).get_text(strip=True)
        main_info.append(info)
    return main_info


def get_data_from_offers() -> list:
    full_data = []
    flat_pages = glob.glob("../pages/flats/*.html")

    for flat in flat_pages:
        with open(flat, 'r', encoding='UTF-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            main_info = get_main_info(soup)
            chars = get_characteristics(soup)
            full_data.append(main_info + chars)
    return full_data

