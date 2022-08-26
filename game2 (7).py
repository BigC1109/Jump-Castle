import aifc

import pygame
import math
import random

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Castle")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 144

pygame.font.init()
GAMEFONT = pygame.font.SysFont('Comic Sans MS', 40)
text = GAMEFONT.render('Some Text', False, (0, 0, 0)).convert_alpha()

playerPos = [1, 1]

BOXSIZE = (41, 42)

ICONSIZE = (25, 25)

BUTTONWIDTH, BUTTONHEIGHT = 200, 100

mainMenu = pygame.image.load("start menu.png")
mainMenu = pygame.transform.scale(mainMenu, (WIDTH, HEIGHT))

startButton = pygame.image.load("start.png")
startButton = pygame.transform.scale(startButton, (BUTTONWIDTH, BUTTONHEIGHT))

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

red = pygame.image.load('red.jpg')
red = pygame.transform.scale(red, (BOXSIZE))

playerAniIdle = []
player0 = pygame.image.load('knight\knight_m_idle_anim_f0.png').convert_alpha()
player0 = pygame.transform.scale(player0, BOXSIZE)
playerAniIdle.append(player0)
player1 = pygame.image.load('knight\knight_m_idle_anim_f1.png').convert_alpha()
player1 = pygame.transform.scale(player1, BOXSIZE)
playerAniIdle.append(player1)
player2 = pygame.image.load('knight\knight_m_idle_anim_f2.png').convert_alpha()
player2 = pygame.transform.scale(player2, BOXSIZE)
playerAniIdle.append(player2)
player3 = pygame.image.load('knight\knight_m_idle_anim_f3.png').convert_alpha()
player3 = pygame.transform.scale(player3, BOXSIZE)
playerAniIdle.append(player3)

playerAniRun = []
player0 = pygame.image.load('knight\knight_m_run_anim_f0.png').convert_alpha()
player0 = pygame.transform.scale(player0, BOXSIZE)
playerAniRun.append(player0)
player1 = pygame.image.load('knight\knight_m_run_anim_f1.png').convert_alpha()
player1 = pygame.transform.scale(player1, BOXSIZE)
playerAniRun.append(player1)
player2 = pygame.image.load('knight\knight_m_run_anim_f2.png').convert_alpha()
player2 = pygame.transform.scale(player2, BOXSIZE)
playerAniRun.append(player2)
player3 = pygame.image.load('knight\knight_m_run_anim_f3.png').convert_alpha()
player3 = pygame.transform.scale(player3, BOXSIZE)
playerAniRun.append(player3)

basicAniIdle = []
monster0 = pygame.image.load('skelet\skelet_idle_anim_f0.png').convert_alpha()
monster0 = pygame.transform.scale(monster0, BOXSIZE)
basicAniIdle.append(monster0)
monster1 = pygame.image.load('skelet\skelet_idle_anim_f1.png').convert_alpha()
monster1 = pygame.transform.scale(monster1, BOXSIZE)
basicAniIdle.append(monster1)
monster2 = pygame.image.load('skelet\skelet_idle_anim_f2.png').convert_alpha()
monster2 = pygame.transform.scale(monster2, BOXSIZE)
basicAniIdle.append(monster2)
monster3 = pygame.image.load('skelet\skelet_idle_anim_f3.png').convert_alpha()
monster3 = pygame.transform.scale(monster3, BOXSIZE)
basicAniIdle.append(monster3)

basicAniRun = []
monster0 = pygame.image.load('skelet\skelet_run_anim_f0.png').convert_alpha()
monster0 = pygame.transform.scale(monster0, BOXSIZE)
basicAniRun.append(monster0)
monster1 = pygame.image.load('skelet\skelet_run_anim_f1.png').convert_alpha()
monster1 = pygame.transform.scale(monster1, BOXSIZE)
basicAniRun.append(monster1)
monster2 = pygame.image.load('skelet\skelet_run_anim_f2.png').convert_alpha()
monster2 = pygame.transform.scale(monster2, BOXSIZE)
basicAniRun.append(monster2)


