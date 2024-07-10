import races

class Profess:
    def __init__(self, name, element_res, accuracy, AC, main_weapon, offhand_weapon) -> None:
        self.name = name
        self.element_res = element_res
        self.accuracy = accuracy
        self.AC = AC
        self.profession_modifier = AC
        self.main_weapon = main_weapon
        self.offhand_weapon = offhand_weapon

# ================================================= Professions ============================================================== #
    
Knight = Profess(name="Knight",
                 element_res= "earth",
                 accuracy= 10,
                 AC= 17,
                 main_weapon="sword",
                 offhand_weapon="shield",
                 )
Wizard = Profess(name="Wizard",
                 element_res="wind",
                 accuracy= 10,
                 AC= 12,
                 main_weapon="staff",
                 offhand_weapon="fists",
                 )
Rogue = Profess(name="Rogue",
                element_res="water",
                accuracy= 16,
                AC=10,
                main_weapon="short_sword",
                offhand_weapon="dagger"
                )
Cleric = Profess(name="Cleric",
                 element_res="fire",
                 accuracy= 10,
                 AC= 16,
                 main_weapon="mace",
                 offhand_weapon="shield",
                 )
Druid = Profess(name="Druid",
                element_res="",
                accuracy= 10,
                AC=13,
                main_weapon="staff",
                offhand_weapon="dagger",
                )
Artificer = Profess(name="Artificer",
                    element_res="",
                    accuracy=10,
                    AC= 13,
                    main_weapon="dagger",
                    offhand_weapon="fists",
                )
Profession_list =[Knight,Wizard,Rogue,Cleric,Druid,Artificer]