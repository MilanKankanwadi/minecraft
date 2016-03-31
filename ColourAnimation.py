from mcpi.minecraft import Minecraft
import mcpi.block as block
import random
import time
mc = Minecraft.create()
p = mc.player.getPos()
x = p.x + 2
y = p.y 
z = p.z + 2
randomColor = random.randrange(0,15)
time.sleep(3)
print("color is " + str(randomColor))
mc.setBlock(x, y, z, block.WOOL.id, randomColor)
time.sleep(3)
randomColor = random.randrange(0,15)
print("color is " + str(randomColor))
mc.setBlock(x, y, z, block.WOOL.id, randomColor)
time.sleep(3)
randomColor = random.randrange(0,15)
print("color is " + str(randomColor))
mc.setBlock(x, y, z, block.WOOL.id, randomColor)
time.sleep(3)
randomColor = random.randrange(0,15)
print("color is " + str(randomColor))
mc.setBlock(x, y, z, block.WOOL.id, randomColor)

