import time
from termcolor import colored, cprint
import csv
import sys
import os
import Dataframex


def main():
    """Entry point for the shopping cart application."""
    menu("Please Enter a Valid Option")


def menu(optiontext):
    """
    Display shopping cart menu and handle user input.
    
    Args:
        optiontext (str): The prompt text to display to the user
    """
    # Display shopping cart header
    cprint('****************************** Shopping Cart ******************************', "cyan")
    
    # Try to display cart contents
    try:
        print(Dataframex.dataframa(location="shopping_cart.txt"))
    except Exception:
        cprint("Shopping Cart is Empty", "red")

    # Get user input (normalized to lowercase)
    choice = input(colored(f"""
                      A: Final Purchase
                      B: Delete one product
                      C: Empty Cart
                      Q: Return to Main Menu
                      

                      {optiontext}: """, "yellow")).lower()

    # Handle user choice
    if choice == "q":
        os.system('cls')
        main()
    elif choice.isnumeric() and optiontext == "Please Enter the Product Number to Delete":
        delete_one(int(choice))
    elif choice == "b":
        os.system('cls')
        menu("Please Enter the Product Number to Delete")
    elif choice == "a":
        purchase()
    elif choice == "c":
        empty_cart()
    else:
        os.system('cls')
        cprint('Invalid Command. Please Try Again', "red")
        main()


def save_product(product_list):
    """
    Save products to shopping cart file.
    
    Args:
        product_list: List of product indices to save
        
    Returns:
        int: Always returns 0 (legacy compatibility)
    """
    df = Dataframex.dataframa()
    cart_df = df.loc[product_list]
    
    # Convert DataFrame to dictionary and save
    res_dict = cart_df.set_index('Name').T.to_dict('list')
    with open('shopping_cart.txt', 'w', encoding="utf-8") as data:
        data.write(str(res_dict))
    return 0


def empty_cart():
    """Clear all items from the shopping cart."""
    open('shopping_cart.txt', 'w').close()
    os.system('cls')
    main()


def delete_one(inde):
    """
    Remove a specific product from the shopping cart.
    
    Args:
        inde (int): Index of product to remove
    """
    try:
        df = Dataframex.dataframa("shopping_cart.txt")
        row_number = len(df.index)
        
        if inde < row_number:
            # Clear file and remove selected item
            open('shopping_cart.txt', 'w').close()
            df = df.drop(inde)
            
            # Save updated cart
            res_dict = df.set_index('Name').T.to_dict('list')
            with open('shopping_cart.txt', 'w', encoding="utf-8") as data:
                data.write(str(res_dict))
                
        os.system('cls')
        main()
    except Exception:
        os.system('cls')
        cprint("Product Number Not found", "red")
        main()


def purchase():
    """Handle final purchase confirmation."""
    cprint("Thank You for Your Purchase!", "green")
    time.sleep(4)
    empty_cart()


if __name__ == "__main__":
    os.system('cls')
    main()
