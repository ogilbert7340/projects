import time, random, mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x+random.randint(-10,+10),50,pos.z+random.randint(-10,+10),13)
    time.sleep(0.2)
	
