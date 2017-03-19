'''
saiful fun game
'''
import pygame

from pygame import *

pygame.init()

pygame.mixer.init()
sounda = pygame.mixer.Sound("birdsound.wav")

green = (0,128,0)

xmax = 960
ymax = 640
screen = pygame.display.set_mode((xmax,ymax))

clock = pygame.time.Clock()

background = pygame.image.load('factoryfromtop3.png')
background = pygame.transform.scale(background, (960, 640))

ball1 = pygame.image.load('bird1.png').convert()
ball1 = pygame.transform.scale(ball1, (60, 40))
ball1.set_colorkey((255,255,255))
xball1 = ball1.get_height()
yball1 = ball1.get_width()

ball2 = pygame.image.load('bird2.png').convert()
ball2 = pygame.transform.scale(ball2, (60, 40))
ball2.set_colorkey((255,255,255))
xball2 = ball2.get_height()
yball2 = ball2.get_width()

ball3 = pygame.image.load('bird3.png').convert()
ball3 = pygame.transform.scale(ball3, (60, 40))
ball3.set_colorkey((255,255,255))
xball3 = ball3.get_height()
yball3 = ball3.get_width()



# [ x, y, step_x, step_y, height, width, surface, rect]

ball1_list = [100,200,1,1, xball1, yball1, ball1, pygame.Rect((100,200),(xball1,yball1))]
ball2_list = [100,200,1,1, xball2, yball2, ball2, pygame.Rect((100,200),(xball2,yball2))]
ball3_list = [100,200,1,1, xball3, yball3, ball3, pygame.Rect((100,200),(xball3,yball3))]

n = 1

n_ball = 1
tp_ball = 1
level = 1
t = 2000
seconds = 0
points = 0


#------- FUNZIONI ---------------------------
def one_num_to_str(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '3'
    elif n == 4:
        return '4'
    elif n == 5:
        return '5'
    elif n == 6:
        return '6'
    elif n == 7:
        return '7'
    elif n == 8:
        return '8'
    elif n == 9:
        return '9'

def int_to_str(n):
    a = one_num_to_str(n/1000) + one_num_to_str((n/100)%10) + one_num_to_str((n/10)%10) + one_num_to_str(n%10)
    return a

def show_level(level):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('level: ' + int_to_str(level), 1, (10,10,10))
    text_pos = text.get_rect(centerx = screen.get_width()/2)
    screen.blit(text, text_pos)

def show_time(seconds):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('time: ' + int_to_str(seconds), 1, (10,10,10))
    screen.blit(text, (0, 0))

def show_points(points):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('points: ' + int_to_str(points), 1, (10,10,10))
    screen.blit(text, ((xmax-155),0))


# -------------------------------------------

pygame.time.set_timer(USEREVENT, t)  # incremento livelli

pygame.time.set_timer(USEREVENT + 1, 1000)  # tempo in secondi

screen.blit(background, (0, 0))
birds = []
birds.append(screen.blit(ball1, ((330 + n), (140 + n / 3))))
birds.append(screen.blit(ball1, ((390 + n), (300 + n / 3))))
birds.append(screen.blit(ball2, ((480 + n), (140 + n / 3))))
birds.append(screen.blit(ball2, ((630 + n), (300 + n / 3))))
birds.append(screen.blit(ball3, ((300 + n), (390 + n / 3))))
birds.append(screen.blit(ball3, ((550 + n), (490 + n / 3))))

counter = 0

while 1:

    ev = pygame.event.get()

    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print pos

            for i in range(0,len(birds)):
                if birds[i].collidepoint(pos):
                    points += 1
                    pygame.draw.rect(screen, green,birds[i] )
                    screen.blit(background, (birds[i].x, birds[i].y), pygame.Rect(birds[i].x, birds[i].y, 60, 40))
                    sounda.play()
                    pygame.display.update()

    show_level(level)

    show_time(seconds)

    show_points(points)
    pygame.display.flip()

    pygame.time.wait(1)
