import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Portcullis prototyping')
screen = pygame.display.set_mode((700, 700))
font = pygame.font.SysFont("arial", 20)

DEBUG = True

WHITE  = (255, 255, 255)
GREY   = (100, 100, 100)
BLUE   = (000, 000, 255)
GREEN  = (000, 255, 000)
RED    = (255, 000, 000)
YELLOW = (255, 255, 000)
ORANGE = (255, 165, 000)
PURPLE = (255, 000 ,255)

alpha = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E', 6 : 'F'}

grid = True
f4key = False
altkey = False
exitcondition = False

playerLoc = 'C5'

doors = {
    # Horizontal
    'A1': {'status': 'W', 'coord':((125,100),(175,100)), 'set': 'omega'},
    'A2': {'status': 'C', 'coord':((125,200),(175,200)), 'set': 'alpha'},
    'A3': {'status': 'C', 'coord':((125,300),(175,300)), 'set': 'alpha'},
    'A4': {'status': 'C', 'coord':((125,400),(175,400)), 'set': 'delta'},
    'A5': {'status': 'C', 'coord':((125,500),(175,500)), 'set': 'alpha'},
    'A6': {'status': 'W', 'coord':((125,600),(175,600)), 'set': 'delta'},
    'B1': {'status': 'W', 'coord':((225,100),(275,100)), 'set': 'omega'},
    'B2': {'status': 'C', 'coord':((225,200),(275,200)), 'set': 'alpha'},
    'B3': {'status': 'C', 'coord':((225,300),(275,300)), 'set': 'beta'},
    'B4': {'status': 'C', 'coord':((225,400),(275,400)), 'set': 'beta'},
    'B5': {'status': 'C', 'coord':((225,500),(275,500)), 'set': 'alpha'},
    'B6': {'status': 'W', 'coord':((225,600),(275,600)), 'set': 'omega'},
    'C1': {'status': 'W', 'coord':((325,100),(375,100)), 'set': 'omega'},
    'C2': {'status': 'C', 'coord':((325,200),(375,200)), 'set': 'alpha'},
    'C3': {'status': 'C', 'coord':((325,300),(375,300)), 'set': 'delta'},
    'C4': {'status': 'C', 'coord':((325,400),(375,400)), 'set': 'delta'},
    'C5': {'status': 'C', 'coord':((325,500),(375,500)), 'set': 'alpha'},
    'C6': {'status': 'X', 'coord':((325,600),(375,600)), 'set': 'omega'},
    'D1': {'status': 'W', 'coord':((425,100),(475,100)), 'set': 'omega'},
    'D2': {'status': 'C', 'coord':((425,200),(475,200)), 'set': 'alpha'},
    'D3': {'status': 'C', 'coord':((425,300),(475,300)), 'set': 'beta'},
    'D4': {'status': 'C', 'coord':((425,400),(475,400)), 'set': 'delta'},
    'D5': {'status': 'C', 'coord':((425,500),(475,500)), 'set': 'alpha'},
    'D6': {'status': 'W', 'coord':((425,600),(475,600)), 'set': 'omega'},
    'E1': {'status': 'W', 'coord':((525,100),(575,100)), 'set': 'omega'},
    'E2': {'status': 'C', 'coord':((525,200),(575,200)), 'set': 'delta'},
    'E3': {'status': 'C', 'coord':((525,300),(575,300)), 'set': 'alpha'},
    'E4': {'status': 'C', 'coord':((525,400),(575,400)), 'set': 'delta'},
    'E5': {'status': 'C', 'coord':((525,500),(575,500)), 'set': 'beta'},
    'E6': {'status': 'W', 'coord':((525,600),(575,600)), 'set': 'omega'},
    # Vertical
    '1A': {'status': 'X', 'coord':((100,125),(100,175)), 'set': 'omega'},
    '2A': {'status': 'W', 'coord':((100,225),(100,275)), 'set': 'omega'},
    '3A': {'status': 'W', 'coord':((100,325),(100,375)), 'set': 'omega'},
    '4A': {'status': 'W', 'coord':((100,425),(100,475)), 'set': 'omega'},
    '5A': {'status': 'W', 'coord':((100,525),(100,575)), 'set': 'omega'},
    '1B': {'status': 'C', 'coord':((200,125),(200,175)), 'set': 'beta'},
    '2B': {'status': 'C', 'coord':((200,225),(200,275)), 'set': 'alpha'},
    '3B': {'status': 'C', 'coord':((200,325),(200,375)), 'set': 'gamma'},
    '4B': {'status': 'C', 'coord':((200,425),(200,475)), 'set': 'alpha'},
    '5B': {'status': 'C', 'coord':((200,525),(200,575)), 'set': 'gamma'},
    '1C': {'status': 'C', 'coord':((300,125),(300,175)), 'set': 'alpha'},
    '2C': {'status': 'C', 'coord':((300,225),(300,275)), 'set': 'delta'},
    '3C': {'status': 'C', 'coord':((300,325),(300,375)), 'set': 'gamma'},
    '4C': {'status': 'C', 'coord':((300,425),(300,475)), 'set': 'alpha'},
    '5C': {'status': 'C', 'coord':((300,525),(300,575)), 'set': 'alpha'},
    '1D': {'status': 'C', 'coord':((400,125),(400,175)), 'set': 'beta'},
    '2D': {'status': 'C', 'coord':((400,225),(400,275)), 'set': 'alpha'},
    '3D': {'status': 'C', 'coord':((400,325),(400,375)), 'set': 'delta'},
    '4D': {'status': 'C', 'coord':((400,425),(400,475)), 'set': 'beta'},
    '5D': {'status': 'C', 'coord':((400,525),(400,575)), 'set': 'alpha'},
    '1E': {'status': 'C', 'coord':((500,125),(500,175)), 'set': 'gamma'},
    '2E': {'status': 'C', 'coord':((500,225),(500,275)), 'set': 'alpha'},
    '3E': {'status': 'C', 'coord':((500,325),(500,375)), 'set': 'gamma'},
    '4E': {'status': 'C', 'coord':((500,425),(500,475)), 'set': 'alpha'},
    '5E': {'status': 'C', 'coord':((500,525),(500,575)), 'set': 'alpha'},
    '1F': {'status': 'W', 'coord':((600,125),(600,175)), 'set': 'omega'},
    '2F': {'status': 'W', 'coord':((600,225),(600,275)), 'set': 'omega'},
    '3F': {'status': 'W', 'coord':((600,325),(600,375)), 'set': 'omega'},
    '4F': {'status': 'W', 'coord':((600,425),(600,475)), 'set': 'omega'},
    '5F': {'status': 'W', 'coord':((600,525),(600,575)), 'set': 'omega'},
}

