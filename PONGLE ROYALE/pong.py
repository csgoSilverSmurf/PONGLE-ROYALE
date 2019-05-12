#***********************************
#Author: Collin
#Date: 29/04/2019
#Title: pong sudo code
#Discription: pseudo code
#***********************************

#import
import pygame
import random
import time
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()


#resolution
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720

#display and caption
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("PONG - Collin,G")

#colors
WHITE = (255,255,255)
GRAY = (185,185,185)
BLACK = (0,0,0)
RED2 = (255, 0, 0)
RED = (150, 0, 0)
GREEN2 = (0, 255, 0)
GREEN = (0, 200, 0)
YELLOW2 = (255, 255, 0)
YELLOW = (230, 230, 0)
ORANGE = (255,64,64)
CYAN = (0,149,139)
GOLD = (255,185,15)
PURPLE = (128,0,128)
VIOLET = (238,130,238)
TAN = (255,165,79)
PALEGREEN = (152,251,154)
CADETBLUE = (95,158,160)

#color list
colors = [WHITE,PURPLE,CYAN,RED,GREEN,YELLOW,ORANGE,GOLD,VIOLET,TAN,PALEGREEN,CADETBLUE]
#score
player1_score = int()
player2_score = int()

#color list
color = colors[random.randint(0,len(colors)-1)]
clock = pygame.time.Clock()

#player paddles
paddle1 = pygame.image.load('player#1.png')
paddle2 = pygame.image.load('player#2.png')

#key images for HOW TO PLAY section
wKey = pygame.image.load('w.jpg')
sKey = pygame.image.load('s.jpg')
downKey = pygame.image.load('down.jpg')
upKey = pygame.image.load('up.jpg')
#demensions of paddles
paddle1_WIDTH = 20
paddle1_HEIGHT = 140
paddle2_WIDTH = 20
paddle2_HEIGHT = 140
#mouse
mouseClick = pygame.mouse.get_pressed()
mousePos = pygame.mouse.get_pos()
#music
pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.set_volume(3)
#loop music
pygame.mixer.music.play(-1)

            
#blue pladdle
def player1(x1,y1):
    gameDisplay.blit(paddle1,(x1,y1))

#red paddle
def player2(x2,y2):
    gameDisplay.blit(paddle2,(x2,y2))

def w(x,y):
    gameDisplay.blit(wKey,(x,y))
    
def s(x,y):
    gameDisplay.blit(sKey,(x,y))

def down(x,y):
    gameDisplay.blit(downKey,(x,y))

def up(x,y):
    gameDisplay.blit(upKey,(x,y))

def ball(ballStartX,ballStartY,ballRadius,color):
    pygame.draw.circle(gameDisplay,BLACK,(int(ballStartX), int(ballStartY)), int(ballRadius))

def textObjects(text,font):
    #black font
    textSurface = font.render(text,True,BLACK)
    return textSurface,textSurface.get_rect()

#this function is for when red OR bluewins
def messageDisplay(text):
    #font size and font type
    largeText = pygame.font.Font("freesansbold.ttf",115)
    textSurf,textRect = textObjects(text,largeText)
    textRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    pygame.time.wait(1000)
    #restarts the match when either player wins
    mainLoop()

#red wins 
def pauseRed():
    #use messageDisplay function
    messageDisplay('Red Won')
    pygame.time.wait(1000)

#blue wins
def pauseBlue():
    messageDisplay('Blue Won')
    pygame.time.wait(1000)

#red score
def score1(count1):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Red: " + str(count1), True, BLACK)
    gameDisplay.blit(text,(150,0))

#blue score
def score2(count2):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Blue: " + str(count2), True, BLACK)
    gameDisplay.blit(text,(DISPLAY_WIDTH-200,0))
    
