game_level = 3 
def create_enemy(): 
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5: 
        new_enemy = enemies[0]

    # You can access new_enemy 
    print(new_enemy)

create_enemy()