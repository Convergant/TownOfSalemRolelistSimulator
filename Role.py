from TownOfSalem.Faction import *
from TownOfSalem.Alignment import *
from aenum import Enum, extend_enum


class Role:
    def __init__(self, name, faction, alignment, shorthand, unique=False, dependant_role=None, goal="", opposing_factions=[]):
        self.name = name
        self.shorthand = shorthand
        self.unique = unique
        self.dependant_role = dependant_role

        self.faction = faction
        self.alignment = alignment
        self.goal = goal
        self.opposing_factions = opposing_factions

    def __str__(self):
        return "{name}: {alignment}\nGoal: {goal}".format(name=self.name, alignment=self.alignment.__str__(), goal=self.faction.goal + self.goal)


# Neutral roles
Amnesiac = Role("Amnesiac", Neutrals, NB, "Amne", goal="Remember who you were and complete that role's goal.")
GuardianAngel = Role("Guardian Angel", Neutrals, NB, "GA", goal="Keep your target alive until the end of the game.")
Survivor = Role("Survivor", Neutrals, NB, "Surv", goal="Live until the end of the game.")

Pirate = Role("Pirate", Neutrals, NC, "Pirate", unique=True, goal="Successfully plunder two players.")
Plaguebearer = Role("Plaguebearer", Neutrals, NC, "PB", unique=True, goal="Infect all living players and become Pestilence.",
                    opposing_factions=[Town, Mafia, Coven, Vampires])
Vampire = Role("Vampire", Vampires, NC, "Vamp")

Executioner = Role("Executioner", Neutrals, NE, "Exe", goal="Get your target lynched at any cost.")
Jester = Role("Jester", Neutrals, NE, "Jest", goal="Get yourself lynched by any means necessary.")
Witch = Role("Witch", Neutrals, NE, "Witch", goal="Live to see the Town lose.")

Arsonist = Role("Arsonist", Neutrals, NK, "Arso", goal="Live to see everyone burn.")
Juggernaut = Role("Juggernaut", Neutrals, NK, "Jugg", unique=True, goal="Kill everyone who would oppose you.",
                  opposing_factions=[Town, Mafia, Coven, Vampires])
SerialKiller = Role("Serial Killer", Neutrals, NK, "SK", goal="Kill everyone who would oppose you.",
                    opposing_factions=[Town, Mafia, Coven, Vampires])
Werewolf = Role("Werewolf", Neutrals, NK, "WW", goal="Kill everyone who would oppose you.",
                opposing_factions=[Town, Mafia, Coven, Vampires], unique=True)

# Town roles
Investigator = Role("Investigator", Town, TI, "Invest")
Lookout = Role("Lookout", Town, TI, "LO")
Psychic = Role("Psychic", Town, TI, "Psy")
Sheriff = Role("Sheriff", Town, TI, "Sher")
Spy = Role("Spy", Town, TI, "Spy")
Tracker = Role("Tracker", Town, TI, "Tracker")

Jailor = Role("Jailor", Town, TK, "Jailor", unique=True)
VampireHunter = Role("Vampire Hunter", Town, TK, "VH", dependant_role=Vampire)
Veteran = Role("Veteran", Town, TK, "Vet", unique=True)
Vigilante = Role("Vigilante", Town, TK, "Vigi")

Bodyguard = Role("Bodyguard", Town, TP, "BG")
Doctor = Role("Doctor", Town, TP, "Doc")

Crusader = Role("Crusader", Town, TP, "Crus")
Trapper = Role("Trapper", Town, TP, "Trapper")

Escort = Role("Escort", Town, TS, "Esc")

Mayor = Role("Mayor", Town, TS, "Mayor", unique=True)
Medium = Role("Medium", Town, TS, "Med")
Retributionist = Role("Retributionist", Town, TS, "Retri", unique=True)
Transporter = Role("Transporter", Town, TS, "Trans")

