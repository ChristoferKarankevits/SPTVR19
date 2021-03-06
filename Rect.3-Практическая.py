import pygame
pygame.init()
 
# Constants
FPS = 60
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 400, 400
RED = (230, 20, 30)
YELLOW = (230, 200, 20)
BLACK = (0, 0, 0)
rect_width = WIN_WIDTH // 2
rect_height = WIN_HEIGHT // 2
rect_size = (rect_width, rect_height) # Common Rect() size
BACK_COLOR = BLACK
CIRCLE_COLOR = YELLOW # Initial circle color
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(SCREEN_SIZE)
sc.fill(BACK_COLOR)
 
rect_1 = pygame.Rect((0, 0), rect_size)
rect_2 = pygame.Rect((rect_width, 0), rect_size)
rect_3 = pygame.Rect((rect_width, rect_height), rect_size)
rect_4 = pygame.Rect((0, rect_height), rect_size)
 
surf_1 = pygame.Surface(rect_size)
surf_2 = pygame.Surface(rect_size)
surf_3 = pygame.Surface(rect_size)
surf_4 = pygame.Surface(rect_size)
 
surf_1.fill(BACK_COLOR)
surf_2.fill(BACK_COLOR)
surf_3.fill(BACK_COLOR)
surf_4.fill(BACK_COLOR)
 
sc.blit(surf_1, rect_1)
sc.blit(surf_2, rect_2)
sc.blit(surf_3, rect_3)
sc.blit(surf_4, rect_4)
 
circle_update = (rect_1, rect_2, rect_3, rect_4) # Updating Rects
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT or \
                i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
            exit()
        if i.type == pygame.KEYDOWN: # Selection of updating Rects
            if i.key == pygame.K_1:
                circle_update = (rect_1, rect_3)
            elif i.key == pygame.K_2:
                circle_update = (rect_2, rect_4)
            elif i.key == pygame.K_0:
                circle_update = (rect_1, rect_2, rect_3, rect_4)
 
    if True: # Change color cycle
        if CIRCLE_COLOR == YELLOW:
            CIRCLE_COLOR = RED
        elif CIRCLE_COLOR == RED:
            CIRCLE_COLOR = YELLOW
        pygame.draw.circle(sc, CIRCLE_COLOR, (WIN_WIDTH // 2, WIN_HEIGHT // 2), 100)
        pygame.display.update(circle_update)
        pygame.time.delay(500)
 
    clock.tick(FPS)