ALPHABET = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

boxSections = {}

boardPlacements = {}

spriteSections = []

boardPos = []

boxOne = [18, 58]

def select_character(location):
    checkCharacter = ''
    characterFound = False

    while characterFound is False:
        checkCharacter = ALPHABET[random.randint(0, 25)]

        # Checks right 1
        if location[0] + 1 in boxSections:
            if boxSections[location[0] + 1][location[1]]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks right 2
        if location[0] + 2 in boxSections:
            if boxSections[location[0] + 2][location[1]]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks left 1
        if location[0] - 1 in boxSections:
            if boxSections[location[0] - 1][location[1]]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks left 2
        if location[0] - 2 in boxSections:
            if boxSections[location[0] - 2][location[1]]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks up 1
        if location[1] + 1 in boxSections[location[0]]:
            if boxSections[location[0]][location[1] + 1]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks up 2
        if location[1] + 2 in boxSections[location[0]]:
            if boxSections[location[0]][location[1] + 2]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks down 1
        if location[1] - 1 in boxSections[location[0]]:
            if boxSections[location[0]][location[1] - 1]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks down 2
        if location[1] - 2 in boxSections[location[0]]:
            if boxSections[location[0]][location[1] - 2]['letter'] != checkCharacter:
                pass
            else:
                continue

        # Checks right 1, up 1
        if location[0] + 1 in boxSections:
            if location[1] + 1 in boxSections[location[0] + 1]:
                if boxSections[location[0] + 1][location[1] + 1]['letter'] != checkCharacter:
                    pass
                else:
                    continue

        # Checks left 1, up 1
        if location[0] - 1 in boxSections:
            if location[1] + 1 in boxSections[location[0] - 1]:
                if boxSections[location[0] - 1][location[1] + 1]['letter'] != checkCharacter:
                    pass
                else:
                    continue

        # Checks right 1, down 1
        if location[0] + 1 in boxSections:
            if location[1] - 1 in boxSections[location[0] + 1]:
                if boxSections[location[0] + 1][location[1] - 1]['letter'] != checkCharacter:
                    pass
                else:
                    continue

        # Checks left 1, down 1
        if location[0] - 1 in boxSections:
            if location[1] - 1 in boxSections[location[0] - 1]:
                if boxSections[location[0] - 1][location[1] - 1]['letter'] != checkCharacter:
                    pass
                else:
                    continue

        characterFound = True

    return checkCharacter

activeMonsters = {}
def setupGame():
    global activeMonsters, boxSections
    activeMonsters = {}
    boxSections = {}

    for x in range(1, 15):
        boxSections[x] = {}
        for y in range(1, 10):
            boxSections[x][y] = {'location': (boxOne[0] + ((x - 1) * 48), boxOne[1] + ((y - 1) * 48)),
                                 'letter': '',
                                 'stoodOn': ''}
            spriteSections.append((boxOne[0] + ((x - 1) * 48), boxOne[1] + ((y - 1) * 48)))
            boardPos.append((x, y))

    for i in boardPos:
        boxSections[i[0]][i[1]]['letter'] = select_character(i)

print(spriteSections)

print(boxSections)

def main_menu(action):
    if action == 'start':
        return True

def draw_window():
    pygame.display.update()

def load_chars():
    for i in boardPos:
        location = boxSections[i[0]][i[1]]['location']
        text = GAMEFONT.render('{}'.format(boxSections[i[0]][i[1]]['letter']), False, (0, 0, 0))
        WIN.blit(text, text.get_rect(center=(location[0] + 20, location[1] + 18)))

