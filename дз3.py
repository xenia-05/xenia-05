#Вводится вектор. Вывести максимум из его элементов.

v = list(map(int, input().split()))
print(max(v))

#Вводится вектор. Заменить в нём каждое число Фибоначчи на следующее.

v = list(map(int, input().split()))
vnew =[]
def fib(n):
    a, b = 1, 1
    for i in range(1, n+1):
        a, b = b, a+b
        if n == a:
            return b
    return n
for i in range(len(v)):
    if fib(v[i]) == v[i]:
        vnew.append(v[i])
    else:
        vnew.append(fib(v[i]))
    
print(vnew)

'''Напишите программу, которая помогает определить какие вещи могут поместиться в рюкзак.
Вводится существующий объем рюкзака.
Затем вводятся объемы всех вещей, которые хочется туда поместить.
Нужно вывести список объемов вещей, которые поместятся в рюкзак.
Постарайтесь максимизировать кол-во вошедших вещей.'''

vr = int(input())
v = list(map(int, input().split()))
v = sorted(v)
vz = []
for i in range(len(v)):
    if vr - v[i] > 0:
        vz.append(v[i])
        vr = vr - v[i]
print(vz)
    



'''
Данные об email-адресах студентов хранятся в словаре: {домен:логины} .
Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном порядке и в формате имя_пользователя@домен
'''


dict_adress = {}
keyrea, keystudy = map(str, input().split())
valuerea = list(map(str, input().split()))
valuestudy = list(map(str, input().split()))
dict_adress[keyrea] = valuerea
dict_adress[keystudy] = valuestudy

polzovateli = []
for items in dict_adress['rea.ru']:
    polzovateli.append(items + '@' + 'rea.ru')
for items in dict_adress['study.com']:
    polzovateli.append(items + '@' + 'study.com')
print(sorted(polzovateli))





























       
    
    
     
