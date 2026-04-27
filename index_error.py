li = [10, 20, 30, 40, 50]

try :

    idx = int(input("인덱스 입력 :"))

    print(li[idx])

except ValueError :

    print("Number Error")

except IndexError :

    print("Index Error")
