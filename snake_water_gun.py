import random
num=random.randint(1,3)


def gameWin(num,i):
    
    if (i!="s")and (i!="w") and (i!="g"):
        return("Invalid Input")
    elif (num==i):
        return(None)
    elif (num=="s"):
        if(i=="w"):
            return(False)
        elif(i=="g"):
            return(True)
    elif (num=="w"):
        if(i=="s"):
            return(True)
        elif(i=="g"):
            return(False)
    elif (num=="g"):
        if(i=="w"):
            return(True)
        elif(i=="s"):
            return(False)
while(True):#For continuous playing.
    print("Press 'q' to exit")    
    i=input("Choose snake(s) or water(w) or gun(g)")
    if(i=='q'):
        break
    if num==1:
        num="s"
    elif num==2:
        num="w"
    elif num==3:
        num="g"

    print(f"You choose {i} and computer choose {num}")
    a=gameWin(num,i)
    if a==None:
        print("Tie")
    elif a==True:
        print("You win")
    elif a==False:
        print("You Loose")
    elif a==("Invalid Input"):
        print("Invalid Input")