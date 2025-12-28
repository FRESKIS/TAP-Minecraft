from mcpi import block

class house:
    lenght = 5
    width = 5
    hight = 5
    Nblocks = 98

    wood = block.WOOD.id
    brick = block.BRICK_BLOCK.id
    air = block.AIR.id
    
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
    def build(cls, mc):
        pos = mc.player.getTilePos() 
        for layer in cls.structure:
            for i in range(cls.lenght):
                for j in range(cls.width):
                    block_type = layer[i * cls.width + j]
                    mc.setBlock(pos.x + i, pos.y, pos.z + j, block_type)
            pos.y += 1

