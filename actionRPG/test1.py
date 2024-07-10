import random

class Player:
    # Creates blueprint for a Player for this match whether computer or human.
    def __init__(self, name, races, profession, weapon) -> None:
        self.name = name
        self.races = races
        self.weapon = weapon 
        self.defense = 0 
        self.profession = profession
        self.AC = self.races.AC + self.profession.profession_modifier
        self.accuracy = self.weapon.weapon_accuracy + self.profession.profession_modifier
        self.hp = 1500
        self.defense = weapon.defense_modifier
        self.races = races
        self.tp = 0
        self.maxtp = 100
        self.mp = 0
        self.maxmp = 100
        self.successful_hits = 0
        self.element_weakness = []
        self.status_effects = {}  # Dictionary to store active status effects
        self.stun_counter = 0  # Counter for the stun effect
        self.accuracy_modifier = self.races.dex + self.races.agi
        self.block_with_shield = 20
        self.confused = False
        self.confusion_turns = 0
        self.equipped_weapons = []

    def Equip(self, weapons):
        if len(weapons) <= 2:
            self.equipped_weapons = weapons
            for weapon in weapons:
                print(f"{self.name} has equipped a {weapon}.")
        else:
            print("holding more than one weapon")

    # Normal Attack
    def Attack(self, target):
        hit_calc = (int(self.accuracy_modifier) + int(self.weapon.weapon_accuracy)) >= target.AC
        if hit_calc:  # If attack hits target
            self.tp += 5  
            self.successful_hits += 1
            if self.tp == self.maxtp:
                self.skillchain_attack(target)
            target.hp -= self.weapon.damage
            print(f'{self.name} hits {target.name} for {self.weapon.damage} damage!')
        else:
            print(f'\n{self.name} missed the target!')

    # Special Attack
    def skillchain_attack(self, target):
        self.successful_hits += 1
        self.tp += self.weapon.tp_modifier
        target.element_weakness.append(self.weapon.element)
        print(f'{self.name} has used {self.weapon.skillchain}')
        if self.tp >= 100:
            self.tp = 0
        if self.successful_hits % 3 == 0:
            print(f'{self.name} gains TP!')
            self.tp += 5
        elif self.tp >= self.maxtp:
            print(f'{self.name} triggers the skillchain attack {self.weapon.skillchain}!')
            self.tp = 0
        if self.weapon.element == "fire":
            print(f'{target.name} is burning!\n')
            target.status_effects.update({'burning': 0.5})
            self.process_status_effects()
        elif self.weapon.element == "water":
            print(f'{target.name} is poisoned!\n')
            target.status_effects.update({'poison': 0.5})
        elif self.weapon.element == "earth":
            print(f'{target.name} is stunned!\n')
            target.status_effects.update({'stun': 0})
            target.stun_counter = 3
        elif self.weapon.element == "wind":
            print(f'{target.name} has lower accuracy!\n')
            target.status_effects.update({'lower accuracy': 0})
            self.process_status_effects()
        elif self.weapon.element == "psychic":
            print(f'{target.name} is losing TP\n')
            print(f'{target.tp}tp%')
            target.status_effects.update({'filling MP': True})
            self.process_status_effects()
        elif self.weapon.element == "lighten":
            print(f'{target.name} is confused!\n')
            target.status_effects.update({'hitting himself!': 5})
            self.process_status_effects()

    # Status effects
    def apply_status_effects(self, effect_name, damage_per_turn):
        self.status_effects[effect_name] = damage_per_turn

    def process_status_effects(self):
        for effect, damage_per_turn in list(self.status_effects.items()):
            if effect == "stun":
                self.stun_counter -= 1
                if self.stun_counter <= 0:
                    del self.status_effects[effect]
                    print(f'{self.name} is no longer stunned!')
            else:
                self.hp = max(0, self.hp - damage_per_turn)
                print(f'{self.name} takes {damage_per_turn} damage from {effect}!')
                if self.hp <= 0:
                    print(f'{self.name} has been defeated by {effect}!')
                    break
                if effect == "burn":
                    print(f'{self.name} is still burning!')
                elif effect == "poison":
                    print(f'{self.name} is still poisoned!')
                elif effect == "lighten":
                    if self.confused:
                        if self.confusion_turn < 3:
                            print(f'{self.name} is confused and hits themselves!\n')
                            self.successful_hits += 1
                            self.confusion_turns += 1
                            return
                        else:
                            print(f'{self.name} is no longer confused.\n')
                            self.confused = False
                            self.confusion_turns = 0
                elif effect == "lower accuracy":
                    print(f'{self.name} still has lower accuracy')
                self.maxmp = min(100, self.maxmp + 20)
                print(f'{self.name} takes {damage_per_turn} loss of TP {effect}!')
                if self.mp >= 20:
                    print(f'{self.name} MP is filling up {effect}!')

    def magic_chain(self):
        if self.mp == self.maxmp:
            print(f"Turn to ASHES: FIREBALL!")
            damage = 24
            print(f"Fireball deals {damage} damage.")
            self.burn_status = True
            self.mp = 0

    def apply_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been turned to ASH!")

    def check_mp(self):
        if self.mp < 10:
            print("MP is below 10%. Draining TP to fill MP..")
            tp_to_fill = 100 - self.mp
            tp_cost = tp_to_fill
            if self.tp >= tp_cost:
                self.mp += tp_to_fill
                self.tp -= tp_cost
                print(f"MP is now {self.mp}%")
            else:
                print("Not enough TP to fill MP.")

    def block_with_shield(self):
        roll = random.randint(1, 20) + self.weapon.defense_modifier
        if roll >= 10:
            print(f"{self.name} blocks with the shield!")
        else:
            print(f"{self.weapon.name} fails to block the attack!")

    def parry_with_sword(self, target):
        roll = random.randint(1, 20) + self.weapon.defense_modifier
        if roll >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            roll = random.randint(1, 20) + target.weapon.attack_modifier
            if roll >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False

    def parry_with_dagger(self, target):
        roll = random.randint(1, 20) + self.weapon.defense_modifier
        if roll >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            roll = random.randint(1, 20) + target.weapon.attack_modifier
            if roll >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False

    def counter_punch_with_fists(self, target):
        roll = random.randint(1, 20) + self.weapon.defense_modifier
        if roll >= 10:
            print(f"{self.profession.name} successfully counters the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to counter the attack!")
            roll = random.randint(1, 20) + target.weapon.attack_modifier
            if roll >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'counter': 0})
            return False

    def defend(self):
        while True:
            choice = input("Choose your defense action: [1] Block with Shield, [2] Parry with Sword, [3] Parry with Dagger, [4] Counter-punch with Fists\n")
            if choice == "1":
                self.block_with_shield()
                break
            elif choice == "2":
                self.parry_with_sword()
                break
            elif choice == "3":
                self.parry_with_dagger()
                break
            elif choice == "4":
                self.counter_punch_with_fists()
                break
            else:
                print("Invalid choice. Please try again.")
