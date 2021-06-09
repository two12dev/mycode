#!/usr/bin/env python3
import os
import time

#Creating function to clear screen during quiz
def clearScreen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

#Points variable to hold points
points = 0
#Title Screen
print("WELCOME TO.......")
print("What type of Developer are you?")
print("--------------------------------")
time.sleep(6)
clearScreen()

# #Display rules and gather name
print("The rules are very simple...")
print("For each question...\nJust select the the number that matches with your choice")
print("-----------------------------------")
name = input("So...before we begin, please ENTER your name:\n>").title()
clearScreen()

# #Start of game
points = 0

print(f"Alrighty then {name}...let's begin!")
print("--------------------------------------")


#Questions
question_one = 0
time.sleep(3)
clearScreen()
while not question_one:
  try:
    print("Is HTML a programming language?")
    question_one = float(input("1) Yes \n2) No\n\n> "))
    question_one = int(question_one)
    if question_one == 1:
      print("Have you looked into trying to hack NASA using your newly found HTML skills?")
      print("--------------------------------------\n") 
    else:
      print("Okay so you're not a total beginner...")
      print("--------------------------------------\n")
      points += 1
  except:
    clearScreen()
    print("Oh no...That was not a good display of attention to details.\nPlease Choose 1 or 2\n\n")  

question_two = 0
time.sleep(3)
clearScreen()
while not question_two:
  try:
    print("Dark Theme or Light Theme for your IDE/Text Editor")
    question_two = float(input("1) Dark \n2) Light\n\n> "))
    question_two = int(question_two)
    if question_two == 1:
      print("Nice, you respect your eyes")
      print("--------------------------------------\n")
      points += 1
    else:
      print("YOU MONSTER!!!")
      print("--------------------------------------\n")   
  except:
    clearScreen()
    print("No sleeping allowed...\nPlease Choose 1 or 2\n\n") 


question_three = 0
time.sleep(3)
clearScreen()
while not question_three:
  try:
    print("Which do you prefer?")
    question_three = float(input("1) i++ \n2) i += 1\n3) i = i + 1\n\n> "))
    question_three = int(question_three)
    if question_three == 1:
      print("So you like strongly typed languages huh?")
      print("--------------------------------------\n") 
    elif question_three == 2:
      print("Okay, so you're flexible")
      print("--------------------------------------\n")
      points += 1
    else:
      print("Yeah we gotta work on that a little bit...")
      print("--------------------------------------\n") 
  except:
    clearScreen()
    print("Are you still there?\nPlease Choose 1 or 2\n\n")    

question_four = 0
time.sleep(3)
clearScreen()
while not question_four:
  try:
    print("Have you ever used JSON")
    question_four = float(input("1) Yes \n2) Jason?\n\n> "))
    question_four = int(question_four)
    if question_four == 1:
      print("So, you definitely know what an API is.")
      print("--------------------------------------\n")
      points += 1 
    else:
      print("Not a typo...yeah not the guy from Friday the 13th")
      print("--------------------------------------\n") 
  except:
    clearScreen()
    print("ERROR - BAD USER INPUT\nPlease Choose 1 or 2\n\n") 

question_five = 0
time.sleep(3)
clearScreen()
while not question_five:
  try:
    print("Do you like math?")
    question_five = float(input("1) Yes \n2) No\n\n> "))
    question_five = int(question_five)
    if question_five == 1:
      print("Do you have time to talk about our Machine Learning and Data Science Savior....PYTHON?")
      print("--------------------------------------\n")
      points += 1 
    else:
      print("Yeah, I'm not a fan either")
      print("--------------------------------------\n") 
  except:
    clearScreen()
    print("ERROR - BAD USER INPUT\nPlease Choose 1 or 2\n\n")   

question_six = 0
time.sleep(3)
clearScreen()
while not question_six:
  try:
    print("Front-End Development is ________!")
    question_six = float(input("1) Easy \n2) Challenging\n\n> "))
    question_six = int(question_six)
    if question_six == 1:
      print("Wow, you must be a beast!!!")
      print("--------------------------------------\n") 
    else:
      print("Yes, it can be challenging depending on the project...")
      print("--------------------------------------\n")
      points += 1 
  except:
    clearScreen()
    print("ERROR - BAD USER INPUT\nPlease Choose 1 or 2\n\n")   

question_seven = 0
time.sleep(3)
clearScreen()
while not question_seven:
  try:
    print("Apple or Windows")
    question_seven = float(input("1) Apple  \n2) Windows\n\n> "))
    question_seven = int(question_seven)
    if question_seven == 1:
      print("Taking notes...")
      time.sleep(3)
      print("--------------------------------------\n") 
      points += 1
    else:
      print("Interesting...")
      print("--------------------------------------\n") 
  except:
    clearScreen()
    print("ERROR - BAD USER INPUT\nPlease Choose 1 or 2\n\n")

clearScreen()
print("Computing Scores.......")
time.sleep(6)

clearScreen()
if points == 7:
  print("You should be a Full-Stack Developer!")
  print("--------------------------------------\n") 
elif points == 6:
  print("Backend Development is your friend!")
  print("--------------------------------------\n") 
else:
  print("Front-End Development is where I'd start!")
  print("--------------------------------------\n") 

print(f"Thanks for playing {name}!")
