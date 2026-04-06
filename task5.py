import requests, random
score, play = 0, "да"
while play.lower() == "да":
    data = requests.get("https://the-trivia-api.com/v2/questions").json()[0]
    q, ok = data['question']['text'], data['correctAnswer']
    options = data['incorrectAnswers'] + [ok]
    random.shuffle(options)
    print("\nВопрос:", q)
    for i in range(len(options)): print(f"{i+1}. {options[i]}")
    ans = input("Выбери номер: ")
    if ans.isdigit() and options[int(ans)-1] == ok:
        score += 1
        print("Верно!")
    else: print("Ошибка, правильно:", ok)
    print("Очков:", score)
    play = input("Продолжить? (да/нет): ")
print("Игра окончена, всего очков:", score)
