from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
#mc = Minecraft.create('192.168.0.4')
mc = Minecraft.create()
time.sleep(10)
hits = mc.events.pollBlockHits()

hitCounter = len(hits)
mc.postToChat("You have hit something " + str(hitCounter) + " times")
