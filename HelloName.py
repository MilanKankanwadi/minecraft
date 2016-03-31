from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input('What is your name?')
mc.postToChat('Hello ' + name)
