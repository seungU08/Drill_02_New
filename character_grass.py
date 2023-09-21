from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')
while True:
    x = 400
    y = 90

    while (x < 800):
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(x,90)
          x = x + 2
          delay(0.01)

    

    while (y < 600): 
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(800,y)
          y = y + 2
          delay(0.01)

    x = 800
    y = 600

    while (x > 0):
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(x,600)
          x = x - 2
          delay(0.01)

    while (y > 90):
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(0,y)
          y = y - 2
          delay(0.01)
    x = 0
    while (x < 400):
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(x,90)
          x = x + 2
          delay(0.01)

    r = -math.pi/2
    while (r < 3*math.pi/2):
          clear_canvas_now()
          grass.draw_now(400 , 30)
          character.draw_now(400 + math.cos(r)*200,290 + math.sin(r)*200)
          r = r  + math.pi / 360
          delay(0.01)
    break


    
close_canvas()
