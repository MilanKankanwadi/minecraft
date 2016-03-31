from mcpi.minecraft import Minecraft
mc = Minecraft.create('192.168.0.4')
userName = input('What is your Minecraft username?')
mc.postToChat(userName + ': Hello')
