t = "aaabbc"

count = 1

text = [ ]

for i in range(len(t) - 1) :

    if t[i] == t[i + 1] :

        count += 1

    else :
        text.append(count)

        count = 1

text.append(count)

print(text)

    
