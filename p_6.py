real = 0
real2 = 0

for i in range(101):
    sumsquares = i * i
    real += sumsquares
    real2 += i

final = real2 * real2
final = final - real

print(final)