# Area of the cirle using onstrutor perimeter
class circle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return (22/7) * self.redius ** 2
    
    def Parameter(self):
        return 2 * (22/7) * self.redius
    
c1 = circle(2)
print(c1.area())
print(c1.Parameter())
