import mcpi.minecraft as minecraft, time
mc = minecraft.Minecraft.create()

time.sleep(3)

#Creates variable for BlockID
glass=20
water=8

#Places swimming pool
mc.setBlocks(45,-7,-51,70,-1,-61,glass)
mc.setBlocks(69,-1,-60,46,-6,-52,water)

#Places swimming pool anywhere START
