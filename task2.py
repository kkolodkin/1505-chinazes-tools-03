import random

def run():
    N = [int(i) for i in str(random.randint(1000,9999))]
    print('Я загадала 4-х значное число')
    n = [int(i) for i in str(int(input('Твой ход:')))]
    while len(n)!= 4:
        print('Это не 4-х значное число')
        n = [int(i) for i in str(int(input('Твой ход:')))]
    while N!= n:
        for i in range(4):
            if n[i]==N[i]:
                print('бык')
            if n[i]!=N[i] and n[i] in N:
                print('корова')
        n = [int(i) for i in str(int(input('Твой ход:')))]
        while len(n)!= 4:
            print('Это не 4-х значное число')
            n = [int(i) for i in str(int(input('Твой ход:')))]
    print('Ты угадал!')
