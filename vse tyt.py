'''age = 18
name = 'lenya'
name2 = 'Piton'
print('Vozrast {} - {}'.format(name, age))
print('Pochemy {0} izuchaet yazik programmirovania - {1}'.format(name, name2))
print('{0:$^25}'.format('CASH'))'''
#1)Написать программу вычисления площади параллелограмма.
'''a=int(input('Ведите высоту - '))
b=int(input('Ведите ширину - '))
s=a*b
print('Площадь прямоугольника - ', s)'''
#2)Написать программу вычисления площади треугольника, если известны длины двух его сторон и величина угла между этими сторонами
'''import cmath
a= fint(input('Введите сторону а - '))
b= int(input('Введите сторону б - '))
x= int(input('Введите велечину угла - '))
s=0.5*a*b*cmath.sin((x*cmath.pi)/180)
print('Площадь треугольника - ', s)'''
#3)Написать программу, которая вычисляет частное от деления двух чисел. Программа должна проверять правильность введенных пользователем данных и, если они неверные (делитель равен нулю), выдавать сообщение об ошибке.
'''a=float(input('Введите число а:'))
b=float(input('Введите делитель б:'))
if b==0:
    print('error')
else:
    c=a/b
    print('Частное от деления а и б - ', c)
print('Завершено')'''
#4)Написать программу вычисления стоимости покупки с учетом скидки. Скидка в 3% предоставляется в том случае, если сумма покупки больше 500 руб., в 5% — если сумма больше 1000 руб.
'''a= int(input('Введите стоимость покупки - '))
if a>=1000:
    a= (a/100)*95
    print('Вам предаствляется скидка 5 %')
    print('Стоимость товара с учетом скидки - ', a)
elif a>=500:
    a= (a/100)*97
    print('Вам предаствляется скидка 3 %')
    print('Стоимость товара с учетом скидки - ', a)
else:
    print('Скидки нет')
print('Завершено')'''
#5)Найти все натуральные делители заданного с клавиатуры числа х.
'''x=int(input('Введите число х:'))
for i in range(1, x):
    if x%i==0:
        print(i)
print('Завершение')'''
#6)Найти все целые двухзначные числа кратные 7.
'''a=[]
x=int(input('Введите размер массива: '))
for i in range(x):
    a.append(int(input('Заполните массив - ')))
for i in range(x):
    if(a[i]%7==0):
        print(a[i])'''
#7)Найти все целые двузначные числа, сумма цифр которых равна 8.
'''a=[]
x=int(input('Введите размер массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
for i in range(x):
    j=a[i]//10
    k=a[i]%10
    if (j+k==8):
        print(a[i])'''
#8)В линейном массиве вещественных чисел a(n) заменить все элементы, большие 10 на число с.
'''a=[]
x=int(input('Введите размер массива: '))
for i in range(x):
    a.append(float(input('Заполните массив: ')))
c=int(input('Введите число С - '))
for i in range(x):
    if(a[i]>=10):
        a[i]=c
for i in range(x):
    print(a[i])'''
#9)В линейном массиве вещественных чисел a(n) заменить все элементы, кратные введенному числу d, на их квадраты.
'''a=[]
x=int(input('Введите размер массива: '))
d=float(input('Введите число d - '))
for i in range(x):
    a.append(float(input('Заполните массив: ')))
for i in range(x):
    if(a[i]%d==0):
        a[i]*=a[i]
for i in range(x):
    print(a[i])'''
#10)Удалить наименьший элемент массива.
'''a=[]
x=int(input('Введите размер массива: '))
min=1000
for i in range(x):
    a.append(int(input('Заполните массив: ')))
for i in range(x):
    if(min<a[i]):
        min=i
        a[i]=0
for i in range(min, x):
    a[i]=a[i+1]
    a[i+1]=0
for i in range(x-1):
    print(a[i])'''
