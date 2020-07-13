# Названия городов: напишите функцию city_country(), которая получает название города и страну. Функция должна возвращать 
# строку в формате “Santiago, Chile”. Вызовите свою функцию по 
# крайней мере для трех пар «город—страна» и выведите возвращенное значение.


def city_country(**kwargs):
    for value in kwargs.values():
        print(value, end=',')
city_country(citi='Kara-Balta',country='Kyrgizstan')
city_country(citi='Moscow',country='Russiya')
city_country(citi='London',country='Angliya')