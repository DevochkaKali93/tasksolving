#УСЛОВИЯ ЗАДАЧИ
#Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке.

#РЕШЕНИЕ

size = int(input())
total = size*size
h = 1
m = 0
number = 1
x = 0
y = 0

a = [[0 for j in range(size)] for i in range(size)]


while number <= total:
  while y <= size-1:
    a[x][y] = number
    number+=1
    if y < size-1:
      y+=1
    else:
        break
  x+=1
  while x <= size-1:
    a[x][y] = number
    number+=1
    if x < size-1:
      x+=1
    else:
        break
  y-=1
  while y >=m:
    a[x][y] = number
    number+=1
    if y > m:
      y-=1
    else:
        break
  x-=1
  while x > m:
    a[x][y] = number
    number+=1
    if x > m:
      x-=1
    else:
        break
  size = size-1
  y+=1
  x+=1
  h+=1
  m+=1
           
import math  
n = 0  #для построчного вывода списка
while n < math.sqrt(total):  
  print(*a[n])
  n+=1


