import random as ra
a = int(ra.randint(0,100))
# print(a)
c = 0
atempt =0
while(c==0):
    atempt +=1
    b = (int(input("Guess the number Between (0-100) : ")))
    if b < a:
        print("Too Small , Guess bigger number")
    elif b > a:
        print("Too Big , Guess the Smaller one")
    
    else:
        print(f"You Choose the correct Number in  {atempt} attempts")
        c= 1
    
