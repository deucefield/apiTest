import requests

base_url = 'https://api.chucknorris.io'
random_request = '/jokes/random'
categories_request = '/jokes/categories'
category_query_param = '?category='


class ChuckAPI:
    """Class for interaction with Chuck API"""

    def __init__(self):
        """Object init"""
        pass

    def get_categories(self):
        """Returns categories list"""

        return requests.get(f'{base_url}{categories_request}').json()

    def get_joke(self, category = None):
        """Returns response of requests to random or categorized joke"""

        if category == None:
            return requests.get(f'{base_url}{random_request}')
        else:
            return requests.get(f'{base_url}{random_request}{category_query_param}{category}')


