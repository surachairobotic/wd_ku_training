def EvenOrOdd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"

a = 10
b = 7
z1 = EvenOrOdd(a)
print(z1)
z2 = EvenOrOdd(b)
print(z2)

class Car:
    def __init__(self):
        self.wheel = 4
        self.color = 'black'
        self.EVcar = False
    def get_info(self):
        return [self.wheel, self.color ,self.EVcar]
    def set_color(self, color):
        self.color = color

x = Car()
print(x.get_info())
x.set_color('red')
print(x.get_info())