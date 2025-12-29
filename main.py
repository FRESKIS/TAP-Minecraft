from mcpi.minecraft import Minecraft
from mcpi import block
from builds import *
import json


mc = Minecraft.create()
pos = mc.player.getTilePos()


b = building(garden)
b.construct(mc, pos)
print(b.properties())