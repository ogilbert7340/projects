import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

wool=35

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

def O(x,y,z,colour):
	mc.setBlocks(x+2,y+1,z,x+2,y+5,z,wool,colour)
	mc.setBlocks(x+3,y,z,x+5,y,z,wool,colour)
	mc.setBlocks(x+3,y+6,z,x+5,y+6,z,wool,colour)
	mc.setBlocks(x+6,y+5,z,x+6,y+1,z,wool,colour)

def Z(x,y,z,colour):
	mc.setBlocks(x+2,y,z,x+7,y,z,wool,colour)
	mc.setBlock(x+2,y+1,z,wool,colour)
	mc.setBlock(x+3,y+2,z,wool,colour)
	mc.setBlock(x+4,y+3,z,wool,colour)
	mc.setBlock(x+5,y+4,z,wool,colour)
	mc.setBlock(x+6,y+5,z,wool,colour)
	mc.setBlock(x+7,y+6,z,wool,colour)
	mc.setBlocks(x+2,y+7,z,x+7,y+7,z,wool,colour)

Z(x,y,z)
