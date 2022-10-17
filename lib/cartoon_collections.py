import ipdb
cheeses = ["cheddar", "gouda", "thyme"]

def roll_call_dwarves(dwarves):
    for i, name in enumerate(dwarves):
        print(f'{i + 1}. {name}')

def summon_captain_planet(elements):
    return [ f"{element.capitalize()}!" for element in elements ]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True      
    return False

def find_the_cheese(snacks):
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
