import mcpi.minecraft as minecraft, time as t
mc = minecraft.Minecraft.create()


t.sleep(3)

#move player close to origin
mc.player.setPos(10,10,0)

#block id variables
black=7
red=14
orange=1
green=5
white=35

#Setup empty lights
mc.setBlock(30,0,0,35,black)
mc.setBlock(30,1,0,35,black)
mc.setBlock(30,2,0,35,black)
mc.setBlock(30,3,0,35,black)
mc.setBlock(30,4,0,35,black)
mc.setBlock(30,5,0,35,black)
mc.setBlock(30,6,0,35,black)
t.sleep(2)

#Building the road
mc.setBlocks(30,-1,1,40,-1,3,35,black)

while True:
        mc.setBlock(30,6,0,35,red)
        t.sleep(10)
        mc.setBlock(30,6,0,35,red)
        mc.setBlock(30,5,0,35,orange)
        t.sleep(3)
        mc.setBlock(30,6,0,35,black)
        mc.setBlock(30,5,0,35,black)
        mc.setBlock(30,4,0,35,green)
        t.sleep(10)
        mc.setBlock(30,4,0,35,black)
        mc.setBlock(30,5,0,35,orange)
        t.sleep(4)

