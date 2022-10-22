import random

#main
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "Abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
gmailcom = "@gmail.com"

#adding
string = upper + lower + numbers 
length = 6
#printing
gmail = "".join(random.sample(string,length))
ready = input ("Are you Ready To See you gmail:")
if ready.lower() == 'no':
    print("Ok")
elif ready.lower() == 'yes':
 print ("Here is you Gmail: "+ gmail + gmailcom)
else:
    yesorno = input ("Yes or No: ")
    if yesorno.lower() == 'no':
        print ("ok")
    elif yesorno.lower() =='yes':
        print ("Here is you Gmail: "+ gmail + gmailcom)
    
    