import picamera,time,json


#
def getPic(name):
    try:
        with picamera.PiCamera() as camera:
            q = "n"
            while q == "n":
                print("Say cheese!")
                camera.start_preview()
                time.sleep(3)
                fn = "{0}.jpeg".format (name)
                camera.capture(fn)
                camera.stop_preview()
                q = input("Is this image okay? (y/n)  ")
    except picamera.exc.PiCameraMMALError:
        print("*** Camera is not connected, re-connect it and reboot. ***")
    print("Your file is called {0}.jpeg".format (name))
    return fn


#
def getChar():

    hairList=["Brown","Blonde","Ginger","Bald","Grey"]
    eyeList=["Brown","Green","Blue","Grey","Hazel"]
    glassesList=["y","n"]
    genderList=["Male","Female","Other"]
    hatList=["y","n"]
    facialList=["y","n"]
    
    
    
    name = ""
    while name == "":
        name = input("What is your name?")
    hair = ""
    while not (hair in hairList):
        hair = input("what colour hair do you have? (Brown/Blonde/Ginger/Grey/Bald)")
    eyes = ""
    while not (eyes in eyeList):
        eyes = input("What colour eyes do you have? (Brown/Green/Blue/Grey/Hazel)")
    glasses = ""
    while not (glasses in glassesList):
        glasses = input("Do you wear glasses or not? (y/n)")
    gender = ""
    while not (gender in genderList):
        gender = input("What gender are you? (Male/Female/Other)")
    hat = ""
    while not (hat in hatList):
        hat = input("Are you wearing a hat or not? (y/n)")
    facial = ""
    while not (facial in facialList):
        facial = input("Do you have facial hair? (y/n)")
    filename = getPic(name)

    profileList = [name,hair,eyes,glasses,gender,hat,facial,filename]

    return profileList

def saveProfile(profiles):
    profile = getChar()
    profiles.append(profile)
    with open("profiles.txt", mode="w") as p:
            json.dump(profiles,p)

def loadProfile():
    try:
        with open("profiles.txt", mode="r") as p:
            profiles = json.load(p)
            print(profiles)
    except IOError:
        print("Profiles.txt not found. Creating a new profile")
        profiles=[]
    return profiles
