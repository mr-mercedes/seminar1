# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def predicat(x, y, z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        return True
    else:
        return False


x, y, z = [int(i) for i in input('Введите x y z: ').split()]
print(predicat(x, y, z))