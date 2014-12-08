import time, random, mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

gravel = 13 #Sets variable that gravel is 13

time.sleep(2) #Waits 2 seconds

while True: #Creates a potentially infinite loop
    pos = mc.player.getPos() #Sets variable of the players position to 'pos'
    x = pos.x #Sets variable of players x position to 'x'
    y = pos.y #Sets variable of players y position to 'y'
    z = pos.z #Sets variable of players z position to 'z'

    a = random.randint(-10,+10) #Sets variable of a random position between
				#-10 to 10 
    mc.setBlock(x+a,50,z+a,gravel) #Sets a random place for a gravel block to
				   #drop
    time.sleep(0.2) #(random.randint(0.2,1.2)) #Waits zero point  two seconds
