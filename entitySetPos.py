from mcpi.minecraft import Minecraft
mc = Minecraft.create('192.168.0.4')

entityId = mc.getPlayerEntityId("Jam_and_pikelets")

mc.player.setPos(entityId, 110, 63, 100);
