import math

class Circle:
     def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self.radius = radius

     def get_radius(self):
        return self.radius

     def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than 0.")
        self.radius = radius

    
    
