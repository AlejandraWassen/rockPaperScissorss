'''
Created on Feb 24, 2020

@author: ITAUser
'''

def keepPlaying = True
if keepPlaying = True:

    print (welcome to rockPaperScissors):
    print (rules (best 2 out of 3 Press 'q' to quit))
    
    #make a key that assigns a number to each choice for the computer
    rock = 1
    scissors = 2
    paper = 3
    
    import randomFunction
    
    computersScore = 0
    playersScore = 0
    
    #while player's score is less than 2 and the computer's score is less tham 2:
    if playersScore < 2 and computersScore < 2:
    `   #computer's choice = random number between 1 and 3
    #player's choice = input(ask player to select Rock, Paper or Scissors)
    input playersChoice
    if player inputs 'q' or 'Q':
    set keepPlaying to False
    stop the loop
    
    elif (player inputs rock and computer chooses rock) or 
    (player inputs paper and computer chooses paper) or
    (player inputs scissors and computer chooses scissors):
    print out DRAW
    print out player's score and computer's score
    
    elif (player inputs rock and computer chooses scissors) or
    (player inputs scissors and computer chooses paper) or
    (player inputs paper and computer chooses rock):
       add one to the player's score
       print out player's score and computer's score
    
    else:
        print(imput is invalid)
    #   tell the user their input was not valid

#print statement thanking the players for playing
print(Thank you for playing)
if player's score is 2:
#   print statement letting player know they won
print(You WON!)