'''
Created on Feb 24, 2020

@author: ITAUser
'''
#import the random function
import random
from builtins import False
#set variable keepPlaying to true
keepPlaying = True
#while keepPlaying is true:
while keepPlaying == True:
    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    print("Welcome to Rock, Paper, Scissors. The rules are whoever wins the best two out of three games wins.")
    #set computer's score to 0
    #set player's score to 0
    computer = 0
    player = 0
#while player's score is less than 2 and computer's score is less than 2:
    while (computer < 2 and player < 2):
        #computer's choice = input(ask player to select rock, paper, or scissors)
        playerChoice = input ("choose (rock, paper, or scissors:")
        playerChoice = playerChoice.lower()
        #if player inputs 'q' or 'Q':
        if(playerChoice == "q"):
            #set keepPlaying to False
            keepPlaying = False
        #stop the loop
        break
    
        #else if (player inputs rock and computer chooses rock) or 
        #(player inputs paper and computer chooses paper) or
        #(player inpurs scissors and computer chooses scissors):
        elif ((playerChoice == "rock" and computerChoice == "rocl") or (playerChoice == "scissors" and computerChoice == "scissors") or (playerChoice == "paper" and computerChoice == "paper")):
            #print out draw
            print("Draw")
            #print out player's score and computer's score
            print("player score = " + player.__str__() + "computer score = " computer.__str__())
        #else if (player inputs rock and computer chooses scissors) or 
        #(player inputs scissors and computer chooses paper) or
        #(player inputs paper and computer chooses rock):
        elif ((playerChoice =="rock" and compuerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "rock")):
            #add one to the player's score
            player = player + 1
            #print out player's score and computer's score
            print("player score = " + player.__str__() + "computer score = " computer.__str__())
        #else if (player inputs rock and computer chooses paper) or
        #(player inputs scissors and computer chooses rock) or
        #(player inputs paper and computer chooses scissors):
        elif ((playerChoice == "scissors" and compuerChoice == "rock") or (playerChoice == "paper" and computerChoice == "scissors") or (playerChoice == "rock" and computerChoice == "paper")):
            #ass one to the computer's score
            computer = computer + 1
            #print out player's score and computer's score
            print("player score = " + player.__str__() + "computer score = " computer.__str__())
            
        #else:
        #tell the user their input was not valid
        else:
            print("your input was not valid, try again.")
        
#print statement thanking the player for playing
print("thank you for playing!")
#if player's score is 2:
if (player == 2):
    #print statement letting player know they won
    print ("you won!")
#if computer's score is 2:
if (computer == 2):
    #print statement letting player know they lost
    print("you lost!")
#print out player's score and computer's score
print("player score = " + player.__str__() + "computer score = " computer.__str__())
    