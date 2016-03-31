from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
# get player position
p = mc.player.getPos()
x = p.x + 2
y = p.y
z = p.z + 2
print('Placing a melon at '
      + str(x) + ',' + str(y) + ',' + str(z))
mc.setBlock(x, y, z, block.SAND.id)
