from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
#mc = Minecraft.create('10.0.1.2')
mc = Minecraft.create()

while True:
  pos = mc.player.getPos()
  mc.setBlock(pos.x, pos.y, pos.z, block.DIAMOND_BLOCK.id, 1)
  time.sleep(1)
