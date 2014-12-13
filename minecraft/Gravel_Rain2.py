import time, random, mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True: #creates potentially infinite loop
    pos = mc.player.getPos() #gets player position
    mc.setBlock(pos.x+random.randint(-10,+10),50,pos.z+random.randint(-10,+10),13) #randomly places gravel blocks in relation to player location
    time.sleep(0.2) #waits 0.2 seconds
	
