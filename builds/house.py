from mcpi import block
from builds.base import base

class house(base):
    lenght = 5
    width = 5
    hight = 5
    Nblocks = 98


    wood = block.WOOD.id
    brick = block.BRICK_BLOCK.id
    air = block.AIR.id

    materials = {"wood": [wood, 62], "brick": [brick, 36]}
    
    structure = [ [wood, wood, wood, wood, wood,
                wood, wood, wood, wood, wood,
                wood, wood, wood, wood, wood,
                wood, wood, wood, wood, wood,
                wood, wood, wood, wood, wood ], 
                [ wood, brick, brick, brick, wood,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                wood, brick, brick, brick, wood ], 
                [ wood, brick, brick, brick, wood,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                wood, brick, brick, brick, wood ],
                [ wood, brick, brick, brick, wood,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                brick, air, air, air, brick,
                wood, brick, brick, brick, wood ],
                [ wood, wood, wood, wood, wood,
              wood, wood, wood, wood, wood,
              wood, wood, wood, wood, wood,
              wood, wood, wood, wood, wood,
              wood, wood, wood, wood, wood ]]

    @classmethod
    def build(cls, mc, pos):
        print("Building house...")
        for layer in cls.structure:
            for i in range(cls.lenght):
                for j in range(cls.width):
                    block_type = layer[i * cls.width + j]
                    mc.setBlock(pos.x + i, pos.y, pos.z + j, block_type)
            pos.y += 1



