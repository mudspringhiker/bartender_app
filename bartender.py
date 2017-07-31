import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def main():
    # print header
    header()
    repeat = True
    while repeat:
        responses = ask_customer(questions)
        create_drink(responses, ingredients)
        repeat = ask_for_another_drink()

def header():
    print("---------------------------------")
    print("    THE PIRATE BARTENDER APP")
    print("---------------------------------\n")


def ask_customer(questions):
    print("What style drink do you like?")
    print()
    responses = {}
    for key, value in questions.items():
        response = input(value + " (y/n) ")
        if response.lower() == "y" or response.lower == "yes":
            responses[key] = True
        else:
            responses[key] = False
    return responses
    
    
def create_drink(responses, ingredients):
    drink = []
    for key, response in responses.items():
        if response:
            drink.append(random.choice(ingredients[key]))
    print()
    if drink:
        print("Ere is yer drink:")
        for ingredient in drink:
            if ingredient == drink[-1]:
                print("\tand a " + ingredient.title() + "!!!!")
            else:
                print("\t" + ingredient.title() + "!")
    else:
        print("Well, I don't think ye want a drink, then!")
    print()
    

def ask_for_another_drink():
    another_drink = input("P'raps another drink? (y/n) ")
    if another_drink.lower() in ['no', 'n']:
        print("Off with ye then!\n")
        return False
    elif another_drink.lower() in ['yes', 'y']:
        print("Aye!\n")
        return True
    else:
        print("Mind repeatin that, matey?")
        return ask_for_another_drink()
    
    
    
if __name__ == "__main__":
    main()
