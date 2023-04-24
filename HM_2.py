# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# import random
# coins = int(input("Enter a number of coins: "))
# list1 = []

# for i in range (0, coins):
#     list1.append(random.randint(0, 1))
# print(list1)

# countUp = 0
# countDown = 0
# for i in range (0, coins-1):
#     if list1[i] == 0:
#         countDown += 1
#     else:
#         countUp += 1

# print(min(countUp, countDown))

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# import random

# one = random.randint(0, 1000)
# two = random.randint(0, 1000)

# s = one + two
# p = one * two
# print(one, two, s, p)

# for i in range (0, s):
#     if i * (s - i) == p:
#         print(i, s - i)
#         break
#     else: 
#         i+=1


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#  не превосходящие числа N.

n = int(input('Enter your number: '))

for i in range(n):
    res = 2**i
    i+=1
    if res < n:
        print(res)
    else:
        break