import time
import sys

# dictionary for player status
player_stats = {
    'player_name'           : "Prisoner",
    #player values           
    'player_health'         : 0,
    'player_magicka'        : 0,
    'player_stamina'        : 0,  
    'player_experience'     : 0,
    'player_level'          : 1,    
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

# initialization for text and other utils
separator = "================================================================================================================="
    # print("\n", separator, "\n")
    # user_choice = input("Enter your choice: ")

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
    print("⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⢠⣾⡿⠁⠀⠀⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀", "[1] NEW GAME           ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠀⢠⣿⡟⠀⠀⠀⠀⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀","[2] CONTINUE GAME      ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠈⣿⣇⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀","[3] EXIT               ")
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
            user_choice = input("Are you sure you want to quit? [ 1 = Y̲E̲S̲ | 2 = N̲O̲ ] ")
            
            if user_choice == "1":
                break
                
            elif user_choice == "2":
                continue
                   
# displays the current actions a user can do
def action_screen():
    while True:
        print("\n", separator, "\n")
        print("                        ( |    (1) S̲T̲A̲T̲U̲S̲    |   (2) M̲E̲N̲U̲    |   (3) E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
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
        print("         ( |    (1) I̲N̲V̲E̲N̲T̲O̲R̲Y̲    |   (2) M̲A̲G̲I̲C̲   |   (3) P̲E̲R̲K̲S̲   |   (4) M̲A̲P̲     |    (5) E̲X̲I̲T̲ M̲E̲N̲U̲   | )")
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
    print("HP:", player_stats['player_health'], 
          "| MP:", player_stats['player_magicka'], 
          "| STA:", player_stats['player_stamina'])
    print("EXP: ", player_stats['player_experience'],
          "| LVL :", player_stats['player_level'])
    print("\n", separator, "\n")


#      GAMEPLAY FUNCTIONS!!!!!!!!!!!!!!!!!

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
        time.sleep(0.03)
    
    # format
    count = 5
    while count > 0:
        print("")
        count = count - 1
        time.sleep(0.1)  
    
    # "Alduin" art with out delay
    print("")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀")
    time.sleep(0.1)
    print("                         ⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀")
    time.sleep(0.1)
    print("                          ⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆")
    time.sleep(0.1)
    print("                          ⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄")
    time.sleep(0.1)
    print("                          ⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷")
    time.sleep(0.1)
    print("                          ⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹")
    time.sleep(0.1)
    print("                          ⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸")
    time.sleep(0.1)
    print("                          ⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼")
    time.sleep(0.1)
    print("                          ⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    time.sleep(0.1)
    print("                          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")   
    time.sleep(0.1)
    
    # format
    count = 5
    while count > 0:
        print("")
        count = count - 1
        time.sleep(0.1)  
    
    print("\n", separator, "\n")
    
    # next scene 
    opening_scene()

def opening_scene():
    #count = 15
    #while count > 0:
       # print(".")
        #count = count - 1
       # time.sleep(0.1)
        
    print("\n", separator, "\n")    
    
    print("\n                                                 ★ U N B O U N D \n\n\n")
    
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
        time.sleep(0.0001)
        
    print("\n", separator, "\n")        
    
    # asks for user input to continue the story
    while True: 
        user_input = input("                                    CONTINUE? [ P̲R̲E̲S̲S̲ 1 T̲O̲ C̲O̲N̲T̲I̲N̲U̲E̲ ] ")
    
        if user_input == "1":
            break
        
    print("\n", separator, "\n")
        
    dialogue =  ""

    
# program launch into main menu

opening_scene()


#main_menu_visual()
#main_menu_function()

#action_screen()