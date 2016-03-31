from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player.getPos()
mc.postToChat("Player position is " + str(p.x) + ", " + str(p.y) + ", " + str(p.z))
