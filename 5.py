import requests
import random

score = 0
url = "https://the-trivia-api.com/v2/questions"

print("--- Викторина запущена! ---")

while True:
    response = requests.get(url)
    data = response.json() 
    
    current_question = data[0] 
    
    question_text = current_question.get('question', {}).get('text', 'Вопрос не найден')
    if question_text == 'Вопрос не найден':
        question_text = current_question.get('question', 'Вопрос не найден')
    
    correct = current_question['correctAnswer']
    options = current_question['incorrectAnswers'] + [correct]

    random.shuffle(options)
    
    print(f"\nВопрос: {question_text}")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    
    user_choice = input("\nТвой ответ (1-4) или '0' для выхода: ")
    
    if user_choice == '0':
        break
        
    try:
        index = int(user_choice) - 1
        if options[index] == correct:
            score += 1
            print("Правильно! +1")
        else:
            print(f"Неверно. Правильный ответ: {correct}")
        print(f"Текущий счет: {score}")
    except:
        print("Ошибка: введи число от 1 до 4!")

print(f"\nИгра окончена! Твой итоговый результат: {score}")
