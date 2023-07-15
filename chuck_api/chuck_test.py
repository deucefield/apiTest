from chuck_api import ChuckAPI

ca = ChuckAPI()
cat_list = ca.get_categories()  # Getting categories list

# Asserting response status code for each category and print an entire joke
for cat in cat_list:
    res = ca.get_joke(cat)
    assert res.status_code == 200
    print(f'{res.json()["value"]}\n')

# Same with random joke
res = ca.get_joke()
assert res.status_code == 200
print(f'{res.json()["value"]}\n')
