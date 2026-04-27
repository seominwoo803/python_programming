import random

count = 0

for _ in range(20) :

    n = random.randint(1, 30)

    if n % 2 == 0 :

        count += 1

print("짝수 개수 :", count)



