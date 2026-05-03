li = [ ]

while True :

    try :

        n = int(input("정수를 입력하세요 :"))

        break

    except ValueError :

        print("정수 형태로 입력해주세요")

while n != 0 :

    li.append(n % 10)

    n //= 10


print(max(li))

    

    
