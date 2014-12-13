userName = ""
while userName=="":
    userName = input("What is your name?") #asks user for there name

print("Good Morning {0}".format(userName)) #prints good morning <user>

#setting variables
password = "cheese"
question = ""

#while loop testing for correct password
while password != question:
    question = input("What is the Password?") #repeats the question until correct
    if password == "cheese":
        print("Correct. Welcome {0}.".format(userName)) #when correct, stops repeating the question and say 'Correct. Welcome <user>'
        
    
