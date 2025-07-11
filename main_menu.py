import time
from termcolor import colored, cprint
import csv
import sys
import os
import store


def main():
    menu()


def menu():
    """Display the main menu and handle user input."""
    cprint('*************** Welcome to DEUS Online Retail Store Demo ***************', "cyan")

    choice = input(colored("""
                      A: Register
                      B: Login
                      Q: Quit

                      Please enter a valid option: """, "yellow")).upper()  # Normalize input to uppercase

    if choice == "A":
        os.system('cls')
        register()
    elif choice == "B":
        os.system('cls')
        login()
    elif choice == "Q":
        sys.exit()
    else:
        os.system('cls')
        cprint('Invalid command. Please try again.', "red")
        menu()


def register():
    """Register a new user by saving username and password to a file."""
    print(colored("****** PLEASE REGISTER ******", "yellow"))
    username = input(colored("Enter a username: ", "white", attrs=['reverse', 'blink']))
    password = input(colored("Enter a password: ", "white", attrs=['reverse', 'blink']))

    # Save username and password in a CSV file
    with open('username_passwords.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        cprint("** Record has been written to file **", "green")
    
    time.sleep(4)
    os.system('cls')
    menu()


def login():
    """Authenticate user by checking credentials against stored records."""
    print(colored("****** PLEASE LOGIN DEAR CUSTOMER ******", "yellow"))
    is_authenticated = False
    username = input(colored("Enter username: ", "white", attrs=['reverse', 'blink']))
    password = input(colored("Enter password: ", "white", attrs=['reverse', 'blink']))

    # Check if credentials match any stored records
    with open("username_passwords.txt", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:  # Check both fields
                is_authenticated = True
                break

    if not is_authenticated:
        cprint("Wrong username or password! Please try again.", "red")
        time.sleep(3)
        os.system('cls')
        login()
    else:
        cprint("\nLogin successful!", "green")
        time.sleep(4)
        os.system('cls')
        store.main()


if __name__ == "__main__":
    os.system('cls')
    main()
