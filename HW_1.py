# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
#______________________________
# print("Input your number: ")
# num = input()

# res = 0
# i = 0
# s = len(num)
# while (i < s):
#     res += int(num[i])
#     i+=1

# print(res)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
#____________________________

# sum = int(input("Input the nimber of toys: "))
# p = sum / 3 / 2
# s = sum / 3 / 2
# k = sum / 3 * 2
# print(f'Petya made {p} toys, Serezha made {s} toys, Kate made {k} toys')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
#  получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

# num = (input("Inter your ticket's number: "))
# if (int(num[0]) + int(num[1]) + int(num[2]) == int(num[-1]) + int(num[-2]) + int(num[-3])):
#     print("This's a lucky ticket")
# else:
#     print("This's not a lucky ticket")
    
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Долек в длинну: "))
m = int(input("Долек в ширину: "))
chocolate = n * m

k = int(input("Хотим отломить долек: "))

if (chocolate % k == m or chocolate % k == n and chocolate > k):
    print("Yes")
else:
    print("NO")