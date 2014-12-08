userName = ""
while userName=="":
    userName = input("What is your name?")

print("Good Morning {0}".format(userName))

password = "cheese"
question = ""

while password != question:
    question = input("What is the Password?")
    if password == "cheese":
        print("Correct. Welcome {0}.".format(userName))
        
    
