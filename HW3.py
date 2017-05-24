# Задача 1
# x1 = input('x1=')
# x1 = int()
# x2 = input('x2=')
# x2 = int()
# y1 = input('y1=')
# y1 = int()
# y2 = input('y2=')
# y2 = int()
#
# def distance (x1, x2, y1, y2):
#             result = (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** (1 / 2)
#             return result
#
# print('distance', distance(x1, x2, y1, y2))

# x1 = int(input('x1='))
# y1 = int(input('y1='))
# x2 = int(input('x2='))
# y2 = int(input('y2='))
# def distance(x1, y1, x2, y2):
#     return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)
# print (distance(x1, y1, x2, y2))

# почему-то первый варант не работает?

# Задача 2

# y = int(input('year='))
#
# def is_year_leap (y):
#     if (y%4==0 and  y%10 >= 0) or y%400 == 0:
#         result = True
#     else:
#         result = False
#     return result
#
# print (is_year_leap (y))

# Задача 3

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

def triangle (a, b, c):
    if a+b>c and b+c>a and c+a>b:
        result = True
    else:
        result = False
    return result

print (triangle (a, b, c))

