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

#displays the current actions a user can do
def action_screen():
    print("")

#displays the menu for inventory, skills, level up perks and map    
def menu_screen():
    print("")
    print("( |    (1) Inventory    |   (2) Magic   |   (3) Perks   |   (4) Map     | )")
    print("")
    user_choice = input("Enter your choice: ")
    
    if user_choice == "1":
        inventory_screen()
    
    elif user_choice == "2":
        magic_screen()
        
    elif user_choice == "3":
        perks_screen()
        
    elif user_choice == "4":
        map_screen()
        

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
    print("")
    print(player_stats['player_name'])
    print("HP:", player_stats['player_health'], 
          "| MP:", player_stats['player_magicka'], 
          "| STA:", player_stats['player_stamina'])
    print("EXP: ", player_stats['player_experience'],
          "| LVL :", player_stats['player_level'])
    print("")

menu_screen()