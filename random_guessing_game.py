#random guessing game sinlge user
import random#is the external package used to generate random value
gen_num=random.randint(1,10)#randint()-->used to tell the random package the random value must be in a range of (1 to 9)
i=1
while True:#infinity loop
    user_num=int(input("your number is:"))
    if(user_num==gen_num):
         print("guessing is correct")
         break
    if(i<3):#iterative statement
        if(user_num < gen_num):
             print("user guess is lower then generation number")
        if(user_num > gen_num):
             print("user guess is higher than generation number")
        i+=1
    else:
        print("your attempt is fail")
        break

    

