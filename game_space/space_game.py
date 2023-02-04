import pygame
import random
import math
from pygame import mixer

pygame.init()
#screen size
Screen = pygame.display.set_mode((900,800)) 
#sounds
mixer.music.load("C:\\Users\\DELL\\Desktop\\game\\background.wav")
mixer.music.play(-1)
#title
pygame.display.set_caption("In the space")
icon = pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\001-startup.png")
pygame.display.set_icon(icon)
#playerg
playerimg =pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\001-spaceship.png")
playerx =450
playery =650
playerx_change=0
playery_change=0
def player(playerx ,playery):
    Screen.blit(playerimg ,(playerx ,playery))
#missile
missimg =pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\002-bullet.png")
missx =1000
missy =1000
missx_change =0
missy_change =0
miss_state ="ready"
def missile(x,y):
    Screen.blit(missimg,(x ,y))
#collision
def shoot_out(missx,missy,enemyx,enemyy):
    distance = math.sqrt(math.pow(enemyx-missx,2) + (math.pow(enemyy-missy,2)))
    if distance <30:
        return True
    else:
        return False
#enemy
enemyimg =pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\001-rock.png")
enemyx = random.randint(0 ,832)
enemyy = random.randint(0,100)
enemyx_change=0
enemyy_change=0
def enemy(enemyx,enemyy):
    Screen.blit(enemyimg,(enemyx ,enemyy ))
disenemy =pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\002-asteroids.png")
dis_enemyx =1000
dis_enemyy =1000
def dis_enemy(enemyx , enemyy):
    Screen.blit(disenemy,(enemyx ,enemyy ))
#master_enemy

m_enemyimg= pygame.image.load("C:\\Users\\DELL\\Desktop\\game\\001-space-ship.png")
m_enemyx = random.randint(0 ,732)
m_enemyy = random.randint(0,100)
m_enemyx_change=0
m_enemyy_change=0
def m_enemy(m_enemyx,m_enemyy):
    Screen.blit(m_enemyimg,(m_enemyx ,m_enemyy ))
#game_over
life =0
khatam =False
def game_over(life):
    if life ==3 :
        return True

#score
score_value =0

font = pygame.font.Font('freesansbold.ttf',32)
textx =0
texty =0
def print_score(x,y):
    score =font.render("Score :" +str(score_value),True,(200,200,200))
    Screen.blit(score,(x ,y ))
#game loop
running =True
while running :
    Screen.fill((0,0,50))
    for event in pygame.event.get() :
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.8
            if event.key ==pygame.K_RIGHT:
                playerx_change = 0.8
            if event.key ==pygame.K_UP:
                if miss_state == "ready":
                    missx=playerx +16
                    missy=playery +30
                    missile(missx,missy)
                    miss_state = "fire"
                    missile_sound = mixer.Sound("C:\\Users\\DELL\\Desktop\\game\\laser.wav")
                    missile_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                playerx_change = 0
        
    
    playerx += playerx_change
    if playerx >= 832:
        playerx = 832
    elif playerx <=0:
        playerx =0
    colli =shoot_out(missx,missy,enemyx,enemyy)
    if colli:
        dis_enemyx = enemyx
        dis_enemyy = enemyy
        miss_state = "ready"
        enemyx = random.randint(0 ,832)
        enemyy = random.randint(0,100)  
        Screen.blit(enemyimg,(enemyx ,enemyy ))
        score_value+= 1
    dis_enemy(dis_enemyx,dis_enemyy)
    m_colli =shoot_out(missx,missy,m_enemyx,m_enemyy)
    if m_colli:
        dis_enemyx = m_enemyx
        dis_enemyy = m_enemyy
        miss_state = "ready"
        m_enemyx = random.randint(0 ,832)
        m_enemyy = random.randint(0,100)  
        Screen.blit(enemyimg,(m_enemyx ,m_enemyy ))
        score_value+= 1
    player(playerx,playery)
    enemy(enemyx-16,enemyy-10)
    if score_value <= 10:
        m_enemy(m_enemyx,m_enemyy)
    missile(missx,missy)
    missy_change =2
    missy -= missy_change
    if missy <= 0:
        miss_state = "ready" 
    enemyy_change =0.3
    enemyy +=enemyy_change
    m_enemyy_change =0.1
    m_enemyy +=m_enemyy_change
    
    if enemyy >=600:
        life= life+1
        khatam = game_over(life)
        enemyx = random.randint(0 ,832)
        enemyy = random.randint(0,100)
    if khatam :
        font2 = pygame.font.Font('freesansbold.ttf',50)
        khatam =font2.render("GAME OVER " ,True,(250,200,200))
        Screen.blit(khatam,(340,400 ))
        playerx_change = 0

    print_score(textx,texty)
    if missy ==enemyy:
            enemyy=1000
            enemyy=1000
    pygame.display.update()