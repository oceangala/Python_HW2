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