matchSets = {
    'alpha': 'beta',
    'beta' : 'alpha',
    'gamma': 'delta',
    'delta': 'gamma',
}

playerLocations = {
    'A1': {'coord': (140, 140, 20, 20)},
    'A2': {'coord': (140, 240, 20, 20)},
    'A3': {'coord': (140, 340, 20, 20)},
    'A4': {'coord': (140, 440, 20, 20)},
    'A5': {'coord': (140, 540, 20, 20)},
    'B1': {'coord': (240, 140, 20, 20)},
    'B2': {'coord': (240, 240, 20, 20)},
    'B3': {'coord': (240, 340, 20, 20)},
    'B4': {'coord': (240, 440, 20, 20)},
    'B5': {'coord': (240, 540, 20, 20)},
    'C1': {'coord': (340, 140, 20, 20)},
    'C2': {'coord': (340, 240, 20, 20)},
    'C3': {'coord': (340, 340, 20, 20)},
    'C4': {'coord': (340, 440, 20, 20)},
    'C5': {'coord': (340, 540, 20, 20)},
    'D1': {'coord': (440, 140, 20, 20)},
    'D2': {'coord': (440, 240, 20, 20)},
    'D3': {'coord': (440, 340, 20, 20)},
    'D4': {'coord': (440, 440, 20, 20)},
    'D5': {'coord': (440, 540, 20, 20)},
    'E1': {'coord': (540, 140, 20, 20)},
    'E2': {'coord': (540, 240, 20, 20)},
    'E3': {'coord': (540, 340, 20, 20)},
    'E4': {'coord': (540, 440, 20, 20)},
    'E5': {'coord': (540, 540, 20, 20)},
}

