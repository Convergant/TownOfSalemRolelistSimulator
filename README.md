# TownOfSalemRolelistSimulator
This is a tool designed to simulate and test the properties of Town of Salem role lists.

REMEMBER: Edit the files provided at your own risk. I've done some basic commenting to help people understand what
each part is for, but small changes can have large consequences, so make sure you know what you're doing BEFORE editing any of the
base files.

If you want to create and generate a role list, here's how:

Step 1. Create a new file, and at the top write "from TownOfSalem.imports import *", and "from TownOfSalem.Role import *"
on a different line, unless you already have.
Note: If you just need a pre-existing 15 player role list, just write "rolelist = (name of gamemode)", and skip to Step 7.

Step 2. Write "rolelist = []", or you can name it something else if you'd like.
Step 3. Fill the [] with each role you'd like, separated by commas, or for example "RM" if you'd like a random Mafia role to spawn,
or "Neutrals" if you'd like a random Neutral role to spawn.
Step 4. Write "rolelist = [Slot(c) for c in rolelist]", or replace "rolelist" with whatever you named it.
Step 5. Write "rolelist = Rolelist(*rolelist)", or replace "rolelist" with whatever you named it.
Step 6. If you want to lift some of the normal restrictions on what a role can be, here's what to do:
    1. Instead of just "rolelist = Rolelist(*rolelist)", write "rolelist = Rolelist(*rolelist, tests = [True, True, True, True, None])",
    and replace "True" with "False" as follows.
        i. The first position corresponds to checking if a role is unique, and will reroll the role if it fails.
        If you want to be able to have multiple unique roles, turn this off.

        ii. The second position corresponds to using the check for having a Mafia role without a Mafia Killing role, and will set
        the role to Mafioso if it fails. Turn this off if you want to use Tactical Mafia Killing.

        iii. The third position corresponds to checking if a Vampire Hunter has been generated without Vampires, and rerolls the role
        if failed. Turn this off if you feel like having a Vigilante with 1 bullet Day 2(?)

        iv. The fourth position corresponds to checking if there are more members of a given faction than are typically allowed,
        and rerolls the role if it fails. Turn this off if you'd like 6 vampires I guess.
        WARNING: Attempting the trick that works in-game of making 4 vampires, Pirate, Plaguebearer and more NC slots does not work
        and will cause the program to get stuck.

        v. The fifth position corresponds to whether all roles have to be of a certain faction, and rerolls if failed. Honestly,
        I honestly don't remember what I used this for, and I recommend leaving it untouched.

    2. Other modifications you can make include:
        i. Writing "classic=True" inside of "Rolelist(*rolelist)", after "*rolelist". This will prevent Coven roles from spawning
        and allow Witch to spawn.
        ii. You can write "debugging=True" to see the details of what roles are being generated, and what checks they fail.
Step 7. Write "rolelist.generate()".
Step 8. Write "print(rolelist)".

You can see an example in the file named "Vigilantics.py".

If you want to create your own role, here's what you need to do:
Step 1. Write "from TownOfSalem.imports import *", and "from TownOfSalem.Role import *"
on a different line, unless you already have.
Step 2. Write "(rolename) = Role("(rolename)", (faction), (alignment), (shortened name))", replacing (rolename) etc with the actual
values.
    1. If you want the role to be unique, you need to add "unique=True" inside of "Role()".
    2. If you want the role to need another to exist, you need to add "dependant_role=(the role it needs)".
    3. You can also add a list of opposing factions as "opposing_factions=[]", putting said factions inside the [].

An example can be found in "Duelist.py"

If you want to create your own faction, here's what you need to do:
Step 1. Write "from TownOfSalem.imports import *", unless you already have.
Step 2. Write "(factionname) = Faction("(factionname)", "(goal)")".
    1. If you want to allow more than 4 members, add "max=(max number)" inside of "Faction()". If you want no limit,
    make "(max number)" "float("inf")".

An example can be found in "PirateFaction.py".

If you want to make your own alignment, here's what you need to do.
Step 1. Write "from TownOfSalem.imports import *", unless you already have.
Step 2. Write "(alignmentname) = Alignment("(factionname)", "(purpose within faction)")"

For example, you would create TI by writing "TI = Alignment("Town", "Investigative")".
