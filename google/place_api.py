import requests

base_url = 'https://rahulshettyacademy.com'
add_resource = '/maps/api/place/add/json'
get_resource = '/maps/api/place/get/json'
delete_resource = '/maps/api/place/delete/json'
key_param = 'key=qaclick123'
req_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }


class PlaceAPI:
    """Class for interaction with Rahul API"""

    def __init__(self):
        pass

    def create_location(self):
        """Creates place and returns response"""

        req_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        req_url = f'{base_url}{add_resource}?{key_param}'
        resp = requests.post(req_url, json=req_body)

        print(resp.text)
        assert resp.status_code == 200
        assert resp.json()['status'] == 'OK'

        return resp

    def get_location(self, place_id):
        """Returns response with info about location by id"""

        req_url = f'{base_url}{get_resource}?{key_param}&place_id={str(place_id)}'
        resp = requests.get(req_url)

        print(resp.text)
        assert resp.status_code == 200 or 404

        return resp

    def delete_location(self, place_id):
        """Deletes location by id and returns response"""

        del_body = {
            "place_id": str(place_id)
        }
        req_url = f'{base_url}{delete_resource}?{key_param}'
        resp = requests.delete(req_url, json=del_body)

        print(resp.text)
        assert resp.status_code == 200
        assert resp.json()['status'] == 'OK'

        return resp