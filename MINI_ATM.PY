print("ATM TRANSACTION")
pas=int(input("enter password:"))#get password from the user
i=0
while True:#creates on infinty loop 
    if(pas==1234):
        print("proceed transaction")
        break
    else:
        if(i<=2):#repeat the loop only in three attempt
            print("invalid password")
            pas=int(input("enter correct password:"))
            i+=1
        else:
            print("exceed number of attempt")
            break
            
        
        
            
        