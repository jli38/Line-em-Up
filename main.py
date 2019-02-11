from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 0 ]


# Q1
draw_line(0, 0, 250, 0, screen, color)
draw_line(0, 0, 250, 250, screen, color)
draw_line(0, 0, 250, 100, screen, color)

# Q2
draw_line(0, 0, 0, 250, screen, color)
draw_line(0, 0, 250, 350, screen, color)

# Q3
draw_line(-250, 350, 0, 0, screen, color)

# Q4
draw_line(-250, 0, 0, 0, screen, color)
draw_line(-250, 250, 0, 0, screen, color)
draw_line(-250, 100, 0, 0, screen, color)

# Q5
draw_line(-250, -100, 0, 0, screen, color)
draw_line(-250, -250, 0, 0, screen, color)

# Q6
draw_line(-250, -350, 0, 0, screen, color)
draw_line(0, -250, 0, 0, screen, color)

# Q7 
draw_line(0, 0, 250, 350, screen, color)

# Q8
draw_line(0, 0, 250, -250, screen, color)
draw_line(0, 0, 250, -100, screen, color)


display(screen)
save_extension(screen, 'img.png')
