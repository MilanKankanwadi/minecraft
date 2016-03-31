from mcpi.minecraft import Minecraft
import mcpi.block as block
#mc = Minecraft.create('192.168.0.4)
mc = Minecraft.create()
x = float(input('Enter the x value')
)
y = float(input('Enter the y value'))
z = float(input('Enter the z value'))
entityId = 3352
b = mc.getBlock(x, y, z)
goAhead = True

print(b)
if b == block.WATER.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
  answer = input("You will get wet! Are you sure you want to teleport?")
  if answer == 'N':
    goAhead = False

if goAhead:
  mc.entity.setPos(entityId, x, y, z)
