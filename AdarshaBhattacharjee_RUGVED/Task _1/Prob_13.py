from abc import ABC
class Shape(ABC):
    def __init__(self,c):
        self.color=c
    def get_color(self):
        return self.color
    def get_area(self):
        return

class Square(Shape):
    def __init__(self,c,side):
        self.color=c
        self.side=side
    super().__init__(c)
    self_side=float(side)
    def get_area(self):
        return self.self_side*self.self_side