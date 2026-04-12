import random

def run():
    while True:
        first = int(input('(макс. -10**10). Начальное число: '))
        last = int(input('(макс. 10**10). Конечное число: '))
        if last > 10**10 or first < -(10**10):
            print('Ошибка')
        elif first>last:
            print('Ошибка')
        else:
            number = random.randint(first,last)
            while True:
                number2 = int(input('Гадай число: '))
                if number2 == number:
                    print('Ты победил')
                    break
                elif number > number2:
                    print('Гадай больше')
                elif number < number2:
                    print('Гадай меньше')
        break
            
        
