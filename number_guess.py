import random

n = random.randint(1, 10)

count = 0

while True :

    me = int(input("1~10사이의 값 입력 :"))

    count += 1

    if me == n :

        break

    elif me > n :

        print("Down")

    else :

        print("Up")

print(f"정답입니다! 시도 횟수 : {count}")

    

