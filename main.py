from mcpi.minecraft import Minecraft
from mcpi import block
from constructor import constructor



mc = Minecraft.create()
pos = mc.player.getTilePos()


b = constructor()

b.build(mc, pos, "house")