animation_cooldown = 200
jumpStates = []
fastMovers = []
amountMoved = 0
def summon_knight(location, last_update, last_jump, last_location, pframe, flip, jumpSpot):
    current_time = pygame.time.get_ticks()
    global amountMoved

    if current_time - last_jump >= animation_cooldown:
        last_jump = current_time
        pframe += 1

        if pframe >= len(playerAniIdle):
            pframe = 0

    if len(jumpStates) > 0:
        if amountMoved == 1:
            jumpcooldown = 10
        elif amountMoved == 2:
            jumpcooldown = 5
        elif 5 > amountMoved >= 3:
            jumpcooldown = 3
        elif amountMoved >= 5:
            jumpcooldown = 0
        else:
            jumpcooldown = 1000000
            print('bro there was an error and I have no idea how it happened')

        ani = playerAniRun[pframe].copy()
        ani = pygame.transform.flip(ani, jumpStates[0][1], False)

        if current_time - last_update >= jumpcooldown:
            last_update = current_time

            WIN.blit(ani, jumpStates[0][0])
            jumpSpot = jumpStates[0][0]

            jumpStates.pop(0)
            if len(jumpStates) == 0:
                jumpSpot = None
        elif jumpSpot is not None:
            WIN.blit(ani, jumpSpot)

        # return last_update, last_location, last_jump, pframe, jumpSpot

    if len(fastMovers) > 0:
        if len(fastMovers) > 1:
            orderLocation = fastMovers[0]
            fastMovers.pop(0)
        elif len(fastMovers) == 1:
            orderLocation = location
            fastMovers.pop(0)
        else:
            orderLocation = location
            print('errorerrorrrr')

        pframe = 0
        newState = boxSections[orderLocation[0]][orderLocation[1]]['location']
        curState = boxSections[last_location[0]][last_location[1]]['location']

        currentflip = flip

        if newState[1] == curState[1]:
            if newState[0] > curState[0]:
                mid = (newState[0] + curState[0]) / 2
                top = newState[1] - 20
                for x in range(curState[0], newState[0], 2):
                    y = ((1 / 28) * (x - mid) ** 2) + top
                    jumpStates.append([(x, y), currentflip])

            elif newState[0] < curState[0]:
                mid = (newState[0] + curState[0]) / 2
                top = newState[1] - 20
                for x in reversed(range(newState[0], curState[0], 2)):
                    y = ((1 / 28) * (x - mid) ** 2) + top
                    jumpStates.append([(x, y), currentflip])

        elif newState[0] == curState[0]:
            if newState[1] > curState[1]:
                top = curState[1] - 12
                x = newState[0]
                for y in reversed(range(top, curState[1], 2)):
                    jumpStates.append([(x, y), currentflip])
                for y in range(top, curState[1], 3):
                    jumpStates.append([(x, y), currentflip])
                for y in range(curState[1], newState[1], 4):
                    jumpStates.append([(x, y), currentflip])

            elif newState[1] < curState[1]:
                top = newState[1] - 12
                x = newState[0]
                for y in reversed(range(newState[1], curState[1], 4)):
                    jumpStates.append([(x, y), currentflip])
                for y in reversed(range(top, newState[1], 3)):
                    jumpStates.append([(x, y), currentflip])
                for y in range(top, newState[1], 2):
                    jumpStates.append([(x, y), currentflip])

        else:
            print('error in summon_knight')

        ani = playerAniIdle[pframe].copy()
        ani = pygame.transform.flip(ani, jumpStates[0][1], False)

        WIN.blit(ani, jumpStates[0][0])
        jumpSpot = jumpStates[0][0]

        jumpStates.pop(0)

        last_location = location

        return last_update, last_location, last_jump, pframe, jumpSpot

    if len(jumpStates) == 0:

        ani = playerAniIdle[pframe].copy()
        ani = pygame.transform.flip(ani, flip, False)
        WIN.blit(ani, boxSections[location[0]][location[1]]['location'])

        amountMoved = 0

    return last_update, last_location, last_jump, pframe, jumpSpot

