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
    'player_gender'             : "male", # default gender
    'player_race'               : "nord", # default race
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
# possible character races with abilities 
races = { 
        'race_man': { 
            
            'nord': { 
                    'health': 100, 
                    'stamina': 100, 
                    'magicka': 100, 
                    'ability': ['Battle Cry', 'Cold Resistance'] 
                    
                    }, 
            
            'imperial': { 
                    'health': 100, 
                    'stamina': 100, 
                    'magicka': 100, 
                    'ability': ['Voice of the Emperor', 'Gold Boost'] 
                    
                    }, 
            
            'breton': { 
                    'health': 100, 
                    'stamina': 100, 
                    'magicka': 100, 
                    'ability': ['Dragon Skin', 'Magicka Resistance'] 
                    
                    }, 
            
            'redguard': { 
                    'health': 100, 
                    'stamina': 100, 
                    'magicka': 100, 
                    'ability': ['Adrenaline Rush', 'Poison Resistance'] 
                        
                    } 
            
            }, 
        
        'race_mer': { 
            
                    'altmer': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100, 
                        'ability': ['Highborn', 'Magicka Boost'] 
                        
                    }, 
                    
                    'dunmer': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100,
                        'ability': ['Ancestor’s Wrath', 'Fire Resistance'] 
                        
                    },
                     
                    'bosmer': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100, 
                        'ability': ['Command Animal', 'Disease Resistance'] 
                        
                    }, 
                    
                    'orsimer': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100, 
                        'ability': ['Berserker Rage', 'Heavy Armor Boost'] 
                        
                    } 
                    
            }, 
        
        'race_beast': { 
            
                    'argonian': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100, 
                        'ability': ['Histskin', 'Water Breathing'] }, 
                    'kahjiit': { 
                        'health': 100, 
                        'stamina': 100, 
                        'magicka': 100, 
                        'ability': ['Night Eye', 'Claw Attacks'] } 
                    
            } 
        
        }

# initialization for text and other utils
separator = "================================================================================================================="
    # print("\n", separator, "\n")
    # user_choice = input("Enter your choice: ")
    
read_speed = 0 # default speed of text that can be changed in the settings

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
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠀⢠⣿⡟⠀⠀⠀⠀⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀","[2] S̲E̲T̲T̲I̲N̲G̲S̲      ")
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
        user_choice = input("\nEnter your choice: ") 
        print("\n", separator, "\n")
        
        # user wishes to start a new game save
        if user_choice == "1":
            game_opening()
            break
        
        # user wishes to continue a past game save 
        elif user_choice == "2":
            settings()
            break
        
        # user wishes to quit the game
        elif user_choice == "3":
            # confirms if the user REALLY wants to quit the game 
            user_choice = input("Are you sure you want to quit? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | ) ")
            
            if user_choice == "1":
                break
                
            elif user_choice == "2":
                continue

# settings for the game           
def settings():
    print("\n", separator, "\n")
    print(" TEXT SPEED: (how fast the dialogue and text gets printed out):\n")
    print("                        ( |    [1] I̲N̲S̲T̲A̲N̲T̲ (0.0)    |   [2] F̲A̲S̲T̲ (0.02)    |   [3] D̲E̲F̲A̲U̲L̲T̲ (0.05)   |   [4] S̲L̲O̲W̲ (0.07)   |   [5] R̲E̲A̲L̲L̲Y̲ S̲L̲O̲W̲ (0.1)   | )\n")
    print("( |  [6] R̲E̲T̲U̲R̲N̲  | )")
    print("\n", separator)
    
    while True:
        user_choice = input("\nEnter your choice: ")
        
        if user_choice == "1":
            read_speed = 0.0 # instant speed
            print(f"Text Speed Set to : Instant ({read_speed})")
            
        
        elif user_choice == "2":
            read_speed = 0.02 # fast speed
            print(f"Text Speed Set to : Fast ({read_speed})")
            
            
        elif user_choice == "3":
            read_speed = 0.5 # default speed
            print(f"Text Speed Set to : Default ({read_speed})")
            
        
        elif user_choice == "4":
            read_speed = 0.07 # slow speed
            print(f"Text Speed Set to : Slow ({read_speed})")
            
            
        elif user_choice == "5":
            read_speed = 0.1 # really slow speed
            print(f"Text Speed Set to : Really Slow ({read_speed})")
        
            
        elif user_choice == "6":
            main_menu_visual()
            main_menu_function()
            break
        
