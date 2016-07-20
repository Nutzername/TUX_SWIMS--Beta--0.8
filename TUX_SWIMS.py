#That is my first programm with Python... so there are maybe a lot of mistakes :D
#The LICENSE and the COPYRIGHT are in the README.txt.
#TUX_SWIMS (Beta)

import pygame
import time
import random

pygame.init()

display_width = 1920
display_height = 990

black = (0,0,0)
white = (255,255,255)
lightblue = (80,200,230)
original_blue = (0,170,200)
blue = (0,140,180)
grund = (150,150,50)

pygame.mixer.music.load("game_sound.mp3")#sound
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.3)

car_width = 220
car_height = 97

#----------------------WINDOW-----------------------#

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('=━=┳︻  (◕‿◕)   (ΘLΘ)-☞  TUX SWIMS  ☜-(ΘLΘ)   (◕‿◕)  ︻┳=━=')
clock = pygame.time.Clock()

#--------------PICTURES--------------#
carImg = pygame.image.load('tuxmini2.png')
winImg = pygame.image.load('win2.jpg')
bildImg = pygame.image.load('win.gif')
bild2Img = pygame.image.load('win.png')
coreImg = pygame.image.load('cor.gif')
#________BLASEN & FISH:________
wandaImg = pygame.image.load('wanda_the_fish.png')
blaseImg = pygame.image.load('blase.png')
rundImg = pygame.image.load('blasen3.png')
rundImgg = pygame.image.load('blaseng.png')
rundImggui = pygame.image.load('blasengui.png')
rundImgpy = pygame.image.load('blasenpy.png')
rundImga = pygame.image.load('blasenanon.png')
#_______________________
aImg = pygame.image.load('apfel.png')
sandImg = pygame.image.load('sand.jpg')
bsdImg = pygame.image.load('bsdsurfer.png')
iceImg = pygame.image.load('icedove.png')
tastenImg = pygame.image.load('tasten.gif')
pfImg = pygame.image.load('pfeil.png')
narrImg = pygame.image.load('narr3.png')
welleImg = pygame.image.load('welle.png')



def things(thingx, thingy):
    gameDisplay.blit(bild2Img,(thingx, thingy))

def core(cx, cy):
    gameDisplay.blit(coreImg,(cx, cy))

def win(xwin, ywin):
    gameDisplay.blit(winImg,(xwin, ywin))

def particle(pax, pay, paw, pah):
    gameDisplay.blit(blaseImg,(pax, pay))

def particle1(pa1x, pa1y, paw, pah,):
    gameDisplay.blit(wandaImg,(pa1x, pa1y))

def particle2(pax, pay, paw, pah, pa1color):
    pygame.draw.rect(gameDisplay, pa1color, [pax, pay, paw, pah])

def rund(rx,ry,r_speed):
    gameDisplay.blit(rundImggui,(rx,ry))
def rund1(rx,ry,r_speed):
    gameDisplay.blit(rundImga,(rx,ry))
def rund2(rx,ry,r_speed):
    gameDisplay.blit(rundImgpy,(rx,ry))
def rund3(rx,ry,r_speed):
    gameDisplay.blit(rundImg,(rx,ry))
def rund4(rx,ry,r_speed):
    gameDisplay.blit(rundImg,(rx,ry))
def rund5(rx,ry,r_speed):
    gameDisplay.blit(rundImgg,(rx,ry))

def welle(wellex, welley):
    gameDisplay.blit(welleImg,(wellex, welley))

def apfel(ax,ay,a_speed):
    gameDisplay.blit(aImg,(ax,ay))
def sand(sax,say,sa_speed):
    gameDisplay.blit(sandImg,(sax,say))
def bsd(bsdx,bsdy,bsd_speed):
    gameDisplay.blit(bsdImg,(bsdx,bsdy))
def ice(ix,iy,i_speed):
    gameDisplay.blit(iceImg,(ix,iy))
def tasten(tx,ty,t_speed):
    gameDisplay.blit(tastenImg,(tx,ty))
