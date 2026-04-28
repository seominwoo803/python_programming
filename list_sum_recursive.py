def nn(n, li) :

    if n == 0 :

        return li[0]

    else :

        return li[n] + nn(n - 1, li)




li = [4, 5, 2, 9, 1]

print(nn(len(li) - 1, li))
