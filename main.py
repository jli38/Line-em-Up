from display import *
from draw import *
import random

screen = new_screen()
color = [ 255, 255, 0 ]


draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 500) % 256, random.randint(0, 500) % 256, random.randint(0, 500) % 256])
draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 500) % 256, random.randint(0, 500) % 256, random.randint(0, 500) % 256])
draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 500) % 256, random.randint(0, 500) % 256, random.randint(0, 500) % 256])
draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 500) % 256, random.randint(0, 500) % 256, random.randint(0, 500) % 256])
draw_line(random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), screen, [random.randint(0, 500) % 256, random.randint(0, 500) % 256, random.randint(0, 500) % 256])


display(screen)
save_extension(screen, 'img.png')
