class Horse:
    sound = 'Frrr'

    def __init__(self, x_distance=0):
        self.x_distance = x_distance
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance=0):
        self.y_distance = y_distance

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
        return self.x_distance and self.y_distance

    def get_pos(self):
        return f'({self.x_distance}, {self.y_distance})'

    def voice(self):
        return print(f'{Eagle.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

p1.voice()
