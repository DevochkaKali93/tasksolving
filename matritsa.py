#УСЛОВИЯ ЗАДАЧИ
#Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
#Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

#РЕШЕНИЕ

#ввод данных
sp = input()
list=[]
while sp != "end":
    list.append(sp)
    sp = input()
    
#преобразование в двухмерный список

dlstr = len(list) - 1 
n = 0
while n <= dlstr:
    list[n]= list[n].split()
    n+=1
    
n = 0
m = 0
dm = len(list[0])-1

while n <= dlstr:
    while m <= dm:
        list[n][m] = int(list[n][m])
        if m <= dm:
            m+=1
    n+=1
    m = 0


dlstr = len(list) - 1
dm = len(list[0])-1
list2= [[0 for x in range(dm+1)] for y in range(dlstr+1)]

#Вычисления  

for x in range(dlstr+1): 
    for y in range(dm+1):
        if y == dm and x == dlstr:
           list2[x][y] =  list[x-1][y] +  list[x-dlstr][y] +  list[x][y-1] +  list[x][y-dm] 
           break
        if y == dm:
            list2[x][y] =  list[x-1][y] +  list[x+1][y] +  list[x][y-1] +  list[x][y-dm]
        elif x == dlstr:
            list2[x][y] =  list[x-1][y] +  list[x-dlstr][y] +  list[x][y-1] +  list[x][y+1]
        else:    
            list2[x][y] =  list[x-1][y] +  list[x+1][y] +  list[x][y-1] +  list[x][y+1]
            #x  y

#Вывод    
n = 0  #для построчного вывода списка
while n <= dlstr:  
  print(*list2[n])
  n+=1
