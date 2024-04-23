import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DELTa={
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(5,0)}
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    tmr = 0
    bk_img=pg.Surface((20,20))
    bk_img.set_colorkey((0,0,0))
    pg.draw.circle(bk_img,(255,0,0),(10,10),10)
    bk_rct=bk_img.get_rect()
    bk_rct.center=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    vx,vy=+5,-5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in DELTa.items():
            if key_lst[k]:
                sum_mv[0] +=v[0]
                sum_mv[1] +=v[1] 

        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()