import random
swg=["Snake","Water","Gun"]
computer=random.choice(swg)
player=False
i=0
pscr=0
cscr=0
while (i<10):
    player=input("Snake , Water , Gun ?")
    if player==computer:
        print("Tie")
    elif player=="Snake":
        if computer=="Gun":
            print("You Lose!")
            pscr-=1
            cscr+=1
        else:
            print("You win!")
            pscr+=1
            cscr=+1
    elif player=="Water":
        if computer=="Snake":
            print("You lose!")
            pscr-=1
            cscr+=1
        else:
            print("You Win!")            
            pscr+=1
            cscr-=1
    elif player=="Gun":
        if computer=="Water":
            print("You Lose!")
            pscr-=1
            cscr+=1
        else:
            print("You Win!")
            pscr+=1
            cscr-=1
    else:
        print("Check your spelling!!")  
    computer=random.choice(swg)
    i=i+1
    if(i==10):
        print("Your Final Score is")
        print(pscr)
        print("Computer Final Score is")
        print(cscr)
        if pscr==cscr:
            print("Game Tie")
        elif pscr>cscr:
            print("You Win!!")
        else:
            print("You Lose..")        


