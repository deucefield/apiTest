from sw_api import SwAPI

sw = SwAPI()


class SwFunctions:
    """Class with some functions"""

    def __init__(self):
        pass

    def get_all_films_with_person(self, person):
        """Returns list with films items by specified person item"""

        films_link_list = sw.get_by_people(person)['films']
        films_list = []

        for link in films_link_list:
            films_list.append(link.split('/')[-2])

        return films_list

    def get_all_persons_from_film(self, film):
        """Returns list with persons items from specified film item"""

        persons_link_list = sw.get_by_film(film)['characters']
        persons_list = []

        for link in persons_link_list:
            persons_list.append(link.split('/')[-2])

        return persons_list

    def get_names_of_characters_from_film(self, film):
        """Returns list with characters names from specified film"""

        persons_list = SwFunctions().get_all_persons_from_film(film)
        character_list = []

        for person in persons_list:
            character_list.append(sw.get_by_people(person)['name'])

        return character_list

    def get_all_characters_names_by_person_in_film(self, person):
        """Returns list with names of all the characters
         in the movie given the specified character"""

        films_list = SwFunctions().get_all_films_with_person(person)
        character_set = []

        for film in films_list:
            character_set += SwFunctions().get_names_of_characters_from_film(film)

        return character_set
