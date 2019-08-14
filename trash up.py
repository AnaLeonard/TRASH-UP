import sys, pygame
import random


pygame.init()


def level_2():
    size = width, height = 700, 389
    screen = pygame.display.set_mode(size)
    background = pygame.transform.scale((pygame.image.load("oceanbackground.jpg")), (700, 389))
    backgroundrect = background.get_rect()
    backgroundflip = pygame.transform.scale((pygame.image.load("oceanbackgroundflip.jpg")), (700, 389))
    backgroundrect2=backgroundflip.get_rect()
    trash = pygame.transform.scale((pygame.image.load("trashpile.png")), (120,80))
    trashrect1 = trash.get_rect()
    trashrect1.y = 250 #
    trashrect1.x = 550 #
    trashcore1 = pygame.transform.scale((pygame.image.load("transparent.png")), (37,40))
    trashcorerect1 = trashcore1.get_rect()
    trashcorerect1.x = 585 #
    trashcorerect1.y = 270 #

    trashrect2 = trash.get_rect()
    trashrect2.y = 160 #
    trashrect2.x = 850 #
    trashcore2 = pygame.transform.scale((pygame.image.load("transparent.png")), (37,40))
    trashcorerect2 = trashcore2.get_rect()
    trashcorerect2.x = 885 #
    trashcorerect2.y = 180 #

    trashrect3 = trash.get_rect()
    trashrect3.y = 60 #
    trashrect3.x = 1150 #
    trashcore3 = pygame.transform.scale((pygame.image.load("transparent.png")), (37,40))
    trashcorerect3 = trashcore3.get_rect()
    trashcorerect3.x = 1185 #
    trashcorerect3.y = 80 #

    good_trash = pygame.transform.scale((pygame.image.load("water.png")), (100,100))
    good_trashrect = good_trash.get_rect()
    good_trashrect.y = 40
    good_trashrect.x = 650
    good_trashcore = pygame.transform.scale((pygame.image.load("transparent.png")), (40,40))
    good_trashcorerect = good_trashcore.get_rect()
    good_trashcorerect.x = 680
    good_trashcorerect.y = 70

    heart = pygame.transform.scale((pygame.image.load("heart.png")), (50,50))
    heartrect = heart.get_rect()
    heartrect.y = 60
    heartrect.x = 3050
    heartcore = pygame.transform.scale((pygame.image.load("transparent.png")), (60,60))
    heartcorerect = heartcore.get_rect()
    heartcorerect.x = 3040
    heartcorerect.y = 60

    can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))
    canrect = can.get_rect()
    canrect.y = 160
    canrect.x = 3550
    cancore = pygame.transform.scale((pygame.image.load("transparent.png")), (70,60))
    cancorerect = cancore.get_rect()
    cancorerect.x = 3560
    cancorerect.y = 150

    dory = pygame.transform.scale((pygame.image.load("dory.png")), (130,75))
    doryrect = can.get_rect()
    doryrect.y = 160
    doryrect.x = 500
    dorycore = pygame.transform.scale((pygame.image.load("transparent.png")), (60,50))
    dorycorerect = dorycore.get_rect()
    dorycorerect.x = 530
    dorycorerect.y = 170

    nemo = pygame.transform.scale((pygame.image.load("nemo.png")), (130,75))
    nemorect = can.get_rect()
    nemorect.y = 60
    nemorect.x = 1100
    nemocore = pygame.transform.scale((pygame.image.load("transparent.png")), (60,50))
    nemocorerect = nemocore.get_rect()
    nemocorerect.x = 1100
    nemocorerect.y = 60

    def move_background():
        if backgroundrect.left<=0:
            backgroundrect.left=backgroundrect.left-2
            backgroundrect2.left=backgroundrect.right
        if backgroundrect2.left<0:
            backgroundrect2.left=backgroundrect2.left-2
            backgroundrect.left=backgroundrect2.right

    def move_nemo():
        nemorect.left = nemorect.left-5
        nemocorerect.left = nemocorerect.left-5
        if nemorect.right<0:
            nemorect.left = 3000
            nemocorerect.left = 3030
            if abs(trashrect2.x - nemorect.x) <= 200:
                nemorect.left += 200
                nemocorerect.left += 230

    def move_dory():
        doryrect.left = doryrect.left-4
        dorycorerect.left = dorycorerect.left-4
        if doryrect.right<-10:
            doryrect.left = 1700
            dorycorerect.left = 1740
            # if abs(trashrect2.x - doryrect.x) <= 200:
            #     doryrect.left += 200
            #     dorycorerect.left += 270

    def move_good_trash():
        good_trashrect.left = good_trashrect.left-3
        good_trashcorerect.left = good_trashcorerect.left-3
        if good_trashrect.right<-10:
            good_trashrect.left = 1000
            good_trashcorerect.left = 1030
            if abs(trashrect3.x - good_trashrect.x) <= 200:
                good_trashrect.left += 200
                good_trashcorerect.left += 230

    def move_heart():
        heartrect.left = heartrect.left-3
        heartcorerect.left = heartcorerect.left-3
        if heartrect.right<-10:
            heartrect.left = 7000
            heartcorerect.left = 6990
            if abs(trashrect3.x - heartrect.x) <= 200 or abs(good_trashrect.x - heartrect.x):
                heartrect.left += 200
                heartcorerect.left += 190

    def move_can():
        canrect.left = canrect.left-3
        cancorerect.left = cancorerect.left-3
        if canrect.right<-10:
            canrect.left = 3000
            cancorerect.left = 2990
            can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))
            # if abs(trashrect2.x - canrect.x) <= 200:
            #     dcanrect.left += 200
            #     cancorerect.left += 190

    def move_bad_trash():
        move_trash(trashrect1, trashcorerect1)
        move_trash(trashrect2, trashcorerect2)
        move_trash(trashrect3, trashcorerect3)

    def move_trash(trashrect, trashcorerect):
        trashrect.left = trashrect.left-3
        trashcorerect.left = trashcorerect.left-3
        if trashrect.right<0:
            trashrect.left = random_x()
            trashcorerect.left = trashrect.left + 30


    def livesRemaining(livesleft):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Lives: ' + str(livesleft), False, (250, 250, 250))
        screen.blit(textsurface, (0,0))

    def scorepoints(scoresadd):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Scores: ' + str(scoresadd), False, (250, 250, 250))
        screen.blit(textsurface, (500,0))


    player = pygame.transform.scale((pygame.image.load("raccoonflip.png")), (100,100))
    playerrect = player.get_rect()
    playerrect.y = 140
    livesleft = 5
    scoresadd = 0
    obi_state = "o"
    score_obi_state = "o"
    heart_obi_state = "o"
    can_obi_state = "o"
    dory_obi_state = "o"
    nemo_obi_state = "o"
    level = "m"
    JUMP_TIME = 750
    jump_start = -1

    while 1:
        if livesleft == 0 or scoresadd>=1000:
            return livesleft, scoresadd
        move_background()
        move_bad_trash()
        move_good_trash()
        move_heart()
        move_can()
        move_dory()
        move_nemo()
        colliding_with_bad_trash = playerrect.colliderect(trashcorerect1) or playerrect.colliderect(trashcorerect2) or playerrect.colliderect(trashcorerect3)
        if obi_state == "o":
            if colliding_with_bad_trash:
                obi_state = "b"
            else:
                obi_state = "o"
        elif obi_state == 'b':
            obi_state = 'i'
        else:
            if colliding_with_bad_trash:
                obi_state = 'i'
            else:
                obi_state = 'o'
        if obi_state == 'b':
             livesleft-=1
             ###### add -1 life annimation
        ##########################################################################################################################################
        if heart_obi_state == "o":
            if playerrect.colliderect(heartcorerect):
                heart_obi_state = "b"
            else:
                heart_obi_state = "o"
        elif heart_obi_state == 'b':
            heart_obi_state = 'i'
        else:
            if playerrect.colliderect(heartcorerect):
                heart_obi_state = 'i'
            else:
                heart_obi_state = 'o'
        if heart_obi_state == 'b' and livesleft<5:
            livesleft+=1
            ############ add score point animation +1
            heart = pygame.transform.scale((pygame.image.load("transparent.png")), (50,50))

        if heartcorerect.right<=0:
            heart = pygame.transform.scale((pygame.image.load("heart.png")), (50,50))
            ######################################################################################################################################
        if score_obi_state == "o":
            if playerrect.colliderect(good_trashcorerect):
                score_obi_state = "b"
            else:
                score_obi_state = "o"
        elif score_obi_state == 'b':
            score_obi_state = 'i'
        else:
            if playerrect.colliderect(good_trashcorerect):
                score_obi_state = 'i'
            else:
                score_obi_state = 'o'

        if score_obi_state == 'b':
            scoresadd+=100
            ###### add score point annimations for water bottle (+100)
            good_trash = pygame.transform.scale((pygame.image.load("transparent.png")), (100,100))

        if good_trashcorerect.right<0:
            good_trash = pygame.transform.scale((pygame.image.load("water.png")), (100,100))

            ##########################################################################################################################################

        if can_obi_state == "o":
            if playerrect.colliderect(cancorerect):
                can_obi_state = "b"
            else:
                can_obi_state = "o"
        elif can_obi_state == 'b':
            can_obi_state = 'i'
        else:
            if playerrect.colliderect(cancorerect):
                can_obi_state = 'i'
            else:
                can_obi_state = 'o'

        if can_obi_state == 'b':
            scoresadd+=100
            ###### add score point annimations for can (+100)
            can = pygame.transform.scale((pygame.image.load("transparent.png")), (50,75))

        if canrect.right<=0:
            can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))

    ############################################################################################################################################################
        if dory_obi_state == "o":
            if playerrect.colliderect(dorycorerect):
                dory_obi_state = "b"
            else:
                dory_obi_state = "o"
        elif dory_obi_state == 'b':
            dory_obi_state = 'i'
        else:
            if playerrect.colliderect(dorycorerect):
                dory_obi_state = 'i'
            else:
                dory_obi_state = 'o'
        if dory_obi_state == 'b':
            scoresadd-=100
            ###### add score point annimations for can (+100)
            dory = pygame.transform.scale((pygame.image.load("transparent.png")), (130,75))
        if doryrect.right<=0:
            dory = pygame.transform.scale((pygame.image.load("dory.png")), (130,75))

    ############################################################################################################################################################
        if nemo_obi_state == "o":
            if playerrect.colliderect(nemocorerect):
                nemo_obi_state = "b"
            else:
                nemo_obi_state = "o"
        elif nemo_obi_state == 'b':
            nemo_obi_state = 'i'
        else:
            if playerrect.colliderect(nemocorerect):
                nemo_obi_state = 'i'
            else:
                nemo_obi_state = 'o'

        if nemo_obi_state == 'b':
            scoresadd-=100
            ###### add score point annimations for can (+100)
            nemo = pygame.transform.scale((pygame.image.load("transparent.png")), (130,75))

        if nemorect.right<=0:
            nemo = pygame.transform.scale((pygame.image.load("nemo.png")), (130,75))


    ############################################################################################################################################################
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and (level == "b" or level == "m"):
                if level == "m":
                    level = "t"
                elif level == "b":
                    level = "m"
                speed = [0,-100]
                playerrect = playerrect.move(speed)
                obi_state = "o"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and (level == "m" or level == "t"):
                if level == "m":
                    level = "b"
                elif level == "t":
                    level = "m"
                speed = [0,100]
                playerrect = playerrect.move(speed)
                obi_state = "o"


        screen.blit(background, backgroundrect)
        screen.blit(backgroundflip, backgroundrect2)
        screen.blit(player, playerrect)
        screen.blit(trash, trashrect1)
        screen.blit(trashcore1, trashcorerect1)
        screen.blit(trash, trashrect2)
        screen.blit(trashcore2, trashcorerect2)
        screen.blit(trash, trashrect3)
        screen.blit(trashcore3, trashcorerect3)
        screen.blit(good_trash, good_trashrect)
        screen.blit(good_trashcore, good_trashcorerect)
        screen.blit(heart, heartrect)
        screen.blit(heartcore, heartcorerect)
        screen.blit(can,canrect)
        screen.blit(cancore, cancorerect)
        screen.blit(dory,doryrect)
        screen.blit(dorycore, dorycorerect)
        screen.blit(nemo,nemorect)
        screen.blit(nemocore, nemocorerect)
        livesRemaining(livesleft)
        scorepoints(scoresadd)
        pygame.display.flip()

