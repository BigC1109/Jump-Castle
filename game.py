import pygame
import math

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 144

curPos = [1, 1]
BOXSIZE = (41, 42)

ICONSIZE = (25, 25)

# Icons, eventually loop them into a list

wall = pygame.image.load("wall.png").convert_alpha()
wall = pygame.transform.scale(wall, ICONSIZE)

wall2 = pygame.image.load("wall.png").convert_alpha()
wall2 = pygame.transform.scale(wall2, BOXSIZE)

pushericon = pygame.image.load("temp.png").convert_alpha()
pushericon = pygame.transform.scale(pushericon, ICONSIZE)
# call this for 2 although doesnt really matter until pusher art
# is completed

pusher = pygame.image.load("temp.png").convert_alpha()
pusher1 = pygame.transform.rotate(pygame.transform.scale(pusher, BOXSIZE), 0)  # East
pusher2 = pygame.transform.rotate(pygame.transform.scale(pusher, BOXSIZE), 90)  # South
pusher3 = pygame.transform.rotate(pygame.transform.scale(pusher, BOXSIZE), 180)  # West
pusher4 = pygame.transform.rotate(pygame.transform.scale(pusher, BOXSIZE), 270)  # North

icons = []
icons.append(wall)

# Background

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

boxSections = {}

boardPlacements = {}

spriteSections = []

boxOne = [18, 58]

for x in range(1, 15):
    boxSections[x] = {}
    for y in range(1, 10):
        boxSections[x][y] = (boxOne[0] + ((x - 1) * 48), boxOne[1] + ((y - 1) * 48))
        spriteSections.append((boxOne[0] + ((x - 1) * 48), boxOne[1] + ((y - 1) * 48)))

iconSections = []

for i in range(0, 5):
    iconSections.append((658 - (i * 30), 9))

print(spriteSections)

print(boxSections)

print(iconSections)

def closest_value(input_list, input_value):
    input_list.sort(reverse=True)
    difference = lambda input_list : abs(input_list - input_value)
    res = min(input_list, key=difference)
    dif = abs(res - input_value)
    return res, dif

def move(side):

    ##########
    # Down = 1
    # Up = 4
    # Right = 2
    # Left = 3
    ##########

    if side == 1:
        try:
            curPos[1] += 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
        except:
            curPos[1] -= 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
            pass
    elif side == 2:
        try:
            curPos[0] += 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
        except:
            curPos[0] -= 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
            pass
    elif side == 3:
        try:
            curPos[0] -= 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
        except:
            curPos[0] += 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
            pass
    elif side == 4:
        try:
            curPos[1] -= 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
        except:
            curPos[1] += 1
            pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
            pass

# def checkClick(sectionChecked, text):
#     pos = pygame.mouse.get_pos()
#
#     if text == 'boardClick':
#         for i in spriteSections:
#             if i[0] <= pos[0] <= (i[0] + BOXSIZE[0]) and i[1] <= pos[1] <= (i[1] + BOXSIZE[1]):
#                 print("Success!")
#                 print(i)
#                 x = (math.floor(spriteSections.index(i) / 9)) + 1
#                 y = (spriteSections.index(i) - ((x - 1) * 9)) + 1
#                 curPos[0], curPos[1] = x, y
#                 break
#
#     elif text == 'iconClick':
#         for i in sectionChecked:
#             if i[0] <= pos[0] <= (i[0] + ICONSIZE[0]) and i[1] <= pos[1] <= (i[1] + ICONSIZE[1]):
#                 print("Icon Selected!")
#                 print(i)
#                 selectedIcon = sectionChecked.index(i)
#                 print(sectionChecked)
#                 clickedPos = (pos[0] - 658, pos[1] - 9)
#                 return selectedIcon, clickedPos
#
#     else:
#         print("If you see this there was likely an error")

def blockType(type, placement):
    if type == 'wall':
        WIN.blit(wall2, (placement[0], placement[1]))
    elif type == 'pusher':
        pusher_direction()
        WIN.blit(pusher, (placement[0], placement[1]))

def pixel(surface, color, pos1, pos2):
    surface.fill(color, (pos1, pos2))

def draw_window():
    pygame.display.update()

def pusher_direction(direction):
    if direction == 'north':
        return pusher4
    elif direction == 'south':
        return pusher2
    elif direction == 'east':
        return pusher1
    elif direction == 'west':
        return pusher3



