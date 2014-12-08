import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

gold=41

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    mc.setBlock(x,y-1,z,gold)

    time.sleep(0.2)
