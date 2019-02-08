import requests
from bs4 import BeautifulSoup


class Google():

    def __init__(self, data):
        self.data = data

    def _string_formatting(self, separator):
        data = self.data[0] + ' ' + self.data[1]
        query_mod = separator.join(data.split(' '))
        return [query_mod]

    def _create_url(self):
        query_in_url = self._string_formatting('+')
        url = ('https://www.google.com/search?q={0}&oq={0}&' 
             'chrome..69i57j69i60l2.1168j0j9&sourceid=chrome&ie=UTF-8'
             .format(query_in_url[0])
            )
        return url

    def _get_html(self):
        url = self._create_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def check(self):
        soup = self._get_html()
        result = soup.find_all('div', {'class':'F7uZG'})
        if result != []:
            return True
        return False

