from mcpi.minecraft import Minecraft
from mcpi import block
from builds.house import house


mc = Minecraft.create()

house.build(mc)


