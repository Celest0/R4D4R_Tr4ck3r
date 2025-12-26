import random

class TargetSimulator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 2
        self.vy = 1

    def step(self):
        self.x += self.vx
        self.y += self.vy
        noise_x = random.gauss(0, 5)
        noise_y = random.gauss(0, 5)
        return [self.x + noise_x, self.y + noise_y]
