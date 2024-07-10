import random
# import equipment
import weapon
# import character

# ========================= Create Player Class =============================

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
            if self.weapon == weapon.shield:
                if self.Attack() <= self.block_with_shield:
                    damage_blocked = self.block_with_shield
                target.hp -= damage_blocked
                print(f'{self.name} blocks with the shield, reducing damage by {damage_blocked}!')
            elif self.weapon == weapon.sword or self.weapon == weapon.dagger or self.weapon == weapon.short_sword or self.weapon == weapon.axe:
                if self.hit_chnce() <= target.AC:
                    if self.weapon == weapon.sword:
                        damage_blocked = self.parry_with_sword(target)
                    if self.weapon == weapon.dagger:
                        damage_blocked = self.parry_with_dagger(target)
                    if self.weapon == weapon.short_sword:
                        damage_blocked = self.parry_with_shortsword(target)
                    elif self.weapon == weapon.axe:
                        damage_blocked = self.parry_with_axe(target)
                    target.hp -= damage_blocked
                    print(f'{self.name} parries with {self.weapon.name}, reducing damage by {damage_blocked}!')
            elif self.weapon == weapon.fists:
                if self.Attack() <= self.counter_punch_with_fists:
                    damage_blocked = self.counter_punch_with_fists(target)
                    target.hp -= damage_blocked
                    print(f"{self.name} counter punches, dealing {damage_blocked} damage!")
                    if hit_calc:
                        print(f"{target.name} counter attacks with a punch!")
                    self.hp -= 5
                    
    


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
            target.apply_status_effects('burning', damage_per_turn=2, duration=3)
        elif self.weapon.element == "water":
            print(f'{target.name} is poisoned!\n')
            target.apply_status_effects('poison', damage_per_turn=2, duration=3)
        elif self.weapon.element == "earth":
            print(f'{target.name} is stunned!\n')
            target.apply_status_effects('stun', damage_per_turn=0, duration=3)
            target.stun_counter = 3
        elif self.weapon.element == "wind":
            print(f'{target.name} has lower accuracy!\n')
            target.apply_status_effects('lower accuracy', damage_per_turn=0, duration=3)
        elif self.weapon.element == "psychic":
            print(f'{target.name} is losing TP')
            print(f'{target.tp}tp%')
            print(f'{self.mp}mp%')
            target.apply_status_effects('filling MP', damage_per_turn=0, duration=3)
        elif self.weapon.element == "lighten":
            print(f'{target.name} is confused!\n')
            target.apply_status_effects('hitting himself!', damage_per_turn=5, duration=3)
    
    # Status effects
    def apply_status_effects(self, effect_name, damage_per_turn):
        self.status_effects[effect_name] = damage_per_turn

    def process_status_effects(self):
        for effect, details in list(self.status_effects.items()):
            damage_per_turn = details['damage_per_turn']
            duration = details['duration']

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

   
    def cast_fireball(self, target):
        mp_cost = 10
        if self.tp >= mp_cost:
            print(f'{self.name} casts Fireball on {target.name}!')
            target.apply_damage(20)
            self.tp -= mp_cost
        else:
            print(f'{self.name} does not have enough TP to cast Fireball!')
            target.check_mp()

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
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.name} blocks with the shield!")
        else:
            print(f"{self.weapon.name} fails to block the attack!")

    def parry_with_sword(self, target):
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            hit_chnce = random.randint(1, 20) + target.weapon.attack_modifier
            if hit_chnce >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False


    def parry_with_shortsword(self, target):
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            hit_chnce = random.randint(1, 20) + target.weapon.attack_modifier
            if hit_chnce >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False

    def parry_with_dagger(self, target):
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            hit_chnce = random.randint(1, 20) + target.weapon.attack_modifier
            if hit_chnce >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False
        
    def parry_with_axe(self, target):
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to parry the attack!")
            hit_chnce = random.randint(1, 20) + target.weapon.attack_modifier
            if hit_chnce >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'parry': 0})
            return False

    def counter_punch_with_fists(self, target):
        hit_chnce = random.randint(1, 20) + self.weapon.defense_modifier
        if hit_chnce >= 10:
            print(f"{self.profession.name} successfully counters the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to counter the attack!")
            hit_chnce = random.randint(1, 20) + target.weapon.attack_modifier
            if hit_chnce >= self.AC:
                print(f"{target.name} hits {self.profession.name}!")
                damage = random.randint(1, 10)
                self.hp -= damage
                print(f"{target.name} deals {damage} damage to {self.profession.name}, {self.name} HP: {self.hp}")
            else:
                print(f"{target.name} misses the attack!")
            self.status_effects.update({'counter': 0})
            return False
        
    def hit_chnce(self, target):
        hit_chnce = random.randint(1, 20)
        return hit_chnce



# ================================================= RACES ===============================================#
  
class Races:
    def __init__(self, name, AC, stre, dex, vit, agi, mind, wis, cha) -> None:
        self.name = name
        self.AC = AC
        self.stre = stre
        self.dex = dex
        self.vit = vit
        self.agi = agi
        self.mind = mind
        self.wis = wis
        self.cha = cha
        pass
# ==================================== Races ====================================================== #
    
human = Races(name="Human",
              AC=11,
              stre=15,
              dex=14,
              vit=13,
              agi=12,
              mind=10,
              wis=12,
              cha=8,
              )
elf = Races(name="Elf",
            AC=11,
            stre=8,
            dex=16,
            vit=12,
            agi=15,
            mind=15,
            wis=10,
            cha=10,
            )
dwarf = Races(name="Dwarf",
              AC=12,
              stre=14,
              dex=10,
              vit=14,
              agi=12,
              mind=10,
              wis=15,
              cha=8,
              )
drakon = Races(name="Drakon",
               AC=12,
               stre=15,
               dex=10,
               vit=14,
               agi=12,
               mind=8,
               wis=12,
               cha=13,
               )
lilfoot = Races(name="Lil-foot",
                AC=11,
                stre=8,
                dex=16,
                vit=12,
                agi=15,
                mind=10,
                wis=14,
                cha=12,
                )
half_orc = Races(name="Half-Orc",
                 AC=12,
                 stre=16,
                 dex=14,
                 vit=14,
                 agi=13,
                 mind=8,
                 wis=10,
                 cha=12,
                 )
Races_list =[human,elf,dwarf,drakon,lilfoot,half_orc]