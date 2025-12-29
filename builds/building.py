from builds.base import base

class building:
    def __init__(self, building: base):
        self.building = building    

    def construct(self, mc, pos):
        self.building.build(mc, pos)

    def properties(self):
        js = {"Nblocks": self.building.Nblocks, "materials": self.building.materials}
        return js