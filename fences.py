from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc = Minecraft.create('192.168.0.4')

for x in range(-55, -20):
    mc.setBlock(x, 64, 330, block.FENCE.id)

for z in range(330, 341):
    mc.setBlock(-20, 64, z, block.FENCE.id)


for x in range(-55, -20):
    mc.setBlock(x, 64, 340, block.FENCE.id)

for z in range(330, 341):
    if z == 335:
        # Fence gate facing east
        mc.setBlock(-55, 64, z, block.FENCE_GATE.id, 5)
    else:
        mc.setBlock(-55, 64, z, block.FENCE.id)
