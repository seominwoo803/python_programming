li = [3, 1, 4]
new_li = [ ]

for i in range(len(li)) :

    count = 0

    for j in range(i + 1, len(li)) :

        if  li[i] < li[j]:

            count += 1

    new_li.append(count)

new_li.append(count)

print(new_li)

        

    
