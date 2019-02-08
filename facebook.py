import requests
from bs4 import BeautifulSoup
from google_check import Google

class Facebook(Google):

    def __init__(self,data):
        self.data = data
        self.title = 'facebook'

    def _string_formatting(self, separator):
        quote = '"'
        name = quote + self.data[0] + quote
        data = name + self.data[1] + self.title
        query_mod = separator.join(data.split(' '))
        return [query_mod]

    def _find_valid(self):
        soup = self._get_html()
        h3_tags = soup.find_all('h3', {'class':'r'})
        for h3 in h3_tags:
            a = h3.find('a').get('href')
            if a[19:27] == self.title:
                link_with_trash = a[7:]
                link = link_with_trash.split('&')[0]
                return link

    def check(self):
        url = self._find_valid()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        span = soup.find('span', {'class':'_14-5'})
        result = span.find_all(text=True)
        if result == ['Постійно зачинене']:
            return True
        return False

    def get_mail(self):
        url = self._find_valid()
        name = url.split('/')[-2]
        url_about = 'https://www.facebook.com/pg/' + \
                    name + '/about/?ref=page_internal'
        r = requests.get(url_about)
        soup = BeautifulSoup(r.text, 'lxml')
        divs = soup.find_all('div', {'class':'_50f4'})
        for div in divs:
            text = div.find_all(text=True)
            if '@' in str(text):
                return ''.join(text)

        