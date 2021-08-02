import pygame
import sys
import numpy as np
import matplotlib.pyplot as plt


from brainFunctions import generateNoisyWave

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (8, 52, 99)
VIOLET = (115, 102, 189)
CYAN = (81, 244, 252)
FAINT_BLUE = (181, 226, 255)

NUM = 1
counter = 0

brainArr = []
brainArr.append(1)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600



pygame.display.set_caption('Brain Game')

GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

MAIN_CHARACTER = pygame.image.load('images/maincharacter.png')

ENEMY_CHARACTER = pygame.image.load('images/enemycharacter.png')

LARGE_MAIN_CHARACTER = pygame.image.load('images/maincharacterlarge.png')

LARGE_ENEMY_CHARACTER = pygame.image.load('images/enemycharacterlarge.png')

GAME_DISPLAY.fill(BACKGROUND_COLOR)

channels = 1
srate = 250




def main_character(x, y):
    GAME_DISPLAY.blit(MAIN_CHARACTER, (x,y))

def enemy_character(ex, ey):
    GAME_DISPLAY.blit(ENEMY_CHARACTER, (ex, ey))

def large_main_character(lx, ly):
    GAME_DISPLAY.blit(LARGE_MAIN_CHARACTER, (lx, ly))

def large_enemy_character(elx, ely):
    GAME_DISPLAY.blit(LARGE_ENEMY_CHARACTER, (elx, ely))

def firstOverlay():
    pygame.draw.line(GAME_DISPLAY, WHITE, (200, 0), (200, 320), 5)
    pygame.draw.line(GAME_DISPLAY, WHITE, (200, 500), (200, 600), 5)

    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Approach the enemy to engage & don\'t touch the walls!', True, WHITE, BACKGROUND_COLOR)

    textRect = text.get_rect()
    textRect.center = (2 * (DISPLAY_WIDTH / 3) - 40, DISPLAY_HEIGHT/6)

    GAME_DISPLAY.blit(text, textRect)

def secondOverlay():
     pygame.draw.line(GAME_DISPLAY, WHITE, (300, 0), (350, 300), 5)
     pygame.draw.line(GAME_DISPLAY, WHITE, (425, 300), (480, 600), 5)
     pygame.draw.line(GAME_DISPLAY, WHITE, (350, 300), (425,  300), 5)

     large_enemy_character(DISPLAY_WIDTH * -0.05, DISPLAY_HEIGHT * 0.25)
     large_main_character(DISPLAY_WIDTH * 0.5, DISPLAY_HEIGHT * 0.25)

     button("Fight", 340, 450, 100, 50, WHITE, VIOLET, "play")

def thirdOverlay():
    
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('To launch an attack mouse over the white square, to change focus (speed) click it!', True, WHITE, BACKGROUND_COLOR)

    textRect = text.get_rect()
    textRect.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3+25)

    GAME_DISPLAY.blit(text, textRect)

    #pygame.draw.line(GAME_DISPLAY, WHITE, (300, 0), (300, 100), 5)

    brain_button(50, 75, 100, 100, WHITE, CYAN)

    

def fourthOverlay():
    pygame.draw.rect(GAME_DISPLAY, CYAN, (200, 200, DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))
    
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render('You Win!', True, WHITE, BACKGROUND_COLOR)

    textRect = text.get_rect()
    textRect.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/5)

    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texte = fonte.render('Click the white square to see the brain data from your choices!', True, WHITE, BACKGROUND_COLOR)

    textRecte = texte.get_rect()
    textRecte.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/4 + 25)

    complex_brain_button(DISPLAY_WIDTH/2-75, DISPLAY_HEIGHT/2-75, 150, 150, FAINT_BLUE, WHITE)

    GAME_DISPLAY.blit(text, textRect)

    GAME_DISPLAY.blit(texte, textRecte)
    
