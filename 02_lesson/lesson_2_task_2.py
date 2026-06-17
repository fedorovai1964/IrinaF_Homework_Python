def is_year_leap(year):
    return year % 4 == 0


int_year = int(input('Введите год:'))
result = is_year_leap(int_year)
print(f'год {int_year}: {result}')
