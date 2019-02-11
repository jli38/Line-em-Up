from display import *
from draw import *
import random

screen = new_screen()
color = [ 255, 255, 0 ]

ran = random.randint(0, 255)

draw_line(ran, ran, ran, ran, screen, [ran, ran, ran])
draw_line(ran, ran, ran, ran, screen, [ran, ran, ran])
draw_line(ran, ran, ran, ran, screen, [ran, ran, ran])
draw_line(ran, ran, ran, ran, screen, [ran, ran, ran])
draw_line(ran, ran, ran, ran, screen, [ran, ran, ran])



display(screen)
save_extension(screen, 'img.png')
