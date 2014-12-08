import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

#set variable 'air'
air=0

#destroys blocks
while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x+1,y,z+1,x-1,y+3,z-1,air)
