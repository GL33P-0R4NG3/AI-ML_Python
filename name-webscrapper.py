import time

import re
import requests
from bs4 import BeautifulSoup as bsoup

def dmnesorgnames():
    response = requests.get('https://dmnes.org/names')

    soup = bsoup(response.content, 'html.parser')

    sorted_by_letters = soup.find_all(class_='index_letter')

    sorted_name_elements = []
    for names in sorted_by_letters:
        sorted_name_elements += names.find_all('a',href=True)

    #print(sorted_name_elements)

    sorted_names = []
    for name in sorted_name_elements:
        sorted_names += name.contents

    #print(sorted_names)

    with open('data/text/webscrapped-medival-names.txt', 'w') as f:
        mtch = '\n'.join(name.lower() for name in sorted_names if re.fullmatch('[a-z]+', name.lower()))
        #test = re.match(r'^(?!.*[a-z]).*$\n?', '\n'.join(sorted_names).lower())
        #print(mtch)
        f.write(mtch)

def forebearsnames():

    sorted_names = ''

    for i in range(ord('a'), ord('z')+1):
        print('Sleeping 1 seconds...')
        time.sleep(1)
        letter = chr(i)
        print(f'Scrapping forebears for letter \'{letter}\'...')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(f'https://forebears.io/forenames/begining-with/{letter}/', headers=headers)
        soup = bsoup(response.content, 'html.parser')

        name_count = 0
        for element in soup.find_all('h4', class_='name'):
            name = element.contents[0].lower()
            if re.fullmatch(r'[a-z]+', name):
                sorted_names += name + '\n'
                name_count += 1

        print(f'Successfully scrapped {name_count} name starting with {letter}.')


    with open('data/text/webscrapped-general-names.txt', 'w') as f:
        #test = re.match(r'^(?!.*[a-z]).*$\n?', '\n'.join(sorted_names).lower())
        #print(mtch)
        f.write(sorted_names)

if __name__ == '__main__':
    dmnesorgnames()
    forebearsnames()