# displays the character creation menu                   
def character_creation():
    print("\n", separator, "\n") 
    print("                                         ( |  CHARACTER CREATION  | )")     
    print("\n", separator, "\n")               
    print("                                          ( |  CHARACTER GENDER  | )")
    while True:
        print("\nWhat is your character's gender? ( | [1] M̲A̲L̲E̲ | [2] F̲E̲M̲A̲L̲E̲ | )")
        user_choice = input("\nEnter your choice: ")
            
            # Male choice
        if user_choice == "1":
                
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")

            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_gender'] = "male"
                break
                
            elif user_choice == "2":
                continue
            
            # Female choice   
        elif user_choice == "2":
                
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")

            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_gender'] = "female"
                break
                    
            elif user_choice == "2":
                continue      
    print("\n", separator, "\n")
    
    print("                                           ( |  CHARACTER RACE  | )\n")
    
    # Nord race
    print(f"[1] Nord : Citizens of Skyrim. They are tall and fair-haired people. Strong and hardy, nords are famous for their resistance to cold and their talent as warriors.")
    print(f"Health: {races['race_man']['nord']['health']} | Stamina: {races['race_man']['nord']['stamina']} | Magicka : {races['race_man']['nord']['magicka']}")
    x = races['race_man']['nord']['ability']
    print(f"Abilities : {x}\n")   
    
    # Imperial race
    print(f"[2] Imperial : Natives of Cyrodiil. They have proved to be shrewed diplomats and traders. They are skilled with combat and magic.\nAnywhere gold coins might be found, Imperials gold coins might be found, Imperials seem to always find a few more.")
    print(f"Health: {races['race_man']['imperial']['health']} | Stamina: {races['race_man']['imperial']['stamina']} | Magicka : {races['race_man']['imperial']['magicka']}")
    x = races['race_man']['imperial']['ability']
    print(f"Abilities : {x}\n") 
    
    # Breton race
    print(f"[3] Breton : In addition to their quick and perceptive grasp of spellcraft, even the humblest of High Rock's Bretons can boast a resistance to magic.")
    print(f"Health: {races['race_man']['breton']['health']} | Stamina: {races['race_man']['breton']['stamina']} | Magicka : {races['race_man']['breton']['magicka']}")
    x = races['race_man']['breton']['ability']
    print(f"Abilities : {x}\n")
    
    # Redguard race           
    print(f"[4] Redguard : The most naturally talented warriors in Tamriel, the Redguards of Hammerfell have a hardy constitution and a natural resistance to poison.")
    print(f"Health: {races['race_man']['redguard']['health']} | Stamina: {races['race_man']['redguard']['stamina']} | Magicka : {races['race_man']['redguard']['magicka']}")
    x = races['race_man']['redguard']['ability']
    print(f"Abilities : {x}\n")    
    
    # Altmer race
    print(f"[5] High Elf : Also known as 'Altmer' in their homeland of Summerset Isle, the high elves are most strongly gifted in the arcane arts of all the races.")
    print(f"Health: {races['race_mer']['altmer']['health']} | Stamina: {races['race_mer']['altmer']['stamina']} | Magicka : {races['race_mer']['altmer']['magicka']}")
    x = races['race_mer']['altmer']['ability']
    print(f"Abilities : {x}\n") 
    
    # Dunmer race
    print(f"[6] Dark Elf : Also known as 'Dunmer' in their homeland of Morrowind, dark elves are noted for their stealth and magic skills.")
    print(f"Health: {races['race_mer']['dunmer']['health']} | Stamina: {races['race_mer']['dunmer']['stamina']} | Magicka : {races['race_mer']['dunmer']['magicka']}")
    x = races['race_mer']['dunmer']['ability']
    print(f"Abilities : {x}\n")
   
    # Bosmer race
    print(f"[7] Wood Elf : The clanfolk of the Western Valendwood forests, also known as 'Bosmer'. Wood elves make good scouts and thieves, and there are no finer archers in all of Tamriel.")
    print(f"Health: {races['race_mer']['bosmer']['health']} | Stamina: {races['race_mer']['bosmer']['stamina']} | Magicka : {races['race_mer']['bosmer']['magicka']}")
    x = races['race_mer']['bosmer']['ability']
    print(f"Abilities : {x}\n")   
    
    # Orsimer race
    print(f"[8] Orc : Also known as 'Orsimer'. The people of Wrothgarian and Dragontail Mountains, orcish smiths are prized for their craftsmanship. Orc troops in heavy armor are among the finest in the Empire.")
    print(f"Health: {races['race_mer']['orsimer']['health']} | Stamina: {races['race_mer']['orsimer']['stamina']} | Magicka : {races['race_mer']['orsimer']['magicka']}")
    x = races['race_mer']['orsimer']['ability']
    print(f"Abilities : {x}\n") 
    
    # Argonian race
    print(f"[9] Argonian : This reptilian race, well-suited for the treacherous swamps of their Black Marsh homeland, has developed a natural resistances to diseases and the ability to breath underwater.")
    print(f"Health: {races['race_beast']['argonian']['health']} | Stamina: {races['race_beast']['argonian']['stamina']} | Magicka : {races['race_beast']['argonian']['magicka']}")
    x = races['race_beast']['argonian']['ability']
    print(f"Abilities : {x}\n") 
    
    print(f"[10] Kahjiit : Hailing from the province of Elsweyr, they are intelligent, quick, and agile. They make excellent thieves due to their natural stealhiness.")
    print(f"Health: {races['race_beast']['kahjiit']['health']} | Stamina: {races['race_beast']['kahjiit']['stamina']} | Magicka : {races['race_beast']['kahjiit']['magicka']}")
    x = races['race_beast']['kahjiit']['ability']
    print(f"Abilities : {x}\n") 
    
    print("\n", separator, "\n")
    print("MAN :    ( | [1] N̲O̲R̲D̲ | [2] I̲M̲P̲E̲R̲I̲A̲L̲ | [3] B̲R̲E̲T̲O̲N̲ | [4] R̲E̲D̲G̲U̲A̲R̲D̲ | )")
    print("MER :    ( | [5] H̲I̲G̲H̲ E̲L̲F̲ | [6] D̲A̲R̲K̲ E̲L̲F̲ | [7] W̲O̲O̲D̲ E̲L̲F̲ | [8] O̲R̲C̲ | )")
    print("BEAST :  ( | [9] A̲R̲G̲O̲N̲I̲A̲N̲ | [10] K̲A̲H̲J̲I̲I̲T̲ | )")
    print("\n", separator, "\n")
        
    while True:  
        print("What is your character's race?")
        user_choice = input("\nEnter your choice: ")

        if user_choice == "1": # nord choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['nord']['health']
                player_stats['player_max_sta'] = races['race_man']['nord']['stamina']
                player_stats['player_max_mp'] = races['race_man']['nord']['magicka']
                player_stats['player_race'] = "nord"
                player_stats["player_ability"] = races['race_man']['nord']['ability']
                break
                
            elif user_choice == "2":
                continue
                            
        elif user_choice == "2": # imperial choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['imperial']['health']
                player_stats['player_max_sta'] = races['race_man']['imperial']['stamina']
                player_stats['player_max_mp'] = races['race_man']['imperial']['magicka']
                player_stats['player_race'] = "imperial"
                player_stats["player_ability"] = races['race_man']['imperial']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "3": # breton choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['breton']['health']
                player_stats['player_max_sta'] = races['race_man']['breton']['stamina']
                player_stats['player_max_mp'] = races['race_man']['breton']['magicka']
                player_stats['player_race'] = "breton"
                player_stats["player_ability"] = races['race_man']['breton']['ability']  
                break
            
            elif user_choice == "2":
                continue
        
        elif user_choice == "4": # redguard choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_man']['redguard']['health']
                player_stats['player_max_sta'] = races['race_man']['redguard']['stamina']
                player_stats['player_max_mp'] = races['race_man']['redguard']['magicka']
                player_stats['player_race'] = "redguard"
                player_stats["player_ability"] = races['race_man']['redguard']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "5": # altmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['altmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['altmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['altmer']['magicka']
                player_stats['player_race'] = "altmer"
                player_stats["player_ability"] = races['race_mer']['altmer']['ability']  
                break
            
            elif user_choice == "2":
                continue
            
        elif user_choice == "6": # dunmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['dunmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['dunmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['dunmer']['magicka']
                player_stats['player_race'] = "dunmer"
                player_stats["player_ability"] = races['race_mer']['dunmer']['ability']  
                break
            
            elif user_choice == "2":
                continue
        
        elif user_choice == "7": # bosmer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['bosmer']['health']
                player_stats['player_max_sta'] = races['race_mer']['bosmer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['bosmer']['magicka']
                player_stats['player_race'] = "bosmer"
                player_stats["player_ability"] = races['race_mer']['bosmer']['ability']  
                break

        elif user_choice == "8": # orsimer choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_mer']['orsimer']['health']
                player_stats['player_max_sta'] = races['race_mer']['orsimer']['stamina']
                player_stats['player_max_mp'] = races['race_mer']['orsimer']['magicka']
                player_stats['player_race'] = "orsimer"
                player_stats["player_ability"] = races['race_mer']['orsimer']['ability']  
                break
            
            elif user_choice == "2":
                continue

        elif user_choice == "9": # argonian choice
            print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
            
            user_choice = input("\nEnter your choice: ")

            if user_choice == "1":
                player_stats['player_max_hp'] = races['race_beast']['argonian']['health']
                player_stats['player_max_sta'] = races['race_beast']['argonian']['stamina']
                player_stats['player_max_mp'] = races['race_beast']['argonian']['magicka']
                player_stats['player_race'] = "argonian"
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
                player_stats['player_race'] = "kahjiit"
                player_stats["player_ability"] = races['race_beast']['kahjiit']['ability']  
                break
            
            elif user_choice == "2":
                continue

    print("\n", separator, "\n")
    print("                                           ( |  CHARACTER NAME  | )")
    
    while True:
        x = input("\nWhat is your character's name? ")
        print("\nAre you sure? ( | [1] Y̲E̲S̲ | [2] N̲O̲ | )   *you cannot change this later*")
        user_choice = input("\nEnter your choice: ")
        if user_choice == "1":
            player_stats['player_name'] == x
            break
                        
        elif user_choice == "2":
            continue
    
    print("\n", separator, "\n")  
 
    execution_scene()
                
# !!! Gameplay Menus !!!               
# displays the current actions a user can do
def action_screen():
    while True:
        print("\n", separator, "\n")
        print("                        ( |    [1] S̲T̲A̲T̲U̲S̲    |   [2] M̲E̲N̲U̲    |   [3] E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
        print("\n", separator, "\n")
        
        user_choice = input("\nEnter your choice: ")
        
        if user_choice == "1":
            display_status()
            break
            
        elif user_choice == "2":
            menu_screen()  
            break
        
        elif user_choice == "3":
            break
    
# displays the menu for inventory, skills, level up perks and map    
def menu_screen():
    while True:
        print("\n", separator, "\n")
        print("         ( |    [1] I̲N̲V̲E̲N̲T̲O̲R̲Y̲    |   [2] M̲A̲G̲I̲C̲   |   [3] P̲E̲R̲K̲S̲   |   [4] M̲A̲P̲     |    [5] E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
        print("\n", separator, "\n")
        user_choice = input("\nEnter your choice: ")
        
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
        user_choice = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_choice == "1":
            break
        
    print("\n", separator, "\n")

    
    # next scene 
    opening_scene_01()

def opening_scene_01():
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
                "-> You see the walls get closer and closer until you are almost beneath its feet...\n\n"
                   
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
        
    print("\n", separator, "\n")        
    
    # asks for user input to continue the story
    while True: 
        user_choice = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_choice == "1":
            break
        
    print("\n", separator, "\n")
    
    opening_scene_02()
        
def opening_scene_02():
    
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
                " > Imperial Soldier : Ralof of Riverwood.\n\n"\
                "-> You learn that the name of Stormcloak Soldier in your carriage is Ralof.\n\n"\
                " > Imperial Soldier : Lokir of Rorikstead.\n\n"\
                "-> It seems that the Horse Thief's name is Lokir..\n"\
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
        user_choice = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_choice == "1":
            break
    
    print("\n", separator, "\n") 
    
    count = 15
    while count > 0:
        print(".")
        count = count - 1
        time.sleep(0.2)
    
    character_creation()

def execution_scene():
    
    count = 15
    while count > 0:
        print(".")
        count = count - 1
        time.sleep(0.2)
    
    print("\n", separator, "\n\n")
        
    # special dialogue for the player's race
    if player_stats['player_race'] == "nord":
            
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : You picked a bad time to come home to Skyrim, kinsman.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
            
    elif player_stats['player_race'] == "imperial":
            
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : You're a long way from the Imperial City. What're you doing in Skyrim?.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                        
    elif player_stats['player_race'] == "breton":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : You from Daggerfall, Breton? Fleeing from some court intrigue?.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                      
    elif player_stats['player_race'] == "redguard":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : What're you doing here, Redguard? You a sellsword? A sailor from Stros M'Kai?.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                 
    elif player_stats['player_race'] == "altmer":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : You're not with the Thalmor Embassy, are you, high elf? No, that can't be right....\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                        
    elif player_stats['player_race'] == "dunmer":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : Another refugee? Gods really have abandoned your people, dark elf.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                        
    elif player_stats['player_race'] == "bosmer":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : Not many wood elves would choose to come alone to Skyrim.\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                        
    elif player_stats['player_race'] == "orsimer":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : You from one of the strongholds, Orc? How did you end up here?\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                   
    elif player_stats['player_race'] == "argonian":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : Are you a relative of one of the Riften dock workers, Argonian?\n"\
                        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                                            
    elif player_stats['player_race'] == "kahjiit":
                
        dialogue =  "-> You tell the imperial soldier with a ledger who you are.\n"\
                    "-> The imperial soldier remarks your race and origin and wonders about your identity.\n\n"\
                    " > Imperial Soldier : Are you a relative of one of the Riften dock workers, Argonian?\n"\
                            
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
    
    # pronouns to be used for the dialogue
    if player_stats['player_gender'] == "male":
        x = "he"
    elif player_stats['player_gender'] == "female":
        x = "she"
    
    dialogue =  f" > Imperial Soldier : Captain. What should we do? {x.title()}'s not on the list.\n"\
                f" > Imperial Captain : Forget the list. {x.title()} goes to the block.\n"\
                " > Imperial Soldier : By your orders, Captain. Follow the Captain, prisoner.\n\n"\
                "-> You follow the Imperial Captain and walks towards the block.\n"\
                "-> You see the other prisoners lined with Ulfric Stormcloak at the forefront.\n\n"\
                " > General Tullius : Ulfric Stormcloak. Some here in Helgen call you a hero. But a hero doesn't use the a power like 𝘛𝘩𝘦 𝘝𝘰𝘪𝘤𝘦 to murder his king and usurp his throne.\n"\
                " > Ulfric Stormcloak : *muffled grunts*\n"\
                " > General Tullius : You started this war, plunged Skyrim into chaos, and now the Empire is going to put you down, and restore the peace.\n\n"\
                "-> You hear a roar in the distance, drawing the attention of everyone gathered around the execution block, but the soldiers think little of it.\n\n"\
                " > Imperial Soldier : What was that?\n"\
                " > General Tullius : It's nothing. Carry on.\n"\
                " > Imperial Captain : Yes General Tullius. Give them their last rites.\n\n"\
                "-> A priest walks up to the center of the scene and starts praying.\n\n"\
                " > Priestess of Arkay : As we commend your souls to Aetherius, blessings of the Eight Divines upon you, for you are the salt and the earth of Nirn, our beloved--\n\n"\
                "-> A prisoner wearing the same armor as the Stormcloak Soldier in your carriage interrupted the priestess.\n"\
                "-> The prisoner walked up to the execution block while exclaiming.\n\n"\
                " > Stormcloak Soldier : For the love of Talos, shut up and let's get this over with.\n"\
                " > Priestess of Arkay : As you wish.\n\n"\
                "-> The soldier is then helped by the captain into the chopping block.\n"\
                "-> You see a man in black garb with his face covered holding an axe with an obscenely large blade.\n"\
                "-> The headsman prepares to swing.\n\n"\
                " > Stormcloak Soldier : Come on, I haven't got all morning.\n"\
                " > Stormcloak Soldier : My ancestors are smiling at me, Imperials. Can you say the same?\n\n"\
                "-> With those last defiant words to Tullius, the Imperial Captain, and the Legionnaires, the Stormcloak Soldier is beheaded by the headsman.\n"\
                "-> The Imperial Captain then shoves his lifeless body off to the side of the chopping block.\n\n"\
                "-> Differing opinions about the execution of the rebels began to form within the crowd.\n"\
                " > Stormcloak Soldier : You Imperial bastards!\n"\
                " > Female Citizen : Justice!.\n"\
                " > Old Woman : Death to the Stormcloaks!.\n\n"\
                "-> The imperials seem to be ignoring the opinions and continues on with the executions.\n\n"
                
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
           
    # special dialogue for player race        
    if player_stats['player_race'] == "nord":
        
        dialogue =  " > Imperial Captain : Next, the nord in the rags!\n\n"
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
        
    elif player_stats['player_race'] == "imperial":
                
        dialogue = " > Imperial Captain : Next, the renegade from Cyrodiil!\n\n"
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
                   
    elif player_stats['player_race'] == "argonian":
        
        dialogue = " > Imperial Captain : Next, the lizard!\n\n"
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
        
    elif player_stats['player_race'] == "kahjiit":
        
        dialogue = " > Imperial Captain : Next, the cat!!\n\n"
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
            
    else:
        
        dialogue = f" > Imperial Captain : Next, the {player_stats['player_race']}!\n\n"
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)
    
    dialogue =  "-> You hear another roar from the distance...\n\n"\
                " > Imperial Soldier : There it is again. Do you hear that?\n"\
                " > Imperial Captain : I said, next prisoner!\n"\
                " > Imperial Soldier : To the block prisoner, nice and easy.\n"\

    
    #proceeds to next scene
    alduin_helgen_attack()

def alduin_helgen_attack():  
    print("\n", separator, "\n\n")
        
    dialogue =  "-> You follow the captain's orders and walk to the block.\n"\
                "-> As you lay on your knees with your neck on the block.\n"\
                "-> The headsman lifts his axe over his head and prepares to swing.\n"\
                "-> You leave yourself to fate and wait....\n\n"\
                ".\n"\
                ".\n"\
                ".\n"\
                ".\n\n"\
                "-> You wait for your head to be lobbed off...\n\n"\
                ".\n"\
                ".\n"\
                ".\n"\
                ".\n\n"\
                "-> Nothing happens...\n\n"\
                ".\n"\
                ".\n"\
                ".\n"\
                ".\n\n"\
                "-> You hear the deafening roar passing by the sky overhead.\n"\
                "-> You see a massive black silhouette in your view flying by the clouds.\n\n"\
                " > General Tullius : What in Oblivion is that!?\n"\
                " > Imperial Captain : Sentries! What do you see?!\n"\
                " > Imperial Soldier : It's in the clouds!\n\n"\
                "-> The dark silhouette soars overhead, descending atop the stone keep before you.\n"\
                "-> Weapons are drawn as every eye turns toward the colossal creature.\n"\
                "-> Its wings stretch wide enough to shroud the sky, its scales gleam like polished obsidian, and its gaping maw looks capable of tearing a man in two.\n\n"\
                " > Stormcloak Soldier : DRAGON!!!!.\n\n"\
                "-> The dragon unleashes a deafening roar.\n"\
                "-> The skies twist and clouds contort into unnatural shapes.\n"\
                "-> Rocks start raining down from the sky.\n"\
                "-> The headsman stumbles and loses balance.\n"\
                "-> The black dragon shouts. Its earth-shaking voice reverberating through the surroundings\n"\
                "-> The headsman is killed, and a powerful Unrelenting Force hurls you backward.\n"\
                " > Black Dragon : FUS.... RO..... DAH!!\n\n"\
                " > General Tullius : Don't just stand there! Kill that thing!\n"\
                " > Imperial Soldier : Move! Move!\n"\
                " > General Tullius : Guards, get the townspeople to safety!\n"\
                " > Imperial Soldier : Gods, what does it take to kill that thing!\n\n"\
                "-> Your head feels unsteady. As you attempt to gather yourself, a familiar voice calls out to you.\n\n"\
            
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
        
    # special race dialogue from Ralof     
    if player_stats['player_race'] == 'nord': # dialogue of the playerrace is a nord
        dialogue =    " > Ralof : Hey, kinsman!\n"\
                        " > Ralof : Get up! Come on, the gods won't give us another chance!\n\n"\
    
    else: # dialogue for every other race
        dialogue =    f" > Ralof : Hey, {player_stats['player_race'].title()}.\n"\
                        " > Ralof : Get up! Come on, the gods won't give us another chance!\n\n"\
                            
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
        
    print("\n", separator, "\n")
    
    escape_from_helgen_1()
                       
def escape_from_helgen_1():
    
    count = 15
    while count > 0:
        print(".")
        count = count - 1
        time.sleep(0.2)
        
    print("\n", separator, "\n")
        
    # asks for user input to continue the story
    while True: 
        user_choice = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_choice == "1":
            break
        
    print("\n", separator, "\n")
        
    dialogue =  "-> Your hands are still bound. Ralof asks you to get up\n" \
            
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
    
    print("\n", separator, "\n")
    
    print("You may:")
    print("( | [1] Get up and follow Ralof | )")
    
    while True: 
        user_choice = input("\nEnter your choice: ")
    
        if user_choice == "1":
            break
        
    print("\n", separator, "\n")
    
    dialogue =  "-> You rise to your feet and follow Ralof.\n" \
                "-> Ralof guides you toward a nearby stone watchtower..\n\n"\
                " > Ralof : This way, come on!\n\n"\
                "-> As you trail behind Ralof, the anguished screams of townspeople fill the air.\n"\
                "-> You catch glimpses of Imperial Soldiers battling the black dragon.\n\n"\
                " > Imperial Soldier : What in the Eight Divines is this thing?!\n"\
                " > Imperial Soldier : How in Oblivion do we kill this thing?!\n"\
                " > Imperial Soldier : It's still coming!\n"\
                " > Imperial Soldier : By Ysmir! Nothing kills it!\n\n"\
                "-> You witness an Imperial soldier struck by a falling meteor, meeting a swift death.\n\n"\
                " > Imperial Soldier : Yeargh!\n\n"\
                "-> You and Ralof enter the watchtower, where several Stormcloak soldiers, along with Ulfric Stormcloak, are taking shelter.\n"\
                "-> Ralof closes the door behind you.\n\n"\
                " > Ralof : Jarl Ulfric! What is that thing?\n"\
                " > Ralof : Could the legends be true?\n"\
                " > Ulfric Stormcloak : Legends dont burn down villages.\n\n"\
                "-> A thunderous explosion erupts outside, shaking the watchtower.\n\n"\
                " > Ulfric Stormcloak : We need to move. Now!\n"\
                " > Ralof : Up through the tower, let's go!\n"\
            
    for i in dialogue:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(read_speed)
        
    print("\n", separator, "\n")
    
    print("You may:")
    print("( |  [1] Follow Ralof up the tower  | )")
    print("( |  [2] Listen in on the wounded Stormcloak Soldiers  | )")

    while True:
        user_choice = input("\nEnter your choice: ")
        
        print("\n", separator, "\n")
    
        if user_choice == "1":
            dialogue_1
            break
        
        elif user_choice == "2":
            dialogue_2 
    
    def dialogue_1():                
        dialogue = "asdasdas"
    
    def dialogue_2(): 
        
        dialogue =  "-> Upon entering the watchtower, you notice Stormcloak soldiers attending to their injuries.\n"\
                        "-> Two wounded Stormcloak Soldiers lie on the floor\n"\
                        "-> Another Stormcloak Soldier is tending to the their wounds.\n"\
                        " > Stormcloak Soldier : They're hurt, but they'll live.\n"\
                        " > Stormcloak Soldier : Another second out there with the dragon and they'd both be dead...\n"\
        
        for i in dialogue:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(read_speed)

                       
# program launch into main menu
#opening_scene_p1()
#opening_scene_p2()
#execution_scene()
#alduin_helgen_attack()
escape_from_helgen_1()

#display_status()
#action_screen()
#character_creation()

#main_menu_visual()
#main_menu_function()