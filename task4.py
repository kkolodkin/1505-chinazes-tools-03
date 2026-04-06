import random

while True:
    s = ['камень', 'ножницы', 'бумага']
    choice1 = input('Выбери: камень, ножницы, бумага: ')
    choice1 = choice1.lower()
    if choice1 in s:
        choice2 = random.choice(s)
        if (choice1 == 'камень' and choice2 == 'ножницы') or (choice1 == 'бумага' and choice2 == 'камень') or (choice1 == 'ножницы' and choice2 == 'бумага'):
            print('Мой выбор: ' + choice2)
            print('Ты выиграл')
        elif choice1 == choice2:
            print('Мой выбор: ' + choice2)
            print('Ничья')
        else:
            print('Мой выбор: ' + choice2)
            print('Я победил')
    else:
        print('Ошибка')
        
    
