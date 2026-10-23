import random 
'''
1=rock
-1=paper
0=scissor'''
computer=random.choice([1,0,-1])
n=input("enter your choice :- ").lower()
x={"r":1,"p":-1,"s":0}
y={1:"rock",-1:"paper",0:"scissor"}
you=x[n]
print(f"you choosed  {y[you]}\ncomputer choosed  {y[computer]}")
if(computer == you):
    print("game draws")
else:
    if(computer ==1 and you==0):
        print("computer wins")
    if(computer ==1 and you==-1):
        print("you win")
    if(computer ==-1 and you==0):
        print("you win")
    if(computer ==-1 and you==1):
        print("computer wins")
    if(computer ==0 and you==1):
        print("you win")
    if(computer ==0 and you==-1):
        print("computer wins")
    else:
        print("error occured")
        '''
        # based on the pattern of comp - you
if((computer-you==1) or (computer-you==-2)):
    print("computer wins")
else:
    print("you win")'''