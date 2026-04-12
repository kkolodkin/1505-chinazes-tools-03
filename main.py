import test
import task2


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
