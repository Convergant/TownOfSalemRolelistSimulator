class Faction:
    def __init__(self, name, goal, max=4, opposing_factions=[]):
        self.name = name
        self.goal = goal
        self.max = max
        self.shorthand = "R" + self.name[0]
        self.opposing_factions = opposing_factions

    def __str__(self):
        return self.name


Town = Faction("Town", "Lynch every criminal and evildoer.", max=float("inf"))
Mafia = Faction("Mafia", "Kill anyone that will not submit to the Mafia.")
Coven = Faction("Coven", "Kill all who would oppose the Coven.")
Vampires = Faction("Vampires", "Convert everyone who would oppose you.")
Neutrals = Faction("Neutrals", "", max=float("inf"))

Town.opposing_factions = [Mafia, Coven, Vampires]
Mafia.opposing_factions = [Town, Coven, Vampires]
Coven.opposing_factions = [Town, Mafia, Vampires]
Vampires.opposing_factions = [Town, Mafia, Coven]

if __name__ == "__main__":
    print(Town)