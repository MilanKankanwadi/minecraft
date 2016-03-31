from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create('192.168.0.4')
entityId = 3352
dir = mc.entity.getDirection(entityId)
print(dir)
