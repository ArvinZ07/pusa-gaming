import sys
import json

def Menu(char1, current_user):
    print("\n---MAIN MENU---")
    print("1. View Profile")
    print("2. Inventory")
    print("3. Collect Items")
    print("4. Stats")
    print("5. Enter Battle")
    print("6. Exit")
    
    while True:
        chosen_menu = input("Enter option >>> ")
        if chosen_menu == "1":
            char1.Profile()
            
        elif chosen_menu == "2":
            char1.ShowInventory()
            
        elif chosen_menu == "3":
            item = input("Enter item to collect: ").strip().title()
            if item:
                char1.AddItem(item)
                
        elif chosen_menu == "4":
            print(" maintenance 4")
            
        elif chosen_menu == "5":
            print(" Comming soon")
            
        elif chosen_menu == "6":
            print("Saving progress and Exiting Game..")

            with open("accounts.json", "r") as f:
                accounts = json.load(f)

            accounts[current_user]["character"]["Inventory"] = char1.Inventory

            with open("accounts.json", "w") as f:
                json.dump(accounts, f)
            
            print("Progress saved!")
            break
        else:
            print(" Invalid input!")