#11)Удалить элемент массива вещественных чисел, больший заданного числа.
#Если таких элементов нет, выдать сообщение «элементы для удаления не найдены».
'''a=[]
k=0
x=int(input('Введите размер массива: '))
c=float(input('Введите число: '))
for i in range(x):
    a.append(float(input('Заполните массив: ')))
for i in range(x):
    if(a[i]>c):
        a[i]=0
        k+=1
for i in range(x-1):
    if(a[i]==0):
        a[i]=a[i+1]
        a[i+1]=0
for i in range(x-k):
    print(a[i])'''
#12)В линейный массив целых чисел вставить на 3 – е место вставить число,
# равное сумме первых двух чисел первого элемента.
'''a=[]
x=int(input('Введите размер массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
c = str(a[0])[:2]
c = int(c)
for i in range(x+1, 3):
    a[i]=a[i-1]
a[2]=(int(c/10))+int((c%10))
for i in range(x+1):
    print(a[i])'''
#13)В линейный массив целых чисел вставить на k- ое место число,
# равное разности минимального и максимального элементов массива.
'''a= []
x=int(input('Ввыедите размер массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
k=int(input('Введите номер k-го места: '))
min=1000
max=-1000
for i in range(x):
    if(min>a[i]):
        min= a[i]
    if(max<a[i]):
        max=a[i]
for i in range(x+1, k):
    a[i]=a[i-1]
a[k-1]=min-max
for i in range (x+1):
    print(a[i])
print('Завершение')'''
#14)Написать программу, которая методом простого выбора
# сортирует по убыванию введенный с клавиатуры одномерный массив.
'''a = []
x=int(input('Введите размер массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
for j in range(x):
    for i in range(x-1):
        if(a[i]<a[i+1]):
            k=a[i+1]
            a[i+1]=a[i]
            a[i]=k
for i in range(x):
    print(a[i])'''
#15)Написать программу, которая из первого массива выбирает только четные числа,
# а из второго только нечетные и объединяет их в один массив,
# отсортированный по убыванию.
'''a=[]
b=[]
c=[]
k=0
x=int(input('Введите размер 1-го массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
y=int(input('Введите размер 2-го массива: '))
for i in range(y):
    b.append(int(input('Заполните массив: ')))
for i in range(x):
    if((a[i]%2)==0):
        c.append(a[i])
        k+=1
for i in range(y):
    if((b[i]%2)==1):
        c.append(b[i])
        k+=1
for j in range(k):
    for i in range(k-1):
        if(c[i]<c[i+1]):
            d=c[i+1]
            c[i+1]=c[i]
            c[i]=d
for i in range(k):
    print(c[i])
print('Завершение')'''
#16)Написать программу, которая объединяет два упорядоченных по возрастанию массива
# в один, также упорядоченный по убыванию массив.
'''a=[]
b=[]
c=[]
x=int(input('Введите размер 1-го массива: '))
for i in range(x):
    a.append(int(input('Заполните массив: ')))
    c.append(a[i])
y=int(input('Введите размер 2-го массива: '))
for i in range(y):
    b.append(int(input('Заполните массив: ')))
    c.append(b[i])
z=x+y
for j in range(x):
    for i in range(x-1):
        if(a[i]>a[i+1]):
            k=a[i+1]
            a[i+1]=a[i]
            a[i]=k
print('Первый отсартированный массив: ')
for i in range(x):
    print(a[i])
for j in range(y):
    for i in range(y-1):
        if(b[i]>b[i+1]):
            k=b[i+1]
            b[i+1]=b[i]
            b[i]=k
print('Второй отсартированный массив: ')
for i in range(y):
    print(b[i])
for j in range(z):
    for i in range((z)-1):
        if(c[i]<c[i+1]):
            k=c[i+1]
            c[i+1]=c[i]
            c[i]=k
print('Третий отсартированный массив: ')
for i in range(z):
    print(c[i])
print('Заверщение')'''