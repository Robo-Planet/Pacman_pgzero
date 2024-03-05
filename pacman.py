import pygame
import random
import time

WIDTH = 800
HEIGHT = 600
BACKGROUND_IMG = 'house_small'

#pygame.mixer.init(22100,-16,2,64)#decrease buffer size

player = Actor('pacman' + "-right-1")
player.pos = 150,100
image_number = 1
#sounds.ghosthouse.play()
delay_timer = 0

score  = 0
game_timer = 10
game_timer_start = 10
timer_loss = 0.2

music.play('ghosthouse.wav')
ghosts_number = 1

ghosts = []
ghosts.append(Actor('ghost_' + str(random.randint(1,4)), pos = (random.randint(0,WIDTH), random.randint(0, HEIGHT))))


def ghost_list_adder():
    if len(ghosts) < ghosts_number:
        ghosts.append(Actor('ghost_' + str(random.randint(1,4)), pos = (random.randint(0,WIDTH), random.randint(0, HEIGHT))))


def create_ghost():
    for i in range(ghosts_number):
        clock.schedule(ghost_list_adder, i)

def player_move():
    global delay_timer, image_number
    if (delay_timer == 5):
        delay_timer = 0
        direction = 'none'

        if (keyboard.up):
            if (player.y > 40):
                player.y -= 20
                direction = 'rear'
        if (keyboard.down):
            if (player.y <560):
                player.y += 20
                direction = 'front'
        if (keyboard.left):
            if (player.x > 40):
                player.x -= 20
                direction = 'left'
        if (keyboard.right):
            if (player.x < 760):
                player.x += 20
                direction = 'right'
        if (direction != 'none'):
            image_number += 1
            sounds.pacman_move.play()

            if (image_number > 4):
                image_number = 1
            player.image = ('pacman' + '-' + direction + '-' + str(image_number))

    else:
        delay_timer += 1




def draw():
    global game_over
    screen.blit(BACKGROUND_IMG,(0,0))
    for ghost in ghosts:
            ghost.draw()
    if (game_timer < 1):
        screen.draw.text("Game Over\nScore " +str(score), fontsize=90, center=(400,300), shadow=(1,1), color=(255,0,0),scolor="#202020")
    player.draw()

    screen.draw.text("Time left:", fontsize=30, center=(50,540), color=(255,255,255))
    screen.draw.text(str(int(game_timer)), fontsize=60, center=(50,575), color = (255,255,255))
    screen.draw.text("Points:", fontsize=30, center=(750,540), color=(255,255,255))
    screen.draw.text(str(score), fontsize=60, center=(750,575), color=(255,255,255))


music.play('ghosthouse.wav')
def update():
    global ghosts_number, score, game_timer
    if (game_timer < 1):
        return
    else:
        game_timer -= 0.017
        player_move()
        for ghost in ghosts:
            if player.colliderect(ghost):
                score += 1
                ghosts_number -= 1
                ghosts.remove(ghost)
                if (score/5).is_integer():
                    ghosts_number += 2
                else:
                    ghosts_number += 1
                create_ghost()
                game_timer = game_timer_start - (score * 0.2)