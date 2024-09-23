from pico2d import *
import math

open_canvas()
hide_lattice()

grass = load_image('grass.png')
character = load_image('character.png')


x=400
y=30
n =0
c0=270
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    
    character.draw_now(x,y)
    if n==0:
        x+=2
        if x>=800:
            n=1
    elif n==1:
        x-=2
        y=y+2*math.sin(60/360*2*math.pi)
        if x<400:
            n=2
    elif n==2:
        x-=2
        y=y-2*math.sin(60/360*2*math.pi)
        if x<0:
            n=3
    elif n==3:
        x+=2
        if x>400:
            n=4
    elif n==4:
        c0+=1;
        x=400+300*math.cos(c0/360*2*math.pi)
        y=330+300*math.sin(c0/360*2*math.pi)
        
        if c0==270+360:
            c0=270
            n=0

    
    delay(0.01)