def random_x():
    x = random.randint(1300,2000)
    return x

def level_two():
        you_screen = pygame.display.set_mode([800, 536])
        button = pygame.Rect(100, 200, 600, 200)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button.collidepoint(mouse_pos):
                        return
            backgroundwin = pygame.transform.scale((pygame.image.load("water1.jpg")), (800, 536))
            backgroundwinrect = backgroundwin.get_rect()
            you_screen.blit(backgroundwin,backgroundwinrect)
            greenS = pygame.image.load("level.png")
            greenSrect = greenS.get_rect()
            greenSrect.center = (400,268)
            #pygame.draw.rect(you_screen, [200, 0, 0], button)
            you_screen.blit(greenS,greenSrect)
            pygame.display.update()

def game_intro():
    begin_screen = pygame.display.set_mode([800, 536])
    button = pygame.Rect(250, 300, 350, 150)
    button2 = pygame.Rect(220, 450, 350, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    print("clicked start game")
                    return "start_game"
                elif button2.collidepoint(mouse_pos):
                    print("clicked instructions button")
                    return "directions"
        background = pygame.image.load("earth2.jpg")
        backgroundrect = background.get_rect()
        begin_screen.blit(background,backgroundrect)

        name = pygame.image.load("uppp.png")
        name = pygame.transform.scale(name, (600, 200))
        namerect = name.get_rect()
        namerect.center = (400, 100)
        begin_screen.blit(name,namerect)

        greenS = pygame.image.load("start.png")
        greenS = pygame.transform.scale(greenS, (300, 400))
        greenSrect = greenS.get_rect()
        greenSrect.center = (400, 400)
        begin_screen.blit(greenS,greenSrect)

        Instructions = pygame.image.load("y.png")
        Instructionsrect = Instructions.get_rect()
        Instructionsrect.center = (400, 500)
        begin_screen.blit(Instructions,Instructionsrect)
        pygame.display.update()

def directions():
    b_screen = pygame.display.set_mode([1000, 667])
    goback = pygame.image.load("arrow1.png")
    goback = pygame.transform.scale(pygame.image.load("arrow1.png"), (100,100))
    gobackrect = goback.get_rect()
    gobackrect.x = 20
    gobackrect.y = 20
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if gobackrect.collidepoint(mouse_pos):
                    return

        font = pygame.font.SysFont("Times New Roman", 30)
        text = ["Welcome to",
                "Collect the           and           AVOID             or you’ll lose a life",
                "Hit the START button to play, and use the UP button to jump!",
                "Get 1000 points to win",
                "In Level 2, avoid                      or lose 100 points. Swim with UP and DOWN keys",
                "You’ve got this!"]
        label = []
        for line in text:
            label.append(font.render(line, True, (255,255,255)))
        background = pygame.transform.scale(pygame.image.load("earthmoon.jpg"), (1000,667))
        backgroundrect = background.get_rect()
        b_screen.blit(background,backgroundrect)
        Instructions = pygame.transform.scale(pygame.image.load("y.png"), (350,100))
        Instructionsrect = Instructions.get_rect()
        Instructionsrect.center = (500, 75)

        trashup = pygame.transform.scale(pygame.image.load("uppp.png"), (300,90))
        trashup_rect = trashup.get_rect()
        trashup_rect.x = 130
        trashup_rect.y = 120
        b_screen.blit(trashup, trashup_rect)

        water = pygame.transform.scale(pygame.image.load("water.png"), (150,150))
        water_rect = water.get_rect()
        water_rect.x = 90
        water_rect.y = 205
        b_screen.blit(water, water_rect)

        can = pygame.transform.scale(pygame.image.load("can.png"), (80,130))
        can_rect = can.get_rect()
        can_rect.x = 265
        can_rect.y = 215
        b_screen.blit(can, can_rect)

        trash = pygame.transform.scale(pygame.image.load("trashpile.png"), (130,130))
        trash_rect = trash.get_rect()
        trash_rect.x = 420
        trash_rect.y = 215
        b_screen.blit(trash, trash_rect)

        dory = pygame.transform.scale(pygame.image.load("dory.png"), (110,110))
        dory_rect = dory.get_rect()
        dory_rect.x = 190
        dory_rect.y = 510
        b_screen.blit(dory, dory_rect)

        nemo = pygame.transform.scale(pygame.image.load("nemo.png"), (110,110))
        nemo_rect = nemo.get_rect()
        nemo_rect.x = 270
        nemo_rect.y = 510
        b_screen.blit(nemo, nemo_rect)

        b_screen.blit(Instructions,Instructionsrect)
        b_screen.blit(goback,gobackrect)
        posX = (1000 * 1/1000)
        posY = (667 * 1/4)
        for words in range(len(label)):
            b_screen.blit(label[words], (posX,posY))
            posY = posY+100
        pygame.display.update()


def you_win():
    you_screen = pygame.display.set_mode([800, 536])
    button = pygame.Rect(100, 200, 600, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    return
        backgroundwin = pygame.image.load("winn.jpg")
        backgroundwin = pygame.transform.scale((pygame.image.load("winn.jpg")), (800,536))
        backgroundwinrect = backgroundwin.get_rect()
        you_screen.blit(backgroundwin,backgroundwinrect)
        greenS = pygame.image.load("won.gif")
        greenSrect = greenS.get_rect()
        greenSrect.center = (400,268)
        greenSrect

        you_screen.blit(greenS,greenSrect)
        pygame.display.update()

def real_game():

    size = width, height = 700, 389
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("gamebackground.jpg")
    backgroundrect = background.get_rect()
    backgroundflip = pygame.image.load("gamebackgroundflip.jpg")
    backgroundrect2=backgroundflip.get_rect()
    trash = pygame.transform.scale((pygame.image.load("trashpile.png")), (120,80))
    trashrect = trash.get_rect()
    trashrect.y = 250 #
    trashrect.x = 550 #
    trashcore = pygame.transform.scale((pygame.image.load("transparent.png")), (37,40))
    trashcorerect = trashcore.get_rect()
    trashcorerect.x = 585 #
    trashcorerect.y = 270 #

    good_trash = pygame.transform.scale((pygame.image.load("water.png")), (100,100))
    good_trashrect = good_trash.get_rect()
    good_trashrect.y = 40
    good_trashrect.x = 650
    good_trashcore = pygame.transform.scale((pygame.image.load("transparent.png")), (40,40))
    good_trashcorerect = good_trashcore.get_rect()
    good_trashcorerect.x = 680
    good_trashcorerect.y = 70

    heart = pygame.transform.scale((pygame.image.load("heart.png")), (50,50))
    heartrect = heart.get_rect()
    heartrect.y = 60
    heartrect.x = 3050
    heartcore = pygame.transform.scale((pygame.image.load("transparent.png")), (60,60))
    heartcorerect = heartcore.get_rect()
    heartcorerect.x = 3060
    heartcorerect.y = 60

    can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))
    canrect = can.get_rect()
    canrect.y = 160
    canrect.x = 3550
    cancore = pygame.transform.scale((pygame.image.load("transparent.png")), (60,60))
    cancorerect = cancore.get_rect()
    cancorerect.x = 3560
    cancorerect.y = 160


    def move_background():
        if backgroundrect.left<=0:
            backgroundrect.left=backgroundrect.left-1
            backgroundrect2.left=backgroundrect.right
        if backgroundrect2.left<0:
            backgroundrect2.left=backgroundrect2.left-1
            backgroundrect.left=backgroundrect2.right

    def move_good_trash():
        good_trashrect.left = good_trashrect.left-2
        good_trashcorerect.left = good_trashcorerect.left-2
        if good_trashrect.right<0:
            good_trashrect.left = 1000
            good_trashcorerect.left = 1030
            good_trashrect.left = good_trashrect.left-2
            good_trashcorerect.left = good_trashcorerect.left-2

    def move_heart():
        if heartrect.right<0:
            if abs(trashrect.right - heartrect.right) <= 200:
                heartrect.left = 7000 + 200
                heartcorerect.left = 7030 + 300
            else:
                heartrect.left = 7000
                heartcorerect.left = 7030
        heartrect.left = heartrect.left-2
        heartcorerect.left = heartcorerect.left-2

    def move_can():
        if canrect.right<0:
            canrect.left = 3000
            cancorerect.left = 3030
            can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))
        canrect.left = canrect.left-2
        cancorerect.left = cancorerect.left-2


    def move_trash():
        trashrect.left = trashrect.left-2
        trashcorerect.left = trashcorerect.left-2
        if trashrect.right<0:
            trashrect.left = 700
            trashcorerect.left = 730
            trashrect.left = trashrect.left-2
            trashcorerect.left = trashcorerect.left-2

    def livesRemaining(livesleft):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Lives: ' + str(livesleft), False, (250, 250, 250))
        screen.blit(textsurface, (0,0))

    def scorepoints(scoresadd):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('Scores: ' + str(scoresadd), False, (250, 250, 250))
        screen.blit(textsurface, (500,0))


    def update_obi_state(old_obi_state):
        if old_obi_state == "o":
            if playerrect.colliderect(trashrect):
                return 'b'
            else:
                return 'o'
        elif old_obi_state == 'b':
            return 'i'
        else:
            if playerrect.colliderect(trashrect):
                return 'i'
            else:
                return 'o'

    player = pygame.transform.scale((pygame.image.load("raccoon.png")), (100,100))
    playerrect = player.get_rect()
    playerrect.y = 225
    livesleft = 5
    scoresadd = 0
    obi_state = "o"
    score_obi_state = "o"
    heart_obi_state = "o"
    can_obi_state = "o"
    level = "b"
    JUMP_TIME = 750
    jump_start = -1

    # good_trash = pygame.transform.scale((pygame.image.load("water.png")), (100,100))
    # heart = pygame.transform.scale((pygame.image.load("heart.png")), (50,50))
    # can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))

    while 1:
        if livesleft == 0 or scoresadd>=1000:
            return livesleft, scoresadd
        move_background()
        move_trash()
        move_good_trash()
        move_heart()
        move_can()
        if obi_state == "o":
            if playerrect.colliderect(trashcorerect):
                obi_state = "b"
            else:
                obi_state = "o"
        elif obi_state == 'b':
            obi_state = 'i'
        else:
            if playerrect.colliderect(trashcorerect):
                obi_state = 'i'
            else:
                obi_state = 'o'
        if obi_state == 'b':
             livesleft-=1
             ###### add -1 life annimation
        ##########################################################################################################################################
        if heart_obi_state == "o":
            if playerrect.colliderect(heartcorerect):
                heart_obi_state = "b"
            else:
                heart_obi_state = "o"
        elif heart_obi_state == 'b':
            heart_obi_state = 'i'
        else:
            if playerrect.colliderect(heartcorerect):
                heart_obi_state = 'i'
            else:
                heart_obi_state = 'o'
        if heart_obi_state == 'b' and livesleft<5:
            livesleft+=1
            ############ add score point animation +1
            heart = pygame.transform.scale((pygame.image.load("transparent.png")), (50,50))

        if heartcorerect.right<=0:
            heart = pygame.transform.scale((pygame.image.load("heart.png")), (50,50))
            ######################################################################################################################################
        if score_obi_state == "o":
            if playerrect.colliderect(good_trashcorerect):
                score_obi_state = "b"
            else:
                score_obi_state = "o"
        elif score_obi_state == 'b':
            score_obi_state = 'i'
        else:
            if playerrect.colliderect(good_trashcorerect):
                score_obi_state = 'i'
            else:
                score_obi_state = 'o'

        if score_obi_state == 'b':
            scoresadd+=100
            ###### add score point annimations for water bottle (+100)
            good_trash = pygame.transform.scale((pygame.image.load("transparent.png")), (100,100))

        if good_trashcorerect.right<0:
            good_trash = pygame.transform.scale((pygame.image.load("water.png")), (100,100))

            ##########################################################################################################################################

        if can_obi_state == "o":
            if playerrect.colliderect(cancorerect):
                can_obi_state = "b"
            else:
                can_obi_state = "o"
        elif can_obi_state == 'b':
            can_obi_state = 'i'
        else:
            if playerrect.colliderect(cancorerect):
                can_obi_state = 'i'
            else:
                can_obi_state = 'o'

        if can_obi_state == 'b':
            scoresadd+=100
            ###### add score point annimations for can (+100)
            can = pygame.transform.scale((pygame.image.load("transparent.png")), (50,75))

        if canrect.right<=0:
            can = pygame.transform.scale((pygame.image.load("can.png")), (50,75))

    ############################################################################################################################################################


        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and (level == "b" or level == "m"):
                if level == "m":
                    level = "t"
                elif level == "b":
                    level = "m"
                speed = [0,-100]
                playerrect = playerrect.move(speed)
                jump_start = pygame.time.get_ticks()


        current_time = pygame.time.get_ticks()
        if jump_start + JUMP_TIME < current_time:
            if level == "m":
                speed = [0, 100]
                playerrect = playerrect.move(speed)
            elif level == "t":
                speed = [0, 200]
                playerrect = playerrect.move(speed)
            level = "b"


        screen.blit(background, backgroundrect)
        screen.blit(backgroundflip, backgroundrect2)
        screen.blit(player, playerrect)
        screen.blit(trash, trashrect)
        screen.blit(trashcore, trashcorerect)
        screen.blit(good_trash, good_trashrect)
        screen.blit(good_trashcore, good_trashcorerect)
        screen.blit(heart, heartrect)
        screen.blit(heartcore, heartcorerect)
        screen.blit(can,canrect)
        screen.blit(cancore, cancorerect)
        livesRemaining(livesleft)
        scorepoints(scoresadd)
        pygame.display.flip()

def game_over():
    ending_screen = pygame.display.set_mode([1022, 554])
    buttonn = pygame.Rect(100, 50, 600, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if buttonn.collidepoint(mouse_pos):
                    return
        backgroundd = pygame.image.load("game_over.jpg")
        backgrounddrect = backgroundd.get_rect()
        ending_screen.blit(backgroundd,backgrounddrect)
        greennS = pygame.image.load("over.png")
        greennSrect = greennS.get_rect()
        greennSrect.center = (511,277)
        ending_screen.blit(greennS,greennSrect)
        pygame.display.update()

        greennS = pygame.image.load("game_over.jpg")
        greennSrect = greennS.get_rect()
        ending_screen.blit(greennS,greennSrect)


while True:
    path = game_intro()
    if path == "directions":
        directions()
    else:
        ll,score = real_game()
        if ll == 0:
            game_over()
        elif score == 1000:
            level_two()
            ll,score = level_2()
            if ll == 0:
                game_over()
            elif score == 1000:
                you_win()
