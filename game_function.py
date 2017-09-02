import pygame
from random import randrange

S_L1 = [-(2 * (i + 1) - 1) for i in range(5)][::-1]
S_L2 = [2 * (i + 1) - 1 for i in range(30)] + [-1,0]

def check_gravity(sprite,wall_list):
    sprite.move(0, 1)
    if pygame.sprite.spritecollide(sprite,wall_list,False):
        sprite.gravity_flag[1] = 0
    else:
        sprite.gravity_flag[1] = 1
    sprite.move(0, -1)


def gravity(sprite):
    if sprite.gravity_flag[0] != 0:
        sprite.gravity_ticker += 1
        for i in range(5):
            if (sprite.gravity_ticker > i * 2 and sprite.gravity_ticker <= (i +
                1) * 2):
                sprite.speed[1] = S_L1[i]
                break
        if sprite.gravity_ticker > 8:
            sprite.gravity_ticker = 0
            sprite.speed[1] = 0
            sprite.gravity_flag[0] = 0

    if sprite.gravity_flag[0] == 0 and sprite.gravity_flag[1] != 0:
        sprite.gravity_ticker += 1
        for i in range(30):
            if (sprite.gravity_ticker > i * 6 and sprite.gravity_ticker <= (i +
                1) * 6):
                sprite.speed[1] = S_L2[i]

    if sprite.gravity_flag[0] == 0 and sprite.gravity_flag[1] == 0 :
        sprite.speed[1] = 0
        sprite.gravity_ticker = 0


def sprite_pos_fix(sprite,wall_list):
    move_list = []
    final_move = [0, 0]

    flag_x = abs(sprite.speed[0]) + sprite.speed[0]
    flag_y = abs(sprite.speed[1]) + sprite.speed[1]

    def judge(flag):
        if flag == 0:
            return -1
        else:
            return 1

    if sprite.speed[0] != 0 and sprite.speed[1] != 0:
        for i in range(sprite.speed[0] * judge(flag_x) + 1):
            for j in range(sprite.speed[1] * judge(flag_y) + 1):
                sprite.move(i * judge(flag_x),j * judge(flag_y))
                if len(pygame.sprite.spritecollide(sprite,wall_list,False)) == 0:
                   move_list.append([i * judge(flag_x),j * judge(flag_y)])
                sprite.move(-i * judge(flag_x),-j * judge(flag_y))

    if sprite.speed[0] != 0 and sprite.speed[1] == 0:
        for i in range(sprite.speed[0] * judge(flag_x) + 1):
            sprite.move(i * judge(flag_x),0)
            if len(pygame.sprite.spritecollide(sprite,wall_list,False)) == 0:
                move_list.append([i * judge(flag_x),0])
            sprite.move(-i * judge(flag_x),0)

    if sprite.speed[0] == 0 and sprite.speed[1] != 0:
        for i in range(sprite.speed[1] * judge(flag_y) + 1):
            sprite.move(0,i * judge(flag_y))
            if len(pygame.sprite.spritecollide(sprite,wall_list,False)) == 0:
                move_list.append([0,i * judge(flag_y)])
            sprite.move(0,-i * judge(flag_y))

    if len(move_list) != 0:
        min_move = 999
        for i in move_list:
            distance = (i[0] - sprite.speed[0])**2 + (i[1] - sprite.speed[1])**2
            if distance < min_move :
                min_move = distance
                final_move = i
    else:
        final_move = [0,0]
   
    sprite.move(final_move[0],final_move[1])


def back_groud_move(ninja,moved_sprite_list):
    if ninja.rect.x >= 366:
        for sprite in moved_sprite_list:
            sprite.rect.x -= ninja.rect.x - 366
            if sprite.rect.x < -140:
                sprite.kill()


def zombie_ai(zombie_list):
    for zombie in zombie_list:
        zombie.move(zombie.speed[0],zombie.speed[1])
        if ((zombie.rect.x <= zombie.standing_wall.rect.x) or (zombie.rect.x >=
            (zombie.standing_wall.rect.x + 112))):
            zombie.speed[0] *= -1













