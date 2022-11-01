def get_count_char(reg_main_str):

    slovar = {}
    NACHAL= 0
    for nov in reg_main_str:
        slovar[nov] = slovar.get(nov,NACHAL) + 1


    return slovar



main_str = """
    Данное предложение будет разбиваться на отдельные слова 
    В качестве разделителя для встроенного метода split будет выбран символ пробела На выходе мы получим список отдельных слов 
    Далее нужно отсортировать слова в алфавитном порядке а после сортировки склеить их с помощью метода строк join Приступим
"""
reg_main_str = ''.join(main_str.lower().split())

print(reg_main_str.isalpha())
print(get_count_char(reg_main_str), reg_main_str.isalpha())