cells = {
    'A1': {'NOR':('A1','XX'), 'SOU':('A2','A2'), 'EAS': ('1B','B1'), 'WES':('1A','XX')},
    'A2': {'NOR':('A2','A1'), 'SOU':('A3','A3'), 'EAS': ('2B','B2'), 'WES':('2A','XX')},
    'A3': {'NOR':('A3','A2'), 'SOU':('A4','A4'), 'EAS': ('3B','B3'), 'WES':('3A','XX')},
    'A4': {'NOR':('A4','A3'), 'SOU':('A5','A5'), 'EAS': ('4B','B4'), 'WES':('4A','XX')},
    'A5': {'NOR':('A5','A4'), 'SOU':('A6','XX'), 'EAS': ('5B','B5'), 'WES':('5A','XX')},
    'B1': {'NOR':('B1','XX'), 'SOU':('B2','B2'), 'EAS': ('1C','C1'), 'WES':('1B','A1')},
    'B2': {'NOR':('B2','B1'), 'SOU':('B3','B3'), 'EAS': ('2C','C2'), 'WES':('2B','A2')},
    'B3': {'NOR':('B3','B2'), 'SOU':('B4','B4'), 'EAS': ('3C','C3'), 'WES':('3B','A3')},
    'B4': {'NOR':('B4','B3'), 'SOU':('B5','B5'), 'EAS': ('4C','C4'), 'WES':('4B','A4')},
    'B5': {'NOR':('B5','B4'), 'SOU':('B6','XX'), 'EAS': ('5C','C5'), 'WES':('5B','A5')},
    'C1': {'NOR':('C1','XX'), 'SOU':('C2','C2'), 'EAS': ('1D','D1'), 'WES':('1C','B1')},
    'C2': {'NOR':('C2','C1'), 'SOU':('C3','C3'), 'EAS': ('2D','D2'), 'WES':('2C','B2')},
    'C3': {'NOR':('C3','C2'), 'SOU':('C4','C4'), 'EAS': ('3D','D3'), 'WES':('3C','B3')},
    'C4': {'NOR':('C4','C3'), 'SOU':('C5','C5'), 'EAS': ('4D','D4'), 'WES':('4C','B4')},
    'C5': {'NOR':('C5','C4'), 'SOU':('C6','XX'), 'EAS': ('5D','D5'), 'WES':('5C','B5')},
    'D1': {'NOR':('D1','XX'), 'SOU':('D2','D2'), 'EAS': ('1E','E1'), 'WES':('1D','C1')},
    'D2': {'NOR':('D2','D1'), 'SOU':('D3','D3'), 'EAS': ('2E','E2'), 'WES':('2D','C2')},
    'D3': {'NOR':('D3','D2'), 'SOU':('D4','D4'), 'EAS': ('3E','E3'), 'WES':('3D','C3')},
    'D4': {'NOR':('D4','D3'), 'SOU':('D5','D5'), 'EAS': ('4E','E4'), 'WES':('4D','C4')},
    'D5': {'NOR':('D5','D4'), 'SOU':('D6','XX'), 'EAS': ('5E','E5'), 'WES':('5D','C5')},
    'E1': {'NOR':('E1','XX'), 'SOU':('E2','E2'), 'EAS': ('1F','XX'), 'WES':('1E','D1')},
    'E2': {'NOR':('E2','E1'), 'SOU':('E3','E3'), 'EAS': ('2F','XX'), 'WES':('2E','D2')},
    'E3': {'NOR':('E3','E2'), 'SOU':('E4','E4'), 'EAS': ('3F','XX'), 'WES':('3E','D3')},
    'E4': {'NOR':('E4','E3'), 'SOU':('E5','E5'), 'EAS': ('4F','XX'), 'WES':('4E','D4')},
    'E5': {'NOR':('E5','E4'), 'SOU':('E6','XX'), 'EAS': ('5F','XX'), 'WES':('5E','D5')},
}

def log(msg):
    if DEBUG:
        print(":> %s" % (str(msg)))

def drawDoor(door, color):
    if door[0].isdigit():
        pygame.draw.line(screen, color, (doors[door]['coord'][0][0], doors[door]['coord'][0][1]-2), (doors[door]['coord'][1][0], doors[door]['coord'][1][1]-2), 5)
    else:
        pygame.draw.line(screen, color, (doors[door]['coord'][0][0]-2, doors[door]['coord'][0][1]), (doors[door]['coord'][1][0]-2, doors[door]['coord'][1][1]), 5)

