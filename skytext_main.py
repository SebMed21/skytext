import time
import sys

# dictionary for player status
player_stats = {
    'player_name'               : "Prisoner",
    # player values           
    'player_max_hp'             : 0,
    'player_current_hp'         : 0,
    
    'player_max_sta'            : 0, 
    'player_current_sta'        : 0, 
    
    'player_max_mp'             : 0,
    'player_current_mp'         : 0, 
    
    'player_experience'         : 0,
    'player_level'              : 1,  
    # character creation
    'player_gender'             : "",
    'player_race'               : "",
    # other
    'player_ability'            : ""
    
    
}
# dictionary for player's equipped gear
player_equipment = {
    
    'player_right_hand'     : "",
    'player_left_hand'      : "",
    'player_helmet'         : "",
    'player_body'           : "",
    'player_gloves'         : "",    
    'player_boots'          : "",
}
# dictionary for the current items in the player inventory
player_inventory = {}

# dictionary for items, equipment, and spells
sword = {}
axe = {}
hammer = {}
shield = {}
helmet = {}
body = {}
gloves = {}
boots = {}

magic  = {}

# things for character customization
#race values
nord_hp = 100
nord_sta = 100
nord_mp = 100

imperial_hp = 100
imperial_sta = 100
imperial_mp = 100

breton_hp = 100
breton_sta = 100
breton_mp = 100

redguard_hp = 100
redguard_sta = 100
redguard_mp = 100

altmer_hp = 100
altmer_sta = 100
altmer_mp = 100

dunmer_hp = 100
dunmer_sta = 100
dunmer_mp = 100

bosmer_hp = 100
bosmer_sta = 100
bosmer_mp = 100

orsimer_hp = 100
orsimer_sta = 100
orsimer_mp = 100

argonian_hp = 100
argonian_sta = 100
argonian_mp = 100

kahjiit_hp = 100
kahjiit_sta = 100
kahjiit_mp = 100

# possible character races with abilities 
races = { 
        'race_man': { 
            
            'nord': { 
                    'health': nord_hp, 
                    'stamina': nord_sta, 
                    'magicka': nord_mp, 
                    'ability': ['Battle Cry', 'Cold Resistance'] 
                    
                    }, 
            
            'imperial': { 
                    'health': imperial_hp, 
                    'stamina': imperial_sta, 
                    'magicka': imperial_mp, 
                    'ability': ['Voice of the Emperor', 'Gold Boost'] 
                    
                    }, 
            
            'breton': { 
                    'health': breton_hp, 
                    'stamina': breton_sta, 
                    'magicka': breton_mp, 
                    'ability': ['Dragon Skin', 'Magicka Resistance'] 
                    
                    }, 
            
            'redguard': { 
                    'health': redguard_hp, 
                    'stamina': redguard_sta, 
                    'magicka': redguard_mp, 
                    'ability': ['Adrenaline Rush', 'Poison Resistance'] 
                        
                    } 
            
            }, 
        
        'race_mer': { 
            
                    'altmer': { 
                        'health': altmer_hp, 
                        'stamina': altmer_sta, 
                        'magicka': altmer_mp, 
                        'ability': ['Highborn', 'Magicka Boost'] 
                        
                    }, 
                    
                    'dunmer': { 
                        'health': dunmer_hp, 
                        'stamina': dunmer_sta, 
                        'magicka': dunmer_mp,
                        'ability': ['Ancestor’s Wrath', 'Fire Resistance'] 
                        
                    },
                     
                    'bosmer': { 
                        'health': bosmer_hp, 
                        'stamina': bosmer_sta, 
                        'magicka': bosmer_mp, 
                        'ability': ['Command Animal', 'Disease Resistance'] 
                        
                    }, 
                    
                    'orsimer': { 
                        'health': orsimer_hp, 
                        'stamina': orsimer_sta, 
                        'magicka': orsimer_mp, 
                        'ability': ['Berserker Rage', 'Heavy Armor Boost'] 
                        
                    } 
                    
            }, 
        
        'race_beast': { 
            
                    'argonian': { 
                        'health': argonian_hp, 
                        'stamina': argonian_sta, 
                        'magicka': argonian_mp, 
                        'ability': ['Histskin', 'Water Breathing'] }, 
                    'kahjiit': { 
                        'health': kahjiit_hp, 
                        'stamina': kahjiit_sta, 
                        'magicka': kahjiit_mp, 
                        'ability': ['Night Eye', 'Claw Attacks'] } 
                    
            } 
        
        }

