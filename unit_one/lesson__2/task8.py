# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.


a = int(input())
b = int(input())
c = int(input())

x = b
y = c
b = a
c = x
a = y



print(a, b, c)
