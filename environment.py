import vectors as vec
class environment():
    def __init__(self, density):
        self.density = density
        self.drag_coefficient = 0.47
        self.g = vec.vec([0,0,-9.8])
    def wind(self, time):
        return vec.vec([5,20,0])