# initialization for text and other utils
separator = "================================================================================================================="
    # print("\n", separator, "\n")
    # user_choice = input("Enter your choice: ")
    
read_speed = 0.02

# displays the opening main menu for the game 
def main_menu_visual():
    print("\n", separator, "\n")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡀⠀⠀⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣇⠀⠀⠀⠀⠀⠀⣠⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠈⠀⡀⠀⠀⠀⠀⠁⠸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀⢸⣷⣀⣀⣀⠔⠀⠀⢸⣿⣿⡄⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⢀⣿⣿⡿⠀⠀⠀⣾⣿⣿⣿⣅⡀⠀⠀⠀⣿⣿⣿⡀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⢀⣾⣿⣿⠇⠀⠀⢸⡿⠋⠀⠈⠉⢻⣧⠀⠀⠸⣿⣿⣷⡀⠀⠀⠀⠀")
    print("⠀⠀⠀⢀⣾⣿⣿⡟⠀⠀⠀⠈⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⣿⣿⣿⣷⡀⠀⠀⠀")
    print("⠀⠀⠀⣾⣿⣿⣿⡿⣦⡀⠀⠀⠀⣠⣴⣶⡿⠟⠁⠀⢠⣴⣿⣿⣿⣿⣷⡀⠀⠀")
    print("⠀⠀⣼⣿⣿⣿⡿⠀⠀⠑⠀⠀⣾⣿⠋⠁⠀⠀⠀⠀⠋⠁⠀⢻⣿⣿⣿⣧⠀⠀")
    print("⠀⣼⣿⣿⣿⣿⠇⠀⠀⠀⠀⠘⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀","              ____   _  ____   __ _____  _____ __  __ _____ ")
    print("⣼⣿⣿⣿⣿⣿⠀⠀⠙⢷⣤⣤⣻⣿⣿⣿⣄⢠⡄⣴⡞⠉⠀⠀⣿⣿⣿⣿⣿⣧","             / ___| | |/ /\ \ / /|_   _|| ____|\ \/ /|_   _|")
    print("⠹⣿⣿⣿⣿⣿⣶⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⠏","             \___ \ | ' /  \ V /   | |  |  _|   \  /   | |  ")
    print("⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀","              ___) || . \   | |    | |  | |___  /  \   | |")
    print("⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀","             |____/ |_|\_\  |_|    |_|  |_____|/_/\_\  |_|  ")
    print("⠀⠀⠀⢿⣿⣿⣿⣿⡏⠻⣿⡿⢿⣿⣿⣿⣿⣿⢿⣿⠟⢻⣿⣿⣿⣿⡿⠀⠀⠀","Turn-based RPG based on the game by Bethesda : The Elder Scrolls V: Skyrim")
    print("⠀⠀⠀⠈⢿⣿⣿⣿⠃⠀⠘⠃⠀⠙⣿⣿⣿⠃⠸⠃⠀⠸⣿⣿⣿⡿⠁⠀⠀⠀")
    print("⠀⠀⠀⠀⠈⢿⣿⡏⠀⠀⠀⠀⠀⠀⠸⣿⣿⡄⠀⠀⠀⠀⣿⣿⡿⠁⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠘⣿⣿⣦⡀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⠃⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣶⠀⠀⠀⢀⣿⡿⠃⠀⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⢠⣾⡿⠁⠀⠀⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀", "[1] N̲E̲W̲ G̲A̲M̲E̲           ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠀⢠⣿⡟⠀⠀⠀⠀⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀","[2] C̲O̲N̲T̲I̲N̲U̲E̲ G̲A̲M̲E̲      ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠈⣿⣇⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀","[3] E̲X̲I̲T̲               ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⣸⡿⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⢀⣠⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    
    
    print("\n", separator, "\n")
# functionality of the main menu to start the game or access the other menus
def main_menu_function():
    while True:
        user_choice = input("Enter your choice: ") 
        print("\n", separator, "\n")
        
        # user wishes to start a new game save
        if user_choice == "1":
            game_opening()
            break
        
        # user wishes to continue a past game save 
        elif user_choice == "2":
            print("hello")
            break
        
        # user wishes to quit the game
        elif user_choice == "3":
            # confirms if the user REALLY wants to quit the game 
            user_choice = input("Are you sure you want to quit? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | ) ")
            
            if user_choice == "1":
                break
                
            elif user_choice == "2":
                continue
# displays the character creation menu                   
def character_creation():
    print("\n", separator, "\n") 
    print("                                         ( |  CHARACTER CREATION  | )")     
    print("\n", separator, "\n")               
    print("                                          ( |  CHARACTER GENDER  | )")
   
    while True:
        print("\nWhat is your character's gender? ( | [1] M̲A̲L̲E̲ | [2] F̲E̲M̲A̲L̲E̲ | )")
        user_choice = input("Enter your choice: ")
            
            # Male choice
        if user_choice == "1":
                
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_gender'] = "Male"
                break
                
            elif user_choice == "2":
                continue
            
            # Female choice   
        elif user_choice == "2":
                
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")

            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_gender'] = "Female"
                break
                    
            elif user_choice == "2":
                continue 
            
    print("\n", separator, "\n")
    
    print("                                           ( |  CHARACTER RACE  | )\n")
    
    # Nord race
    print(f"[1] Nord : text here")
    print(f"Health: {nord_hp} | Stamina: {nord_sta} | Magicka : {nord_mp}")
    x = races['race_man']['nord']['ability']
    print(f"Abilities : {x}\n")   
    
    # Imperial race
    print(f"[2] Imperial : text here")
    print(f"Health: {imperial_hp} | Stamina: {imperial_sta} | Magicka : {imperial_mp}")
    x = races['race_man']['imperial']['ability']
    print(f"Abilities : {x}\n") 
    
    # Breton race
    print(f"[3] Breton : text here")
    print(f"Health: {breton_hp} | Stamina: {breton_sta} | Magicka : {breton_mp}")
    x = races['race_man']['breton']['ability']
    print(f"Abilities : {x}\n")
    
    # Redguard race           
    print(f"[4] Redguard : text here")
    print(f"Health: {redguard_hp} | Stamina: {redguard_sta} | Magicka : {redguard_mp}")
    x = races['race_man']['redguard']['ability']
    print(f"Abilities : {x}\n")    
    
    # Altmer race
    print(f"[5] Altmer : text here")
    print(f"Health: {altmer_hp} | Stamina: {altmer_sta} | Magicka : {altmer_mp}")
    x = races['race_mer']['altmer']['ability']
    print(f"Abilities : {x}\n") 
    
    # Dunmer race
    print(f"[6] Dunmer : text here")
    print(f"Health: {dunmer_hp} | Stamina: {dunmer_sta} | Magicka : {dunmer_mp}")
    x = races['race_mer']['dunmer']['ability']
    print(f"Abilities : {x}\n")
   
    # Bosmer race
    print(f"[7] Bosmer : text here")
    print(f"Health: {bosmer_hp} | Stamina: {bosmer_sta} | Magicka : {bosmer_mp}")
    x = races['race_mer']['bosmer']['ability']
    print(f"Abilities : {x}\n")   
    
    # Orsimer race
    print(f"[8] Orsimer : text here")
    print(f"Health: {orsimer_hp} | Stamina: {orsimer_sta} | Magicka : {orsimer_mp}")
    x = races['race_mer']['orsimer']['ability']
    print(f"Abilities : {x}\n") 
    
    # Argonian race
    print(f"[9] Argonian : text here")
    print(f"Health: {argonian_hp} | Stamina: {argonian_sta} | Magicka : {argonian_mp}")
    x = races['race_beast']['argonian']['ability']
    print(f"Abilities : {x}\n") 
    
    print(f"[10] Kahjiit : text here")
    print(f"Health: {kahjiit_hp} | Stamina: {kahjiit_sta} | Magicka : {kahjiit_mp}")
    x = races['race_beast']['kahjiit']['ability']
    print(f"Abilities : {x}\n") 
    
    print("\n", separator, "\n")
    print("MAN :    ( | [1] N̲O̲R̲D̲ | [2] I̲M̲P̲E̲R̲I̲A̲L̲ | [3] B̲R̲E̲T̲O̲N̲ | [4] R̲E̲D̲G̲U̲A̲R̲D̲ | )")
    print("MER :    ( | [5] A̲L̲T̲M̲E̲R̲ | [6] D̲U̲N̲M̲E̲R̲ | [7] B̲O̲S̲M̲E̲R̲ | [8] O̲R̲S̲I̲M̲E̲R̲ | )")
    print("BEAST :  ( | [9] A̲R̲G̲O̲N̲I̲A̲N̲ | [10] K̲A̲H̲J̲I̲I̲T̲ | )")
    print("\n", separator, "\n")
        
    while True:  
        print("What is your character's race?")
        user_choice = input("Enter your choice: ")

        if user_choice == "1": # nord choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['nord']['health']
                player_stats['player_max_sta'] = races['race_man']['nord']['stamina']
                player_stats['player_max_mp'] = races['race_man']['nord']['magicka']
                player_stats['player_race'] = races['race_man']['nord']
                player_stats["player_ability"] = races['race_man']['nord']['ability']
                break
                
            elif user_choice == "2":
                continue
                            
        elif user_choice == "2": # imperial choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['imperial']['health']
                player_stats['player_max_sta'] = races['race_man']['imperial']['stamina']
                player_stats['player_max_mp'] = races['race_man']['imperial']['magicka']
                player_stats['player_race'] = races['race_man']['imperial']
                player_stats["player_ability"] = races['race_man']['imperial']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "3": # breton choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['breton']['health']
                player_stats['player_max_sta'] = races['race_man']['breton']['stamina']
                player_stats['player_max_mp'] = races['race_man']['breton']['magicka']
                player_stats['player_race'] = races['race_man']['breton']
                player_stats["player_ability"] = races['race_man']['breton']['ability']  
                break
            
            elif user_choice == "2":
                continue
        
        elif user_choice == "4": # redguard choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['redguard']['health']
                player_stats['player_max_sta'] = races['race_man']['redguard']['stamina']
                player_stats['player_max_mp'] = races['race_man']['redguard']['magicka']
                player_stats['player_race'] = races['race_man']['redguard']
                player_stats["player_ability"] = races['race_man']['redguard']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "5": # altmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['altmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['altmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['altmer']['magicka']
                player_stats['player_race'] = races['race_mer']['altmer']
                player_stats["player_ability"] = races['race_mer']['altmer']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "6": # dunmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['dunmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['dunmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['dunmer']['magicka']
                player_stats['player_race'] = races['race_mer']['dunmer']
                player_stats["player_ability"] = races['race_mer']['dunmer']['ability']  
                break
            
            elif user_choice == "2":
                continue
        
        elif user_choice == "7": # bosmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['bosmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['bosmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['bosmer']['magicka']
                player_stats['player_race'] = races['race_mer']['bosmer']
                player_stats["player_ability"] = races['race_mer']['bosmer']['ability']  
                break

        elif user_choice == "8": # orsimer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['orsimer']['health']
                player_stats['player_max_sta'] = races['race_mer']['orsimer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['orsimer']['magicka']
                player_stats['player_race'] = races['race_mer']['orsimer']
                player_stats["player_ability"] = races['race_mer']['orsimer']['ability']  
                break
            
            elif user_choice == "2":
                continue

        elif user_choice == "9": # argonian choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_beast']['argonian']['health']
                player_stats['player_max_sta'] = races['race_beast']['argonian']['stamina']
                player_stats['player_max_mp'] = races['race_beast']['argonian']['magicka']
                player_stats['player_race'] = races['race_beast']['argonian']
                player_stats["player_ability"] = races['race_beast']['argonian']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "10": # kahjiit choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_beast']['kahjiit']['health']
                player_stats['player_max_sta'] = races['race_beast']['kahjiit']['stamina']
                player_stats['player_max_mp'] = races['race_beast']['kahjiit']['magicka']
                player_stats['player_race'] = races['race_beast']['kahjiit']
                player_stats["player_ability"] = races['race_beast']['kahjiit']['ability']  
                break
            
            elif user_choice == "2":
                continue

    print("\n", separator, "\n")
    print("                                           ( |  CHARACTER NAME  | )")
    
    while True:
        x = input("\nWhat is your character's name? ")
        print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            player_stats['player_name'] == x
            break
                        
        elif user_choice == "2":
            continue 

                
# !!! Gameplay Menus !!!               
# displays the current actions a user can do
def action_screen():
    while True:
        print("\n", separator, "\n")
        print("                        ( |    [1] S̲T̲A̲T̲U̲S̲    |   [2] M̲E̲N̲U̲    |   [3] E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
        print("\n", separator, "\n")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            display_status()
            return False
            
        elif user_choice == "2":
            menu_screen()  
            return False
        
        elif user_choice == "3":
            return False
    
# displays the menu for inventory, skills, level up perks and map    
def menu_screen():
    while True:
        print("\n", separator, "\n")
        print("         ( |    [1] I̲N̲V̲E̲N̲T̲O̲R̲Y̲    |   [2] M̲A̲G̲I̲C̲   |   [3] P̲E̲R̲K̲S̲   |   [4] M̲A̲P̲     |    [5] E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
        print("\n", separator, "\n")
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            inventory_screen()
            break
        
        elif user_choice == "2":
            magic_screen()
            break
            
        elif user_choice == "3":
            perks_screen()
            break
            
        elif user_choice == "4":
            map_screen()
            break

        elif user_choice == "5":
            break
        
# displays the contents of the player's inventory
def inventory_screen():
    print("*show inventory here*")
    
# displays the magic spells the player can currently use
def magic_screen():
    print("*show magic here*")

# displays the perks the player can take (character upgrades)
def perks_screen():
    print("*show perks here*")
    
# displays the map
def map_screen():
    print("*shows the map*")
    
# displays current player status
def display_status():
    print("\n", separator, "\n")
    
    print(player_stats['player_name'])
    
    print("HP:", player_stats['player_current_health'],"/", player_stats['player_max_health'], 
          "| MP:", player_stats['player_current_magicka'],"/", player_stats['player_max_magicka'], 
          "| STA:", player_stats['player_current_stamina'],"/", player_stats['player_max_stamina'])
    
    print("EXP: ", player_stats['player_experience'], "/ 100",
          "| LVL: ", player_stats['player_level'])
    
    print("RACE: ", player_stats['player_race'])
    
    print("\n", separator, "\n")

# !!! Gameplay Functions !!!
def game_opening():
    # "." dot delay
    count = 15
    while count > 0:
        print(".")
        count = count - 1
        time.sleep(0.2)
    
    print("\n", separator, "\n")
    
    # opening text
    string = "             Scrolls have foretold, of black wings in the cold, that when brothers wage war come unfurled!\n                 Alduin, bane of kings, ancient shadow unbound, With a hunger to swallow the world!\n" 
    # text output delay
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    
    # format
    count = 5
    while count > 0:
        print("")
        count = count - 1
        time.sleep(0.1)  
    
    # "Alduin" art with print delay
    print("")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀")
    time.sleep(0.2)
    print("                              ⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀")
    time.sleep(0.2)
    print("                               ⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆")
    time.sleep(0.2)
    print("                               ⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄")
    time.sleep(0.2)
    print("                               ⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷")
    time.sleep(0.2)
    print("                               ⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹")
    time.sleep(0.2)
    print("                               ⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸")
    time.sleep(0.2)
    print("                               ⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼")
    time.sleep(0.2)
    print("                               ⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.2)
    print("                               ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")   
    time.sleep(0.2)
    
    # format
    count = 5
    while count > 0:
        print("")
        count = count - 1
        time.sleep(0.1)  
    
    print("\n", separator, "\n")
    
    # asks for user input to continue the story
    while True: 
        user_input = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_input == "1":
            break
        
    print("\n", separator, "\n")

    
    # next scene 
    opening_scene_p1()

def opening_scene_p1():
    count = 15
    while count > 0:
        print(".")
        count = count - 1
        time.sleep(0.1)
        
    print("\n", separator, "\n")    
    
    print("\n                                                 ★ U N B O U N D \n\n")
    
    dialogue =  "-> You open your eyes and wake up. You look around and see that you're on a wobbly carriage.\n" \
                "-> You try to move but your arms are bound.\n"\
                "-> You then hear a voice that calls you out.\n"\
                "-> You see a blond man with hands bound, wearing what seems to be light armor with blue markings and an emblem of a bear..\n \n"\
                " > Stormcloak Soldier : Hey you. You're finally awake.\n"\
                " > Stormcloak Soldier : You we're trying to cross the border, right?\n"\
                " > Stormcloak Soldier : Walked right into that imperial ambush, same as us, and that thief over there.\n\n"\
                "-> You look around the carriage, and see another man, he is wearing ragged clothes with his hands tied.\n"\
                "-> The man in ragged clothes then talks\n \n"\
                " > Horse Thief : Damn you Stormcloaks. \n"\
                " > Horse Thief : Skyrim was fine until you came along. Empire was nice and lazy.\n"\
                " > Horse Thief : If they hadn't been looking for you, I could've stolen that horse and been halfway to Hammerfell.\n"\
                " > Horse Thief : You there.\n\n"\
                "-> The man in the ragged robes looks at you.\n\n"\
                " > Horse Thief : You and me, we shouldn't be here. It's these Stormcloaks the Empire wants.\n"\
                " > Stormcloak Soldier : We're all brothers and sisters in binds now, thief.\n \n"\
                " > Imperial Soldier : Shut up back there!\n\n"\
                " > Thief : And what's wrong with him, huh?\n"\
                " > Stormcloak Soldier : Watch your tongue! You're speaking to Ulfric Stormcloak, the true High King.\n\n"\
                "-> You look beside you and see a man wearing a black tunic. His hands are bound and his mouth is gagged.\n\n"\
                " > Thief : Ulfric? The Jarl of Windhelm? You're the leader of the rebellion.\n"\
                " > Thief : But if they've captured you... Oh gods, where are they taking us!?\n"\
                " > Stormcloak Soldier : I don't know where we're going, but Sovngarde awaits. \n"\
                " > Thief : No, this can't be happening. This isn't happening!\n\n"\
                "-> You see grey stone walls appear on the distance.\n"\
                "-> Tall towers loom behind the stretch of walls and a gate is visible breaking up the length of stone.\n\n"\
                " > Stormcloak Soldier : Hey, what village are you from, horse thief?\n"\
                " > Horse Thief : Why do you care?\n"\
                " > Stormcloak soldier : A nord's last thoughts should be of home.\n"\
                " > Horse Thief : Rorikstead. I'm... I'm from Rorikstead.\n\n"\
                "-> You see the walls get closer and closer until you are almost beneath it's feet...\n\n"
                   
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
        
    print("\n", separator, "\n")        
    
    # asks for user input to continue the story
    while True: 
        user_input = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_input == "1":
            break
        
    print("\n", separator, "\n")
    
    opening_scene_p2()
        
def opening_scene_p2():
    
    dialogue =  "-> As the carriage you're riding nears the wooden gates of the walled settlement, you look out and see an imperial soldier atop the gates.\n"\
                "-> The soldier calls out to the white haired man clad in gilded armor riding atop a horse.\n\n"\
                " > Imperial Soldier : General Tullius, sir! The headsman is waiting!\n"\
                " > General Tullius : Good. Let's get this over with.\n\n"\
                "-> You turn your head back to your companions in the carriage.\n"\
                "-> You and your companions realize that you'll all be heading for the chopping block.\n"\
                "-> You hear the horse thief start calling out to the Divines\n\n"\
                " > Horse Thief : Shor, Mara, Dibella, Kynareth, Akatosh! Divines, please help me!\n\n"\
                "-> You now look toward the right side of the carriage and see the man in gilded armor.\n"\
                "-> Inferring from the soldier atop the gate earlier. It seems that this 'Tulius' is a general of the empire.\n"\
                "-> Riding beside him is a golden skinned elf in elegant gilded black robes.\n\n"\
                " > Stormcloak Soldier : Look at him, General Tulius, the Military Governor.\n"\
                " > Stormcloak Soldier : And it looks like the Thalmor are with him.\n"\
                " > Stormcloak Soldier : Damn elves. I bet they had something to do with this.\n\n"\
                "-> The carriage is now well inside the settlement\n"\
                "-> You look around and see wooden houses with tatched roof and a few tall stone towers scattered about.\n\n"\
                " > Stormcloak Soldier : This is Helgen. I used to be sweet on a girl from here.\n"\
                " > Stormcloak Soldier : Wonder if Vilod is still making that mead with juniper berries mixed in\n"\
                " > Stormcloak Soldier : Funny, when I was a boy, imperial walls and towers used to make me feel so safe.\n\n"\
                "-> You turn your head far to the left side of the carriage and see a little boy with his father.\n\n"\
                " > Little Boy : Who are they daddy? Where are they going?\n"\
                " > Father : You need to go inside now, little cub.\n"\
                " > Little Boy : Why? I want to watch the soldiers.\n"\
                " > Father : Inside the house. Now.\n"\
                " > Little Boy : Yes, papa.\n\n"\
                " > Imperial Captain : Get these prisoners out of the carts. Move it!\n"\
                " > Horse Thief : Why are we stopping?\n"\
                " > Stormcloak Soldier : Why do you think? End of the line.\n"\
                " > Stormcloak Soldier : Let's go. Shouldn't keep the gods waiting for us.\n\n"\
                "-> You turn your gaze forward and see a large stone keep.\n"\
                "-> The imperial soldier stops the carriage. It seems this is your final destination.\n"\
                "-> You and your fellow prisoners make your way down the carriage.\n\n"\
                " > Horse Thief : No! Wait! We're not rebels!\n"\
                " > Stormcloak Soldier : Face your death with some courage, thief.\n"\
                " > Horse Thief : You've got to tell them! We weren't with you! This is a mistake!\n"\
                " > Imperial Captain : Step towards the block when we call your name. One at a time.\n\n"\
                "-> An imperial soldier with a ledger and a quill is reading off a list and begins to call the names of your fellow prisoners.\n\n"\
                " > Stormcloak Soldier : Empire loves their damn lists.\n"\
                " > Imperial Soldier : Ulfric Stormcloak. Jarl of Windhelm.\n"\
                " > Stormcloak Soldier : It has been an honor Jarl Ulfric!\n"\
                " > Imperial Soldier : Ralof of Riverwood.\n"\
                " > Imperial Soldier : Lokir of Rorikstead.\n\n"\
                "-> It seems that the Horse Thief's name was Lokir..\n"\
                "-> As the others make their way to the block. Lokir made a run for his life.\n\n"\
                " > Lokir : You're not going to kill me!\n"\
                " > Imperial Captain : Archers!\n\n"\
                "-> Imperial archers aim for Lokir as he is running. Two arrows find their way through Lokir's back\n"\
                "-> Lokir the horse thief drops dead on the cobblestone road.\n\n"\
                " > Imperial Captain : Anyone else feel like running?\n\n"\
                "-> It seems that it is now your turn to be called.\n"\
                "-> The imperial soldier checks the list for your name and indentity but finds nothing.\n\n"\
                " > Imperial Soldier : Wait. You there. Step forward.\n"\
                " > Imperial Soldier : Who are you?\n"\
                      
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)    
        
    print("\n", separator, "\n") 
    
    while True: 
        user_input = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_input == "1":
            break
    
    print("\n", separator, "\n") 
    
    character_creation_menu()
    
# program launch into main menu
#opening_scene_p1()
#opening_scene_p2()
#display_status()
#action_screen()
character_creation()


#main_menu_visual()
#main_menu_function()

