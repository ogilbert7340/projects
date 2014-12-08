import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

air=0
wool=35
green=13
black=15

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def Space_Invader(x,y,z):
    mc.setBlocks(x,y-1,z,x+12,y-2,z+9,wool,black)
    mc.setBlocks(x+4,y-1,z+1,x+5,y-1,z+1,wool,green)
    mc.setBlocks(x+7,y-1,z+1,x+8,y-1,z+1,wool,green)

    mc.setBlocks(x+1,y-1,z+2,x+1,y-1,z+4,wool,green)
    mc.setBlocks(x+11,y-1,z+2,x+11,y-1,z+4,wool,green)

    mc.setBlocks(x+2,y-1,z+4,x+2,y-1,z+5,wool,green)
    mc.setBlocks(x+10,y-1,z+4,x+10,y-1,z+5,wool,green)

    mc.setBlocks(x+3,y-1,z+2,x+3,y-1,z+6,wool,green)
    mc.setBlocks(x+9,y-1,z+2,x+9,y-1,z+6,wool,green)

    mc.setBlocks(x+4,y-1,z+3,x+8,y-1,z+4,wool,green)
    mc.setBlocks(x+5,y-1,z+5,x+7,y-1,z+6,wool,green)

    mc.setBlocks(x+4,y-1,z+6,x+4,y-1,z+7,wool,green)
    mc.setBlocks(x+8,y-1,z+6,x+8,y-1,z+7,wool,green)

    mc.setBlock(x+3,y-1,z+8,wool,green)
    mc.setBlock(x+9,y-1,z+8,wool,green)

Space_Invader(x,y,z)
