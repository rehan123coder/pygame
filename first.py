import pygame
pygame.init()
SH,SW=500,500
screen=pygame.display.set_mode((SH,SW))
pygame.display.set_caption("my first game")
screen.fill((255,255,255))
green=(0,255,0)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(125,75,35),pygame.Rect(30,30,100,100))
    pygame.draw.rect(screen,(125,75,35),pygame.Rect(130,130,100,100),5)
    pygame.draw.circle(screen,green,(300,300),50)
    pygame.draw.circle(screen,green,(400,400),50,5)
    pygame.display.flip()