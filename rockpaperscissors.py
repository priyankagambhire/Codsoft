import random

p_count = 0
c_count = 0

while True:
    print(" | 1 --> Rock | 2 --> Paper | 3 --> Scissor | \n")
    player_turn = int(input(" Play your Move : " ))
    if( player_turn > 3 or player_turn < 1 ):
        print("\n Please Enter a VALID CHOICE \n")
        continue
    else:print()

    
    computer_turn = random.randint(1,3)

    if player_turn == 1 :print(" You have played Rock \n")
    elif player_turn == 2 :print(" You have played Paper \n")
    elif player_turn == 3 :print(" You have played Scissor \n")

    if computer_turn == 1 :print(" Computer has played Rock \n")
    elif computer_turn == 2 :print(" Computer has played Paper \n")
    elif computer_turn == 3 :print(" Computer has played Scissor \n")

    if(player_turn == 1 and computer_turn == 3):
        print("\n !!! Rock Wins !!! \n")
        p_count+=1
    elif(player_turn == 1 and computer_turn == 2):
        print("\n !!! Paper Wins !!! \n")
        c_count+=1
    elif(player_turn == 2 and computer_turn == 3):
        print("\n !!! Scissor Wins !!! \n")
        c_count+=1
    elif(player_turn == 2 and computer_turn == 1):
        print("\n !!! Paper Wins !!! \n")
        p_count+=1
    elif(player_turn == 3 and computer_turn == 1):
        print("\n !!! Rock Wins !!! \n")
        c_count+=1
    elif(player_turn == 3 and computer_turn == 2):
        print("\n !!! Scissor Wins !!! \n")
        p_count+=1
    else:
        print(" !!! TIED !!! \n")
    
    if p_count == 2 : 
        print(" !!! PLAYER HAS WON THE GAME !!! \n")
        exit()
    elif c_count == 2:
        print(" COMPUTER HAS WON THE GAME  \n")
        print(" BETTER LUCK NEXT TIME :( \n ")
        exit()
    else:
        print(f"PLAYER SCORE --> {p_count} \nCOMPUTER SCORE --> {c_count} \n")