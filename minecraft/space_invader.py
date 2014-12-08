import mcpi.minecraft as minecraft,time
mc = minecraft.Minecraft.create()

#defining the block ID
air=0
wool=35
green=13
black=15

#defines player positions
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

#defines the programe space invader
def Space_Invader(x,y,z):
    while True:
        #places the blank 'canvas'
        mc.setBlocks(x,y-1,z,x+12,y-2,z+9,wool,black)
        #places the arms and side of body
        mc.setBlocks(x+4,y-1,z+1,x+5,y-1,z+1,wool,green)
        mc.setBlocks(x+7,y-1,z+1,x+8,y-1,z+1,wool,green)
        #places side of body
        mc.setBlocks(x+1,y-1,z+2,x+1,y-1,z+4,wool,green)
        mc.setBlocks(x+11,y-1,z+2,x+11,y-1,z+4,wool,green)
        #places the main body
        mc.setBlocks(x+2,y-1,z+4,x+2,y-1,z+5,wool,green)
        mc.setBlocks(x+10,y-1,z+4,x+10,y-1,z+5,wool,green)

        mc.setBlocks(x+3,y-1,z+2,x+3,y-1,z+6,wool,green)
        mc.setBlocks(x+9,y-1,z+2,x+9,y-1,z+6,wool,green)

        mc.setBlocks(x+4,y-1,z+3,x+8,y-1,z+4,wool,green)
        mc.setBlocks(x+5,y-1,z+5,x+7,y-1,z+6,wool,green)

        mc.setBlocks(x+4,y-1,z+6,x+4,y-1,z+7,wool,green)
        mc.setBlocks(x+8,y-1,z+6,x+8,y-1,z+7,wool,green)
        #places the ears
        mc.setBlock(x+3,y-1,z+8,wool,green)
        mc.setBlock(x+9,y-1,z+8,wool,green)

        #waits 1 second
        time.sleep(1)
    
        #resets the canvas
        mc.setBlocks(x,y-1,z,x+12,y-2,z+9,wool,black)
        #builds space invader with arms up
        mc.setBlocks(x+4,y-1,z+1,x+5,y-1,z+1,wool,green)
        mc.setBlocks(x+7,y-1,z+1,x+8,y-1,z+1,wool,green)
        #places side of body
        mc.setBlocks(x+1,y-1,z+7,x+1,y-1,z+5,wool,green)
        mc.setBlocks(x+11,y-1,z+7,x+11,y-1,z+5,wool,green)
        #places the main body
        mc.setBlocks(x+2,y-1,z+4,x+2,y-1,z+5,wool,green)
        mc.setBlocks(x+10,y-1,z+4,x+10,y-1,z+5,wool,green)

        mc.setBlocks(x+3,y-1,z+2,x+3,y-1,z+6,wool,green)
        mc.setBlocks(x+9,y-1,z+2,x+9,y-1,z+6,wool,green)

        mc.setBlocks(x+4,y-1,z+3,x+8,y-1,z+4,wool,green)
        mc.setBlocks(x+5,y-1,z+5,x+7,y-1,z+6,wool,green)

        mc.setBlocks(x+4,y-1,z+6,x+4,y-1,z+7,wool,green)
        mc.setBlocks(x+8,y-1,z+6,x+8,y-1,z+7,wool,green)
        #places the ears
        mc.setBlock(x+3,y-1,z+8,wool,green)
        mc.setBlock(x+9,y-1,z+8,wool,green)

        time.sleep(1)

Space_Invader(x,y,z)
