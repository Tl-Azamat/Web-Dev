'''
Задача №253. Високосный год
Требуется определить, является ли данный год високосным. 
(Напомним, что год является високосным, если его номер кратен 4, 
но не кратен 100, а также если он кратен 400.)
'''

year = int(input())
print('YES' if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 'NO')