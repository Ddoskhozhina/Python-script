import random

num = input(
    "Welcome to Oracle! \nAsk me anything so that I can answer Yes or No \nWhen ready press enter")
oracle = ['Yes - your wish will become true, congrats!', 'No - sorry, dude']
value = random.choice(oracle)
print(value)
