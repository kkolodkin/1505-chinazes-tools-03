import random
def run():
    L = int(input('Длинна пароля:'))
    while L<1 or L>100:
        print('Пароль должен быть от 1 до 100 символов.')
        L = int(input('Длинна пароля:'))
    alp = 'qwertyuiopasdfghjklzxcvbnm'
    S = '!@#$%^&*()_+{}:"<>?,./;[]\|/"`~' + "'"
    ALP = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    N = '1234567890'
    n = input('Использовать цифры?(Да/Нет):')
    if n == 'Да':
        alp += N
    s = input('Использовать спец символы?(Да/Нет):')
    if s == 'Да':
        alp += S
    a = input('Использовать заглавные буквы?(Да/Нет):')
    if a == 'Да':
        alp += ALP
    password = "".join(random.sample(alp,L))
    print(password)

