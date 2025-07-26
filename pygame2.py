import pygame3
pygame3.init()
SH,SW=500,500
screen=pygame3.display.set_mode((SH,SW))
pygame3.display.set_caption("my first game")
background_image = pygame3.transform.scale(
    pygame3.image.load('').convert(),
    (SH,SW))
done=False
while not done:
    for event in pygame3.event.get():
        if event.type==pygame3.QUIT:
            pygame3.quit()
    pygame3.display.flip()