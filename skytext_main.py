#dictionary for player status
player_stats = {
    'player_name'           : "Prisoner",
    #player values           
    'player_health'         : 100,
    'player_magicka'        : 100,
    'player_stamina'        : 100,  
    'player_experience'     : 0,
    'player_level'          : 1,    
}
#dictionary for player's equipped gear
player_equipment = {
    'player_right_hand'     : "",
    'player_left_hand'      : "",
    'player_helmet'         : "",
    'player_body'           : "",
    'player_gloves'         : "",    
    'player_boots'          : "",
}
#dictionary for the current items in the player inventory
player_inventory = {}

#dictionary for items, equipment, and spells
sword = {}
axe = {}
hammer = {}
shield = {}
helmet = {}
body = {}
gloves = {}
boots = {}

magic  = {}

#initialization for text and other utils
separator = "=========================================================================================="
    #print("\n", separator, "\n")

#displays the current actions a user can do
def action_screen():
    while True:
        print("\n", separator, "\n")
        print("( |    (1) S̲T̲A̲T̲U̲S̲    |   (2) M̲E̲N̲U̲    |   (3) E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
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
    
#displays the menu for inventory, skills, level up perks and map    
def menu_screen():
    while True:
        print("\n", separator, "\n")
        print("( |    (1) I̲N̲V̲E̲N̲T̲O̲R̲Y̲    |   (2) M̲A̲G̲I̲C̲   |   (3) P̲E̲R̲K̲S̲   |   (4) M̲A̲P̲     |    (5) E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
        print("\n", separator, "\n")
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            inventory_screen()
            return False
        
        elif user_choice == "2":
            magic_screen()
            return False
            
        elif user_choice == "3":
            perks_screen()
            return False
            
        elif user_choice == "4":
            map_screen()
            return False

        elif user_choice == "5":
            return False
        
#displays the contents of the player's inventory
def inventory_screen():
    print("*show inventory here*")
    
#displays the magic spells the player can currently use
def magic_screen():
    print("*show magic here*")

#displays the perks the player can take (character upgrades)
def perks_screen():
    print("*show perks here*")
    
#displays the map
def map_screen():
    print("*shows the map*")
    
#displays current player status
def display_status():
    print("\n", separator, "\n")
    print(player_stats['player_name'])
    print("HP:", player_stats['player_health'], 
          "| MP:", player_stats['player_magicka'], 
          "| STA:", player_stats['player_stamina'])
    print("EXP: ", player_stats['player_experience'],
          "| LVL :", player_stats['player_level'])
    print("\n", separator, "\n")


action_screen()