def main():
    clickedPos = 0
    selectedIcon = None
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        WIN.blit(background, (0, 0))
        pixel(WIN, WHITE, boxSections[curPos[0]][curPos[1]], BOXSIZE)
        for i in iconSections:
            WIN.blit(wall, i)

        if None not in boardPlacements:
            for i in list(boardPlacements.keys()):
                # print(boardPlacements)
                placement = boxSections[i[0]][i[1]]
                # this is in a try except in case there is something placed in front of
                # a pusher while it is iterating over the list
                try:
                    blockType(boardPlacements[i]['type'], placement)
                except:
                    print('error')
                    break

                if boardPlacements[i]['type'] == 'pusher':

                    try:
                        typeA = (i[0] + 1, i[1])
                        typeB = boardPlacements[typeA]
                        typeC = (i[0] + 2, i[1])
                        if typeB == 'wall':
                            placement = boxSections[i[0] + 2][i[1]]
                            blockType(typeB, placement)
                            boardPlacements[typeC] = typeB
                            del boardPlacements[typeA]
                            # print(boardPlacements)
                    except:
                        # print('error')
                        pass


                # call blockPlacement here in order to determine
                # what type of block is being placed

                # WIN.blit(wall2, (placement[0], placement[1]))
                # draw_window()

        if selectedIcon is not None:
            pos = pygame.mouse.get_pos()
            realPosition = (pos[0] - clickedPos[0], pos[1] - clickedPos[1])
            WIN.blit(wall, realPosition)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for i in spriteSections:
                    if i[0] <= pos[0] <= (i[0] + BOXSIZE[0]) and i[1] <= pos[1] <= (i[1] + BOXSIZE[1]):
                        x = (math.floor(spriteSections.index(i)/9)) + 1
                        y = (spriteSections.index(i) - ((x - 1) * 9)) + 1
                        curPos[0], curPos[1] = x, y
                        break

                # (changeme), (changeme) = checkClick(spriteSections, 'boardClick')
                # selectedIcon, clickedPos = checkClick(iconSections, 'iconClick')

                for i in iconSections:
                    if i[0] <= pos[0] <= (i[0] + ICONSIZE[0]) and i[1] <= pos[1] <= (i[1] + ICONSIZE[1]):
                        selectedIcon = iconSections.index(i)
                        clickedPos = (pos[0] - i[0], pos[1] - i[1])

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if selectedIcon == 0:
                    for i in spriteSections:
                        if i[0] <= pos[0] <= (i[0] + BOXSIZE[0]) and i[1] <= pos[1] <= (i[1] + BOXSIZE[1]):
                            x = int((math.floor(spriteSections.index(i) / 9)) + 1)
                            y = int((spriteSections.index(i) - ((x - 1) * 9)) + 1)
                            boardPlacements[(x, y)] = 'wall'
                            break

                elif selectedIcon == 1:
                    for i in spriteSections:
                        if i[0] <= pos[0] <= (i[0] + BOXSIZE[0]) and i[1] <= pos[1] <= (i[1] + BOXSIZE[1]):
                            direction = ''
                            directionListX = [i[0], i[0] + BOXSIZE[0]]
                            directionListY = [i[1], i[1] + BOXSIZE[1]]

                            val1, dif1 = closest_value(directionListX, pos[0])
                            val2, dif2 = closest_value(directionListY, pos[1])

                            if dif2 <= dif1:
                                if val2 == i[1]:
                                    direction = 'north'
                                elif val2 == i[1] + BOXSIZE[1]:
                                    direction = 'south'
                            elif dif2 > dif1:
                                if val1 == i[0]:
                                    direction = 'west'
                                elif val1 == i[0] + BOXSIZE[0]:
                                    direction = 'east'

                            print(direction)

                            x = int((math.floor(spriteSections.index(i) / 9)) + 1)
                            y = int((spriteSections.index(i) - ((x - 1) * 9)) + 1)
                            boardPlacements[(x, y)] = {'type': 'pusher',
                                                       'direction': directionListY}
                            break

                selectedIcon = None

            if event.type == pygame.MOUSEMOTION:
                if selectedIcon != None:
                    pos = pygame.mouse.get_pos()
                    realPosition = (pos[0] - clickedPos[0], pos[1] - clickedPos[1])

                    WIN.blit(wall, realPosition)
                    draw_window()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    move(1)

                if event.key == pygame.K_RIGHT:
                    move(2)

                if event.key == pygame.K_LEFT:
                    move(3)

                if event.key == pygame.K_UP:
                    move(4)

                if event.key == pygame.K_m:
                    pass

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
