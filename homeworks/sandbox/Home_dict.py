def transliterate(name):
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'ґ': 'g', 'д': 'd', 'е': 'e',
              'є': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'ї': 'i', 'й': 'i',
              'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
              'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
              'ш': 'sh', 'щ': 'sch', 'ь': '', 'ю': 'u', 'я': 'ya',
              'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ґ': 'g', 'Д': 'D', 'Е': 'E',
              'Є': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'І': 'i', 'Ї': 'i', 'Й': 'i',
              'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
              'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'CH',
              'Ш': 'SH', 'Щ': 'SCH', 'Ь': '', 'Ю': 'U', 'Я': 'YA',
              }

    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

print(transliterate(name='Кохайтеся, чорнобриві\n'
                         'Та не з москалями\n'
                         'Бо москалі - чужі люди\n'
                         'Роблять лихо з вами\n'
                         'Москаль любить жартуючи\n'
                         'Жартуючи кине\n'
                         'Піде в свою Московщину\n'
                         'А дівчина гине...\n'
                         'Якби сама, ще б нічого\n'
                         'А то й стара мати\n'
                         'Що привела на світ божий\n'
                         'Мусить погибати\n'
                         'Серце в\'яне співаючи\n'))
# Коли знає за що
# Люде серце не побачать
# А скажуть - ледащо!
# Кохайтеся ж, чорнобриві
# Та не з москалями
# Бо москалі - чужі люде
# Знущаються вами
# Сміються над нами
# Сміються над вами...
# Не слухала Катерина
# Ні батька, ні неньки
# Полюбила москалика
# Як знало серденько
# Полюбили молодого
# В садочок ходила
# Поки себе, свою долю
# Так занапастила
# Кличе мати вечеряти
# А донька не чує
# Де жартує з москаликом
# Там і заночує
# На дві ночі карі очі
# Любо цілувала
# Поки слава на все село
# Недобрая стала
# Нехай собі тії люде
# Що хотять говорять
# Вона любить та не чує
# Що вкралося горе
# Прийшли вісті недобрії -
# В поход затрубили
# Пішов москаль в Туреччину
# Катрусю накрили
# Незчулася, та й байдуже
# Що коса покрита:
# За милого, як співати
# Любо й потужити
# Обіцявся чорнобривий
# Коли не загине
# Обіцявся вернутися
# Тойді Катерина
# Буде собі московкою
# Забудеться горе
# А поки що, нехай люде
# Що хотять говорять
# Нехай що хотять нам говорять.
# Нам говорять!'))
