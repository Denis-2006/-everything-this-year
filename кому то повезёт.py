#знаки
'+' - складывает
'-' - вычитает
'=' - равенство
'==' - равняется ли одно число другому
'/' - деление
'//' - делит число нацело
'*' - умножение
'**' - степень
'%' - остаток от деления
'%x' - ищет числа кратные x

#команды:
1. print- вывод
2. int - работа c числами
3. input - считывание с консоли
4. float - работает с дробными числами
5. min - ищет минимальное число
6. max - ищет максимальное число
7. ord('x') - ищет код буквы x
8. chr('98') - ищет значение по коду 98
exit() - прекращает работу может вылететь)(лучше sys.exit())
import X - подключает функцию X
import os - 
import time:
    while True:
        
sys.quit() - без аварийно выходит из программы
if x i: - есть ли элемент x в массиве
f"Error: {x}" - выводит перед x Error

#import random
randint(0,10) - [0;10] в математике ерёт любые числа от 0 до 10
randint(0,10)
randrange(11) - [0;2),th`n k.,st xbckf jn 0 lj 10
randint(1,99)/100 - работает с дробными числами

#ГЕНЕРАТОР
[i + 5 for i in range(10)] - прибавляет каждому элементу 5
[i for i in a if i>0] -  оставляет только положительные элементы

#исключения
except - отлавливает исключения
Exception - все програмные исключения
import sys
as e - блок ошибки
else: - для написания логов (не работает с ботом из-за бесконечного цикла) 
sys.exit(0) - для завершения сценария и возврата кода 0
try:
    a = 5 / 5
except Exception as e:
    print(f"Error: {e}")

else:
    print("none")
finally:
    print('the end')
#масив с нохождением нулей путём укакзывания на число
a = [5,0,8,7,0,0,0,0,4,0,0]
X = 0
for i in range(len(a)):
if a[i] == 0:
X += 1
print(X)

#масив с нахождением нулей путём перебирания
a = [5,0,8,7,0,0,0,0,4,0,0]
X = 0
for i in a:
if i == 0:
X += 1
print(X)

#определениение чётного числа
a = int(input())
if a%2 = 0:
print('Yes')
else:
print('No')

#вывод чисел в обычном порядке или обратном
a = int(input())
b = int(input())
if a > b:
for i in range(a,b,-1):
print(i)
elif b > a:
for i in range(a,b):
print(i)
else:
print('числа равны')

#программа ищущая одинаковые числа в массиве
a = [1, 2, 3, 4, 4]
flag = False
for i in range (len(a)):
for j in range(len(a)):
if a[i] == a[j] and i != j:
flag = True
break
if flag == True:
print('Yes')
else:
print('No')

#массив[]
a = []
list(map(int,input().split()))- переводит числа в массив
#добавление
    a.append() - добовляет число в массив
    a.extend[] - обовляет несколько элементов в массив
    a.insert() - вставляет число по индексу
#удаление
    a.clear() - очищщает масссив
    a.remove() - очищщает число по значению (только один элемент)(по значению)
    a.pop() - удаляет и возвращает число из массива(по индекс)
#остальные
    a.count() - ищет сколько повтаряющихся значений указанных в скобках
    a.reverse() - переворачивает массив
    a.sort() - сортерует по возрастанию
    a.index() -узнаёт индекс элемента
    
len(a) - узнаёт размер массива
sum(a) - ищет сумму чисел в массиве
abs(i) - ищет модуль элемента
#картэж()

a[i] - ищет значение в массиве a по индексу i
a.split(' ') - разделяет массив по пробелу
#множество set()
a = set() - создаёт пустое множество
set(map(int,input().split()))- перевод из 
#добавление
    a.add() - добавляет значение в множесво
    a.apdate({}) - добавляет несколько значений в {}
#удаление
    a.discard() -удаляет значение(ничего не делает если его нет)
    a.remove() - очищщает число по значению (только один элемент)(по значению)
    a.pop() - удаляет и возвращает число из массива(по индекс)
    a.clear() - очищщает множество
#словарь{}
s = {} - создаёт пустой словарь
s = {1 : 2, 2 : 7} - создаёт словарь у которого 2 с ключом 1(1 : 2) и 7 с ключом 2(2 : 7)
s[1] = 2 - щет значение по ключу 1
print(s['d']) - выдаст исключение если его нет
s.clear() - отчищает словарь
s.yet('d') - 
s.pop(1) - даляет значение с ключом 1 
s.update ({3 : 5}) - добавляет 5 с ключом 3
list(s.keys()) - 
list(s.values()) - 
#кортеж
#htmi
find - находит первое совпадение
find_all - находит все совпадения и добавляет в массив

#циклы
for - для
while - пока

#код записывающий 5 чисел из консоли в массив
a = []
for i in range(5):
a.append(int(input()))
print(a)

#код ищющий среднее орифметическое число
a = []
for i in range(5):
a.append(int(input()))
for i in a:
b = sum(a) / len(a)
print(b)
git hub

#код для нахождения минимального числа по модулю
a = []
for i in range(5):
a.append(int(input()))
d = a[0]
for i in a:
if d > abs(i):
d = abs(i)
print(d)
#код для нахождения минимального индекса числа по модулю
a = []
for i in range(5):
a.append(int(input()))
d = a[0]
e = 0
for i in range(len(a)):
if d > abs(a[i]):
d = abs(a[i])
e = i
print(e)

#код узнающий кол одинаковых элементов
a = []
b = 0
d = 0
for i in range(5):
a.append(int(input()))
for i in a:
if a.count(i) > b:
b = a.count(i)
d = i
print(d)

#код узнающий какое число повторяется больше всего
a = [1,2,3,1,2,2,5,6]
counts = 0
i = 0
result = 0
while i < len(a):
if a.count(a[i])> counts:
counts = a.count(a[i])
result = a[i]
i += 1
print (result)

#код который выводит вторую половину массива
a = [-1,2,3,-1,2,-2,5,6]
print(a[len(a)//2: ])

#код для нахождения мин числа в масиве с инд
a = []
s = 0
b = 0
for i in range(5):
a.append(int(input()))
s = a[0]
for i in range(len(a)):
if i < s:
s = a[i]
b = i
print(s,b)
#код для нахождения макс числа в массиве с инд
a = []
s = 0
b = 0
for i in range(5):
a.append(int(input()))
for i in range(len(a)):
if a[i] > s:
s = a[i]
b = i
print(s,b)
#функции
#код для нахождения макс числа при помощи функций
def maxim(a):
s = a[0]
b = 0
for i in range(len(a)):
if a[i] > s:
s = a[i]
b = i
return str(s) + ' ' + str(b)
b = [1,2,3,4,1,5,6,7,4]
print(maxim(b))
#
a = list(map(int,input().split()))
#код для докупанию шаров до одинакогого количества
input()
a = list(map(int,input().split()))
one=[]
two=[]
result=0
for i in range(len(a)):
if a.count(a[i])==1 or a[i] not in one:
one.append(a[i])
print(one)
for i in range (len(one)):
two.append(a.count(one([i]))
print(two)
m = max(two)
for i in two:
if m>=i:
result+= m - i
print(result)
#код для вывидения чатов с новыми сообщениями на верх
def revers (a):
temp=[]
 
for i in range (len(a)-1,-1,-1):
if a[i] not in temp:
temp.append(a[i])
return temp

two = []
one = []
N = int(input())
for i in range(N):
one.append(input())
m = int(input())
for i in range(m):
two.append(input())
temp=revers(two)
for i in temp:
one.remove(i)
temp.extend(one)
for i in range(len(temp)):
print (temp[i])
#код для нахождения уникальных слов в предложениях в тексте
s = input()
razd = s.split('.')
for i in razd:
    temp = i.split()
    temp2 = set(temp)
    print(len(temp2))
    print(temp2)
#проверка номера
a = input()
flag = False
ABC = ["A", "B", "C", "E"]
nom = ['1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
if len(a) == 6:
    for i in range (6):
        if 0 < i < 4:
            if a[i] not in nom:
                flag = True
                break
        else:
            if a[i] not in ABC:
                flag = True
                break
else:
    flag = True
if flag == False:
    print('Yes')
else:
    print('No')
#работа с файлами
s = open("X.fd") - открывает файл X.fd (олько если в одной папке)
s.close() - закрывает файл
s.write('Привет') - переписывает файл и пишет привет
    #ткрывает файл из того же места (по строчно)
        s = open("2 февраля.py")
        for i in s:
            print(i)
        s.close()

    #открывает файл из того же места(целиком)
        s = open("2 февраля.py")
        print(read(s)
        s.close()

    #перезаписывает файл и пишет Привет
        s = open("фигня какая-то.py", 'w')
        s.write('Привет')
        s.close()

    #добавляет в конец файла 'Привет'
        s = open("фигня какая-то.py", 'a')
        s.write('Привет')
        s.close()

    #комбо дозаписи и считывания
        s = open("фигня какая-то.py", 'a')
        s.write('Привет')
        s.close()
        s = open("фигня какая-то.py")
        print(s.read())
        s.close()
    #нахождение уникальных слов в предложении через файлыт
        s = open("tada.txt", "r")
text = s.read()

open("result.txt", "w", encoding = "utf - 8").close()
razd = text.split('.')
for i in razd:
    temp = i.split()
    temp2 = set(temp)
    print(len(temp2))
    s.close()
    s = open("result.txt", "a")
    s.write(str(len(temp2)) + "\n")
    s.close()
    s = open("result.txt", "r")
    print(s.read())
    s.close()

from tkinter import * - подключает библиотеку(ВСЮ)
root=Tk() - оздаёт главное окно
root.geometry ("400x400") адаёт размер размер окна
root.resizable(False,False)
but=Button(text="итальянские макаронни") создай кнопку и называем
but.pack() расположи элемент(
but.place(height=5,wiath,x=5,y=5) много чего задает высоту и т,д
root.title("дЕНИс") низвание фигни
but.bind("<Button-1>",klicer) связывает события с функции

def klicer (event):
    but["text"]="фигер"
root.mainloop() обрпбатывает события          
 #код для кликера чекк
from tkinter import *
schet=0
def klicer (event):
    global schet
    schet+=1000
    but["text"]=schet
    
root = Tk()
root.title("дЕНИс")
root.geometry ("500x500")
but["text"]="фигер"
but=Button(text="фигер")
#расположение кнопки
but.pack() распологает кнопку (сверху по середине)
but.place(height=500, width=40,x=5,y=5)
but.greed(row=50,coloum=50) 
root.title("дЕНИс") 
but.bind("<Button-1>",klicer) 
root.mainloop() - обрабатывает событие
a.resizable(width=False, height=False) - запрещает изменение экрана cmd
a.resizable(width=True, height=True) - разрешает изменение экрана cmd
        #базы данных
`id` INTEGER PRIMARY KEY AUTOINCREMENT - делает id строки автоматом
a = 
          

               


              

