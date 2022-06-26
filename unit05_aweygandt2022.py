############################################################
#     Aidan Weygandt                        04.23.21       #
#     Unit 5 Problems                                      #    
#     clock countdown, Divisible by 5 or 6,                #
#     display a pyramid, math game, Number Guessing Game   #
############################################################

import time
import random
import turtle

print ("Problem #1 - Countdown")
secs = int(input("Enter the number of seconds you'd like to countdown: ")) #user input
for each in range(0, secs,): #for every number form 0-userInput print it and wait one second
  print (secs)
  time.sleep(1)
  secs -= 1


print ("\n\nProblem #2 - Divisible by 5 or 6")
nline = ""
counter2 = 0
for each in range(100, 1000 + 1): #from 100-1000 if evenly divisable by 5 or 6 copy it to a string
  if each // 5 == each / 5 or each // 6 == each / 6:
    if counter2 == 10: 
      print (nline)
      nline = ""
      counter2 = 0
    nline = nline + str(each) + " "
    counter2 += 1
print (nline)


print ("\n\nProblem #3 - Pyramid")
pnum = int(input("Enter the number of lines (1-15) for pyramid: ")) #user input
while 1: #locks input to only number from 1 to 15
  if pnum >= 1 and pnum <= 15:
    break
  else: pnum = int(input("Please enter a number between 1-15: "))
xp = range(pnum)
for x in xp:
  for space in range(pnum-x): #adds spaces between egde and numbers
    print("  ", end=" ")
  for y1 in range(x+1, 0, -1): #prints left side numbers
    print(format(y1, "2d"), end=" ") #keeps triangle length the same in double digits and prints y1
  for y2 in range(2, x+2): #prints number on right side
    print(format(y2, "2d"), end=" ") #formats and prints y2
  print ()


print ("\n\nProblem #4 - Math Game") 
win = 0
loss = 0
gnum1 = random.randint(0, 9)
gnum2 = random.randint(0, 9)
gametype = input("Welcome to the math game, would you like to do addition (A), subtraction (S) or\nboth (B): ").lower() #user input
while 1: #restricts input to A, S or B
  if gametype == "a" or gametype == "s" or gametype == "b":
    break
  else: gametype = input("Please enter an A, S or B: ")
negative = input("Would you like negative answers with subtraction? (Y or N): ").lower() #user input
while 1: #restricts input to Y or N
  if negative == "y" or negative == "n":
    break
  else: negative = input("Please enter a Y or N: ").lower()
while win < 5 and loss < 3: #runs until player gets 3 wrong or 5 right
  pl_mi = "+" if random.randint(0, 1) == 0 else "-" #for both add and sub games
  if gametype == "a": pl_mi = "+" #for only addition problems
  elif gametype == "s": pl_mi = "-" #for only subtraction games
  if gnum1 < gnum2 and pl_mi == "-" and negative == "n": #for answering with negative numbers
    swap = gnum1
    gnum1 = gnum2
    gnum2 = swap
  question = "\nWhat is " + str(gnum1)+ " " + pl_mi + " " + str(gnum2) + "? "
  userinp = int(input(question)) #promts user with math question
  if (gnum1 + gnum2 == userinp and pl_mi == "+") or (gnum1 - gnum2 == userinp and pl_mi == "-"): #if answer was correct add piont
    win +=1
    print (gnum1, pl_mi, gnum2, "=", userinp, "is true")
  else: #else add loss
    loss += 1
    print (gnum1, pl_mi, gnum2, "=", userinp, "is false")
  gnum1 = random.randint(0, 9)
  gnum2 = random.randint(0, 9)
if win == 5: #if won
  print ("\nYou won.", "You got", loss, "wrong and", win, "right.")
elif loss == 3: #if lost
  print ("\nYou lost.", "You got", loss, "wrong and", win, "right.")
else: print("\nerror") #incase the computer messes up and definetly not me


print ("\n\nProblem #5 - Number Guessing Game")
numanswer = int(input("When prompted please respond with too high (H), too low (L) or correct (C). \nPlease Enter a number between 1-100: ")) #user input
while 1: #restricts input to number from 1 to 100
  if 100 < numanswer or numanswer < 1:
    numanswer = int(input("Must be between 1-100: "))
  else:
    break
high = 101
low = 1
guess = 50
times = 0
while 1:
  response = "Is your number " + str(int(guess)) + "? (H, L, C): " #user input
  hi_lo = input(response).lower()
  while 1: #restricts input to H, L or C
    if hi_lo != "h" and hi_lo != "l" and hi_lo != "c":
      hi_lo = input("Must enter a H, L or C: ").lower()
    else: break
  if guess == numanswer and hi_lo != "c": #if correct but user is LYING
    print("I smell LIES!", end=" ")
  elif hi_lo == "l": #if low makes guess new mininum guess
    low = guess
    guess = low + (round((high - low)/2, 0)) #new guess is halfway between low and high
  elif hi_lo == "h": #if high makes guess new maximum guess
    high = guess
    guess = low + (round((high - low)/2, 0))
  elif guess == numanswer and hi_lo == "c": #if correct ends game
    break
  times += 1
print ("Your number was", int(guess), "and it only took me",  times, "tries to geuss it!")