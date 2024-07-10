import random
# import equipment
import weapon
import races

# ========================= Create Player Class =============================

class Player:
    
    # Creates blueprint for a Player for this match whether computer or human.
    def __init__(self, name, races, profession, weapon) -> None:
        self.name = name
        self.weapon = weapon 
        self.defense = 0 
        self.AC = self.races + self.profession
        self.accuracy = self.weapon + self.profession
        self.hp = 1500
        self.defense = weapon.defense_modifier
        self.profession = profession
        self.races = races
        self.tp = 0
        self.maxtp = 100
        self.mp = 0
        self.maxmp = 100
        self.successful_hits = 0
        self.element_weakness = []
        self.status_effects = {} # Dictionary to store active status effects
        self.stun_counter = 0 #Counter for the stun effect
        self.accuracy_modifier = self.races.dex + self.races.agi
        self.block_with_shield = 20
        self.confused = False
        self.confusion_turns = 0


    def Equip(self, weapons):
        if len(weapons) <= 2:
            self.weapon = weapons
        else:
              print("holding more then one weapon")

        
    # Normal Attack
    def Attack(self, target):
        hit_calc = (int(self.accuracy_modifier) + int(self.weapon.weapon_accuracy)) >= target.AC
        if hit_calc:
            # print(hit_calc)
            # If attack hits target
            
            # print(f'Target HP: {target.hp} / 300')
            self.tp += 5
            self.successful_hits += 1
            if self.tp == self.maxtp:
                  self.skillchain_attack(target)
            if self.weapon == weapon.shield:
                if self.Attack() <= self.block_with_shield:
                    damage_blocked = self.block_with_shield = 5
                target.hp -= damage_blocked
            elif self.weapon == weapon.sword or self.weapon == weapon.dagger:
                if self.Attack() <= self.parry_with_sword_or_dagger(target):
                 damage_blocked = self.parry_with_sword_or_dagger(target)
            elif self.weapon == weapon.fists:
                if self.Attack() <= self.counter_punch_with_fists:
                     damage_blocked = self.counter_punch_with_fists(target)
                damage_dealt = self.counter_punch_with_fists(target)
                target.hp -= damage_dealt
                # Counter attack with fists for 5 damge if successful counter
                if hit_calc:
                    print(f"{target.name} counter attacks with a punch!")
                self.hp -= 5

            # Happens no matter what
            target.hp = target.hp - self.weapon.damage
            print(f'{self.name} hits {target.name} for {self.weapon.damage} damage!')
        else:
            # If attack misses target
            print(f'\n{self.name} missed the target!')

    


    # Special Attack
    def skillchain_attack(self, target): #element, weakness, skillchain, name, psychic):
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
                        #Apply burning effect with DoT of 0.5
                        target.status_effect.update({'burning':0.5})
                        self.process_status_effects()
            elif self.weapon.element == "water":
                        print(f'{target.name} is poison!\n')
                        #Apply poison effect with DoT of 0.5
                        target.status_effect.update({'poison':0.5})
            elif self.weapon.element == "earth":
                    print(f'{target.name} is stunned!\n')
                    #Appy stun effect (no DoT)
                    target.status_effect.update({'stun':0})
                    #Set stun counter to 3 turns
                    target.stun_counter = 3
            elif self.weapon.element == "wind":
                    print(f'{target.name} has lower accuracy!\n')
                    #Apply lower accuracy effect (no DoT)
                    target.status_effect.update({'lower accuracy':0})
                    self.process_status_effects()
            elif self.weapon.element == "psychic":
                    print(f'{target.name} is loosing TP\n')
                    print(f'{target.tp}tp%')
                    #Apply loosing TP to fill Mp
                    target.status_effect.update({'filling MP': True})
                    self.process_status_effects()
            elif self.weapon.element == "Lighten":
                  print(f'{target.name} is confused!\n')
                  # Apply an confusion effect to make the player hit himself.
                  target.status_effect.update({'hitting him self!':5})
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
                    print(f'{self.name} is still poison!')
                elif effect == "lighten":
                      if self. confused:
                       if self.confusion_turn < 3:
                            print(f'{self.name} is confused and hits themselves!\n')
                            self.successful_hits
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
                    print(f'{self.name} MP is feeling up {effect}!')


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
                    print(f"{self.name} has been turn to ASH!")
    def check_mp():
            global mp, tp
            if mp < 10:
                    print("MP is below 10%. Draining TP to fill MP..")
                    tp_to_fill = 100 - mp
                    tp_cost = tp_to_fill
                    if tp >= tp_cost:
                            mp += tp_to_fill
                            tp -= tp_cost
                            print(f"MP is now {mp}%")
                    else:
                            print("Not enough TP to fill MP.")

    def block_with_shield(self):
           # SHIELD BLOCKING LOGIC
                  roll = random.randint(1, 20) + self.weapon.defense_modifier
                  if roll >= 10:
                    self.block_with_shield(target)
                    print(f"{self.name} blocks with the shield!")
                  else:
                    print(f"{self.weapon.shield} fails to block the attack!")
                    
            # Assuming shield bash does 3 damage
            # return 3

    def parry_with_sword_or_dagger(self, target):
        roll = random.randint(1, 20) + self.weapon.defense_modifier
        if roll >= 10:
            print(f"{self.profession.name} successfully parries the attack!")
            return True
        else:
            print(f"{self.profession.name} fails to perry the attack!")
        # while self.hp > 0 and target.hp > 0:
            # Player 2 attacks Player 1
            roll = random.randint(1, 20) + self.weapon.defense_modifier
            if roll >= target.AC:
                print(f"{target.name} hits {self.profession.name}!")
                # Player1 attempts to parry
                if not self.parry_with_sword_or_dagger(target):
                     # If parry fails, Player2 deals damage
                    #  self.hp -= random.randint(1, 10) #Assuming damge is 1-10
                     print(f"{target.name} deals damage to {self.profession.name}. {self.name} HP: {self.hp}")
            # if (random.randint(1, 20)+ self.weapon.defense_modifier) >= 20:
            #     print(f"{self.name} parries with the sword/dagger!")
                # Assuming parry deals no damge but adds a status effect for the next attack
            self.status_effects.update({'parry':0})

    def counter_punch_with_fists(self):
            print(f"{self.name} counters with a punch!")
            # Assuming counter punch deals 5 damage
            return 5
    


       