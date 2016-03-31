from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = input('Enter the x value')
y = input('Enter the y value')
z = input('Enter the z value')
print("Set position to " + x + "," + y + "," + z)
mc.player.setPos(float(x), float(y), float(z))