def inrange(ix, iy, iex, iey):
    if (abs(iey - iy) <= 10) and (abs(iex - ix) <= 100):
        return True

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + 50 > mouse[1] > y:
        pygame.draw.rect(GAME_DISPLAY, ac, (x, y, w, h))
        if click[0] == True and action != None:
            
            if action == 'play':
                fight_loop()

            elif action == 'quit':
                pygame.quit()
                quit()
            
    else:
        pygame.draw.rect(GAME_DISPLAY, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    GAME_DISPLAY.blit(textSurf, textRect)

def brain_button(x, y, w, h, ic, ac):
    
    global NUM
    global brainArr
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + 100 > mouse[1] > y:
        pygame.draw.rect(GAME_DISPLAY, ac, (x, y, w, h))
        if click[0] == True:
            factor = input("Change your focus (speed)? (y/n)")
            if factor == 'n':
                multiple = 1
            elif factor == 'y':
                multiple = input("By what factor? E.g. 1, 2... ")
                multiple = int(multiple)
                if multiple > 5:
                    multiple == 5
                NUM = multiple
                
                
            else:
                multiple = 1
            if NUM != brainArr[len(brainArr) - 1]:
                    brainArr.append(NUM)
            times = np.linspace(0,1,srate) # One second at 250Hz
            y = generateNoisyWave(times, 3 * multiple, 10, 2)

            plt.plot(times, y)
            plt.show()
            
    else:
        pygame.draw.rect(GAME_DISPLAY, ic, (x, y, w, h))

def complex_brain_button(x, y, w, h, ic, ac):
    global brainArr
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + 100 > mouse[1] > y:
        pygame.draw.rect(GAME_DISPLAY, ac, (x, y, w, h))
        if click[0] == True:
            for i in brainArr:
                times = np.linspace(0,1,srate)
                freqs = i
                amps = 1

                wave = generateNoisyWave(times, freqs, amps, noise=0.5)
            

                plt.plot(times, wave)
                plt.show()
   
    else:
        pygame.draw.rect(GAME_DISPLAY, ic, (x, y, w, h))

def finale_loop():

    while True:
        GAME_DISPLAY.fill(BACKGROUND_COLOR)
        fourthOverlay()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        pygame.display.update()
        

def fight_loop(): 
    global counter

    X = (DISPLAY_WIDTH * 0.05)
    Y = (DISPLAY_HEIGHT * 0.15)
    EX = (DISPLAY_WIDTH * 0.5)
    EY = (DISPLAY_HEIGHT * 0.75)
    GAME_DISPLAY.fill(BACKGROUND_COLOR)
    
    flag = 0
    main_flag = 0
    
    while True:
        #brain_button(50, 75, 100, 100, WHITE, CYAN)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 50 < mouse[0] < 150 and 75 < mouse[1] < 175:
            main_flag = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        GAME_DISPLAY.fill(BACKGROUND_COLOR)
        thirdOverlay()
        
        
        if not inrange(X, Y, EX, EY):
            main_character(X, Y)
            enemy_character(EX, EY)

        if inrange(X, Y, EX, EY):
            counter += 1
            if counter > 3:
                finale_loop()

        if EX == 0 and flag == 0:
            flag = 1
        if EX == DISPLAY_WIDTH and flag == 1:
            flag = 0

        if EX > DISPLAY_WIDTH * 0 and flag == 0:
            EX -= 1
        elif EX < DISPLAY_WIDTH and flag == 1:
            EX += 1
            
        if main_flag == 0:
            X += 1 * NUM

        #Movement controls.
        if X >= DISPLAY_WIDTH * 0.8:
            main_flag = 1 

        if X <= DISPLAY_WIDTH * 0.2:
            main_flag = 0
        
        if main_flag == 1:
            X -= 1 * NUM
            
        if main_flag == 2 and Y <= DISPLAY_HEIGHT * 0.9:
            Y += 2 * NUM
        if Y >= DISPLAY_HEIGHT * 0.9:
            main_flag = 3
        if main_flag == 3 and Y > DISPLAY_HEIGHT * 0.2:
            Y -= 2 * NUM
        if main_flag == 3 and Y <= DISPLAY_HEIGHT * 0.2:
            main_flag = 1
        
        

        pygame.display.update()

def encounter_loop():
    
    GAME_DISPLAY.fill(BACKGROUND_COLOR)

    while True:
        secondOverlay()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def main_loop():
    
    x = (DISPLAY_WIDTH * 0.05)
    y = (DISPLAY_HEIGHT * 0.15)
    x_change = 0
    y_change = 0

    ex = (DISPLAY_WIDTH * 0.75)
    ey = (DISPLAY_HEIGHT * 0.75)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -1
                elif event.key == pygame.K_DOWN:
                    y_change = 1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                elif event.key == pygame.K_LEFT:
                    x_change = -1
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = 0

        GAME_DISPLAY.fill(BACKGROUND_COLOR)

        x += x_change
        y += y_change

        if inrange(x, y, ex, ey):
            encounter_loop()
        else:
            main_character(x, y)
            enemy_character(ex, ey)
            firstOverlay()

        if ey > DISPLAY_HEIGHT * 0.2 and ex == DISPLAY_WIDTH * 0.75:
            ey -= 0.5
        elif ex > DISPLAY_WIDTH * 0.4 and ey == DISPLAY_HEIGHT * 0.2:
            ex -= 0.5
        elif ey < DISPLAY_HEIGHT * 0.8 and ex == DISPLAY_WIDTH * 0.4: 
            ey += 0.5
        elif ex <= DISPLAY_WIDTH * 0.75 and ey == DISPLAY_HEIGHT * 0.8:
            ex += 0.5

        

        if (x == 200 and y > 430) or (x == 200 and y < 320): #Collision controls.
            pygame.quit()
            quit()

        if x > DISPLAY_WIDTH - 100:
            x = DISPLAY_WIDTH - 100
    
        if x < 0:
            x = 0

        if y > DISPLAY_HEIGHT - 100:
            y = DISPLAY_HEIGHT - 100
    
        if y < 0:
            y = 0

        
        pygame.display.update()



main_loop()