import os
import sys
import pygame as pg
import random
import time


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DELTa={ # 移動量辞書（押下キー：移動量タプル）
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(5,0)}

def check_bound(obj_rct:pg.Rect) -> tuple[bool, bool]:
    """
    こうかとんRect，または，爆弾Rectの画面内外判定用の関数
    引数：こうかとんRect，または，爆弾Rect
    戻り値：横方向判定結果，縦方向判定結果（True：画面内／False：画面外）
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right: 
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate



def rote_bir(kk_dir:list) -> list[bool, bool]:
    dir=0
    """
    移動方向からこうかとんの向いている方向を決定する関数
    引数：移動する値のリスト
    戻り値：角度8方向のうちのひとつ
    """
    
    dir_lst = [0, 45, 90, 135, 180, 225, 270, 315]#360/8の倍数

    if kk_dir[0]==-5 and kk_dir[1]==0:
        dir = 0
    if kk_dir[0]==-5 and kk_dir[1]==5:
        dir = 1
    if kk_dir[0]==0 and kk_dir[1]==5:
        dir = 2
    if kk_dir[0]==5 and kk_dir[1]==5:
        dir = 3
    if kk_dir[0]==5 and kk_dir[1]==0:
        dir = 4
    if kk_dir[0]==5 and kk_dir[1]==-5:
        dir = 5
    if kk_dir[0]==0 and kk_dir[1]==-5:
        dir = 6
    if kk_dir[0]==-5 and kk_dir[1]==-5:
        dir = 7
    
    return dir_lst[dir]

def big_bomb(screen):
    """
    時間とともに爆弾を10段階程度で拡大，加速させる関数
    引数：screen
    戻り値　拡大率と加速度のリストのタプル
    """
    accs = [a for a in range(1, 11)]
    for r in range(1, 11):
        bb_img = pg.Surface((20*r, 20*r))
    pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
    avx = vx*bb_accs[min(tmr//500, 9)]
    bb_img = bb_imgs[min(tmr//500, 9)]
    print("時間切れ")


def follow_bomb(screen):
    """
    爆弾から見てこうかとんRectがある方に向かせ、条件で追尾させるようにする関数
   
    上記の条件を満たす関数
    引数：screen
    戻り値　上記の条件を満たす爆弾の速度ベクトル（タプル）
    """
    print("時間切れ")
    

def GameOver(screen):
    """
    こうかとんに爆弾が着弾した際に，画面をブラックアウトし，
    泣いているこうかとんの画像と「Game Over」の文字列を
    5秒間表示させる関数
    引数：screen
    なお評価の観点のため追記：
    この関数において鳥の画像と「Game Over」の文字列の位置に指定はない。
    """
    #ゲームオーバー背景の設定
    back_GO=pg.Surface((WIDTH, HEIGHT))
    pg.draw.rect(back_GO, (0, 0, 0), (0,0,1600,900), width=0)
    back_GO.set_alpha(70)
    font_GO=pg.font.Font(None,80)
    txt_GO=font_GO.render("Game Over",True,(255,255,255))
    sadbird_img=(pg.image.load("fig/8.png"))
    screen.blit(back_GO,[0,0])
    screen.blit(txt_GO, [WIDTH/2, HEIGHT/2]) 
    screen.blit(sadbird_img, [WIDTH/4, HEIGHT/2]) 
    screen.blit(sadbird_img, [WIDTH*3/4, HEIGHT/2]) 

    pg.display.update()
    time.sleep(5)
    return




def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    
     # ここからこうかとんの設定
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bg_img = pg.image.load("fig/pg_bg.jpg") 
    kk_direct = 0   
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), kk_direct, 2.0)

    clock = pg.time.Clock()
    tmr = 0
    # ここから爆弾の設定
    bk_img=pg.Surface((20,20))
    bk_img.set_colorkey((0,0,0))
    pg.draw.circle(bk_img,(255,0,0),(10,10),10)
    bk_rct=bk_img.get_rect()
    bk_rct.center=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    vx=+5
    vy=-5
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bk_rct):  # こうかとんと爆弾がぶつかったら
            GameOver(screen)
            
            return
            
        screen.blit(bg_img, [0, 0]) 
         # こうかとんの移動と表示
         
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in DELTa.items():
            if key_lst[k]:
                sum_mv[0] +=v[0]
                sum_mv[1] +=v[1] 

        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        kk_direct = rote_bir(sum_mv)  # 方向を決める
        kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), kk_direct, 2.0)
        screen.blit(kk_img, kk_rct)
        # 爆弾の移動と表示
        big_bomb(screen)
        bk_rct.move_ip(vx,vy)
        screen.blit(bk_img,bk_rct)
        yoko, tate = check_bound(bk_rct)
        if not yoko:  # 横方向にはみ出てたら
            vx *= -1
        if not tate:  # 縦方向にはみ出てたら
            vy *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
