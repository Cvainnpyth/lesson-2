year = int (input ('Год рождения А.С. Пушкина? '))
if year == 1799:
    day = int(input('А какой день рождения А.С. Пушкина? '))
    if day == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')