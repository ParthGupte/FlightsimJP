import math
import vectors as vec
class sphere():
    def __init__(self, radius, mass, velocity, position):
        self.object_type = 'Sphere'
        self.object_radius = radius
        self.mass = mass
        self.velocity = velocity
        self.position = position
    def projection_area(self):
        return math.pi * ((self.object_radius)**2)
    def drag(self, environment,time):
        velocity_rel = self.velocity - environment.wind(time)
        drag = ((1/2) * environment.drag_coefficient * environment.density * self.projection_area() * vec.mod(velocity_rel)) * (-1) * (velocity_rel)
        return drag
