import test
import task1.py
import task2.py
import task3.py
import task4.py
import task5.py
import task6.py
import task7.py
import task8.py
import task9.py
import task10.py
import task11.py
import task12.py
import task13.py
import task14.py

def print_menu():
    print(
'''
============================
Menu options

1. Run Test Module
2. task2.py
0. Exit
============================
''')

print("Hello! Welcome to Chinazes Tools!")

while 1:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()
    
    if user_choice == '1':
        test.run()
    elif user_choice=='2':
        task2.run()
    elif user_choice == '0':
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")
