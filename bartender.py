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
    # ask what style of drink a customer likes
    # gather responses in a new dict
    responses = ask_customer(questions)
    # construct a drink as a list then return it
    print(create_drink(responses, ingredients))
    

def header():
    print("--------------------------")
    print("    THE BARTENDER APP")
    print("--------------------------")
    print()


def ask_customer(questions):
    print("What style drink do you like? \nAnswer yes or no:")
    print()
    responses = {}
    for key, value in questions.items():
        response = input(value + " ")
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
    return drink
    
    
if __name__ == "__main__":
    main()
