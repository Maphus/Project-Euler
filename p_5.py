i = 21
j = 1
vrai = 0

while vrai == 0:
    j = 1
    while j < 21:
        if i % j != 0:
            vrai = 0
            break
        vrai = 1
        j+=1
    i += 1

print i