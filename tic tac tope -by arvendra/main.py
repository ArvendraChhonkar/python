import pygame, sys
from pygame.locals import *
from pygame import *
import time

#global variable
GAME_SPRITE = {}
FPS = 30
SCREENWIDTH = 400
SCREENHEIGHT = 400
b1 = 'E'
b2 = 'E'
b3 = 'E'
b21 = 'E'
b22 = 'E'
b23 = 'E'
b31 = 'E'
b32 = 'E'
b33 = 'E'
sel = True



SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

GAME_SPRITE['1'] = pygame.image.load('1.png').convert_alpha()
GAME_SPRITE['0'] = pygame.image.load('0.png').convert_alpha()

GAME_SPRITE['p1'] = pygame.image.load('player1.png').convert_alpha()
GAME_SPRITE['p0'] = pygame.image.load('palyer0.png').convert_alpha()

GAME_SPRITE['E'] = pygame.image.load('E.png').convert_alpha()


def all():
    global b1,b2,b3,b21,b22,b23,b31,b32,b33,sel
    while True:
        if (b1 == '1' and b2 == '1' and b3 == '1') or (b21 == '1' and b22 == '1' and b23 == '1') or (b31 == '1' and b32 == '1' and b33 == '1') or (b1 == '1' and b21 == '1' and b31 == '1')  or (b2 == '1' and b22 == '1' and b32 == '1') or (b3 == '1' and b23 == '1' and b33 == '1') or (b1 == '1' and b22 == '1' and b33 == '1') or (b3 == '1' and b22 == '1' and b31 == '1'):
            print("player One wone")
            SCREEN.blit(GAME_SPRITE['p1'],(10,10))
            pygame.display.update()
            time.sleep(2)
            b1 = 'E'
            b2 = 'E'
            b3 = 'E'
            b21 = 'E'
            b22 = 'E'
            b23 = 'E'
            b31 = 'E'
            b32 = 'E'
            b33 = 'E'
            sel = True

        
        if (b1 == '0' and b2 == '0' and b3 == '0') or (b21 == '0' and b22 == '0' and b23 == '0') or (b31 == '0' and b32 == '0' and b33 == '0') or (b1 == '0' and b21 == '0' and b31 == '0')  or (b2 == '0' and b22 == '0' and b32 == '0') or (b3 == '0' and b23 == '0' and b33 == '0') or (b1 == '0' and b22 == '0' and b33 == '0') or (b3 == '0' and b22 == '0' and b31 == '0'):
            print("player Zero wone")
            SCREEN.blit(GAME_SPRITE['p0'],(10,10))
            pygame.display.update()
            time.sleep(2)
            b1 = 'E'
            b2 = 'E'
            b3 = 'E'
            b21 = 'E'
            b22 = 'E'
            b23 = 'E'
            b31 = 'E'
            b32 = 'E'
            b33 = 'E'
            sel = True
        else:
            pass
        xm,ym = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT or(event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()  
            #1 row
            if (xm > 10 and ym > 10 and xm < 110 and ym < 110 and event.type == MOUSEBUTTONDOWN and b1 == 'E'):
                b1 = str(int(sel))
                sel = not(sel)
            if (xm > 120 and ym > 10 and xm < 220 and ym < 110 and event.type == MOUSEBUTTONDOWN and b2 == 'E'):
                b2 = str(int(sel))
                sel = not(sel)
            if (xm > 230 and ym > 10 and xm < 330 and ym < 110 and event.type == MOUSEBUTTONDOWN and b3 == 'E'):
                b3 = str(int(sel))
                sel = not(sel)

            #2 row 
            if (xm > 10 and ym > 120 and xm < 100 and ym < 220 and event.type == MOUSEBUTTONDOWN and b21 == 'E'):
                b21 = str(int(sel))
                sel = not(sel)
            if (xm > 120 and ym > 120 and xm < 220 and ym < 220 and event.type == MOUSEBUTTONDOWN and b22 == 'E'):
                b22 = str(int(sel))
                sel = not(sel)
            if (xm > 230 and ym > 120 and xm < 330 and ym < 220 and event.type == MOUSEBUTTONDOWN and b23 == 'E'):
                b23 = str(int(sel))
                sel = not(sel)
            #3 row
            if (xm > 10 and ym > 230 and xm < 100 and ym < 330 and event.type == MOUSEBUTTONDOWN and b31 == 'E'):
                b31 = str(int(sel))
                sel = not(sel)
            if (xm > 120 and ym > 230 and xm < 220 and ym < 330 and event.type == MOUSEBUTTONDOWN and b32 == 'E'):
                b32 = str(int(sel))
                sel = not(sel)
            if (xm > 230 and ym > 230 and xm < 330 and ym < 330 and event.type == MOUSEBUTTONDOWN and b33 == 'E'):
                b33 = str(int(sel))
                sel = not(sel)

            if (xm > 340 and ym > 10 and xm < 440 and ym < 110 and event.type == MOUSEBUTTONDOWN):
                b1 = 'E'
                b2 = 'E'
                b3 = 'E'
                b21 = 'E'
                b22 = 'E'
                b23 = 'E'
                b31 = 'E'
                b32 = 'E'
                b33 = 'E'
                sel = True


            else:
                SCREEN.blit(GAME_SPRITE[b1],(10, 10))
                SCREEN.blit(GAME_SPRITE[b2],(120,10))
                SCREEN.blit(GAME_SPRITE[b3],(230,10))

                SCREEN.blit(GAME_SPRITE[b21],(10, 120))
                SCREEN.blit(GAME_SPRITE[b22],(120,120))
                SCREEN.blit(GAME_SPRITE[b23],(230,120))
                
                SCREEN.blit(GAME_SPRITE[b31],(10, 230))
                SCREEN.blit(GAME_SPRITE[b32],(120,230))
                SCREEN.blit(GAME_SPRITE[b33],(230,230))

                SCREEN.blit(GAME_SPRITE['E'],(340,10))

                pygame.display.update()
                FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    #MAIN FUNCTION
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('TIC TAC TOE')
    while True:
        all()