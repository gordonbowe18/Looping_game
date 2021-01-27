#Set some empty lists for later
player_1_score = []
player_2_score = []
player_1_rounds_score = []
player_2_rounds_score = []
player_1_rounds = 0
player_2_rounds = 0

#Name and welcome the players

print ("Who is Player 1?")
player_1 = input ()
print ("Hello " + player_1 + "!")
print ("Who is Player 2?")
player_2 = input ()
print ("Hello " + player_2 + "!")

#Establish the shot numbers
shots = ''
while shots.isdigit() == False:
    print ("Enter the number of shots per round please!")
    shots = input()
#Needs some sad path handling, they might put in letters...
shots = int(shots)
print ("There will be " + str(shots) + " shots per round. Take it in turns one by one and I will print the final scores and the winners of the round!") 
print ("Go stick that Wicket!")
keep_going = 'yes'
while keep_going == 'yes':
#loop through shot numbers, and add their scores to the lists. Also needs unhappy path control, cause they might put letters in again...
    while len(player_1_score) < shots:
        print ("What was " + player_1 + "'s score?")
        add_1 = input()
        print ("What was " + player_2 + "'s score?")
        add_2 = input()
        player_1_score.append(add_1)
        player_2_score.append(add_2)

#create the summable lists
    player_1_score_map = list(map(int, player_1_score))
    player_2_score_map = list(map(int, player_2_score))
    player_1_sum = sum(player_1_score_map)
    player_2_sum = sum(player_2_score_map)

    print (player_1 + " has scored " + str(player_1_sum) + " points this round.")
    print (player_2 + " has scored " + str(player_2_sum) + " points this round.")

#State who has won the game based on who scored the most
    if player_1_sum > player_2_sum:
        print ("Well done " + player_1 + ", you smashed it this round! But don't get cocky, I'm sure " + player_2 + " is more detemined than ever...")
        player_1_rounds += 1
    elif player_1_sum < player_2_sum:
        print ("Well done " + player_2 + ", you smashed it this round! But don't get cocky, I'm sure " + player_1 + " is more determined than ever...")
        player_2_rounds += 1
    else:
        print ("What a waste of time...")
    player_1_rounds_score += player_1_score_map
    player_1_rounds_score.append("|")
    
    player_2_rounds_score += player_2_score_map
    player_2_rounds_score.append("|")
    
    player_1_score = []
    player_2_score = []
    print (player_1 + " has the following round scores...")
    print (player_1_rounds_score)
    print (player_2 + " has the following round scores...")
    print (player_2_rounds_score)
#find out if they want to continue. Is it unhappy path to have anything except 'yes' to be the way forward? What if they type in 'Y'...
    print('Would you like to keep playing? Please enter yes or no...')
    keep_going = input()
print (player_1 + " won " + str(player_1_rounds) + " rounds.")
print (player_2 + " won " + str(player_2_rounds) + " rounds.")

#State who is best to end the program
if player_1_rounds > player_2_rounds:
    print (player_1 + " is the bestest!")
else:
    print (player_2 + " is the bestest!")
print ("Press the enter key to exit")
leave = input()





