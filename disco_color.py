
class Disco_colors:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 3

    def disco_colors(self):
        for _ in range(1):
            self.a += 1
            if self.a == self.c:
                if self.b == 6:
                    self.a = 0
                    self.b = 0
                    self.c = 3
                else:
                    self.b += 1
                    self.c += 3
