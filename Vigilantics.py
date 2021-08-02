from TownOfSalem.imports import *

rolelist = [Vigilante, Witch, Vigilante, Vigilante, Witch, Vigilante, Vigilante, Witch, Vigilante, Vigilante, Vigilante, Witch,
            Vigilante, Vigilante, Witch]
rolelist = [Slot(c) for c in rolelist]
rolelist = Rolelist(*rolelist, classic=True, debugging=True)
rolelist.generate()
print(rolelist)