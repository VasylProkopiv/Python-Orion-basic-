# import goslate
# l = [1 , 2 , 3 , 4, 5, 6, 7, 8, 9, 10]
# l.append(11)
# l.append(12)
# print(l[0])
# print(l[:-1:2])
# print(l)
stringa = 'Гетьте, думи, ви, хмари осінні! \nТо ж тепера весна золота!\nЧи то так у жалю, в голосінні\n' \
    'Проминуть молодії літа?\nНі, я хочу крізь сльози сміятись,\nСеред лиха співати пісні'
stringa_1 = 'Як умру, то поховайте Мене на могилі Серед степу широкого На Вкраїні милій, Щоб лани широкополі, ' \
     'І Дніпро, і кручі Було видно, було чути, Як реве ревучий. Як понесе з України У синєє море Кров ворожу... ' \
     'отойді я І лани і гори — Все покину, і полину До самого Бога Молитися... а до того Я не знаю Бога. ' \
     'Поховайте та вставайте, Кайдани порвіте І вражою злою кров’ю Волю окропіте. ' \
     'І мене в сем’ї великій, В сем’ї вольній, новій, Не забудьте пом’янути Незлим тихим словом.'
# print(s)
lesja = stringa
taras = stringa_1
# print(id(lesja))
# print(id(s))
# print(lesja)
# l = s.split('\n')
list_1 = lesja.split()
list_2 = taras.split()
# s2 = s.translate()
list_3 = ' '
virsh = list_3.join(list_2)

# print(lesja)
# print('експереент з лістом №0',list_1)
# print('експереент з лістом №1',list_1[2:12])
# print('експереент з лістом №2', list_1[2:12:4])
# print(virsh)

list_children_1 = ['David_2009', 'AnnaMaria_2005', 'Gregory_2014', 'Ilaria_2017']

def by_year(name):
    return name.split('_')[-1]

# print(by_year(list_children_1[1]))
sorted_children = sorted(list_children_1, key=by_year)
print(sorted_children)