def check_key(keypressed, location, flip):
    global amountMoved

    # Checks right 1
    if location[0] + 1 in boxSections:
        if boxSections[location[0] + 1][location[1]]['letter'] == keypressed:
            fastMovers.append((location[0] + 1, location[1]))
            amountMoved += 1
            return [True, [location[0] + 1, location[1]], False]

    # Checks left 1
    if location[0] - 1 in boxSections:
        if boxSections[location[0] - 1][location[1]]['letter'] == keypressed:
            fastMovers.append((location[0] - 1, location[1]))
            amountMoved += 1
            return [True, [location[0] - 1, location[1]], True]

    # Checks up 1
    if location[1] + 1 in boxSections[location[0]]:
        if boxSections[location[0]][location[1] + 1]['letter'] == keypressed:
            fastMovers.append((location[0], location[1] + 1))
            amountMoved += 1
            return [True, [location[0], location[1] + 1], flip]

    # Checks down 1
    if location[1] - 1 in boxSections[location[0]]:
        if boxSections[location[0]][location[1] - 1]['letter'] == keypressed:
            fastMovers.append((location[0], location[1] - 1))
            amountMoved += 1
            return [True, [location[0], location[1] - 1], flip]

    return [False]

basicCount = 0
monstersetup = []
setupUpdate = 0
val = 0
newtime = 3
def monsters_setup():
    global basicCount, setupUpdate, newtime
    time = 0
    currentTime = pygame.time.get_ticks()/1000

    monsterCount = len(activeMonsters)
    if len(monstersetup) > 0:
        time = 9999999
    elif len(monstersetup) == 0:
        time = newtime
    if currentTime - setupUpdate >= time:
        newtime = random.randint(10, 20)
        setupUpdate = currentTime
        basicCount += 1
        val = currentTime
        spawnTime = random.randint(2, 8)
        nextMove = random.randint(1, 3)
        monstersetup.append(f'basic{basicCount}')
        activeMonsters[f'basic{basicCount}'] = {'location': [random.randint(1, 14), random.randint(1, 9)],
                                                'spawnTime': val + spawnTime,
                                                'timewhenspawned': 0,
                                                'nextMove': nextMove,
                                                'totalTime': val + spawnTime,
                                                'jumpAnimation': [],
                                                'lastUpdate': 0,
                                                'jumpSpot': None,
                                                'flip': False}

    for i in monstersetup:
        if currentTime >= activeMonsters[i]['spawnTime']:
            activeMonsters[i]['timewhenspawned'] = pygame.time.get_ticks()/1000
            monstersetup.remove(i)

def monster_jump_animation(old_location, new_location, monster, flip):
    if new_location[1] == old_location[1]:
        if new_location[0] > old_location[0]:
            mid = (new_location[0] + old_location[0]) / 2
            top = new_location[1] - 20
            for x in range(old_location[0], new_location[0], 2):
                y = ((1 / 28) * (x - mid) ** 2) + top
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])

        elif new_location[0] < old_location[0]:
            mid = (new_location[0] + old_location[0]) / 2
            top = new_location[1] - 20
            for x in reversed(range(new_location[0], old_location[0], 2)):
                y = ((1 / 28) * (x - mid) ** 2) + top
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
        else:
            print('error1')

    elif new_location[0] == old_location[0]:
        if new_location[1] > old_location[1]:
            top = old_location[1] - 12
            x = new_location[0]
            for y in reversed(range(top, old_location[1], 2)):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
            for y in range(top, old_location[1], 3):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
            for y in range(old_location[1], new_location[1], 4):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])

        elif new_location[1] < old_location[1]:
            top = new_location[1] - 12
            x = new_location[0]
            for y in reversed(range(new_location[1], old_location[1], 4)):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
            for y in reversed(range(top, new_location[1], 3)):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
            for y in range(top, new_location[1], 2):
                activeMonsters[monster]['jumpAnimation'].append([(x, y), flip])
        else:
            print('error2')

    else:
        print('error in monster_jump_animation')

