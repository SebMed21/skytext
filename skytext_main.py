#dictionary for player status
player_stats = {
    'player_name'           : "Prisoner",
    #player values           
    'player_health'         : 100,
    'player_magicka'        : 100,
    'player_stamina'        : 100,  
    'player_exp'            : 0,
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

#a function that displays current player status
def display_status():
    print("")
    print(player_stats['player_name'])
    print("HP:", player_stats['player_health'], 
          "| MP:", player_stats['player_magicka'], 
          "| STA:", player_stats['player_stamina'])
    print("")
    
display_status()