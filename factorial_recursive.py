def nn(n) :

    if n <= 1 :

        return 1

    else :

        return n * nn(n - 1)

n = int(input("정수 입력 :"))

print(nn(n))
    
