# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.


import random
count0 = 0
count1 = 0
for i in range(5):
    x = random.randrange(0, 2, 1)
    print(x, end=" ")
    if x == 0:
        count0+=1
    else:
        count1+=1
print()
print('Придется перевернуть монеток: ', min(count1, count0))