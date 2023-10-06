from pygame import *


window = display.set_mode((700, 500))
display.set_caption('Догонялки')

background = transform.scale(image.load("background.png"), (700, 500))

x1 = 100
y1 = 300
x2 = 500
y2 = 300
player1 = transform.scale(image.load('sprite1.png'), (100,100))
player2 = transform.scale(image.load('sprite2.png'), (100,100))
step = 5
game = True
clock = time.Clock()
fps = 60
while game:
    window.blit(background, (0,0))
    window.blit(player1, (x1,y1))
    window.blit(player2, (x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_w] and y1 > 0:
        y1 -= step
    if key_pressed[K_s] and y1 < 400:
        y1 += step
    if key_pressed[K_a] and x1 > 0:
        x1 -= step
    if key_pressed[K_d] and x1 < 600:
        x1 += step
    if key_pressed[K_UP] and y2 > 0:
        y2 -= step
    if key_pressed[K_DOWN] and y2 < 400:
        y2 += step
    if key_pressed[K_LEFT] and x2 > 0:
        x2 -= step
    if key_pressed[K_RIGHT] and x2 < 600:
        x2 += step
    display.update()
    clock.tick(fps)
