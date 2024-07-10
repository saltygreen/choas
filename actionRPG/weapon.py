# ========================= Create weapon class to define weapon attributes =============================
class Weapon:
    def __init__(self, name, damage, defense_modifier, accuracy, skillchain, element, weakness, tp, tp_modifier, status_effect):
        self.name = name
        self.damage = damage
        self.defense_modifier = defense_modifier
        self.weapon_accuracy = accuracy
        self.skillchain = skillchain
        self.element = element
        self.weakness = weakness
        self.tp_modifier = tp_modifier
        self.tp = tp
        self.status_effect = status_effect
        self.main_weapon = None
        self.offhand_weapon = None

# ========================= Create weapons list =============================

# ============================ SWORD =========================================== #

sword = Weapon(
    # Balanced weapon
    name='sword',
    damage=7,
    defense_modifier=2,
    accuracy=5,
    skillchain="Pink_blossom_blade",
    element="fire",
    weakness='water',
    tp_modifier=2,
    tp= 5,
    status_effect="burn"
)

# ====================================== SHORT_SWORD ============================================= #

short_sword = Weapon(
    # Balanced weapon
    name='short_sword',
    damage=6,
    defense_modifier=1,
    accuracy=6,
    skillchain="Hawk's_Mirage_Blade",
    element="fire",
    weakness='water',
    tp_modifier=2,
    tp= 5,
    status_effect="burn"
)

# ======================================== DAGGER ============================================= #

dagger = Weapon(
    # Lighter damage and defense_modifier but higher accuracy.
    name='dagger',
    damage=4,
    defense_modifier=1,
    accuracy=9,
    skillchain="Wisp_bee_sting",
    element="wind",
    weakness='earth',
    tp_modifier=1,
    tp= 5,
    status_effect="lower accucery"
)



# =========================================================== MACE ========================================== #

mace = Weapon(
    # heavier damage but lower accuracy
    name='mace',
    damage=10,
    defense_modifier=3,
    accuracy=1,
    skillchain="Bubble_gum_blast",
    element="water",
    weakness='fire',
    tp_modifier=3,
    tp= 5,
    status_effect="poison"
)   

# ======================================================= FISTS ===================================================== #

fists = Weapon(
    name='fists',
    damage=5,
    defense_modifier=0,
    accuracy=10,
    skillchain="Bear_claw_pommel",
    element="earth",
    weakness='water',
    tp_modifier=5,
    tp=5,
    status_effect="stun"
)

# ========================================================= STAFF ================================================= #

staff = Weapon(
    name='staff',
    damage=7,
    defense_modifier=0,
    accuracy=4,
    skillchain="banshee_kiss",
    element="psychic",
    weakness=None,
    tp_modifier=4,
    tp= 0,
    status_effect="filling MP",
)

# ================================================================= AXE ============================================= #

axe = Weapon(
    name='axe',
    damage=6,
    defense_modifier=2,
    accuracy=6,
    skillchain="Storm_render",
    element="lighten",
    weakness="water",
    tp_modifier=2,
    tp= 0,
    status_effect="confusion",
)

# ===================================== SHIELD ======================================================================= #

shield = Weapon(
    name="shield",
    damage=0.5,
    defense_modifier= 5,
    accuracy= 0,
    skillchain=None,
    element=None,
    weakness=None,
    tp_modifier=10,
    tp=0,
    status_effect=None,
)
# Compiled list of Weapons
weapons_list =[dagger, mace, sword, short_sword, fists, staff, axe, shield]
# Look to have a Player class that will hold player and computer information. 
# Used to help determine outcome so that weapons will aid the user rather than become the outcome.


