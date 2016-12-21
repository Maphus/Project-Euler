i = 21
j = 1
vrai = 0

while vrai == 0:
    j = 1
    while j < 21:
        vrai = 1
        if i % j != 0:
            vrai = 0
        j+=1
    i += 1

print i