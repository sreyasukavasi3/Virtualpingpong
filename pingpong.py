import pygame
import random
import math
import cv2
import numpy as np
pygame.init()

screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
ballimg=pygame.image.load('ball.png')
barimg=pygame.image.load('bar.png') 
ball_x=float(490.0)
ball_y=746.0

player1_x=400
player1_y=779

def ball(x,y):
    screen.blit(ballimg,(x,y))
def player1(x,y):
    screen.blit(barimg,(x,y))
bh=1
moving=False
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
k1=2.333
k2=2.3333    
while running:
    screen.fill((0,0,0))   
    player1_change_x=0
    player1_change_y=0
    player2_change_x=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1_change_x-=30
            if event.key == pygame.K_RIGHT:
                player1_change_x+=30
            if (event.key == pygame.K_SPACE and moving == False):
                moving=True
                a=random.randint(0,10000000000000000000)
                ball_slope=float(a)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1_change_x=0
        
        

    player1_x+=player1_change_x
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
            ball_x=490.0
            ball_y=746.0
            player1_x=400
            player1_y=779

        else:
            bh=1
            k=random.randrange(45,61,1)
            k1=2*math.sin(k)
            k2=2*math.cos(k)
    elif(ball_y<0):
        ball_y=0
        bh=3
        k=random.randrange(45,61,1)
        k1=2*math.sin(k)
        k2=2*math.cos(k)
    elif(ball_x<0):
        ball_x=0
        bh=4
        k=random.randrange(45,61,1)
        k1=2*math.sin(k)
        k2=2*math.cos(k)
    elif(ball_x>970):
        ball_x=970
        bh=2
        k=random.randrange(45,61,1)
        k1=2*math.sin(k)
        k1=abs(k1)
        k2=2*math.cos(k)
        k2=abs(k2)

    ball(ball_x,ball_y)
    #moving=False
    pygame.display.update()
