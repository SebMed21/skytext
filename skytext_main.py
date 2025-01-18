player_stats = {
    'player_name'           : "Prisoner",
    #player values           
    'player_health'         : 100,
    'player_magicka'        : 100,
    'player_stamina'        : 100,  
    'player_exp'            : 0,
    'player_level'          : 1,    
}

player_equipment = {
    'player_right_hand'     : "",
    'player_left_hand'      : "",
    'player_helmet'         : "",
    'player_body'           : "",
    'player_gloves'         : "",    
    'player_boots'          : "",
}

def display_status():
    print(player_stats['player_name'])
    print("")
    print("HP:", player_stats['player_health'])
    print("MP:", player_stats['player_magicka'])
    print("STA:", player_stats['player_stamina'])
    
display_status()