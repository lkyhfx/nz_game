import pygame
from random import randrange,choices
import sprite_class as sc

class BeforeGame():
    def __init__(self):
        self.all_drawed_list = pygame.sprite.Group()
        self.all_wall_list = pygame.sprite.Group()
        self.move_wall_list = pygame.sprite.Group()
        self.zombie_list = pygame.sprite.Group()
        self.gravity_list = pygame.sprite.Group()
        self.all_smoke_list = pygame.sprite.Group()


    def create_sprite_list(self,ninja):
        self.all_drawed_list.add(ninja)
        self.gravity_list.add(ninja)

        first_floor_x_array = choices(range(140,5860,420),k=30)
        second_floor_x_array = choices(first_floor_x_array,k=10)
        zombie_sx_array = choices(second_floor_x_array,k=5)
        zombie_fx_array = choices(first_floor_x_array,k=10)

        for i in first_floor_x_array:
            wall = sc.Wall(140,20)
            wall.rect.x = i
            wall.rect.y = 430
            self.all_wall_list.add(wall)
            self.move_wall_list.add(wall)
            self.all_drawed_list.add(wall)
            if i in zombie_fx_array:
                zombie = sc.Zombie(i,430 - 34)
                zombie.standing_wall = wall
                zombie.speed[0] = 1
                self.all_drawed_list.add(zombie)
                self.gravity_list.add(zombie)
                self.move_wall_list.add(zombie)
                self.zombie_list.add(zombie)


        for i in second_floor_x_array:
            wall = sc.Wall(140,20)
            wall.rect.x = i + 175
            wall.rect.y = 390
            self.all_wall_list.add(wall)
            self.move_wall_list.add(wall)
            self.all_drawed_list.add(wall)

            if i in zombie_sx_array:
                zombie = sc.Zombie(i + 175,390 - 34)
                zombie.standing_wall = wall
                zombie.speed[0] = 1
                self.all_drawed_list.add(zombie)
                self.gravity_list.add(zombie)
                self.move_wall_list.add(zombie)
                self.zombie_list.add(zombie)


        wall_down = sc.Wall(600,400)
        wall_down.rect.x = 0
        wall_down.rect.y = 450

        wall_left = sc.Wall(30,450)
        wall_left.rect.x = -30
        wall_left.rect.y = 0

        wall_right = sc.Wall(30,450)
        wall_right.rect.x = 600
        wall_right.rect.y = 0


        self.all_wall_list.add(wall_left)
        self.all_wall_list.add(wall_down)
        self.all_wall_list.add(wall_right)





























