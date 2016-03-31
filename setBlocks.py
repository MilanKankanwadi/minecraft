from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
#mc = Minecraft.create('192.168.0.4')
mc = Minecraft.create()

mc.setBlocks(78, 63, 299, -100, 50, 350, block.SAND.id)
