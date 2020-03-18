#1
import pygame
pygame.init()
 
sc = pygame.display.set_mode((400, 400))
 
rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((30, 30, 30, 30))
 
print(rect1.bottomright)  # вывод (30, 30)
print(rect2.bottomright)  # (60, 60)
 
rect2.move_ip(10, 10)
print(rect2.topleft)  # (40, 40)
 
rect1.union_ip(rect2)
print(rect1.width)  # 70
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
#2
import pygame
pygame.init()
 
sc = pygame.display.set_mode((300, 300))
sc.fill((200, 255, 200))
 
surf1 = pygame.Surface((200, 200))
surf1.fill((220, 200, 0))  # желтая
surf2 = pygame.Surface((100, 100))
surf2.fill((255, 255, 255))  # белая
 
rect = pygame.Rect((70, 20, 0, 0))
 
surf1.blit(surf2, rect)
sc.blit(surf1, rect)
 
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
#3
import pygame
pygame.init()
 
sc = pygame.display.set_mode((300, 300))
sc.fill((200, 255, 200))
 
surf2 = pygame.Surface((100, 100))
surf2.fill((255, 255, 255))  # белая
 
rect = surf2.get_rect()  # создается Rect
 
print(surf2.get_width())  # вывод 100
print(rect.width)  # 100
print(rect.x, rect.y)  # 0 0
 
sc.blit(surf2, rect)
pygame.display.update()
 
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    rect.x += 1
 
    sc.fill((200, 255, 200))
    sc.blit(surf2, rect)
    pygame.display.update()
 
    pygame.time.delay(20)