from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]
draw_line( 0, 0, 250, 125, screen, color )
draw_line( 0, 0, 125, 250, screen, color )
draw_line( 0, 500, 250, 375, screen, color )
draw_line( 0, 500, 125, 250, screen, color )
draw_line( 500, 0, 250, 125, screen, color )
draw_line( 500, 0, 375, 250, screen, color )
draw_line( 500, 500, 250, 375, screen, color )
draw_line( 500, 500, 375, 250, screen, color )

draw_line( 0, 0, 200, 200, screen, color )
draw_line( 0, 500, 200, 300, screen, color )
draw_line( 500, 0, 300, 200, screen, color )
draw_line( 500, 500, 300, 300, screen, color )

draw_line( 200, 200, 200, 300, screen, color )
draw_line( 200, 300, 300, 300, screen, color )
draw_line( 300, 300, 300, 200, screen, color )
draw_line( 300, 200, 200, 200, screen, color )

draw_line( 125, 250, 200, 250, screen, color )
draw_line( 250, 125, 250, 200, screen, color )
draw_line( 375, 250, 300, 250, screen, color )
draw_line( 250, 375, 250, 300, screen, color )

display(screen)
save_extension(screen, 'img.png')
