#Equipmemt
class Equipemtn:
    def __init__(self, name, description, body_slot, attributes) -> None:
        self.name = name
        self.description = description
        self.body_slot = body_slot
        self.attributes = attributes
        self.armor_bonus = stats
        self.stats= []


circlet = Equipemtn(name="circlet",
                     description="metal band with a stone in the middle",
                       body_slot="head",
                         attributes="int, cha",
                         armor_bonus=0,
                         )

Wizhat = Equipemtn(name="Wizard hat",
                   description="well made hat with an essience of magic",
                   body_slot="head",
                   attributes= "int, dex",
                   armor_bonus=0,
                   )

leatherhelm = Equipemtn(name="leather helm",
                        description="animal hide made into a hat",
                        body_slot="head",
                        attributes="agli, dex",
                        armor_bonus=0,
                        )

halfHelm = Equipemtn(name="Half Helm",
                     description="open face helm",
                     body_slot="head",
                     attributes="str, agli",
                     armor_bonus=0,
                     )

fullhelm = Equipemtn(name="Full Helm",
                     description="full face helm with eye slits",
                     body_slot="head",
                     attributes="str, con",
                     armor_bonus=0,
                     )

vest = Equipemtn(name="vest",
                 description= "cotton vest",
                 body_slot="body",
                 attributes="wis, int",
                 armor_bonus=0,
                 )
robe = Equipemtn(name="robe",
                 description="well tailor 3 sections of cloth, covering the whole body with a rope cord around the waist",
                 body_slot="body",
                 attributes="dex, wis",
                 armor_bonus=0,
                 )
studdedleather = Equipemtn(name="studded leather",
                           description="leather coat with overlapping metal pins",
                           body_slot="body",
                           attributes="agli, dex",
                           armor_bonus=0,
                           )
halfplate = Equipemtn(name="half plate",
                      description="plate of armor that fits half the body",
                      body_slot="body",
                      attributes="str, con"
                      armor_bonus=0,
                      )
platemail = Equipemtn(name="plate mail",
                      description="plate armor that covers the whole body",
                      body_slot="body",
                      attributes="con, wis",
                      armor_bonus=0,
                      )
straps = Equipemtn(name="straps",
                   description="straps of clothes, that wrapped around hands to protect the knuckles",
                   body_slot="hands",
                   attributes="wis, agli",
                   armor_bonus=0,
                   )
gloves = Equipemtn(name="gloves",
                    description="fine well made gloves",
                    body_slot="hands",
                    attributes="cha, int",
                    armor_bonus=0,
                    )
leatherbracers = Equipemtn(name="leather bracers",
                          description="leather bracers protective arm covering that typically cover the forearm",
                          body_slot="hands",
                          attributes="cha, dex",
                          armor_bonus=0,
                          )
halfhand = Equipemtn(name="half hand",
                     description="plate metal that fits around the knuckles of the hand, leaving the fingers exposed",
                     body_slot="hands",
                     attributes="con, agli",
                     armor_bonus=0,
                     )
gauntlets = Equipemtn(name="gauntlets",
                      description="plate metal that covers the whole hand and finger tips",
                      body_slot="hands",
                      attributes="str, dex",
                      armor_bonus=0,
                      )
shorts = Equipemtn(name="shorts",
                   description="cotton short that are either cut off at the knees or anckles",
                   body_slot="legs",
                   attributes="int, dex",
                   armor_bonus=0,
                   )
pants = Equipemtn(name="pants",
                  description="fine tailor pants",
                  body_slot="legs",
                  attributes="cha, wis",
                  armor_bonus=0,
                  )
leathergreaves = Equipemtn(name="leather greaves",
                        body_slot="legs",
                         description="protect the lower leg, from the knee to the ankle",
                         attributes="cha, con",
                         armor_bonus=0,
                         )
cuisses = Equipemtn(name="cuisse",
                    description="thigh armor, that covers the thighs but not the full leg",
                    body_slot="legs",
                    attributes="con, agli",
                    armor_bonus=0,
                    )
plateGCKPT = Equipemtn(name="plate mail leg",
                       description="protect the full leg in metal",
                       body_slot="legs",
                       attributes="str, dex",
                       armor_bonus=0,
                       )

Equipemtn_list =[circlet,Wizhat,leatherhelm,halfHelm,fullhelm,vest,robe,studdedleather,halfplate,platemail,straps,leatherbracers,halfhand,gauntlets,shorts,pants,leathergreaves,cuisses,plateGCKPT]






