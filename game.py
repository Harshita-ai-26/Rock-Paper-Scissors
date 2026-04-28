import random
options=['ROCK','PAPER','SCISSORS']

def play(select):
    comp_choice=random.choice(options)
    print(f"Computer's choice:{comp_choice}")
    result=(options.index(select)-options.index(comp_choice))%3 #Compares user and computer choice indices using modulo for circular logic
    return["Draw","WIN","LOST"][result] #Returns result by using 'result' as index to pick value from list
    
while True:
    print('____Welcome to the Game____\nROCK  PAPER  SCISSORS  EXIT')
    select=input("Choose one from the above:").upper()
    if select=='EXIT':
        print("Game Ended")
        break
    if select not in options:
        print("Invalid Choice!")
        continue
    print(play(select))