def drawPlayer():
    pygame.draw.rect(screen, BLUE, playerLocations[playerLoc]['coord'])

def updateDoorStatus():
    for door in list(doors.keys()): # Redraw doors
        COLOR = (0,0,0)
        if doors[door]['status'].upper() == 'C':   # Closed Door
            COLOR = RED
        elif doors[door]['status'].upper() == 'O': # Open Door
            COLOR = GREEN
        elif doors[door]['status'].upper() == 'W': # Wall
            COLOR = WHITE
        elif doors[door]['status'].upper() == 'X': # Exit
            COLOR = PURPLE
        else:
            COLOR = ORANGE
        drawDoor(door, COLOR)

def updateSet(newStatus, changeSet):
    for door in list(doors.keys()):
        if doors[door]['set'] == changeSet:
            doors[door]['status'] = newStatus
        if doors[door]['set'] == matchSets[changeSet]:
            if newStatus == 'C':
                doors[door]['status'] = 'O'
            if newStatus == 'O':
                doors[door]['status'] = 'C'

    updateDoorStatus()

def doorClick():
        mouse = pygame.mouse.get_pos()
        for door in list(doors.keys()):
            doorToUpdate = ''
            if door[0].isdigit(): # Vertical
                if doors[door]['coord'][0][0]+10 > mouse[0] > doors[door]['coord'][0][0]-5 and doors[door]['coord'][0][1]+50 > mouse[1] > doors[door]['coord'][0][1]:
                    doorToUpdate = door
            else: # Horizontal
                if doors[door]['coord'][0][0]+50 > mouse[0] > doors[door]['coord'][0][0] and doors[door]['coord'][0][1]+10 > mouse[1] > doors[door]['coord'][0][1]-5:
                    doorToUpdate = door
            for dir in list(cells[playerLoc].keys()):
                if cells[playerLoc][dir][0] == doorToUpdate:
                    if doors[door]['status'] == 'C':
                        newStatus = 'O'
                    else:
                        newStatus = 'C'

                    changeSet = doors[doorToUpdate]['set']
                    log('door: %s, set: %s, status: %s' % (doorToUpdate, changeSet, newStatus))
                    if doors[doorToUpdate]['status'] != 'W' and doors[doorToUpdate]['status'] != 'X' and doors[doorToUpdate]['status'] != '':
                        doors[doorToUpdate]['status'] = newStatus
                        updateSet(newStatus, changeSet)
                    break

def playerMovement(key, playerLoc):
    dir = ''
    if key == pygame.K_UP:
        dir = 'NOR'
    if key == pygame.K_DOWN:
        dir = 'SOU'
    if key == pygame.K_LEFT:
        dir = 'WES'
    if key == pygame.K_RIGHT:
        dir = 'EAS'
    if dir != '':
        if doors[cells[playerLoc][dir][0]]['status'] == 'O':
            if cells[playerLoc][dir][1] != 'XX':
                playerLoc = cells[playerLoc][dir][1]
    return playerLoc

def drawPlayerSpaces():
    for loc in list(playerLocations.keys()):
            pygame.draw.rect(screen, GREY, playerLocations[loc]['coord']) #Player Spaces

if grid: # Displays grid as guide if enabled
    for i in range(1,7):
        pygame.draw.line(screen, WHITE, [i*100, 100], [i*100,600], 1) # Vertical
        screen.blit(font.render(alpha[i], True, WHITE),((i*100)-5, 70)) # Alpha characters
        pygame.draw.line(screen, WHITE, [100, i*100], [600,i*100], 1) # Horizontal
        screen.blit(font.render(str(i), True, WHITE),(80, (i*100)-10)) # Digits
    drawPlayerSpaces()

updateDoorStatus() # draw doors first time
drawPlayer() # draw player first time

while not exitcondition:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitcondition=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RALT or event.key==pygame.K_LALT:
                altkey=True
            elif event.key==pygame.K_F4:
                f4key=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RALT or event.key==pygame.K_LALT:
                altkey=False
            elif event.key==pygame.K_F4:
                f4key=False
        if event.type == pygame.MOUSEBUTTONUP:
            doorClick()
        if event.type == pygame.KEYDOWN:
            playerLoc = playerMovement(event.key, playerLoc)
            drawPlayerSpaces()
            drawPlayer()
    if altkey and f4key:
        exitcondition=True

    pygame.display.flip()