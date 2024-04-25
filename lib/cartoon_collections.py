def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start= 1):
        print(f"{i}. {dwarf}")
    pass

def summon_captain_planet(planeteer):
    return [call.capitalize() + '!' for call in planeteer] 
    pass

def long_planeteer_calls(calls):
    for word in calls:
        if len(word) > 4:
            return True
    return False
    pass

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for ingredient in snacks:
        if ingredient in cheeses:
            return ingredient
    return None
    pass
