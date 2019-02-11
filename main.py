from display import *
from draw import *
import random

screen = new_screen()
color = [ 255, 255, 0 ]

def randy():
    ran = random.randint(0, 500)
    return ran

for x in range(0, 101):
    
    draw_line(randy(), randy(), randy(), randy(), screen, [randy() % 256, randy() % 256, randy() % 256])
    



display(screen)
save_extension(screen, 'img.png')
