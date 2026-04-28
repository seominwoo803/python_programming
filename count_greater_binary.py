li = [2, 5, 8, 12, 17, 23, 31, 45, 52, 67]
x = 20


l = 0
r = len(li) - 1

rn = len(li)


while l <= r :

    mid = (l + r) // 2

    if li[mid] > x :

        r = mid - 1

        rn = mid

        

    else :

        l = mid + 1

count = len(li) - rn 

print(f'값 x보다 큰 값의 개수 : {count}')

    
