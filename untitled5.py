import pygame
pygame.init()
 
 
def turning(car_surf):  # Function turning car(need for using original car_surf every time)
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] \
            or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
        car_surf = pygame.transform.rotate(car_surf, turn)
        sc.fill(BLACK)
        sc.blit(car_surf, car_rect)
        pygame.display.update()
 
 
# Constants
FPS = 60
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
UP = 0
DOWN = 180
RIGHT = -90
LEFT = 90
speed = 3
 
sc = pygame.display.set_mode(SCREEN_SIZE)
sc.fill(BLACK)
clock = pygame.time.Clock()
 
car_surf = pygame.image.load('C:/Users/PPCPPPPPPPPPPPPPPPPP/Desktop/car.png')
car_rect = car_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))  # Set car in center of screen
sc.blit(car_surf, car_rect)
 
pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    # Change direct car moving with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        turn = UP
        car_rect.y -= speed
    elif keys[pygame.K_DOWN]:
        turn = DOWN
        car_rect.y += speed
    elif keys[pygame.K_RIGHT]:
        turn = RIGHT
        car_rect.x += speed
    elif keys[pygame.K_LEFT]:
        turn = LEFT
        car_rect.x -= speed
 
    turning(car_surf)
 
    clock.tick(FPS)