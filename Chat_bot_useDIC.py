dic={1:"hello ,welcome",
     2:"120/80 BP mmg",
     3:"72 time per min",
     4:"90 ml per blood"
     }#dictionary contain key,value pair which store the input in the form of value
print("welcome to bot")
while True:
    user=input("you:")#get a input
    
    if user.lower() in ["quit","stop","thankyou"]:
        print("bot:Thankyou for using bot.bye ,have a nice day")
        break
    if user.lower() in ["hello","hii","good morning"]:
        print("bot:",dic[1])#dic[]-->representing the index value
    if user.lower() in ["what is the blood pressure of blood?"]:
        print("bot:",dic[2])
    if user.lower() in ["what is the breathing rate of healthy human?"]:
        print("bot:",dic[3])
    if user.lower() in ["what is the healthy oxygen level in the blood?"]:
        print("bot:",dic[4])