def mess(xmess,ymess):
    gameDisplay.blit(narrImg,(xmess,ymess))

def pfeil(fx,fy,f_speed):
    gameDisplay.blit(pfImg,(fx,fy))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def bild(bx,by,b_speed):
    gameDisplay.blit(bildImg,(bx,by))

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def car2(x2,y2):
    gameDisplay.blit(hImg,(x2,y2))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    gameDisplay.fill(black)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

def crash():
    message_display("YOU CRASHED (x_x)")

def eaten_fish(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width - 220),(display_height/32))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def musik():
    pygame.mixer.music.load("game_sound.mp3")#sound
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.4)
    print ('SOUND')

def musik_off():
    pygame.mixer.music.load("game_sound.mp3")
    pygame.mixer.stop()
    print ('SOUND OFF')

def musik_plus():
    pygame.mixer.music.set_volume(1.0)
    print ('Plus')

def musik_normal():
    pygame.mixer.music.set_volume(0.4)
    print ('Normal')

def musik_minus():
    pygame.mixer.music.set_volume(0.1)
    print ('Minus')

def freeswsong():
    pygame.mixer.music.load("FreeSWSong.ogg")
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.3)
    print ('FreeSWSong')

def game_loop():
    x = (display_width * 0.0)
    y = (display_height * 0.4)

    x_change = 0
    y_change = 0

    x_change2 = 0
    y_change2 = 0

    x2 = (display_width * 0.0)
    y2 = (display_height * 0.0)

    x2_change = 0
    y2_change = 0

    thing_startx = 1920
    thing_starty = random.randrange(0, display_height)
    thing_speed =  -12
    thing_width = 150
    thing_height = 100

    cx = 1920
    cy = y
    c_speed = -6
    c_width = 150
    c_height = 100

    k_startx = 1920
    k_startx2 = 1730
    k_startx3 = 1540
    k_startx4 = 1350
    k_startx5 = 1160
    k_startx6 = 970
    k_startx7 = 780
    k_startx8 = 590
    k_startx9 = 400
    k_startx10 = 205
    k_startx11 = 0
    k_starty = 0
    k_speed =  -6
    wellex = k_startx
    wellex2 = k_startx2
    wellex3 = k_startx3
    wellex4 = k_startx4
    wellex5 = k_startx5
    welley = 50
    wellew = 100
    welleh = 100

    particle_startx = 1920
    particle_starty = random.randrange(150, display_height)
    particle_speed =  -6
    particle_width = 10
    particle_height = 10

    pab_x = 2500
    pab_y = random.randrange(150, display_height)

    particle1_startx = 2100
    particle1_starty = random.randrange(200, display_height)
    particle1_speed =  -6
    particle1_width = 10
    particle1_height = 10

    particle2_startx = 2300
    particle2_starty = random.randrange(0, display_height)
    particle2_speed =  -6
    particle2_width = 2
    particle2_height = 2

    ax = 4000
    ay = 880
    a_speed =  -6

    sax = 0
    sax1 = sax + 120
    sax2 = sax1 + 120
    sax3 = sax2 + 120
    sax4 = sax3 + 120
    sax5 = sax4 + 120
    sax6 = sax5 + 120
    sax7 = sax6 + 120
    sax8 = sax7 + 120
    sax9 = sax8 + 120
    sax10 = sax9 + 120
    sax11 = sax10 + 120
    sax12 = sax11 + 120
    sax13 = sax12 + 120
    sax14 = sax13 + 120
    sax15 = sax14 + 120
    sax16 = sax15 + 120
    sax17 = sax16 + 120
    say = 950
    sa_speed =  -6

    bsdx = 2100
    bsdy = 40
    bsd_speed =  -1

    ix = 2100
    iy = 0
    i_speed =  -6.5

    tx = 700
    ty = 0
    t_speed = 1
    t_speed2 = -6

    fx = 50
    fy = 160
    f_speed =  0.1

    bx = 1920
    by = random.randrange(0, display_height)
    b_speed =  -6
    b_width = 100
    b_height = 100

    rx = 400
    ry = y
    r_speed =  -6
    r_width = 100
    r_height = 100
    ###############
    rx1 = 100
    ry1 = y-45
    r_speed1 =  -6
    r_width1 = 100
    r_height1 = 100
    rx2 = 200
    ry2 = y-20
    r_speed2 =  -6
    r_width2 = 100
    r_height2 = 100
    r_speed4 =  -6
    rx5 = 300
    ry5 = y-50
    r_speed5 =  -6
    r_width5 = 100
    r_height5 = 100

    xwin = 0
    ywin = 0

    narr = 0
    xmess = 0
    ymess = -40
    booom = 0
    mu = 0
    dis = 0

    song = False
    fish = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True


