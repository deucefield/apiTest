from place_api import PlaceAPI

places_file_path = 'resources/places.txt'
existing_places_file_path = 'resources/existing_places.txt'
pa = PlaceAPI()

# Creates n locations and writes ids in file
fw = open(places_file_path, 'w')
for _ in range(5):
    fw.write(pa.create_location().json()['place_id'] + '\n')
fw.close()

# Finds all locations by ids from file
fr = open(places_file_path, 'r')
places_id = fr.readlines()
for place in places_id:
    pa.get_location(place.rstrip('\n'))
fr.close()

# Deletes even locations
for place in places_id[1::2]:
    print(place.rstrip('\n'))
    pa.delete_location(place.rstrip('\n'))

# Write to file only existing ids
fw = open(existing_places_file_path, 'w')
for place in places_id:
    if pa.get_location(place.rstrip('\n')).status_code == 200:
        fw.write(place)
fw.close()