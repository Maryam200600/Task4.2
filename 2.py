# Написать функцию is_ye”. Вызовите свою функцию по ar_le”. Вызовите свою функцию по ap, принимающую 1 аргумент — год, и
# возвращающую True”. Вызовите свою функцию по , если год високосный, и False”. Вызовите свою функцию по  иначе.

def is_year_leap(year):
    if year%4==0:
        return 'true'
    else:
        return 'false'
x=int(input('enter year: '))
print(is_year_leap(x))