import pygame , sys
from pygame.locals import *
from pygame import *
import time
FPS = 30
GAME_SPRITE = {}

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

SCREEN = pygame.display.set_mode((350,450))
GAME_SPRITE['1'] = pygame.image.load('1.png').convert_alpha()
GAME_SPRITE['0'] = pygame.image.load('0.png').convert_alpha()
GAME_SPRITE['E'] = pygame.image.load('E.png').convert_alpha()
GAME_SPRITE['p1'] = pygame.image.load('player1.png').convert_alpha()
GAME_SPRITE['p0'] = pygame.image.load('palyer0.png').convert_alpha()

GAME_SPRITE['bkg'] = pygame.image.load('bkg.png').convert_alpha()

GAME_SPRITE['re'] = pygame.image.load('re.png').convert_alpha()


def main():
    global b1,b2,b3,b21,b22,b23,b31,b32,b33,sel
    while True:
        if (b1 == '1' and b2 == '1' and b3 == '1') or (b21 == '1' and b22 == '1' and b23 == '1') or (b31 == '1' and b32 == '1' and b33 == '1') or (b1 == '1' and b21 == '1' and b31 == '1')  or (b2 == '1' and b22 == '1' and b32 == '1') or (b3 == '1' and b23 == '1' and b33 == '1') or (b1 == '1' and b22 == '1' and b33 == '1') or (b3 == '1' and b22 == '1' and b31 == '1'):
            SCREEN.blit(GAME_SPRITE['p1'],(10,340))
            pygame.display.update()
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
            time.sleep(3)
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
            SCREEN.blit(GAME_SPRITE['p0'],(10,340))
            pygame.display.update()
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
            time.sleep(3)
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


            
        x,y = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (b1 == 'E' and x > 10 and y > 10 and x < 110 and y < 110 and event.type == MOUSEBUTTONDOWN):
                b1 = str(int(sel))
                sel = not(sel)
            if (b2 == 'E' and x > 120 and y > 10 and x < 220 and y < 110 and event.type == MOUSEBUTTONDOWN):
                b2 = str(int(sel))
                sel = not(sel)
            if (b3 == 'E' and x > 230 and y > 10 and x < 330 and y < 110 and event.type == MOUSEBUTTONDOWN):
                b3 = str(int(sel))
                sel = not(sel)
            
            if (b21 == 'E' and x > 10 and y > 120 and x < 110 and y < 220 and event.type == MOUSEBUTTONDOWN):
                b21 = str(int(sel))
                sel = not(sel)
            if (b22 == 'E' and x > 120 and y > 120 and x < 220 and y < 220 and event.type == MOUSEBUTTONDOWN):
                b22 = str(int(sel))
                sel = not(sel)
            if (b23 == 'E' and x > 230 and y > 120 and x < 330 and y < 220 and event.type == MOUSEBUTTONDOWN):
                b23 = str(int(sel))
                sel = not(sel)
            
            if (b31 == 'E' and x > 10 and y > 230 and x < 110 and y < 330 and event.type == MOUSEBUTTONDOWN):
                b31 = str(int(sel))
                sel = not(sel)
            if (b32 == 'E' and x > 120 and y > 230 and x < 220 and y < 330 and event.type == MOUSEBUTTONDOWN):
                b32 = str(int(sel))
                sel = not(sel)
            if (b33 == 'E' and x > 230 and y > 230 and x < 330 and y < 330 and event.type == MOUSEBUTTONDOWN):
                b33 = str(int(sel))
                sel = not(sel)
            if (x > 230 and y > 340 and x < 330 and y < 440 and event.type == MOUSEBUTTONDOWN):
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
                SCREEN.blit(GAME_SPRITE['bkg'],(0, 0))
            
                SCREEN.blit(GAME_SPRITE[b1],(10, 10))
                SCREEN.blit(GAME_SPRITE[b2],(120, 10))
                SCREEN.blit(GAME_SPRITE[b3],(230, 10))
                
                SCREEN.blit(GAME_SPRITE[b21],(10, 120))
                SCREEN.blit(GAME_SPRITE[b22],(120, 120))
                SCREEN.blit(GAME_SPRITE[b23],(230, 120))
                
                SCREEN.blit(GAME_SPRITE[b31],(10, 230))
                SCREEN.blit(GAME_SPRITE[b32],(120, 230))
                SCREEN.blit(GAME_SPRITE[b33],(230, 230))

                SCREEN.blit(GAME_SPRITE['re'],(230, 340))
                pygame.display.update()
                
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("My game")
    #FPSCLOCK = pygame.time.clock()
    while True:
        main()
