import pygame
import sprite_class as sc
import before_game
import game_function as gf

WHITE = (255,255,255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600,450))
    pygame.display.set_caption('Ninja vs Zombie')
    clock = pygame.time.Clock()

    ninja = sc.Ninja(0,423)
    bg = before_game.BeforeGame()
    bg.create_sprite_list(ninja)


    spr_star_list = pygame.sprite.Group()
    star_ticker = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if ninja.gravity_flag[0] == 0 and  ninja.gravity_flag[1] == 0:
                        ninja.jump()
                if event.key == pygame.K_RIGHT:
                    ninja.speed[0] = 2
                elif event.key == pygame.K_LEFT:
                    ninja.speed[0] = -2
                elif event.key == pygame.K_a:
                    if star_ticker == 0:
                        spr_star = sc.SprStar(ninja.rect.midright[0],ninja.rect.midright[1] - 4)
                        spr_star.speed[0] = 5
                        spr_star_list.add(spr_star)
                        bg.all_drawed_list.add(spr_star)
                        star_ticker = 20
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ninja.speed[0] = 0
                if event.key == pygame.K_RIGHT:
                    ninja.speed[0] = 0

        screen.fill(WHITE)

        if star_ticker > 0:
            star_ticker -= 1

        gf.zombie_ai(bg.zombie_list)

        for star in spr_star_list:
           star.move(star.speed[0],star.speed[1])
           if pygame.sprite.spritecollide(star,bg.all_wall_list,False):
               star.kill()
               continue
           if pygame.sprite.spritecollide(star,bg.zombie_list,False):
               for zombie in \
               pygame.sprite.spritecollide(star,bg.zombie_list,False):
                   smoke = sc.Smoke(zombie.rect.x,zombie.rect.y)
                   bg.all_drawed_list.add(smoke)
                   bg.all_smoke_list.add(smoke)
                   bg.move_wall_list.add(smoke)
                   zombie.kill()
               star.kill()

        for smoke in bg.all_smoke_list:
            smoke.suicide()

        gf.check_gravity(ninja,bg.all_wall_list)
        gf.gravity(ninja)
        gf.sprite_pos_fix(ninja,bg.all_wall_list)
        gf.back_groud_move(ninja,bg.move_wall_list)

        if not bg.move_wall_list:
            pass
        elif ninja.rect.x > 366:
            ninja.rect.x = 366

        for drawed in bg.all_drawed_list:
            screen.blit(drawed.image,[drawed.rect.x,drawed.rect.y])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()



















