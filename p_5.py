i = 0
j = 2
vrai = 0

while vrai == 0:
    j = 1
    i += 60
    while j < 20:
        if i % j != 0:
            vrai = 0
            break
        vrai = 1
        j += 1

print i