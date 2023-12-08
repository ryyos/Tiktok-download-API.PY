import requests
from pyquery import PyQuery

class Scrapper:
    def __init__(self) -> None:
        self.__api = 'https://ssstik.io/abc?url=dl'
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'insomnia/8.4.5'}
    

    def ex(self, tiktok_url: str):

        payload = {'id': tiktok_url, 'locale' : 'id', 'tt':'RjU5bWlk'}
        response = requests.post(url=self.__api, data=payload, headers=self.__headers)
        print(PyQuery(response.text)('a:first-child').attr('href'))

        return PyQuery(response.text)('a:first-child').attr('href')

