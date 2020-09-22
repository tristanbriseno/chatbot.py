from random import choice
#I basically used the example that was provided for this project as a blueprint for my chat bot.
#what is happening here is that the code is using a psudo-code called random that acts as an rng and selects amoungst the choices provided.
def get_rude_bot_response(user_response):
#Here I am defining that get_rude_bot_response
  
  bot_response_good = ["Oh, my bad! I didnt mean to make you think I care.", "Alright good talk", "oh, sorry, gotta take this call", "Awe man i just remembered, I've got this thing I gotta do, so yeah....Tootles!"]
  #here I am making 2 lists of reponses based off of the imput from the user
  bot_response_bad = ["But did you die?", "    Are you always such an idiot, or do you just show off when I’m around?", "Are you about to cry?", ".............Oh did you say somethin?", "ZzzZzzZzzZzzZzzZzz" ]
  #here it is saying that if the user inputs good then respond with bot_response_good and if the user inputs bad then respond with bot_response_bad else return the text provided.
  if user_response ==  "good":
    return choice(bot_response_good)
  elif user_response == "bad" :
    return choice(bot_response_bad)
  else:
    return " Yeah, I'm gonna be honest I wast really paying attention just now.... soooo, what were you saying?"



#here the bot is being introduced and the user is given instructions on how to operate the bot.
print(" Welcome to Rude Bot")
print(" Do you feel good or bad?")

user_response = ""

while True:
  user_response = input(" Hey, whatsup?: ")
  
#this basically ends the code if you input done. Otherwise the input request will repeate infinitly 
  if user_response == 'done':
    break

  
  bot_response = get_rude_bot_response(user_response)
  print(bot_response)
