import os
from tkinter import *
import random
import time

def print_mass(a):
    os.system("cls")
    for i in a:
        print(i)
        
def tick(n, m):
	global entries
	temp = [[False for col in range(m)] for row in range(n)]

	for row in range(n):
		for col in range(m):
			if neighboard(row, col) == 3:
				temp[row][col] = True
			elif entries[row][col] == True and neighboard(row, col) == 2:
				temp[row][col] = True
			else:
				temp[row][col] = False

def my_count(a, i, j):
    res = 0
    if a[i][j-1] == 1:
        res += 1
    if a[i-1][j] == 1:
        res += 1
    if a[i-1][j-1] == 1:
        res += 1
    if a[i][j+1] == 1:
        res += 1
    if a[i+1][j] == 1:
        res += 1
    if a[i+1][j+1] == 1:
        res += 1
    if a[i+1][j-1] == 1:
        res += 1
    if a[i-1][j+1] == 1:
        res +=1
    return res

os.system("cls")

n = 10
a = []

wind = Tk()
wind.geometry('300x300')
wind.resizable(width=False, height=False)
wind.title("Жизнь")
wind['bg'] = 'grey22'

#while True:  
for i in range(n):
    a.append([random.randrange(2) for i in range(n)]) #генерировали в каждом элементе массива другой массив длинной в m
#print_mass(a)
#[random.randrange(0,3,2) for j in range(m)]
while True:
    temp = []
    temp = a.copy()
    for i in range(1,len(a)-1):
        for j in range(1,len(a[i])-1):
            if (a[i][j] == 1 and my_count(a,i,j) == 2) or my_count(a,i,j) == 3:
                temp[i][j] = 1
            else:
                temp[i][j] = 0
    a = temp.copy()
    print_mass(a)
    wind.mainloop()
    time.sleep(2)

#print (my_count(a,i,j))
    #time.sleep(0.9)
#print("==============================")

