import sys

from chuck_api import ChuckAPI

ca = ChuckAPI()
cat_list = ca.get_categories()
cat_list.append('random')   # Getting categories list with possibility to get random joke

# Asking user to specify joke category and validating it
user_cat = input(f'Allowed joke categories:\n{cat_list}\n'
                 f'Enter a joke category: ')
if user_cat not in cat_list:
    print('You specified an illegal category')
    sys.exit()

# Sending request and check its status code
res = ca.get_joke() if user_cat == 'random' else ca.get_joke(user_cat)
assert res.status_code == 200

# Print an entire joke
print(f'\nYour joke: {res.json()["value"]}')
