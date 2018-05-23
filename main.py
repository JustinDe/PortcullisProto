import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Portcullis prototyping')
screen = pygame.display.set_mode((700, 700))
font = pygame.font.SysFont("arial", 20)

WHITE  = (255, 255, 255)
GREY   = (240, 240, 240)
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

doors = {
    # Horizontal
    'A1': {'status': 'W', 'coord':((125,100),(175,100)), 'set': 'omega'},
    'A2': {'status': 'C', 'coord':((125,200),(175,200)), 'set': 'alpha'},
    'A3': {'status': 'C', 'coord':((125,300),(175,300)), 'set': 'alpha'},
    'A4': {'status': 'C', 'coord':((125,400),(175,400)), 'set': 'alpha'},
    'A5': {'status': 'C', 'coord':((125,500),(175,500)), 'set': 'alpha'},
    'A6': {'status': 'W', 'coord':((125,600),(175,600)), 'set': 'omega'},
    'B1': {'status': 'W', 'coord':((225,100),(275,100)), 'set': 'omega'},
    'B2': {'status': 'C', 'coord':((225,200),(275,200)), 'set': 'alpha'},
    'B3': {'status': 'C', 'coord':((225,300),(275,300)), 'set': 'beta'},
    'B4': {'status': 'C', 'coord':((225,400),(275,400)), 'set': 'beta'},
    'B5': {'status': 'C', 'coord':((225,500),(275,500)), 'set': 'alpha'},
    'B6': {'status': 'W', 'coord':((225,600),(275,600)), 'set': 'omega'},
    'C1': {'status': 'W', 'coord':((325,100),(375,100)), 'set': 'omega'},
    'C2': {'status': 'C', 'coord':((325,200),(375,200)), 'set': 'alpha'},
    'C3': {'status': 'C', 'coord':((325,300),(375,300)), 'set': 'alpha'},
    'C4': {'status': 'C', 'coord':((325,400),(375,400)), 'set': 'alpha'},
    'C5': {'status': 'C', 'coord':((325,500),(375,500)), 'set': 'alpha'},
    'C6': {'status': 'X', 'coord':((325,600),(375,600)), 'set': 'omega'},
    'D1': {'status': 'W', 'coord':((425,100),(475,100)), 'set': 'omega'},
    'D2': {'status': 'C', 'coord':((425,200),(475,200)), 'set': 'alpha'},
    'D3': {'status': 'C', 'coord':((425,300),(475,300)), 'set': 'beta'},
    'D4': {'status': 'C', 'coord':((425,400),(475,400)), 'set': 'alpha'},
    'D5': {'status': 'C', 'coord':((425,500),(475,500)), 'set': 'alpha'},
    'D6': {'status': 'W', 'coord':((425,600),(475,600)), 'set': 'omega'},
    'E1': {'status': 'W', 'coord':((525,100),(575,100)), 'set': 'omega'},
    'E2': {'status': 'C', 'coord':((525,200),(575,200)), 'set': 'alpha'},
    'E3': {'status': 'C', 'coord':((525,300),(575,300)), 'set': 'alpha'},
    'E4': {'status': 'C', 'coord':((525,400),(575,400)), 'set': 'alpha'},
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
    '3B': {'status': 'C', 'coord':((200,325),(200,375)), 'set': 'alpha'},
    '4B': {'status': 'C', 'coord':((200,425),(200,475)), 'set': 'alpha'},
    '5B': {'status': 'C', 'coord':((200,525),(200,575)), 'set': 'alpha'},
    '1C': {'status': 'C', 'coord':((300,125),(300,175)), 'set': 'alpha'},
    '2C': {'status': 'C', 'coord':((300,225),(300,275)), 'set': 'alpha'},
    '3C': {'status': 'C', 'coord':((300,325),(300,375)), 'set': 'alpha'},
    '4C': {'status': 'C', 'coord':((300,425),(300,475)), 'set': 'alpha'},
    '5C': {'status': 'C', 'coord':((300,525),(300,575)), 'set': 'alpha'},
    '1D': {'status': 'C', 'coord':((400,125),(400,175)), 'set': 'beta'},
    '2D': {'status': 'C', 'coord':((400,225),(400,275)), 'set': 'alpha'},
    '3D': {'status': 'C', 'coord':((400,325),(400,375)), 'set': 'alpha'},
    '4D': {'status': 'C', 'coord':((400,425),(400,475)), 'set': 'beta'},
    '5D': {'status': 'C', 'coord':((400,525),(400,575)), 'set': 'alpha'},
    '1E': {'status': 'C', 'coord':((500,125),(500,175)), 'set': 'alpha'},
    '2E': {'status': 'C', 'coord':((500,225),(500,275)), 'set': 'alpha'},
    '3E': {'status': 'C', 'coord':((500,325),(500,375)), 'set': 'alpha'},
    '4E': {'status': 'C', 'coord':((500,425),(500,475)), 'set': 'alpha'},
    '5E': {'status': 'C', 'coord':((500,525),(500,575)), 'set': 'alpha'},
    '1F': {'status': 'W', 'coord':((600,125),(600,175)), 'set': 'omega'},
    '2F': {'status': 'W', 'coord':((600,225),(600,275)), 'set': 'omega'},
    '3F': {'status': 'W', 'coord':((600,325),(600,375)), 'set': 'omega'},
    '4F': {'status': 'W', 'coord':((600,425),(600,475)), 'set': 'omega'},
    '5F': {'status': 'W', 'coord':((600,525),(600,575)), 'set': 'omega'},
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

def drawDoor(door, color):
    if door[0].isdigit():
        pygame.draw.line(screen, color, (doors[door]['coord'][0][0], doors[door]['coord'][0][1]-2), (doors[door]['coord'][1][0], doors[door]['coord'][1][1]-2), 5)
    else:
        pygame.draw.line(screen, color, (doors[door]['coord'][0][0]-2, doors[door]['coord'][0][1]), (doors[door]['coord'][1][0]-2, doors[door]['coord'][1][1]), 5)

def updateDoorStatus():
    for door in doors.keys(): # Redraw doors
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

def updateSet(door, newStatus, changeSet):
    for door in doors.keys():
        if doors[door]['set'] == changeSet:
            doors[door]['status'] = newStatus
    updateDoorStatus()

def doorClick():
        mouse = pygame.mouse.get_pos()
        for door in doors.keys():
            doorToUpdate = ''
            newStatus = ''
            if door[0].isdigit(): # Vertical
                if doors[door]['coord'][0][0]+10 > mouse[0] > doors[door]['coord'][0][0]-5 and doors[door]['coord'][0][1]+50 > mouse[1] > doors[door]['coord'][0][1]:
                    doorToUpdate = door
            else: # Horizontal
                if doors[door]['coord'][0][0]+50 > mouse[0] > doors[door]['coord'][0][0] and doors[door]['coord'][0][1]+10 > mouse[1] > doors[door]['coord'][0][1]-5:
                    doorToUpdate = door
                    
            if doorToUpdate != '':
                if doors[doorToUpdate]['status'] != 'W' and doors[doorToUpdate]['status'] != 'X':
                    if doors[door]['status'] == 'C':
                        newStatus = 'O'
                    else:
                        newStatus = 'C'

                changeSet = doors[door]['set']
                if newStatus != '': 
                    doors[doorToUpdate]['status'] = newStatus
                    updateSet(doorToUpdate, newStatus, changeSet)
                    print 'door %s clicked - changing set: %s to status: %s' % (doorToUpdate, changeSet, newStatus,)
                break

if grid: # Displays grid as guide if enabled
        for i in range(1,7):
            pygame.draw.line(screen, WHITE, [i*100, 100], [i*100,600], 1) # Vertical
            screen.blit(font.render(alpha[i], True, WHITE),((i*100)-5, 70)) # Alpha characters
            pygame.draw.line(screen, WHITE, [100, i*100], [600,i*100], 1) # Horizontal
            screen.blit(font.render(str(i), True, WHITE),(80, (i*100)-10)) # Digits

updateDoorStatus() # draw doors first time

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
            doorClick();
    if altkey and f4key:
        exitcondition=True

    for loc in playerLocations.keys():
        pygame.draw.rect(screen, GREY, playerLocations[loc]['coord']) #Player

    pygame.display.flip()