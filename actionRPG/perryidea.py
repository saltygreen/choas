import random

class Player:
    def __init__(self, name, AC, defense_modifier):
        self.name = name
        self.AC = AC
        self.defense_modifier = defense_modifier
        self.hp = 100  # Assuming starting HP is 100

    def parry_attempt(self):
        roll = random.randint(1, 20) + self.defense_modifier
        if roll >= 20:
            print(f"{self.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.name} fails to parry the attack.")
            return False

class Combat:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start_combat(self):
        while self.player1.hp > 0 and self.player2.hp > 0:
            # Player 2 attacks Player 1
            attack_roll = random.randint(1, 20) + self.player2.defense_modifier
            if attack_roll >= self.player1.AC:
                print(f"{self.player2.name} hits {self.player1.name}!")
                # Player 1 attempts to parry
                if not self.player1.parry_attempt():
                    # If parry fails, Player 2 deals damage
                    self.player1.hp -= random.randint(1, 10)  # Assuming damage range is 1-10
                    print(f"{self.player2.name} deals damage to {self.player1.name}. {self.player1.name} HP: {self.player1.hp}")
            else:
                print(f"{self.player2.name} misses the attack.")

            # Check if Player 1 is defeated
            if self.player1.hp <= 0:
                print(f"{self.player2.name} wins!")
                break

if __name__ == "__main__":
    player1 = Player("Player 1", AC=15, defense_modifier=2)
    player2 = Player("Player 2", AC=12, defense_modifier=1)
    combat = Combat(player1, player2)
    combat.start_combat()
