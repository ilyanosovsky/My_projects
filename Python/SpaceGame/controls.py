import pygame
import sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets): # Check events of the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            # sys.exit()
            pygame.quit()

        elif event.type == pygame.KEYDOWN: # Check if the key is pressed
            # move the gun to the right
            if event.key == pygame.K_RIGHT: 
                gun.mright = True
            elif event.key == pygame.K_LEFT: 
                gun.mleft = True
            elif event.key == pygame.K_SPACE: # Check if the key is SPACE
                new_bullet = Bullet(screen, gun) 
                bullets.add(new_bullet) # Add new bullet to the group of bullets
        elif event.type == pygame.KEYUP: # Check if the key is released
            # stop the gun
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

# create fonction to start the game with press any key to start
# def game_start(screen, stats, sc):
#     # show the screen with pressd any key to start
#     screen.fill((0, 0, 0))
#     # press any key to start
#     font = pygame.font.SysFont(None, 48)
#     text = font.render("Press any key to start", True, (255, 255, 255))
#     text_rect = text.get_rect()
#     text_rect.center = screen.get_rect().center
#     screen.blit(text, text_rect)
#     pygame.display.flip()
#     # wait for key press
#     time.sleep(3)
#     sc.image_score()
#     sc.image_guns()
#     pygame.display.flip() # Make the most recently drawn screen visible.

def update(bg_img, screen, stats, sc, gun, inos, bullets): # Update screen
    # redraw the screen during each pass through the loop
    screen.blit(bg_img, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets): # Update bullets
    # delete bullets that have disappeared
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True) # Check collisions between bullets and Inos
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    # check if the Inos have reached the bottom of the screen
    # game_start(screen, stats, sc)
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:   
        stats.run_game = False
        # sys.exit()
        game_over(screen, stats, sc)



def update_inos(stats, screen, sc, gun, inos, bullets):
    # update the position of all Inos in the army
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos): 
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos, bullets):
    # check whether inos got to the bottom of the screen or not
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos):
    # create an army of Inos
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) /  ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 3 * ino_height - 100) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def check_high_score(stats, sc):
    # check if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('SpaceGame/highscore.txt', 'w') as file_object:
            file_object.write(str(stats.high_score))

def game_over(screen, stats, sc):
    # display game over
    # screen.fill((0, 0, 0))
    screen_rect = screen.get_rect()
    font = pygame.font.SysFont(None, 65)
    game_over_image = font.render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
    game_over_rect = game_over_image.get_rect()
    game_over_rect.center = screen_rect.center
    screen.blit(game_over_image, game_over_rect)
    # press any Key to Resrart
    font = pygame.font.SysFont(None, 42)
    restart_image = font.render('Press any Key to Restart', True, (255, 255, 255), (0, 0, 0))
    restart_rect = restart_image.get_rect()
    restart_rect.center = screen_rect.center
    restart_rect.y += 100
    screen.blit(restart_image, restart_rect)
    pygame.display.flip()
    stats.run_game = False
    # sys.exit()
    # pygame.quit()
    


