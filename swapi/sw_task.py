from sw_func import SwFunctions

sw = SwFunctions()
chars = set(sw.get_all_characters_names_by_person_in_film(4))

fw = open('characters.txt', 'w')
for char in chars:
    fw.write(f'{char}\n')
fw.close()