def monster_run(monster):
    global playerPos
    currenttime = pygame.time.get_ticks()

    allLocations = []
    for i in list(activeMonsters.keys()):
        if i != monster:
            allLocations.append(activeMonsters[i]['location'])

    monsterLocation = activeMonsters[monster]['location']
    mx = monsterLocation[0]
    my = monsterLocation[1]
    px = playerPos[0]
    py = playerPos[1]
    monsterLocation = [mx, my]

    if len(activeMonsters[monster]['jumpAnimation']) > 0:
        jumpcooldown = 10

        ani = basicAniRun[mRunframe].copy()
        ani = pygame.transform.flip(ani, activeMonsters[monster]['jumpAnimation'][0][1], False)

        if currenttime - activeMonsters[monster]['lastUpdate'] >= jumpcooldown:
            activeMonsters[monster]['lastUpdate'] = currenttime

            WIN.blit(ani, activeMonsters[monster]['jumpAnimation'][0][0])
            activeMonsters[monster]['jumpSpot'] = activeMonsters[monster]['jumpAnimation'][0][0]

            activeMonsters[monster]['jumpAnimation'].pop(0)
            if len(activeMonsters[monster]['jumpAnimation']) == 0:
                activeMonsters[monster]['jumpSpot'] = None
        elif activeMonsters[monster]['jumpSpot'] is not None:
            WIN.blit(ani, activeMonsters[monster]['jumpSpot'])


    elif abs(mx - px) > abs(my - py):

        if [activeMonsters[monster]['location'][0] + 1, activeMonsters[monster]['location'][1]] in allLocations and activeMonsters[monster]['location'][0] + 1 < 15:
            mx = 100
        if [activeMonsters[monster]['location'][0] - 1, activeMonsters[monster]['location'][1]] in allLocations and activeMonsters[monster]['location'][0] - 1 > 0:
            px = 100
        try:
            if mx - px > 0:  # moving left 1
                activeMonsters[monster]['location'][0] -= 1
                activeMonsters[monster]['flip'] = True
                oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
            elif mx - px < 0:  # moving right 1
                activeMonsters[monster]['location'][0] += 1
                activeMonsters[monster]['flip'] = False
                oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
            elif mx - px == 0:  # don't move
                pass
        except:
            pass
    elif abs(mx - px) < abs(my - py):

        if [activeMonsters[monster]['location'][0], activeMonsters[monster]['location'][1] - 1] in allLocations and activeMonsters[monster]['location'][1] - 1 > 0:
            my = 100
        if [activeMonsters[monster]['location'][0], activeMonsters[monster]['location'][1] + 1] in allLocations and activeMonsters[monster]['location'][1] + 1 < 9:
            py = 100

        try:
            if my - py > 0:  # moving down 1
                activeMonsters[monster]['location'][1] -= 1
                oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
            elif my - py < 0:  # moving up 1
                activeMonsters[monster]['location'][1] += 1
                oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
            elif mx - px == 0:  # don't move
                pass
        except:
            pass
    elif abs(mx - px) == abs(my - py):
        if random.randint(0, 1) == 0:

            if [activeMonsters[monster]['location'][0] + 1, activeMonsters[monster]['location'][1]] in allLocations and activeMonsters[monster]['location'][0] + 1 < 15:
                mx = 100
            if [activeMonsters[monster]['location'][0] - 1, activeMonsters[monster]['location'][1]] in allLocations and activeMonsters[monster]['location'][0] - 1 > 0:
                px = 100
            try:
                if mx - px > 0:  # moving left 1
                    activeMonsters[monster]['location'][0] -= 1
                    activeMonsters[monster]['flip'] = True
                    oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                    newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                    monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
                elif mx - px < 0:  # moving right 1
                    activeMonsters[monster]['location'][0] += 1
                    activeMonsters[monster]['flip'] = False
                    oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                    newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                    monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
                elif mx - px == 0:  # don't move
                    pass
            except:
                pass
        else:

            if [activeMonsters[monster]['location'][0], activeMonsters[monster]['location'][1] - 1] in allLocations and activeMonsters[monster]['location'][1] - 1 > 0:
                my = 100
            if [activeMonsters[monster]['location'][0], activeMonsters[monster]['location'][1] + 1] in allLocations and activeMonsters[monster]['location'][1] + 1 < 9:
                py = 100
            try:
                if my - py > 0:  # moving down 1
                    activeMonsters[monster]['location'][1] -= 1
                    oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                    newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                    monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
                elif my - py < 0:  # moving up 1
                    activeMonsters[monster]['location'][1] += 1
                    oldTrueLocation = boxSections[monsterLocation[0]][monsterLocation[1]]['location']
                    newTrueLocation = boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location']
                    monster_jump_animation(oldTrueLocation, newTrueLocation, monster, activeMonsters[monster]['flip'])
                elif mx - px == 0:  # don't move
                    pass
            except:
                pass

    if len(activeMonsters[monster]['jumpAnimation']) == 0:
        try:
            ani = basicAniIdle[mIdleframe].copy()
            ani = pygame.transform.flip(ani, activeMonsters[monster]['flip'], False)
            WIN.blit(ani, boxSections[activeMonsters[monster]['location'][0]][activeMonsters[monster]['location'][1]]['location'])
        except:
            pass
