import pygame
def main (): 
    pygame.init()
    SH,SW=500,500
    screen=pygame.display.set_mode((SH,SW))
    pygame.display.set_caption("my first game")
    colors ={
        'red':pygame.color('red'),
        'green':pygame.color('green'),
        'blue':pygame.color('blue'),
        'yellow':pygame.color('yellow'),
        'white':pygame.color('white')
    }
    current__colour=colors('white')
    x,y=30,30
    spw,sph=60,60
    clock= pygame.time.Clock()
    done=False
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True    
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -=3
        if pressed[pygame.K_RIGHT]: x +=3
        if pressed[pygame.K_UP]: y -=3
        if pressed[pygame.K_DOWN]: y +=3
        x=min (max(0,x)),SW-spw
        y=min (max(0,y)),SH-sph
        if x == 0 : current__colour =colors ['blue']
        elif x ==SW-spw:current__colour =colors ['yellow']
        elif x == 0 : current__colour =colors ['red']
        elif y ==SH-sph:current__colour =colors ['green']
        else:
            current__colour=colors('white')
        screen.fill((255,255,255))
        pygame.draw.rect(screen,current__colour,
                        x,y,spw,sph )
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
    main()