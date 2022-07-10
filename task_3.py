# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def find_quoter(x, y):
    if y > 0 and x > 0:
        return 1
    elif y > 0 and x < 0:
        return 2
    elif y < 0 and x < 0:
        return 3
    elif y < 0 and x > 0:
        return 4
    else:
        return 0

x, y = [int(i) for i  in input('Введите значения X и Y: ').split()]
if find_quoter == 0:
    print('Error: X ≠ 0 и Y ≠ 0, input another x and y')  
else:
    print(f'Точка с координатами х = {x} у = {y} находится  в четверти {find_quoter(x, y)}')