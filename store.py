from termcolor import colored, cprint
import sys
import os
import Dataframex
import time
import cart


def main():
    """Entry point of the application."""
    menu("Please Enter a Valid Option")


def menu(optiontext, filtered=False, df=Dataframex.dataframa()):
    """
    Display main menu and handle user choices.
    
    Args:
        optiontext (str): The prompt text to display
        filtered (bool): Flag for filter mode
        df: The products dataframe
    """
    # Display store header
    cprint('***************Welcome to DEUS Online Retail Store Demo*****************\n', "cyan")
    
    # Show products dataframe
    print(df)
    
    # Get user input
    choice = input(colored(f"""
                      A: Filter
                      B: Add Products to Cart
                      C: Go to Shopping Cart
                      Q: Reset

                      {optiontext}: """, "yellow"))

    # Handle user choice
    if choice.lower() == "q":
        # Reset to initial state
        os.system('cls')
        main()
    elif filtered:
        # Handle filter operation
        try:
            os.system('cls')
            menu("Please Enter a Valid Option", 
                 df=Dataframex.filtered_dataframa(choice))
        except:
            os.system('cls')
            cprint('Invalid Command. Please Try Again', "red")
            filtor()
    elif choice.lower() == "a":
        # Enter filter mode
        os.system('cls')
        filtor()
    elif choice.lower() == "b":
        # Add products to cart
        try:
            text = input("Enter Products Number: ")
            cart.save_product(list(set(map(int, text.split()))))
            os.system('cls')
            cprint("Products Saved to Cart", "green")
            main()
        except:
            os.system('cls')
            cprint("Enter Valid Product Number", "red")
            main()
    elif choice.lower() == "c":
        # Go to shopping cart
        os.system('cls')
        cart.main()
    else:
        # Invalid input
        os.system('cls')
        cprint('Invalid Command. Please Try Again', "red")
        menu("Please Enter a Valid Option")


def filtor():
    """Display and handle product filtering interface."""
    menu("Please Enter Your Filtering Criteria", filtered=True)


if __name__ == "__main__":
    os.system('cls')
    main()
