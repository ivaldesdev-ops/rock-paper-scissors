# Isaac Valdes
# CMP 135-001
# 4/17/2023
# Final Project

# ----------------- Process -----------------

"""
- take in user input of 'r,p,s, or q'
    * if input = 'q', quit game and show results. Otherwise, keep playing.
    * add a counter to count how many times each object is played, wins, losses, ties,
      and total games played.
      
- use the random.choice() thing to assign a number to r, p, and s so the computer's
  part is randomized.

- compare the user input to the computer's random output and declare the winner.

- have a blank value to store the wins, losses, and ties of the user and add the 
  math functions to update it until the user presses 'q'.

-
"""

# ----------------- Imports -----------------
import random

# ----------------- Declarations -----------------

# Lists and Dictionaries
plays = ['Rock', 'Paper', 'Scissors']

# Variables to store values to display at the end.
wins = 0
losses = 0
ties = 0
timesr = 0
timesp = 0
timess = 0
timescompr = 0
timescompp = 0
timescomps = 0

userinput = input("Please enter your move by pressing 'r' for Rock, 'p' for Paper,'s' for Scissors, or 'q' for Quit.\n")
gameon = True
gamesplayed = 0

def mostlikelyoutcome():
    global compchoice
    if timesp > timesr and timess:
        compchoice = 'Scissors'
    elif timesr > timesp and timess:
        compchoice = 'Paper'
    elif timess > timesp and timesr:
        compchoice = 'Rock'

if timesr or timess or timesp > 1:
    mostlikelyoutcome()
else:
    compchoice = random.choice(plays)
    
def collectinput():
    global userinput
    userinput= input("Please enter your move by pressing 'r' for Rock, 'p' for Paper,'s' for Scissors, or 'q' for Quit.\n")
    
def playgame():
    #gameon = True

    while True:  

        # Detects User Input
        collectinput()
        # Player plays Rock
        if userinput == 'r':
            global userresponser
            userresponser = 'Rock'
            global timesr 
            global compchoice
            timesr += 1
            print(f"Your play: {userresponser}")
            if compchoice=='Rock':
                global timescompr 
                timescompr += 1
            elif compchoice=='Paper':
                global timescompp
                timescompp += 1
            elif compchoice=='Scissors':
                global timescomps 
                timescomps += 1
            print(f"Computer's play: {compchoice}")
            judgewinner()
            
            
            
        # Player plays Paper
        elif userinput == 'p':
            global userresponsep 
            userresponsep = 'Paper'
            global timesp 
            timesp += 1
            print(f"Your play: {userresponsep}")
            compchoice = random.choice(plays)
            if compchoice=='Rock':
                timescompr += 1
            elif compchoice=='Paper':
                timescompp += 1
            elif compchoice=='Scissors':
                timescomps += 1
            print(f"Computer's play: {compchoice}")
            judgewinner()
            
            
            

        # Player plays Scissors
        elif userinput == 's':
            global userresponses 
            userresponses = 'Scissors'
            global timess 
            timess += 1
            print(f"Your play: {userresponses}")
            compchoice = random.choice(plays)
            if compchoice=='Rock':
                timescompr += 1
            elif compchoice=='Paper':
                timescompp += 1
            elif compchoice=='Scissors':
                timescomps += 1
            print(f"Computer's play: {compchoice}")
            judgewinner()
            
            

        # Player quits
        elif userinput == 'q':
            showstats()
            break

        # Player pushes the wrong button
        else:
            print("Invalid move. Please enter your move by pressing 'r' for Rock, 'p' for Paper,'s' for Scissors, or 'q' for Quit.\n")
            break
        
        #Repeat()
        repeat = input("Would you like to go another round? y/n")
        if repeat == 'y':
            playgame()
        elif repeat == 'n':
            False
        break

def judgewinner():
    global userresponses
    userresponses = 'Scissors'
    global userresponsep
    userresponsep = 'Paper'
    global userresponser
    userresponser = 'Rock'
    global timescompr 
    global timescompp 
    global timescomps 
    if compchoice=='Rock':
        timescompr += 1
    elif compchoice=='Paper':
        timescompp += 1
    elif compchoice=='Scissors':
        timescomps += 1
        
            
    if (compchoice=='Rock' and userinput == 's') or (compchoice=='Scissors' and userinput =='p') or (compchoice=='Paper' and userinput=='r'):
        print("Computer wins")
        global losses 
        losses += 1
    elif (userinput =='r' and compchoice == 'Scissors') or (userinput=='s' and compchoice=='Paper') or (userinput=='p' and compchoice=='Rock'):
        print("You Win!")
        global wins 
        wins += 1
    else:
        print('Tie')
        global ties
        ties += 1
 
    
    global gamesplayed 
    gamesplayed+= 1
    #Repeat()

def showstats():
    print("Game Over!\n")
    print("-------------------\n")
    print(f"Games played: {gamesplayed}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print(f"\nYou played rock {timesr} times.")
    print(f"You played paper {timesp} times.")
    print(f"You played scissors {timess} times.")


        
    
# ----------------- Actions -----------------
playgame()
showstats()