from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
#mc = Minecraft.create('192.168.0.4')
mc = Minecraft.create()
for x in range(-55, -20):
    if x % 2 == 0:
      mc.setBlock(x, 64, 330, block.FENCE.id)
    else:
      mc.setBlock(x, 64, 330, block.DIAMOND_BLOCK.id)
      mc.setBlock(x, 65, 330, block.DIAMOND_BLOCK.id)
 
