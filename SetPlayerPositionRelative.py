from mcpi.minecraft import Minecraft
mc = Minecraft.create()
p = mc.player.getPos()
mc.player.setPos(p.x - 10, p.y + 2, p.z)
