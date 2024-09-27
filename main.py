import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((750, 500))
finish = pygame.Rect(730, 0, 60, 500)

def reset_game():
    global rect, enemy, enemy2, enemy3, enemy_y_pos, enemy_y_posTwo, enemy_y_posThree, going_down, going_downTwo, going_downThree
    rect = pygame.Rect(50, 50, 50, 50)
    enemy = pygame.Rect(375, 0, 60, 60)
    enemy2 = pygame.Rect(200, 440, 60, 60)
    enemy3 = pygame.Rect(550, 220, 60, 60)
    enemy_y_pos = enemy.y
    enemy_y_posTwo = enemy2.y
    enemy_y_posThree = enemy3.y
    going_down = True
    going_downTwo = True
    going_downThree = True

def finishgame():
    screen.fill((0, 0, 0))
    f1 = pygame.font.Font(None, 54)
    text1 = f1.render('WIN', 1, (255, 255, 255))
    text2 = f1.render('До выхода : 3 секунды...', 1, (255, 255, 255))
    screen.blit(text1, (355, 250))
    screen.blit(text2, (255, 300))
    pygame.display.update()
    pygame.time.wait(3000)
    exit()
reset_game()

while True:
    if going_down:
        enemy_y_pos += 4.25
        if enemy_y_pos >= 440:
            going_down = False
    else:
        enemy_y_pos -= 4.25
        if enemy_y_pos <= 0:
            going_down = True
    if going_downTwo:
        enemy_y_posTwo += 4.25
        if enemy_y_posTwo >= 440:
            going_downTwo = False
    else:
        enemy_y_posTwo -= 4.25
        if enemy_y_posTwo <= 0:
            going_downTwo = True
    if going_downThree:
        enemy_y_posThree += 4.25
        if enemy_y_posThree >= 440:
            going_downThree = False
    else:
        enemy_y_posThree -= 4.25
        if enemy_y_posThree <= 0:
            going_downThree = True

    enemy.y = enemy_y_pos
    enemy2.y = enemy_y_posTwo
    enemy3.y = enemy_y_posThree

    if rect.colliderect(enemy) or rect.colliderect(enemy2) or rect.colliderect(enemy3):
        reset_game()

    if rect.colliderect(finish):
        finishgame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)

    pygame.time.wait(15)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), rect, 0)
    pygame.draw.rect(screen, (255, 0, 0), enemy, 10)
    pygame.draw.rect(screen, (255, 0, 0), enemy2, 5)
    pygame.draw.rect(screen, (255, 0, 0), enemy3, 0)
    pygame.draw.rect(screen, (0, 255, 0), finish, 0)
    pygame.display.flip()