mRunframe = 0
mIdleframe = 0
monsterUpdate = 0
anitime = 0
mFlip = False
def summon_monster(time_since_enter):
    global mRunframe, mIdleframe, monsterUpdate, anitime, mFlip, playerPos
    anitime = pygame.time.get_ticks()
    currentTime = pygame.time.get_ticks()/1000

    if anitime - monsterUpdate >= animation_cooldown:
        monsterUpdate = anitime
        mIdleframe += 1
        mRunframe += 1

        if mIdleframe >= len(basicAniIdle):
            mIdleframe = 0
        if mRunframe >= len(basicAniRun):
            mRunframe = 0

    for i in list(activeMonsters.keys()):
        if i in monstersetup:
            return
        elif currentTime - activeMonsters[i]['timewhenspawned'] <= 3:
            WIN.blit(red, boxSections[activeMonsters[i]['location'][0]][activeMonsters[i]['location'][1]]['location'])

        elif currentTime - activeMonsters[i]['timewhenspawned'] > 3:
            if currentTime - (activeMonsters[i]['nextMove']) >= activeMonsters[i]['totalTime']:

                monster_run(i)

                if len(activeMonsters[i]['jumpAnimation']) == 0:
                    if activeMonsters[i]['location'] == playerPos:
                        return True
                    if time_since_enter > 30:
                        activeMonsters[i]['nextMove'] = random.randint(1, 2)
                    elif time_since_enter > 60:
                        activeMonsters[i]['nextMove'] = 1
                    elif time_since_enter > 90:
                        rval = random.randint(0, 1)

                        activeMonsters[i]['nextMove'] = rval
                    else:
                        activeMonsters[i]['nextMove'] = random.randint(1, 3)

                    activeMonsters[i]['totalTime'] += activeMonsters[i]['nextMove']

            elif currentTime - (activeMonsters[i]['nextMove']) < activeMonsters[i]['totalTime']:
                if activeMonsters[i]['location'][0] == 15:
                    activeMonsters[i]['location'][0] = 14
                if activeMonsters[i]['location'][0] == 0:
                    activeMonsters[i]['location'][0] == 1
                if activeMonsters[i]['location'][1] == 10:
                    activeMonsters[i]['location'][1] = 9
                if activeMonsters[i]['location'][1] == 0:
                    activeMonsters[i]['location'][1] = 1
                try:
                    ani = basicAniIdle[mIdleframe].copy()
                    ani = pygame.transform.flip(ani, activeMonsters[i]['flip'], False)
                    WIN.blit(ani, boxSections[activeMonsters[i]['location'][0]][activeMonsters[i]['location'][1]]['location'])
                except:
                    pass

            else:
                print('error in summon_monster')
                ani = basicAniIdle[mIdleframe].copy()
                ani = pygame.transform.flip(ani, activeMonsters[i]['flip'], False)
                WIN.blit(ani, boxSections[activeMonsters[i]['location'][0]][activeMonsters[i]['location'][1]]['location'])

    return False