#############_______________HANDLUNG_______________############

            if booom == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        narr = 1
                        c_speed = 0
                        b_speed = 0
                        thing_speed = 0
                        booom = 1
            if booom == 1:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_n:
                        print ('AAAAAAAAAAAAAA')
                        booom = 3



            print ('narr:' + str(narr))
            #print ('mu:' + str(mu))


            if booom == 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        narr = 0
                        f_speed = 0.1
                        c_speed = -6
                        b_speed = -6
                        thing_speed = -12
                        booom = 2
            if booom == 2:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_n:
                        booom = 0

#__________________--------MUSIK:--------____________________#

            if mu == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        mu = 1
            if mu == 1:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        mu = 3

            if mu == 1:
                musik_off()

            if mu == 2:
                musik()

            if mu == 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        mu = 2
            if mu == 2:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        mu = 0


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    musik_plus()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_i:
                    musik_minus()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_o:
                    musik_normal()
#<<<<<<<<<<<<<-----Bewegung der Figur----->>>>>>>>>>>>>>>>>:


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -7
                if event.key == pygame.K_DOWN:
                    y_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -7
                if event.key == pygame.K_s:
                    y_change = 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

############



        if y < 0:
            y_change = 2

        if y > 900:
            y = 900

        if y > 50 and y_change == 2:
            y_change = 0

        if y < cy:
            y_change2 = -2
        if y-100 > cy:
            y_change2 = 2

        cy += y_change2


        if narr == 0:
            y += y_change


