#    PROJECT    01
# ROLLING DICE NUMBER GUESSING GAME

import random
m= int(input("Enter number of times you want to play: "))  #No. of times user wants to play
score=0
if m>0:
    for i in range(0,m):
        n=int(input("Number: "))                           #No. guessed by student
        if 1<=n<=6:
            x=random.randint(1,6)
            if n==x:
                score+=1
    print(score)