#main menu
def mainMenu():
    menu = True
    #ball bouncing around in menu for cosmetic purposes
    ballStartX = 620
    ballStartY = 300
    ballSpeedX = 8
    ballSpeedY = 12
    ballRadius = 10
    #white background will change later on
    gameDisplay.fill(WHITE)
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()

        #menu title
        largeText = pygame.font.Font("freesansbold.ttf",90)
        textSurf,textRect = textObjects("Pongle Royale!",largeText)
        textRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
        gameDisplay.blit(textSurf,textRect)

        largeText = pygame.font.Font("freesansbold.ttf",25)
        textSurf,textRect = textObjects("By Collin Guo",largeText)
        textRect.center = (620,620)
        gameDisplay.blit(textSurf,textRect)

        #main rects for buttons
        pygame.draw.rect(gameDisplay, GREEN, (123,450,200,75))
        pygame.draw.rect(gameDisplay, YELLOW, (536,450,200,75))
        pygame.draw.rect(gameDisplay, RED, (934, 450, 200,75))

        #black outlines
        pygame.draw.rect(gameDisplay, BLACK, [123,450,200,75],4)
        pygame.draw.rect(gameDisplay, BLACK, [536,450,200,75],4)
        pygame.draw.rect(gameDisplay, BLACK, [934,450,200,75],4)

        #change color if mouse glides over
        if 123+200 > mousePos[0] > 123 and 450+75 > mousePos[1] > 450:
            pygame.draw.rect(gameDisplay,GREEN2,(123,450,200,75))
            pygame.draw.rect(gameDisplay, BLACK, [123,450,200,75],4)

            #if clicked, a function is called
            if mouseClick[0] == 1:
                mainLoop()

        if 536+200 > mousePos[0] > 536 and 450+75 > mousePos[1] > 450:
            #rectangle becomes a light shade of green when the mouse is over the rectangle
            pygame.draw.rect(gameDisplay,GREEN2,(536,450,200,75))
            pygame.draw.rect(gameDisplay, BLACK, [536,450,200,75],4)
            if mouseClick[0] == 1:
                    instructions()

        if 934+200 > mousePos[0] > 934 and 450+75 > mousePos[1] > 450:
            pygame.draw.rect(gameDisplay,GREEN2,(934,450,200,75))
            pygame.draw.rect(gameDisplay, BLACK, [934,450,200,75],4)
            if mouseClick[0] == 1:
                quit()

        #button lables
        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("PLAY", largeText)
        textRect.center = (220, 485)
        gameDisplay.blit(textSurf, textRect)

        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("HOW TO PLAY", largeText)
        textRect.center = (635, 485)
        gameDisplay.blit(textSurf, textRect)

        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("QUIT", largeText)
        textRect.center = (1035, 485)
        gameDisplay.blit(textSurf, textRect)
        
        pygame.draw.circle(gameDisplay,BLACK,(ballStartX,ballStartY),ballRadius)

        #ball changes random color in list when it hits a wall
        if ballStartY >= DISPLAY_HEIGHT - ballRadius or ballStartY <= 0:
            color = colors[random.randint(0,len(colors)-1)]
            gameDisplay.fill(color)
            #ball also gets reflected
            ballSpeedY *= -1
           
            
        if ballStartX >= DISPLAY_WIDTH - ballRadius or ballStartX <= 0:
            color = colors[random.randint(0,len(colors)-1)]
            gameDisplay.fill(color)
            ballSpeedX *= -1
            
            

        ballStartX += ballSpeedX
        ballStartY += ballSpeedY
        
        pygame.display.update()
        clock.tick(60)

