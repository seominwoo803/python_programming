li = [3, 7, 12, 18, 25, 31, 42, 56, 68, 79]
x = 31

l = 0
r = len(li) - 1

result = -1

while l <= r :

    mid = (l + r) // 2

    if li[mid] == x :

        result = mid

        break

    elif li[mid] < x :

        l = mid + 1

    else :

        r = mid - 1

print(f"x값의 위치 : {result}")
