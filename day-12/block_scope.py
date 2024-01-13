# # global scope
# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()

# print(player_health)
# enemies = 1
game_level = 3
def create_ennemy():
    enemies = ['Skeleton','Zombie','Alien']
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)