def instructions():
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(color)

        mouseClick = pygame.mouse.get_pressed()
        mousePos = pygame.mouse.get_pos()
        
        #instruction images
        w(350,100)
        s(350,400)
        up(650,100)
        down(650,400)

        #instruction text
        largeText = pygame.font.Font("freesansbold.ttf", 25) #font size
        textSurf, textRect = textObjects("Red Player (Left)", largeText) #content
        textRect.center = (450, 50) #center placement of text
        gameDisplay.blit(textSurf, textRect) #display text

        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("Blue Player (Right)", largeText)
        textRect.center = (750, 50)
        gameDisplay.blit(textSurf, textRect)

        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("UP", largeText)
        textRect.center = (250, 200)
        gameDisplay.blit(textSurf, textRect)

        largeText = pygame.font.Font("freesansbold.ttf", 25)
        textSurf, textRect = textObjects("DOWN", largeText)
        textRect.center = (250, 500)
        gameDisplay.blit(textSurf, textRect)
        
        #draw yellow rectangle and black rectangle with no fill for an outline
        pygame.draw.rect(gameDisplay,YELLOW,(900,165,300,75))
        pygame.draw.rect(gameDisplay, BLACK ,[900,165,300,75],4) #4 value for outline
        
        largeText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = textObjects("First to 7 points wins", largeText)
        textRect.center = (1050, 206)
        gameDisplay.blit(textSurf, textRect)

        pygame.draw.rect(gameDisplay,YELLOW,(900,365,300,75))
        pygame.draw.rect(gameDisplay, BLACK ,[900,365,300,75],4)
        
        largeText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = textObjects("Reflect the ball with your paddle", largeText)
        textRect.center = (1050, 406)
        gameDisplay.blit(textSurf, textRect)

        pygame.draw.rect(gameDisplay,YELLOW,(900,565,300,75))
        pygame.draw.rect(gameDisplay, BLACK ,[900,565,300,75],4)
        
        largeText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = textObjects("Score on the opposite side to gain points", largeText)
        textRect.center = (1050, 606)
        gameDisplay.blit(textSurf, textRect)

        #return to mainMenu

        #rectangle
        pygame.draw.rect(gameDisplay, GREEN, (75,50,200,75))
        pygame.draw.rect(gameDisplay, BLACK ,[75,50,200,75],4)

        if 75+200 > mousePos[0] > 75 and 100+75 > mousePos[1] > 50:
            pygame.draw.rect(gameDisplay,GREEN2,(75,50,200,75))
            pygame.draw.rect(gameDisplay,BLACK,[75,50,200,75],4)
            if mouseClick[0] == 1:
                mainMenu()
        
        #text 
        largeText = pygame.font.Font("freesansbold.ttf",25)
        textSurf,textRect = textObjects("RETURN",largeText)
        textRect.center = (173,90)
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(60)
    
    

