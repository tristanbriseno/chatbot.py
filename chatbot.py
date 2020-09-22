from random import choice


def get_mood_bot_response(user_response):

  
  bot_response_happy = ["Oh, my bad! I didnt mean to make you think I care.", "Alright good talk", "oh, wait sorry, gotta take this call", "Awe man i just remembered, I've got this thing I gotta do, so yeah....Tootles!"]
  bot_response_sad = ["But did you die?", "    Are you always such an idiot, or do you just show off when I’m around?", "Are you about to cry?", ".............Oh did you say somethin?", "ZzzZzzZzzZzzZzzZzz" ]

  if user_response ==  "good":
    return choice(bot_response_happy)
  elif user_response == "bad" :
    return choice(bot_response_sad)
  else:
    return " Yeah, I'm gonna be honest I wast really paying attention just now.... sooooo, what were you saying?"




print(" Welcome to Rude Bot")
print(" Do you feel good or bad?")

user_response = ""

while True:
  user_response = input(" Hey, whatsup?: ")
  

  if user_response == 'done':
    break

  
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)