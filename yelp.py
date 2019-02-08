import requests
from bs4 import BeautifulSoup
from google_check import Google

class Yelp(Google):


    def _string_formatting(self, separator):
        #only name and city i data
        address = self.data[1].split(' ')
        city = []
        for word in address:
            if word.isdigit():
                break
            city.append(word)

        self.data[1] = ' '.join(city)

        #'and' instead '&'
        name = self.data[0].split(' ')
        new_name = []
        for word in name:
            if word == '&':
                word = 'and'
            new_name.append(word)

        #delete apostrophe
        new_name_1 = []
        for word in new_name:
            new_word = ''
            for letter in word:
                if letter != "'":
                    new_word += letter 
            new_name_1.append(new_word)

        self.data[0] = ' '.join(new_name_1)

        query_mod = []
        for string in self.data:
            new_string = separator.join(string.split(' '))
            query_mod.append(new_string)
        return query_mod


    def _create_url(self):
            query_in_url = self._string_formatting('-')
            name = query_in_url[0]
            address = query_in_url[1]
            url = ('https://www.yelp.com/biz/{0}-{1}'.format(name, address))
            return url


    def check(self):
        url = self._create_url()
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        p = soup.find_all('p', {'class':'alert-message'})
        if len(p) > 0:
            return True
        return False
