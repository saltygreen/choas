import random
import races
import monstars


def start_story():
    print("You wake up in a mysterious forest. You see a path to your left and a path to your right.")
    choice = input("Which path do you choose? (left/right): ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_story()

def left_path():
    print("You chose the left path. You come across a river. Do you swim across or find another way?")
    choice = input("What do you do? (swim/find): ").lower()
    
    if choice == "swim":
        roll = random.randint(1, 20)
        if roll >= 10:
            print(roll)
            print("You swim across and reach the other side safely.")
        elif roll <= 10:
            print(roll)
            print("You are having trouble swimming across so you must find another way.")
        elif choice == "find":
            print("You look around and find a bridge to cross the river.")
    else:
        print("Invalid choice. Please try again.")
        left_path()

def right_path():
    random_monstars = random.choice(monstars.monstars_list)
    print(random_monstars.name)
    print("You chose the right path. You encounter a group of monsters. Do you fight or run away?")
    choice = input("What do you do? (fight/run): ").lower()
    
    if choice == "fight":
        
        print("You bravely are your read? " + monstars)
        
    elif choice == "run":
        print("You run away from the goblins and escape.")
        return

# # Start the story
# start_story()
