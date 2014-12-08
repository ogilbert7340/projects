import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

brick = 45
air = 0
wood = 5

def buildhouse(x,y,z):
	mc.setBlocks(x-2,y-1,z,x-12,y+5,z-8,brick)
	mc.setBlocks(x-3,y,z-1,x-11,y+4,z-7,air)
	mc.setBlocks(x-4,y,z,x-4,y+1,z,air)
	mc.setBlocks(x-3,y,z-1,x-11,y,z-7,wood)

for space in (x,x+15,x+30,x+45,x+60):
	buildhouse(space,y,z)
