import pygame
import random
import math
import cv2
import numpy as np
pygame.init()
video=cv2.VideoCapture(0)
screen=pygame.display.set_mode((850,800))
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
ballimg=pygame.image.load('ball.png')
barimg=pygame.image.load('bar.png') 
ball_x=float(390.0)
ball_y=746.0

player1_x=300
player1_y=779
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
prev =0
def ball(x,y):
    screen.blit(ballimg,(x,y))
def player1(x,y):
    screen.blit(barimg,(x,y))
bh=1
moving=False
check,frame=video.read()
sd=1
se=1
sdd=1
for i in range(0,480):
    for j in range(640):
        b,g,r=frame[i][j]
        if(r>=140 and g>=0 and g<=90 and b<=100):
            sdd+=i
            se+=j
            sd+=1
sdd=sdd//sd
ass=max(sdd-75,0)
running = True
def moveball(x,y,bh,k1,k2):
    if(bh==1):
        x=x+k2
        y=y-k1
    elif(bh==2):
        x=x-k2
        y=y-k1
    elif(bh==3):
        x=x-k2
        y=y+k1
    else:
        x=x+k2
        y=y+k1
    a=[]
    a.append(x)
    a.append(y)
    return a
pygame.key.set_repeat(50, 50)
k=45
k1=40
k2=50
sf=50
sd1=False

while running:
    check,frame=video.read()
    sd=1
    se=1
    sdd=1
    for i in range (ass,min(ass+150,480)):
        for j in range(640):
            b,g,r=frame[i][j]
            if(r>=140 and g>=0 and g<=90 and b<=100):
                sdd+=i
                se+=j
                sd+=1
            
    se=se//sd
    sdd=sdd//sd
    sdd=max(0,sdd-100)
    se=abs(se-640)
    print(se)
    screen.fill((0,0,0))   
    player1_change_x=0
    player1_change_y=0
    player2_change_x=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE and moving == False):
                moving=True
                prev=ass
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1_change_x=0
        
    if(sd!=1):
        if(sdd<prev):
            ass=ass-50
            prev=ass
        elif(sdd>prev):
            ass=ass+50
            prev=ass
        if (moving):
            player1_x=se
        if(player1_x<0):
            player1_x=0
        if(player1_x>800):
            player1_x=775
        player1(player1_x,player1_y)
        
        if(moving):
            a=moveball(float(ball_x),float(ball_y),bh,k1,k2)
            ball_x=a[0]
            ball_y=a[1]
            
        if(ball_y>=746):
            ball_y=746

            if(ball_x<(player1_x-16) or ball_x>(player1_x+216)):
                moving=False
                ball_x=390.0
                ball_y=746.0
                player1_x=300
                player1_y=779

            else:
                bh=1
                k=random.randrange(45,61,1)
                k1=sf*math.sin(k)
                k2=sf*math.cos(k)
        elif(ball_y<0):
            ball_y=0
            bh=3
            k=random.randrange(45,61,1)
            k1=sf*math.sin(k)
            k2=sf*math.cos(k)
        elif(ball_x<0):
            ball_x=0
            bh=4
            k=random.randrange(45,61,1)
            k1=sf*math.sin(k)
            k2=sf*math.cos(k)
        elif(ball_x>820):
            ball_x=820
            bh=2
            k=random.randrange(45,61,1)
            k1=sf*math.sin(k)
            k1=abs(k1)
            k2=sf*math.cos(k)
            k2=abs(k2)
    else:
        sd=1
        se=1
        sdd=1
        for i in range(0,480):
            for j in range(640):
                b,g,r=frame[i][j]
                if(r>=140 and g>=0 and g<=90 and b<=100):
                    sdd+=i
                    se+=j
                    sd+=1
        sdd=sdd//sd
        ass=max(sdd-75,0)
        print("assupdate",ass)
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('object into camera zone', True, green, blue)
        textRect = text.get_rect() 
        textRect.center = (850 // 2,  800// 4) 
        screen.blit(text,textRect)
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('game paused', True, green, blue)
        textRect = text.get_rect() 
        textRect.center = (850 // 4,  800// 2) 
        screen.blit(text,textRect)

        
    ball(ball_x,ball_y)
    #moving=False
    pygame.display.update()
