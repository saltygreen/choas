import weapon
import random
 

class Monstars:
    def __init__(self, name, AC, hp, tp, mp, stre, dex, vit, agi, mind, wis, cha, num_attack, main_weapon, offhand_weapon) -> None:
        self.name = name
        self.hp = hp

        self.tp = tp
        self.mp = mp
        self.AC = AC
        self.stre = stre
        self.dex = dex
        self.vit = vit
        self.agi = agi
        self.mind = mind
        self.wis = wis
        self.cha = cha
        self.successful_hits = 0
        self.accuracy_modifier = self.dex + self.agi
        self.num_attack = num_attack
        self.weapon_accuracy = []
        self.main_weapon = main_weapon
        self.offhand_weapon = offhand_weapon
        self.element_weakness = []
        self.status_effects = {} # Adding status_effects attribute
        self.stun_counter = 0 # Counter for the stun effect
        self.confused = False
        self.confused_turns = 0
        self.accuracy = 0
        # self.Attacks = num_attack
        # self.stats = monstars_stats


    
    def Equip(self, main_weapon, offhand_weapon):
        if main_weapon is not None and offhand_weapon is not None:
            self.main_weapon = main_weapon
            self.offhand_weapon = offhand_weapon
            
        else:
                print("Please provide both main and offhand weapons")

    # Normal Attack
    def Attack(self, target):
        hit_calc = (int(self.accuracy_modifier) + int(self.main_weapon.weapon_accuracy)) >= target.AC
        damage = self.main_weapon.damage

        # If attack hits target
        if hit_calc: 
            self.tp += 5
            self.successful_hits += 1
            # if self.offhand_weapon == weapon.shield:
            #     damage_blocked = self.block_with_shield(target)
            #     target.hp -= damage_blocked
            # elif self.main_weapon == weapon.sword or self.main_weapon == weapon.dagger:
            #     self.parry_with_sword_or_dagger(target)
            # elif self.main_weapon == weapon.fists:
            #     damage_dealt = self.counter_punch_with_fists()
            #     target.hp -= damage_dealt
            #     # Counter attack with fists for 5 damge if successful counter
            #     if hit_calc:
            #         print(f"{target.name} counter attacks with a punch!")
            #     self.hp -= 5

            
            target.hp -= damage
            print(f'{self.name} hits {target.name} for {self.main_weapon.damage} damage!')

    
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
            
        else:
            # If attack misses target
            print(f'\n{self.name} missed the target!')

    def apply_status_effects(self, effect_name, damage_per_turn, duration):
        self.status_effects[effect_name] = {'damage_per_turn': damage_per_turn, 'duration': duration}

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
                details['duration'] -= 1
                if details['duration'] <= 0:
                    del self.status_effects[effect]
                    print(f'{self.name} is no longer affected by {effect}!')
                if self.hp <= 0:
                    print(f'{self.name} has been defeated by {effect}!')
                    break
                if effect == "burn":
                    print(f'{self.name} is still burning!')
                elif effect == "poison":
                    print(f'{self.name} is still poisoned!')
                elif effect == "lighten":
                    if self.confused:
                        if self.confusion_turns < 3:
                            print(f'{self.name} is confused and hits themselves!')
                            self.confusion_turns += 1
                        else:
                            print(f'{self.name} is no longer confused.')
                            self.confused = False
                            self.confusion_turns = 0
                elif effect == "lower accuracy":
                    print(f'{self.name} still has lower accuracy')

  

# =============================================== Monstars ===================================================================== #

goblin_boss = Monstars(name="Goblin Boss",
                  AC=17,
                  hp=1421,
                  tp=0,
                  mp=0,
                  stre=10,
                  dex=14,
                  vit=10,
                  agi=16,
                  mind=10,
                  wis=8,
                  cha=10,
                  num_attack=3,
                  main_weapon=weapon.sword,
                  offhand_weapon=weapon.axe,
                  )

goblin = Monstars(name="Goblin",
                  AC=10,
                  hp=1500,
                  tp=0,
                  mp=0,
                  stre=10,
                  dex=10,
                  vit=10,
                  agi=10,
                  mind=10,
                  wis=10,
                  cha=10,
                  num_attack=2,
                  main_weapon= weapon.dagger,
                  offhand_weapon=weapon.shield,
                  )

goblin_mage = Monstars(name="goblin Mage",
                  AC=10,
                  hp=1300,
                  tp=0,
                  mp=100,
                  stre=5,
                  dex=10,
                  vit=10,
                  agi=10,
                  mind=16,
                  wis=11,
                  cha=10,
                  num_attack=1,
                  main_weapon=weapon.staff,
                  offhand_weapon=weapon.fists,
                  )
orge = Monstars(name="Orge",
                AC=11,
                hp=1459,
                tp=0,
                mp=0,
                stre=19,
                dex=8,
                vit=16,
                agi=8,
                mind=5,
                wis=7,
                cha=7,
                num_attack= 4,
                main_weapon=weapon.mace,
                offhand_weapon=weapon.fists,
                )
bugbear = Monstars(name="Bugbear Chief",
                   AC=17,
                   hp=1465,
                   tp=0,
                   mp=0,
                   stre=17,
                   dex=14,
                   vit=15,
                   agi=13,
                   mind=14,
                   wis=11,
                   cha=12,
                   num_attack=3,
                   main_weapon=weapon.axe,
                   offhand_weapon=weapon.sword,
                   )
gnoll = Monstars(name="Gnoll Fang of Yeet",
                 AC=14,
                 hp=1465,
                 tp=0,
                 mp=0,
                 stre=16,
                 dex=14,
                 vit=15,
                 agi=15,
                 mind=6,
                 wis=10,
                 cha=7,
                 num_attack=2,
                 main_weapon=weapon.axe,
                 offhand_weapon=weapon.axe,
                 )
troll =Monstars(name="Troll",
                 AC=15,
                 hp=1484,
                 tp=0,
                 mp=0,
                 stre=18,
                 dex=13,
                 vit=20,
                 agi=11,
                 mind=7,
                 wis=9,
                 cha=7,
                 num_attack=4,
                 main_weapon=weapon.axe,
                 offhand_weapon=weapon.shield,
                 )
monstars_list =[goblin_boss, goblin, goblin_mage, orge, bugbear, gnoll, troll]
# monstars_stats = {
#      'goblin' : (10,14,10,16,10,8,10),
#     'orge' : ( 19,8,16,8,5,7,7),
#     'bugbear': (17,14,15,13,14,11,12),
#     'gnoll': (16,14,15,15,6,10,7),
#     'troll': (18,13,20,11,7,9,7),
# }

# goblin = monstars(
#       name="Goblin",
#       AC=10,
#       hp=1500,
#       stre=10,
#       dex=10,
#       vit=10,
#       agi=10,
#       inte=10,
#       wis=10,
#       cha=10,
#       num_attack=2,
#       weapon=weapon.dagger
# )