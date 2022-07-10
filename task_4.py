# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def find_coordinate(number):
    if number == 1:
        return f'x = (0; +бесконечности), y = (0; +бесконечности)'
    elif number == 2:
        return f'x = (-бесконечности; 0), y = (0; +бесконечности)'
    elif number == 3:
        return f'x = (-бесконечности; 0), y = (-бесконечности; 0)'
    elif number == 4:
        return f'x = (0; +бесконечности), y = (-бесконечности; 0)'
    elif number <  1 or number > 4:
        return 0
        
        
    

user_number = int(input('Введите номер четверти от 1 до 4: '))
if find_coordinate(user_number) == 0:
    print(f'Четверти номер {user_number} не существует, введите число от 1 до 4')
else:
    print(f'Диапазон возможных точек для {user_number} четверти {find_coordinate(user_number)}')
