from mcpi import block
from builds.base import base

class garden(base):
    lenght = 3
    width = 3
    hight = 2
    Nblocks = 10


    flower = block.FLOWER_CYAN.id
    grass = block.GRASS.id
    air = block.AIR.id

    materials = {"flower": [flower, 1], "grass": [grass, 9]}
    
    structure = [ [grass, grass, grass,
                grass, grass, grass,
                grass, grass, grass ], 
                [ flower, air, flower,
                flower, air, flower,
                flower, flower, flower ]]

    @classmethod
    def build(cls, mc, pos):
        print("Building garden...")
        for layer in cls.structure:
            for i in range(cls.lenght):
                for j in range(cls.width):
                    block_type = layer[i * cls.width + j]
                    mc.setBlock(pos.x + i, pos.y, pos.z + j, block_type)
            pos.y += 1




