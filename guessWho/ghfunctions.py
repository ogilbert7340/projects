import picamera, time, json

def getPicture(name):
     try:
          with picamera.PiCamera() as camera:
              check = False
              while check == False:
                  camera.start_preview()
                  time.sleep(2)
                  camera.capture(name + ".jpg")
                  time.sleep(1)
                  camera.stop_preview()
                  answer = input("Is this picture alright? ").lower()
                  if answer == ("y") or answer == ("yes"):
                      check = True
                  else:
                     check = False
     except picamera.exc.PiCameraError:
          print("There is a problem with the pi camera, please check if its connected")
          name=""

     return name
     
        
def getCharProfile():
     #User Name
     nameFine = False
     while nameFine != True:
          name = input("What is your name? ").lower()
          if name == "":
               nameFine = False
          else:
               nameFine = True

     #Hair Colour
     hairColourFine = False
     while hairColourFine != True:
          hairColour = input("What is your hair colour? ").lower()
          if hairColour == "":
               hairColourFine = False
          else:
               hairColourFine = True

     #Hat yes/no
     hatFine = False
     while hatFine != True:
          hat = input("Are you wearing a hat? ").lower()
          if hat == "y":
               hatFine = True
          elif hat == "yes":
               hatFine = True
          elif hat == "":
               hatFine = False
          
     #Eye Colour
     eyeColourFine = False
     while eyeColourFine != True:
          eyeColour = input("What colour are your eyes? ").lower()
          if eyeColour == "blue":
               eyeColourFine = True
          elif eyeColour == "brown":
               eyeColourFine = True
          elif eyeColour == "green":
               eyeColourFine = True
          elif eyeColour == "hazel":
               eyeColourFine = True
          else:
               eyeColourFine = False

     #Gender
     genderFine = False
     while genderFine != True:
          gender = input("Are you a boy or a girl? ").lower()
          if gender == "boy":
               genderFine = True
          elif gender == "girl":
               genderFine = True
          else:
               genderFine = False

     #Glasses
     glassesFine = False
     while glassesFine != True:
          glasses = input("Are you wearing any glasses in the photo? ").lower()
          if glasses == "y":
               glassesFine = True
          elif glasses == "yes":
               glassesFine = True
          elif glasses == "":
               glassesFine = False

     #Facial Hair
     facialHairFine = False
     while facialHairFine != True:
          facialHair = input("Do you even facial hair? ").lower()
          if facialHair == "y":
               facialHairFine = True
          elif facialHair == "yes":
               facialHairFine = True
          elif facialHair == "":
               facialHairFine = False

     return name,hairColour,eyeColour,hat,gender,glasses,facialHair

def saveProfile():
     getCharProfile()
     profile = [name,hairColour,eyeColour,hst,gender,glasses,facialHair]
     profiles.append(profile)

def loadProfile():
     try:
          with open
