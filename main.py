import task1
import task2

import task4
import task5
import task6
import task7

import task9

import task11
import task12
import task13
import task14

def print_menu():
    print(
'''
============================
Menu options

1. Run task1.py
2. Run task2.py
3. Run task3.py
4. Run task4.py
5. Run task5.py
6. Run task6.py
7. Run task7.py
8. Run task8.py
9. Run task9.py
10. Run task10.py
11. Run task11.py
12. Run task12.py
13. Run task13.py
14. Run task14.py


0. Exit
============================
''')

print("Hello! Welcome to Chinazes Tools!")

while 1:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()
    
    if user_choice == '1':
        task1.run()
    elif user_choice=='2':
        task2.run()
    elif user_choice=='4':
        task4.run()
    elif user_choice=='5':
        task5.run()
    elif user_choice=='6':
        task6.run()
    elif user_choice=='7':
        task7.run()
    elif user_choice=='9':
        task9.run()
    elif user_choice=='11':
        task11.run()
    elif user_choice=='12':
        task12.run()
    elif user_choice=='13':
        task13.run()
    elif user_choice=='14':
        task14.run()
    elif user_choice == '0':
        print("Bye!")
        break
    else:
        print("Invalid choice. Try again.")
