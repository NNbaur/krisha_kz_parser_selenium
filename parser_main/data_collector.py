import bs4
from bs4 import BeautifulSoup
from typing import Type

with open('pages/flats/flat_1.html', 'r', encoding='UTF-8') as f:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')


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