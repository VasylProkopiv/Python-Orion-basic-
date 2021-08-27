

list_children_1 = ['david_2009', 'annaMaria_2005', 'gregory_2014', 'ilaria_2017']

names = []

for child_name in list_children_1:
    surname = child_name.split('_')[0].title()
    # surname = surname.title()
    names.append(surname)


print(names)
