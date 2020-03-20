import pygame
pygame.init()
 
FPS = 30
H, W = 500, 500
font = pygame.font.Font(pygame.font.match_font('dejavusans'), 36)
 
WHITE = (255, 255, 255)
BLACK = (50, 50, 50)
GREEN = (0, 255, 0)
 
sc = pygame.display.set_mode((H,W))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
 
x, y = 0, 0
text1 = font.render('Здравствуйте! Это Крис', 1, (180,0,0))
 
surf_master = pygame.Surface((50, 50))
 
surf_slave = pygame.Surface((100,100))
slave_x = 50
slave_y = 100
slave_rect = pygame.Rect(slave_x, slave_y, surf_slave.get_size()[0], \
                         surf_slave.get_size()[1])
 
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
 
    master_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], \
                          surf_master.get_size()[0], surf_master.get_size()[1])
 
    sc.fill(WHITE)
    surf_master.fill(BLACK)
    surf_slave.fill(GREEN)
 
    sc.blit(surf_slave, (slave_x, slave_y))
    sc.blit(surf_master, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
 
    if slave_rect.contains(master_rect) == 1:
        sc.blit(text1, (H//3,W//2))
 
    pygame.display.update()
    clock.tick(FPS)