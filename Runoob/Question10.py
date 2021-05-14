def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


for i in range(101, 201):
    if prime(i):
        print(i, end=' ')
