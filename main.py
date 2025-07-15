import sys
import json
from main_menu import Menu


class Character:
    def __init__(self, Username,ClassName,Type,School,Inventory=None):
        self.Username = Username
        self.ClassName = ClassName
        self.Type = Type
        self.School = School
        self.Inventory = Inventory if Inventory is not None else []

    def Intro(self):
        print(f'Welcome,{self.Username} successfully created!')
        print(" ")
        
    def Profile(self):
        print(f'Username:{self.Username}')
        print(f'ClassName:{self.ClassName}')
        print(f'Type:{self.Type}')
        print(f'School:{self.School}')
        print(f'Level: 1')
        print(f'Inventory:{self.Inventory}')
        
    def AddItem(self, item):
        self.Inventory.append(item)
        print(f'{item} has been added to your inventory!')
        
    def ShowInventory(self):
        print('\n🎒 Inventory: ')
        if self.Inventory:
            for i, item in enumerate(self.Inventory, 1):
                print(f'{i}.{item}')
        else:
            print('Inventory is empty! ')
                
        
        
print("Game Initializing....")
print("Welcome to PUSA GAMING")

game_mode = ["Register","Start","Exit"]
print(" ")
print("Available modes >>",game_mode)

registered = False
login_name = ""
password = ""

try:
    with open("accounts.json", "r") as f:
        accounts = json.load(f)
except FileNotFoundError:
    accounts = {}
    
while True:
    chosen_mode = input("Select Mode >> ").strip().title()
    if chosen_mode not in game_mode:
        print("Invalid option,Please choose [ Register, Start, Exit ]")
    
    if chosen_mode == "Register":
        login_name = input("Create Login Name: ")
        if login_name in accounts:
            print("That login name is already taken")
            continue
        password = input("Create Password: ").strip()
        
        accounts[login_name] = {
    "password": password,
    "character": None  # Character will be created later
}

# Save to file
        with open("accounts.json", "w") as f:
            json.dump(accounts, f)
        
        print(f'\nAccount successfully created!Login Name:{login_name}\n')
        
    elif chosen_mode == "Start":
        enter_login = input("Enter LoginName: ").strip()
        if enter_login not in accounts:
            print(f'{enter_login} not registered')
        else:
            enter_password = input("Enter Password: ")
            if enter_password == accounts[enter_login]["password"]:
                print(f'\nWelcome {enter_login} to PUSA GAMING!')
            
                char_data = accounts[enter_login]["character"]
                if char_data:
                    print("\n🧝 Character already exists:")
                    for key, value in char_data.items():
                        print(f"{key}: {value}")
                    print("\nProceeding to main menu...")
                    current_user = enter_login   
                    char1 = Character(
                        char_data["Username"],
                        char_data["ClassName"],
                        char_data["Type"],
                        char_data["School"],
                        char_data.get("Inventory",[])
                        )
                    Menu(char1, current_user)
                    sys.exit()
                break
            else:
                print("Wrong password")
        
    elif chosen_mode == "Exit":
        print("Exiting game...")
        sys.exit()

    
print("")  
Username = input("Enter character name: ")
Classes = { 
    "Swordsman" : "⚔️",
    "Brawler" : "🦾",
    "Archer" : "🏹",
    "Shaman" : "🪄" }

while True:
    for item_class in Classes:
        print(f'{item_class.title()}{Classes[item_class]}')
    chosen_class = input("\nChoose Class: ").strip().title()
    if chosen_class in Classes:
        ClassName = (f'{chosen_class}{Classes[chosen_class]}')
        print(f'\nYou chose: {ClassName}')
        break
    else:
        print("\nEnter valid Class from the list")
print(" ")

Types = {
    "Dex" : "🟥",
    "Pow" : "🟧",
    "Int" : "🟦" } 
    
while True:
    for item_type in Types:
        print(f'{item_type.title()}{Types[item_type]}')
    chosen_type = input("\nChoose Type: ").strip().title()
    if chosen_type in Types:
        Type = (f'{chosen_type}{Types[chosen_type]}')
        print(f'\nYou are {Type} type')
        break
    else:
        print("\nEnter valid Types from the list")
print(" ")

School_choices = {
    "Sg" : "✡️",
    "Mp" : "♓",
    "Ph" : "♊" }
    
while True:
    for item_school in School_choices:
        print(f'{item_school.title()}{School_choices[item_school]}')
    chosen_school = input("\nChoose School: " ).strip().title()
    if chosen_school in School_choices:
        School = (f'{chosen_school}{School_choices[chosen_school]}')
        print(f'\nYou are in {School} Campus')
        break
    else:
        print("\nEnter valid School from the list")
print(" ")

char1 = Character(Username,ClassName,Type,School,Inventory)
#update char info in the account
accounts[current_user]["character"] = {
    "Username": Username,
    "ClassName": ClassName,
    "Type": Type,
    "School": School,
    "Level": 1,
    "Inventory":char1.Inventory
}

# Save updated account with character
with open("accounts.json", "w") as f:
    json.dump(accounts, f)

    
char1.Intro()
char1.Profile()
Menu(char1)

