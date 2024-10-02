class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self


class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self

    def get_pos(self):
        return f'({self.x_distance}, {self.y_distance})'

    def voice(self):
        return print(f'{super().sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

