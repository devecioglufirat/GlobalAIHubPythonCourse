from random import randint

A=[[[] for i in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        devam = True
        while devam:
            num = randint(0, 10000)
            if num > 1:
                for a in range(2, num):
                    if (num % a) == 0:
                        devam = True
                        break
                else:
                    A[i][j] = num
                    devam = False
print(A)