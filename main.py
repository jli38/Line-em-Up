from display import *
from draw import *
from subprocess import Popen, PIPE
import random

screen = new_screen()
color = [ 255, 255, 0 ]

for i in range(0,500,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( i, 0, i, 500, screen, color)

for i in range(0,500,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, i, 500, i, screen, color)


######
for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, i, i, 0, screen, color)

for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, i, (i+random.randrange(100))*2, 0, screen, color)

for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, i, (i-random.randrange(100))*0.5 , 0, screen, color)

######
for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, 500-i, i, 500, screen, color)

for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
    draw_line( 0, 500-i, (i+random.randrange(100))*2, 500, screen, color)

for i in range(0,1000,100):
    color = [ (i+random.randrange(100)%256), (i+random.randrange(100))%256, (i+random.randrange(100))%256]
draw_line( 0, 500-i, (i-random.randrange(100))*0.5 , 500, screen, color)


display(screen)
save_extension(screen, 'img.png')
