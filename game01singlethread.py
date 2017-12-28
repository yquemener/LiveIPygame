import pygame

pygame.init()
size = (500,500)
disp=pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
running = True
x=10
y=20
dirx=1
color = (255,255,255)

while( running ):
    disp.fill((0, 0, 0))
    pygame.draw.circle(disp, color, (x, y), 15)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False
    if x>500:
        dirx=-1
    if x<0:
        dirx=1
    x+=dirx
    pygame.time.delay(5)
pygame.quit()
