import pygame

class Ninja(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.image_list = [0 for i in range(5)]
        self.image_list[0] = pygame.image.load('run1.png').convert_alpha()
        self.image_list[1] = pygame.image.load('run2.png').convert_alpha()
        self.image_list[2] = pygame.image.load('run3.png').convert_alpha()
        self.image_list[3] = pygame.image.load('run4.png').convert_alpha()
        self.image_list[4] = pygame.image.load('run5.png').convert_alpha()
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.move_ticker = 0
        self.gravity_ticker = 0
        self.rect.x = position_x
        self.rect.y = position_y
        self.speed = [0, 0]
        self.gravity_flag = [0, 0]

    def move(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed

        if self.speed[0] <= 0:
            self.move_ticker = 0

        self.move_ticker += 1

        for i in range(4):
            if self.move_ticker > i * 30 and self.move_ticker <= (i + 1) * 30:
                self.image = self.image_list[i]
        if self.move_ticker > 4 * 30:
            self.move_ticker = 0
            self.image = self.image_list[0]

    def jump(self):
        self.gravity_flag[0] = 1

#123
class SprStar(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.image = pygame.image.load('spr_star_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = [0, 0]
        self.rect.x = position_x
        self.rect.y = position_y

    def move(self, x_speed, y_speed):
        self.rect.x += x_speed
        self.rect.y += y_speed


class Zombie(Ninja):
    def __init__(self, position_x, position_y):
        super().__init__(position_x, position_y)
        self.image_list = [0 for i in range(6)]
        self.image_list[0] = pygame.image.load('zombieL1.png').convert_alpha()
        self.image_list[1] = pygame.image.load('zombieL2.png').convert_alpha()
        self.image_list[2] = pygame.image.load('zombieL3.png').convert_alpha()
        self.image_list[3] = pygame.image.load('zombieR1.png').convert_alpha()
        self.image_list[4] = pygame.image.load('zombieR2.png').convert_alpha()
        self.image_list[5] = pygame.image.load('zombieR3.png').convert_alpha()
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y


    def move(self, x_speed, y_speed):
        if x_speed > 0:
            if (self.image is self.image_list[0] or self.image is
                self.image_list[1] or self.image is self.image_list[2]):
                self.move_ticker = 0
            self.move_ticker += 1
            for i in range(3):
                if self.move_ticker > i * 40 and self.move_ticker <= (i+1)*40:
                    self.image = self.image_list[i + 3]
            if self.move_ticker > 120:
                self.image = self.image_list[0]
                self.move_ticker = 0
        if x_speed <= 0:
            if (self.image is self.image_list[3] or self.image is
                self.image_list[4] or self.image is self.image_list[5]):
                self.move_ticker = 0
            self.move_ticker += 1
            for i in range(3):
                if self.move_ticker > i * 40 and self.move_ticker <= (i+1)*40:
                    self.image = self.image_list[i]
                if self.move_ticker > 120:
                    self.image = self.image_list[0]
                    self.move_ticker = 0

        self.rect.x += x_speed
        self.rect.y += y_speed


class Smoke(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.image_list = [0 for i in range(5)]
        self.image_list[0] = pygame.image.load('spr_smoke_0.png').convert_alpha()
        self.image_list[1] = pygame.image.load('spr_smoke_1.png').convert_alpha()
        self.image_list[2] = pygame.image.load('spr_smoke_2.png').convert_alpha()
        self.image_list[3] = pygame.image.load('spr_smoke_3.png').convert_alpha()
        self.image_list[4] = pygame.image.load('spr_smoke_4.png').convert_alpha()
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.suicide_ticker = 0

    def suicide(self):
        self.suicide_ticker += 1
        for i in range(5):
            if (self.suicide_ticker > i * 10 and self.suicide_ticker < (i + 1) *
                10):
                self.image = self.image_list[i]
        if self.suicide_ticker > 50:
            self.kill()

class Wall(pygame.sprite.Sprite):
    """class of wall"""
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((226, 236, 160))
        self.rect = self.image.get_rect()























