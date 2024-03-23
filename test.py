# from 1 to 100 print the prime numbers
for i in range(2, 101):
    if i % 2 == 0 or i % 3 == 0:
        continue
    for j in range(5, int(i ** 0.5) + 1, 6):
        if i % j == 0:
            break
    else:
        print(i)

