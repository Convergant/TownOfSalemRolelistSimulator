from TownOfSalem.imports import *
from TownOfSalem.Role import *
from aenum import Enum
from random import choice, shuffle


def intersection(a, b):
    # Return all values that are in 2 lists
    temp = set(b)
    return [value for value in a if value in temp]


class SlotType(Enum):
    # A slot can be a role (like Jailor), alignment (like TS), a faction (like RT), or Any.
    Role = "Role"
    Alignment = "Alignment"
    Faction = "Faction"
    Any = "Any"


class Slot:
    def __init__(self, value):
        assert type(value) in (Role, Alignment, Faction) or value == "Any"

        self.value = value

        if type(value) == Role:
            self.type = SlotType.Role
            self.shorthand = self.value.shorthand

        elif type(value) == Alignment:
            self.type = SlotType.Alignment
            self.shorthand = self.value.shorthand

        elif type(value) == Faction:
            self.type = SlotType.Faction
            self.shorthand = self.value.shorthand

        else:
            self.type = SlotType.Any
            self.shorthand = "Any"

    def generate(self):
        if self.type == SlotType.Role:
            return self.value

        elif self.type != SlotType.Any:
            return choice(RoleEnum[self.value.shorthand].value)

        else:
            return choice(RoleEnum["Any"].value)


class Rolelist:
    def __init__(self, *slots, debugging=False, classic=False, tests=[True] * 4 + [None]):
        self.slots = slots
        self.roles = []
        self.debugging = debugging
        self.classic = classic
        self.factions_names = [c.name for c in factions]
        self.factions_count = [0] * 5

    def generate(self):
        self.factions_count = [0] * 5
        self.possible_roles = [c.name for c in roles]

        for slot in self.slots:
            self.generate_valid_role(slot)

        del self.possible_roles

        # Shuffle the roles so you can't immediately know someone's role by their position
        shuffle(self.roles)

        # file.write(",".join([str(c) for c in self.factions_count]))

    def generate_valid_role(self, slot, use_unique_check=True, use_maf_without_MK_check=True, use_dependant_check=True,
                            use_max_faction_check=True, valid_faction=None):
        valid = False

        role = slot.generate()

        use_faction_check = bool(valid_faction)

        msg = "Generated role not valid because it failed the following tests: "

        while not valid:
            # Loop until none of the checks fail

            error_messages = []

            if self.debugging:
                print("Attempting to use role:", role.name)

            if use_unique_check and role.name not in self.possible_roles:
                role = slot.generate()
                error_messages.append("Unique role already taken")

            elif use_maf_without_MK_check and role.faction.name == "Mafia" and role.name not in ["Godfather", "Mafioso"] and not any([c.alignment == MK for c in self.roles]):
                role = Mafioso
                valid = True

            elif use_dependant_check and role.dependant_role and role.dependant_role not in self.roles:
                role = slot.generate()
                error_messages.append("VH without vamps")

            elif use_max_faction_check and self.factions_count[self.factions_names.index(role.faction.name)] >= role.faction.max:
                role = slot.generate()
                error_messages.append("Faction is at its limit")

            elif use_faction_check and role.faction != valid_faction:
                role = slot.generate()
                error_messages.append("Not in the correct faction")

            elif role == Witch and not self.classic or self.classic and role in coven_roles:
                role = slot.generate()
                error_messages.append("Coven role in classic/Witch in coven")

            else:
                valid = True

            if self.debugging and not valid:
                print(msg + ", ".join(error_messages))

        if role.unique:
            self.possible_roles.remove(role.name)

        self.roles.append(role)
        self.factions_count[self.factions_names.index(role.faction.name)] += 1

        return role

    def __str__(self):
        return "\n".join(["({}) ".format(i+1) + self.roles[i].name for i in range(len(self.roles))])


Classic = [Sheriff, Lookout, Investigator, Jailor, Doctor, Escort, Medium, TK,
           Town, Godfather, Mafioso, Framer, SerialKiller, Executioner, Jester]
Classic = Rolelist(*[Slot(c) for c in Classic], classic=True)

Ranked = [Jailor, TI, TI, TP, TK, TS, Town, Town, Town, Godfather, Mafioso, Mafia, Mafia, Executioner, Witch]
Ranked = Rolelist(*[Slot(c) for c in Ranked], classic=True)

Rainbow = [Godfather, Arsonist, Survivor, Jailor, Amnesiac, SerialKiller, Witch, "Any", Witch, SerialKiller, Amnesiac, Veteran, Survivor, Arsonist, Mafioso]
Rainbow = Rolelist(*[Slot(c) for c in Rainbow], classic=True)

DracualasPalace = [Doctor, Lookout, Lookout, Jailor, Vigilante, TP, TS, VampireHunter, Jester, Witch, Vampire, Vampire, Vampire, Vampire]
DracualasPalace = Rolelist(*[Slot(c) for c in DracualasPalace], classic=True)

TownTraitor = [Sheriff, Jailor, Doctor, Lookout, TI, TP, TK, TS, Town, Town, Town, Godfather, Mafioso, Mafia, Witch]
TownTraitor = Rolelist(*[Slot(c) for c in TownTraitor], classic=True)

CovenClassic = [Sheriff, Lookout, Psychic, Jailor, TP, CovenLeader, PotionMaster, Executioner, Coven, Medusa, Town, Plaguebearer, Town, Pirate, Town]
CovenClassic = Rolelist(*[Slot(c) for c in CovenClassic])

CovenRanked = [Jailor, TI, TI, TS, TP, TK, Town, Town, Town, CovenLeader, Medusa, Coven, Coven, NK, NE]
CovenRanked = Rolelist(*[Slot(c) for c in CovenRanked])

MafiaReturns = [Sheriff, Lookout, Psychic, Jailor, TP, Godfather, Ambusher, Mafia, Hypnotist, Executioner, Plaguebearer, Pirate, Town, Town, Town]
MafiaReturns = Rolelist(*[Slot(c) for c in MafiaReturns])

CovenVIP = [Sheriff, Crusader, Psychic, Vigilante, Trapper, CovenLeader, PotionMaster, GuardianAngel, Coven, Medusa, Tracker, TP, TS, Pirate, TP]
CovenVIP = Rolelist(*[Slot(c) for c in CovenVIP])

CovenLovers = [Sheriff, Doctor, Psychic, Tracker, TP, TP, TS, TS, Pirate, Arsonist, Werewolf, SerialKiller, Godfather, Medusa, Plaguebearer]
CovenLovers = Rolelist(*[Slot(c) for c in CovenLovers])

CovenTownTraitor = [Sheriff, Jailor, Crusader, Tracker, TI, TP, TK, TS, Town, Town, Town, CovenLeader, Medusa, Coven, Coven]
CovenTownTraitor = Rolelist(*[Slot(c) for c in CovenTownTraitor])

CovenAllAny = Rolelist(*[Slot("Any")]*15)


if __name__ == "__main__":
    pass