# Mafia roles
Disguiser = Role("Disguiser", Mafia, MD, "Disg")

Forger = Role("Forger", Mafia, MD, "Forger")
Framer = Role("Framer", Mafia, MD, "Framer")
Hypnotist = Role("Hypnotist", Mafia, MD, "Hypno")
Janitor = Role("Janitor", Mafia, MD, "Jani")

Ambusher = Role("Ambusher", Mafia, MK, "Amb", unique=True)

Godfather = Role("Godfather", Mafia, MK, "GF", unique=True)
Mafioso = Role("Mafioso", Mafia, MK, "Mafioso", unique=True)

Blackmailer = Role("Blackmailer", Mafia, MS, "BMer")

Consigliere = Role("Consigliere", Mafia, MS, "Consig")
Consort = Role("Consort", Mafia, MS, "Cons")

# Coven roles
CovenLeader = Role("Coven Leader", Coven, CE, "CL", unique=True)

HexMaster = Role("Hex Master", Coven, CE, "Hex", unique=True)
Medusa = Role("Medusa", Coven, CE, "Dusa", unique=True)
Necromancer = Role("Necromancer", Coven, CE, "Necro", unique=True)
Poisoner = Role("Poisoner", Coven, CE, "Poisoner", unique=True)
PotionMaster = Role("Potion Master", Coven, CE, "PMer", unique=True)


roles = [Amnesiac, GuardianAngel, Survivor, Pirate, Plaguebearer, Vampire, Executioner, Jester, Arsonist, Juggernaut, SerialKiller, Werewolf,
         Investigator, Lookout, Psychic, Sheriff, Spy, Tracker, Jailor, VampireHunter, Veteran, Vigilante, Bodyguard, Doctor, Crusader,
         Trapper, Escort, Mayor, Medium, Retributionist, Transporter, Disguiser, Forger, Framer, Hypnotist, Janitor, Ambusher, Godfather,
         Mafioso, Blackmailer, Consigliere, Consort, CovenLeader, HexMaster, Medusa, Necromancer, Poisoner, PotionMaster, Witch]

coven_roles = [CovenLeader, HexMaster, Medusa, Necromancer, Poisoner, PotionMaster, GuardianAngel, Juggernaut, Pirate, Plaguebearer,
               Crusader, Psychic, Tracker, Trapper]

RT_roles = [c for c in roles if c.faction == Town]
RM_roles = [c for c in roles if c.faction == Mafia]
RC_roles = [c for c in roles if c.faction == Coven]

RN_roles = [c for c in roles if c.faction == Neutrals]

TI_roles = [c for c in roles if c.alignment == TI]
TK_roles = [c for c in roles if c.alignment == TK]
TP_roles = [c for c in roles if c.alignment == TP]
TS_roles = [c for c in roles if c.alignment == TS]

MD_roles = [c for c in roles if c.alignment == MD]
MK_roles = [c for c in roles if c.alignment == MK]
MS_roles = [c for c in roles if c.alignment == MS]

NB_roles = [c for c in roles if c.alignment == NB]
NC_roles = [c for c in roles if c.alignment == NC]
NE_roles = [c for c in roles if c.alignment == NE]
NK_roles = [c for c in roles if c.alignment == NK]

factions = [Town, Mafia, Coven, Neutrals, Vampires]


class RoleEnum(Enum):
    RT = RT_roles
    RM = RM_roles
    RC = RC_roles
    RN = RN_roles

    TI = TI_roles
    TK = TK_roles
    TP = TP_roles
    TS = TS_roles

    MD = MD_roles
    MK = MK_roles
    MS = MS_roles

    NB = NB_roles
    NC = NC_roles
    NE = NE_roles
    NK = NK_roles


    Any = roles


for role in roles:
    extend_enum(RoleEnum, role.name, role)


if __name__ == "__main__":
    print(RoleEnum["MS"].value)