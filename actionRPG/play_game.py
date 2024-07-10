import random
import os
import weapon
import races
# import equipment
import time
import profession
import monstars
# import character
# import story


#=================================================== GAMELOGIC====================================================#


# Create gameplay logic
def play_game():
    print("Welcome to 'Die slowly!'\n")


    # player1 = (races.human, profession.Knight, weapon.sword,)
    player1 = races.Player(name="Player1", races=races.elf, profession=profession.Knight, weapon=weapon.sword)
    print(player1.races.name)
    print(player1.profession.name)
    print(player1.weapon.name)
    print(f"TP:{player1.tp}%")
    print(f"MP:{player1.mp}%")
    print('')
  



 
    # Player2 = monstars.Player2,weapon.main_weapon_name, weapon.offhand_weapon_name
    Player2 = random.choice(monstars.monstars_list)
    
    
    print(Player2.name)
    print(Player2.main_weapon.name)
    print(Player2.offhand_weapon.name)
    print(f"TP:{Player2.tp}%")
    print(f"HP:{Player2.hp}")

    # input()
    # Quick stop to check things

   

    turn = 0
    while player1.hp > 0 and Player2.hp > 0:
        turn+=1
        print('=======================================================================================')
        print(f'Turn: {turn}\n')
        print(f'{player1.races.name} {player1.profession.name} turn:')
        print(player1.status_effects)
        player1.Attack(Player2)
        print(f'{Player2.name} health:', Player2.hp)
        print()

        if Player2.hp <= 0:
            print("Player 1 wins!")
            break

        print("Player 2's turn:")
        print(Player2.status_effects)
        for _ in range(Player2.num_attack):
         Player2.Attack(player1)
        print(f'{player1.profession.name} health:', player1.hp)
        print()

        if player1.hp <= 0:
            print("Player 2 wins!")
            break




if __name__ == "__main__":
  play_game()
