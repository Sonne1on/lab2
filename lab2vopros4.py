import csv


def esc(code):
    return f'\u001b[{code}m'


WHITE = esc(47)
BLACK = esc(107)
END = esc(0)
RED = esc(41)

bef_1997 = 0
aft_1997 = 0
a = 0

with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for r in table:        # Посчитаем кол-во до 1997 года и после
        if a != 0:
            if r[6][6:10] <= '2017':
                bef_1997 += 1
            else:
                aft_1997 += 1
        a += 1

bef_p = int((bef_1997/(bef_1997+aft_1997))*100)           # Пересчитаем в процентах до 1997
aft_p = 100 - bef_p           # Пересчитаем в процентах после 1997

print(f'             До 2017 {bef_p}%')
print(f'{BLACK + " " * bef_p + END} {bef_1997} шт')
print()
print(f'          После 2017 {aft_p}%')
print(f'{RED + " " * aft_p + END} {aft_1997} шт')
