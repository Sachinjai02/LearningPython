class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = self.pi * (radius **2)

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


my_circle1 = Circle()
my_circle2 = Circle(100)

print('Circumference is {} and area is {}'.format(my_circle1.get_circumference(), my_circle1.area))
print('Circumference is {} and area is {}'.format(my_circle2.get_circumference(), my_circle2.area))
