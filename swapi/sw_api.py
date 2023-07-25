import requests


base_url = 'https://swapi.dev/'
people_resource = 'api/people/'
film_resource = 'api/films/'


class SwAPI:
    """Class for interact with Star Wars API"""

    def __init__(self):
        pass

    def get_by_people(self, item):
        """Returns response of request to people resource in json"""

        return requests.get(f'{base_url}{people_resource}{item}').json()

    def get_by_film(self, item):
        """Returns response of request to film resource in json"""

        return requests.get(f'{base_url}{film_resource}{item}').json()
