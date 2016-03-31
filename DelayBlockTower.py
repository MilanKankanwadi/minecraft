from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import random
mc = Minecraft.create()
# get player position
p = mc.player.getPos()
x = p.x + 2
y = p.y - 1
z = p.z + 2
mc.setBlock(x, y, z, block.SAND)
y = y + 1
time.sleep(random.randrange(0,10))
mc.setBlock(x, y, z, block.CACTUS)
y = y + 1
time.sleep(random.randrange(0,10))
mc.setBlock(x, y, z, block.CACTUS)
y = y + 1
time.sleep(random.randrange(0,10))
mc.setBlock(x, y, z, block.CACTUS)
