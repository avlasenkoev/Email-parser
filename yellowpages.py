import requests
from bs4 import BeautifulSoup

class ParserYellowpages():
    def __init__(self, data):
        self.data = data

    def _string_formatting(self, separator):
        query_mod = []
        for string in self.data:
            new_string = separator.join(string.split(' '))
            query_mod.append(new_string)
        return query_mod

    def _create_url(self):
        query_in_url = self._string_formatting('+')
        name = query_in_url[0]
        address = query_in_url[1]
        url = ('https://www.yellowpages.com/search?search_terms={0}&'
              'geo_location_terms={1}'.format(name, address))
        return url

    def _parse_found(self):
        url = self._create_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        link = soup.find_all('h2', {'class':'n'})
        result_href = []
        for i in link:
            res = i.find('a').get('href')
            result_href.append(res)
        return result_href

    def _find_valid(self):
        result_href = self._parse_found()
        name = ''.join(self._string_formatting('-')[0]).lower()
        for href in result_href:
            if name in href:
                valid_link = 'https://www.yellowpages.com' + href
                return valid_link

    def _parse_page(self):
        url = self._find_valid()
        if url == None:
            return None
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        email_div = soup.find_all('div', {'class':'business-card-footer'})
        for tag in email_div:
            result = tag.find('a', {'class':'email-business'})
            if result != None:
                result = result.get('href')
                return result

    def get_email(self):
        email = self._parse_page() 
        if email == None:
            return None
        return email[7:]
        