#main game
def mainLoop():
    #main starts at False

    #BLUE PADDLE
    x1 = (DISPLAY_WIDTH  * 0.98)
    y1 = (DISPLAY_HEIGHT * 0.45)

    #RED PADDLE
    x2 = (DISPLAY_WIDTH * 0.01)
    y2 = (DISPLAY_HEIGHT * 0.45)

    #paddle speeds 0 for now
    yVelocity1 = 0
    yVelocity2 = 0

    #ball starts in middle
    ballStartX = DISPLAY_WIDTH*0.5
    ballStartY = DISPLAY_HEIGHT*0.5

    #ball first going to red paddle on left
    ballSpeedX = -20

    #y speed of ball 0 for now
    ballSpeedY = 0
    ballRadius = 10
    player1_score = 0
    player2_score = 0

    #wait given time in order for players to prepare
    pygame.time.wait(250)
    
    gameExit = False
    while gameExit == False:
        #for all events in the game
        for event in pygame.event.get():
            #if event is "quit"
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    yVelocity1 = -15
                    
                elif event.key == pygame.K_DOWN:
                    yVelocity1 = 15
                    
                elif event.key == pygame.K_w:
                    yVelocity2 = -15
                          
                elif event.key == pygame.K_s:
                     yVelocity2 = 15              
                    
            #Release causes velocity to be 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yVelocity1 = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    yVelocity2 = 0

        #changes the placement on the axis
        
        gameDisplay.fill(color)
        
        #green rectangle
        pygame.draw.rect(gameDisplay, GREEN, (50,25,100,50))
        pygame.draw.rect(gameDisplay, BLACK ,[50,25,100,50],4)

        #mouse stuff

        #checks if mouse is pressed
        mouseClick = pygame.mouse.get_pressed()
        #checks position of mouse
        mousePos = pygame.mouse.get_pos()

        #if mouse glides over green rectangle
        if 50+100 > mousePos[0] > 50 and 100+25 > mousePos[1] > 25:
            pygame.draw.rect(gameDisplay,GREEN2,(50,25,100,50))
            pygame.draw.rect(gameDisplay,BLACK,[50,25,100,50],4)
            #if mouse is clicked
            if mouseClick[0] == 1:
                mainMenu()
        #text 
        largeText = pygame.font.Font("freesansbold.ttf",15)
        textSurf,textRect = textObjects("RETURN",largeText)
        textRect.center = (100,50)
        gameDisplay.blit(textSurf, textRect)

        #ball start
        ball(ballStartX,ballStartY,ballRadius,BLACK)
        

        #if hit BLUE paddle
        if ballStartY+ballRadius >= y1 and (ballStartY-ballRadius <= y1+paddle1_HEIGHT) and ballStartX+ballRadius >= x1:
            ballSpeedX *= -1

            ballSpeedY = ((y1+(y1+paddle1_HEIGHT))/2)-ballStartY
            ballSpeedY = -ballSpeedY/((5*ballRadius)/7)

        elif (ballStartY+ballRadius == y1 or (ballStartY-ballRadius == y1+paddle1_HEIGHT)) and ballStartX+ballRadius >= x1:
            ballSpeedY *= -1
        

        #if hit RED paddle

        #top of the screen == 0
        #bottom of the screen == 0

        #if ball is between top point and top point + paddle height AND ball is between the far left point and the far right point 
        if ballStartY+ballRadius >= y2 and (ballStartY-ballRadius <= y2+paddle2_HEIGHT) and ballStartX-ballRadius <= x2+paddle2_WIDTH:
            #ball x speed is reversed
            ballSpeedX *= -1

            #ball y speed depends on where the paddle hits the ball (further away from middle, the larger the angle)
            ballSpeedY = ((y2+(y2+paddle2_HEIGHT))/2)-ballStartY
            ballSpeedY = -ballSpeedY/((5*ballRadius)/7)

        elif (ballStartY+ballRadius == y2 or (ballStartY-ballRadius == y2+paddle2_HEIGHT)) and ballStartX-ballRadius <= x2+paddle2_WIDTH:
            ballSpeedY *= -1
        
        #if hit bottom or top wall
        if ballStartY >= DISPLAY_HEIGHT - ballRadius or ballStartY <= 0:
            ballSpeedY *= -1

        #if hit blue side
        if ballStartX > x1+paddle1_WIDTH:
            player1_score += 1

            #ball and player positions reset
            ballStartX = DISPLAY_WIDTH*0.5
            ballStartY = DISPLAY_HEIGHT*0.5
            x1 = (DISPLAY_WIDTH  * 0.98)
            y1 = (DISPLAY_HEIGHT * 0.45)
            x2 = (DISPLAY_WIDTH * 0.01)
            y2 = (DISPLAY_HEIGHT * 0.45)

            #winner recieves ball (ball goes left to red)
            ballSpeedX = -20
            ballSpeedY = 0
            pygame.time.wait(200)
            
            
        #if hit red side
        if ballStartX < x2-paddle2_WIDTH:
            player2_score += 1
            ballStartX = DISPLAY_WIDTH*0.5
            ballStartY = DISPLAY_HEIGHT*0.5

            x1 = (DISPLAY_WIDTH  * 0.98)
            y1 = (DISPLAY_HEIGHT * 0.45)
            x2 = (DISPLAY_WIDTH * 0.01)
            y2 = (DISPLAY_HEIGHT * 0.45)
            ballSpeedX = 20
            ballSpeedY = 0
            pygame.time.wait(200)
            
            
        #if blue player won
        if player1_score == 7:
            pauseRed()
        #if red player won
        if player2_score == 7:
            pauseBlue()
            
        #display score
        score1(player1_score)
        score2(player2_score)

        #display paddles
        player1(x1,y1)
        player2(x2,y2)
        
        #paddles do not go off screen
        if y1 > DISPLAY_HEIGHT - paddle1_HEIGHT:
            y1 = DISPLAY_HEIGHT - paddle1_HEIGHT
            #paddle stops
            yVelocity1 = 0
        if y2 > DISPLAY_HEIGHT - paddle2_HEIGHT:
            y2 = DISPLAY_HEIGHT - paddle2_HEIGHT
            yVelocity2 = 0
        if y1 < 0:
            #paddle repositioned to edge of screen 
            y1 = 0
            yVelocity1 = 0
        if y2 < 0:
            y2 = 0
            yVelocity2 = 0
        
       
        #new ball posistion is: old ball position + ball speed   
        ballStartX += ballSpeedX
        ballStartY += ballSpeedY 

        y1 = y1 + yVelocity1
        y2 = y2 + yVelocity2

        pygame.display.update()
        #fps
        clock.tick(60)
#call main menu
mainMenu()
