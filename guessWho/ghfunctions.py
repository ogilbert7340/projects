import picamera, time

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
          if hat == "y" or "yes":
               hatFine = True
          else:
               hatFine = False
          
     #Eye Colour
     eyeColourFine = False
     while eyeColourFine != True:
          eyeColour = input("What colour are your eyes? ").lower()
          if eyeColour == "blue" or "brown" or "green" or "hazel":
               eyeColourFine = True
          else:
               eyeColourFine = False

     #Gender
     genderFine = False
     while genderFine != True:
          gender = input("Are you a boy or a girl? ").lower()
          if gender == "boy" or "male" or "b" or "boy":
               genderFine = True
          elif gender == "girl" or "female" or "g" or "f":
               genderFine = True
          else:

               genderFine = False

     #Glasses
     glassesFine = False
     while glassesFine != True:
          glasses = input("Are you wearing any glasses in the photo? ").lower()
          if glasses == "y" or "yes":
               glassesFine = True
          else:
               glassesFine = False

     #Facial Hair
     facialHairFine = False
     while facialHairFine != True:
          facialHair = input("Do you even facial hair? ").lower()
          if facialHair == "y" or "yes":
               facialHairFine = True
          else:
               facialHairFine = False

return name,hairColour,eyeColour,hat,gender,glasses,facialHair
