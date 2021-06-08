#!/usr/bin/env python3
i = 0
while i < 3:

    char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)\n").lower()

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()

    heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
 }

    print(f"{char_name.title()}'s {char_stat} is: {heroes[char_name][char_stat].title()}")
    i += 1