#Hintergrund:
        gameDisplay.fill(blue)

        pygame.draw.rect(gameDisplay, grund, (0,950,1920,40))

        sand(sax, say, sa_speed)
        sax += sa_speed

        if sax < -120:
           sax = 1920

        sand(sax1, say, sa_speed)
        sax1 += sa_speed

        if sax1 < -120:
           sax1 = 1920

        sand(sax2, say, sa_speed)
        sax2 += sa_speed

        if sax2 < -120:
           sax2 = 1920

        sand(sax3, say, sa_speed)
        sax3 += sa_speed

        if sax3 < -120:
           sax3 = 1920

        sand(sax4, say, sa_speed)
        sax4 += sa_speed

        if sax4 < -120:
           sax4 = 1920

        sand(sax5, say, sa_speed)
        sax5 += sa_speed

        if sax5 < -120:
           sax5 = 1920

        sand(sax6, say, sa_speed)
        sax6 += sa_speed

        if sax6 < -120:
           sax6 = 1920

        sand(sax7, say, sa_speed)
        sax7 += sa_speed

        if sax7 < -120:
           sax7 = 1920

        sand(sax8, say, sa_speed)
        sax8 += sa_speed

        if sax8 < -120:
           sax8 = 1920

        sand(sax9, say, sa_speed)
        sax9 += sa_speed

        if sax9 < -120:
           sax9 = 1920

        sand(sax10, say, sa_speed)
        sax10 += sa_speed

        if sax10 < -120:
           sax10 = 1920

        sand(sax11, say, sa_speed)
        sax11 += sa_speed

        if sax11 < -120:
           sax11 = 1920

        sand(sax12, say, sa_speed)
        sax12 += sa_speed

        if sax12 < -120:
           sax12 = 1920

        sand(sax13, say, sa_speed)
        sax13 += sa_speed

        if sax13 < -120:
           sax13 = 1920

        sand(sax14, say, sa_speed)
        sax14 += sa_speed

        if sax14 < -120:
           sax14 = 1920

        sand(sax15, say, sa_speed)
        sax15 += sa_speed

        if sax15 < -120:
           sax15 = 1920

        sand(sax16, say, sa_speed)
        sax16 += sa_speed

        if sax16 < -120:
           sax16 = 1920

        sand(sax17, say, sa_speed)
        sax17 += sa_speed

        if sax17 < -120:
           sax17 = 1920

        apfel(ax, ay, a_speed)
        ax += a_speed

        if ax < -200 :
           ax = 4000
           ay = 880

        welle(wellex, welley)
        wellex = k_startx -150

        welle(wellex, welley)
        wellex = k_startx5 -150

        welle(wellex, welley)
        wellex = k_startx2 -150

        welle(wellex, welley)
        wellex = k_startx3 -150

        welle(wellex, welley)
        wellex = k_startx4 -150

        welle(wellex, welley)
        wellex = k_startx6 -150

        welle(wellex, welley)
        wellex = k_startx7 -150

        welle(wellex, welley)
        wellex = k_startx8 -150

        welle(wellex, welley)
        wellex = k_startx9 -150

        welle(wellex, welley)
        wellex = k_startx10 -150

        welle(wellex, welley)
        wellex = k_startx11 -150

        rund(rx, ry, r_speed)
        rx += r_speed

        if rx < -r_width-100:
           rx = 200
           ry = y-45

        rund1(rx1, ry1, r_speed1)
        rx1 += r_speed1

        if rx1 < -r_width-100 :
           rx1 = 200
           ry1 = y-45

        rund2(rx2, ry2, r_speed2)
        rx2 += r_speed2

        if rx2 < -r_width-100:
           rx2 = 200
           ry2 = y-45

        rund5(rx5, ry5, r_speed4)
        rx5 += r_speed5

        if rx5 < -r_width-100 :
           rx5 = 200
           ry5 = y-45

        ##########_________THE_SEE________############

        pygame.draw.circle(gameDisplay, lightblue, (k_startx, k_starty), 120)
        k_startx += k_speed

        if k_startx < -100:
           k_startx = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx2, k_starty), 120)
        k_startx2 += k_speed

        if k_startx2 < -100:
           k_startx2 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx3, k_starty), 120)
        k_startx3 += k_speed

        if k_startx3 < -100:
           k_startx3 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx4, k_starty), 120)
        k_startx4 += k_speed

        if k_startx4 < -100:
           k_startx4 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx5, k_starty), 120)
        k_startx5 += k_speed

        if k_startx5 < -100:
           k_startx5 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx6, k_starty), 120)
        k_startx6 += k_speed

        if k_startx6 < -100:
           k_startx6 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx7, k_starty), 120)
        k_startx7 += k_speed

        if k_startx7 < -100:
           k_startx7 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx8, k_starty), 120)
        k_startx8 += k_speed

        if k_startx8 < -100:
           k_startx8 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx9, k_starty), 120)
        k_startx9 += k_speed

        if k_startx9 < -100:
           k_startx9 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx10, k_starty), 120)
        k_startx10 += k_speed

        if k_startx10 < -100:
           k_startx10 = 1920 + 100
           k_starty = 0

        pygame.draw.circle(gameDisplay, lightblue, (k_startx11, k_starty), 120)
        k_startx11 += k_speed

        if k_startx11 < -100:
           k_startx11 = 1920 + 100
           k_starty = 0

        bsd(bsdx, bsdy, bsd_speed)
        if fx > 300:
            bsdx += bsd_speed
        if bsdx < 0 and bsd_speed < -0.6:
            bsd_speed = 0.5

        if bsdx > 300 and bsd_speed > 0.4:
            bsd_speed = -0.5

        ice(ix, iy, i_speed)
        if fx > 1700:
            ix += i_speed

        tasten(tx, ty, t_speed)
        ty += t_speed
        if ty > 400:
            tx += t_speed2
            t_speed = 0
        if tx < -200:
            t_speed2 = 0

        #PARTICLE################################

        particle(particle_startx, particle_starty, particle_width, particle_height)
        particle_startx += particle_speed

        if particle_startx < -10:
            particle_startx = 2300 - particle_height
            particle_starty = random.randrange(150,display_height)

        particle(pab_x, pab_y, particle_width, particle_height)
        pab_x += particle_speed

        if pab_x < -10:
            pab_x = 1920
            pab_y = random.randrange(150,display_height)

        particle1(particle1_startx, particle1_starty, particle1_width, particle1_height)
        particle1_startx += particle_speed

        if particle1_startx < -10:
            particle1_startx = 1920 - particle1_height
            particle1_starty = random.randrange(200,display_height)

        particle2(particle2_startx, particle2_starty, particle2_width, particle2_height, white)
        particle2_startx += particle_speed

        if particle2_startx < -2:
            particle2_startx = 1920 - particle2_height
            particle2_starty = random.randrange(150,display_height)

        # things #####################################

        things(thing_startx, thing_starty)
        if fx > 90:
            thing_startx += thing_speed

        if thing_startx > display_width:
            thing_startx = 0 - thing_width
            thing_starty = random.randrange(0,display_height)
            dodged += 1
            thing_speed += 1
            thing_height += (dodged * 1.2)

        car(x,y)

        bild(bx, by, b_speed)
        if fx > 90:
            bx += b_speed

        if bx > display_width:
           bx = 0 - b_width
           by = random.randrange(0,display_height)
           dodged += 1
           b_speed += 1
           b_height += (dodged * 1.2)

        core(cx, cy)
        if fx > 200:
            cx += c_speed

        if cx > display_width:
            cx = 0 + c_width
            cy = random.randrange(0,display_height)
            dodged += 1
            c_speed += 1
            c_height += (dodged * 1.2)



        ##############___CRASH___###############

        if thing_startx < -150:
            thing_startx = 1920 - thing_height
            thing_starty = random.randrange(0,display_height)

        if x > thing_startx-car_width and thing_starty > y-car_height and thing_starty < y+car_height :
            print('crossover')
            thing_startx = 1920
            bx = 1920
            cx = 1920
            if fx > 250:
                fx = fx - 200
            else:
                fx = 50
            crash()

        if bx < -100:
           bx = 1920 - b_height
           by = random.randrange(0,display_height)

        if x > bx-car_width and by > y-car_height and by < y+car_height :
            print('crossover')
            thing_startx = 1920
            bx = 1920
            cx = 1920
            if fx > 250:
                fx = fx - 200
            else:
                fx = 50
            crash()

        if cx < -100:
           cx = 1920 - c_height
           cy = random.randrange(0,display_height)

        if x > cx-car_width and cy > y-car_height and cy < y+car_height :
            print('crossover')
            thing_startx = 1920
            bx = 1920
            cx = 1920
            if fx > 250:
                fx = fx - 200
            else:
                fx = 50
            crash()

        if x > particle1_startx-car_width and particle1_starty  > y-car_height and particle1_starty < y+car_height :
            print('eat')
            particle1_startx = 2100
            particle1_starty = random.randrange(200, display_height)
            fish = fish + 1


        pygame.draw.line(gameDisplay, black, (20,172), (1900,172),2)

        pfeil(fx, fy, f_speed)
        fx += f_speed

        if narr == 1:
                f_speed = 0
                mess(xmess, ymess)

        if fx > 1900 and fx < 1901:
            print("play")
            freeswsong()

        if fx > 1900:
            win(xwin, ywin)
            thing_startx = 1000
            bx = 1000
            cx = 1000

        eaten_fish("eaten fish:" + str(fish))

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