def main():
    global playerPos
    clock = pygame.time.Clock()
    run = True
    startGame = False
    last_update = pygame.time.get_ticks()
    last_jump = pygame.time.get_ticks()
    last_location = [1, 1]
    pframe = 10
    flip = False
    start_time = 0
    jumpSpot = None
    previousRun = 0
    leaderboard = 0
    while run:
        clock.tick(FPS)

        WIN.blit(mainMenu, (0, 0))
        WIN.blit(startButton, ((WIDTH/2) - (BUTTONWIDTH/2), (HEIGHT/2) - (BUTTONHEIGHT/2) - 180))
        if previousRun != 0:
            if previousRun > leaderboard:
                leaderboard = previousRun

            text = GAMEFONT.render(f'Your Time Was: {previousRun}', False, (0, 0, 0))
            WIN.blit(text, text.get_rect(center=(WIDTH/2, 405)))
            leadtext = GAMEFONT.render(f'Top Time: {leaderboard}', False, (0, 0, 0))
            WIN.blit(leadtext, leadtext.get_rect(center=(WIDTH/2, 465)))

        if startGame:
            time_since_enter = pygame.time.get_ticks() - start_time

            WIN.blit(background, (0, 0))
            load_chars()
            text = GAMEFONT.render(f'{round(time_since_enter, -2)/1000}', False, (0, 0, 0))
            WIN.blit(text, text.get_rect(center=(WIDTH/2, 20)))

            last_update, last_location, last_jump, pframe, jumpSpot = summon_knight(playerPos, last_update, last_jump, last_location, pframe, flip, jumpSpot)

            monsters_setup()

            if len(activeMonsters) > 0:
                if summon_monster(time_since_enter/1000):
                    previousRun = round(time_since_enter, -2)/1000
                    startGame = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pass

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        check = check_key('A', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_b:
                        check = check_key('B', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_c:
                        check = check_key('C', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_d:
                        check = check_key('D', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_e:
                        check = check_key('E', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_f:
                        check = check_key('F', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_g:
                        check = check_key('G', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_h:
                        check = check_key('H', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_i:
                        check = check_key('I', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_j:
                        check = check_key('J', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_k:
                        check = check_key('K', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_l:
                        check = check_key('L', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_m:
                        check = check_key('M', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_n:
                        check = check_key('N', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_o:
                        check = check_key('O', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_p:
                        check = check_key('P', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_q:
                        check = check_key('Q', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_r:
                        check = check_key('R', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_s:
                        check = check_key('S', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_t:
                        check = check_key('T', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_u:
                        check = check_key('U', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_v:
                        check = check_key('V', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_w:
                        check = check_key('W', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_x:
                        check = check_key('X', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_y:
                        check = check_key('Y', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]
                    if event.key == pygame.K_z:
                        check = check_key('Z', playerPos, flip)
                        if check[0]:
                            playerPos, flip = check[1], check[2]

        elif startGame is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # WIN.blit(startButton, ((WIDTH/2) - (BUTTONWIDTH/2), (HEIGHT/2) - (BUTTONHEIGHT/2) - 100))
                    startleft = (WIDTH/2) - (BUTTONWIDTH/2)
                    startright = (HEIGHT/2) - (BUTTONHEIGHT/2) - 180
                    if startleft <= pos[0] <= (startleft + BUTTONWIDTH) and startright <= pos[1] <= (startright + BUTTONHEIGHT):
                        global jumpStates, monstersetup
                        startGame = True
                        setupGame()
                        playerPos = [1, 1]
                        jumpStates = []
                        last_location = [1, 1]
                        pframe = 10
                        flip = False
                        start_time = pygame.time.get_ticks()
                        jumpSpot = None
                        monstersetup = []

        draw_window()

if __name__ == "__main__":
    main()