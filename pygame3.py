import pygame3

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame3.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame3.display.set_caption('Adding image and background image')
background_image = pygame3.transform.scale(
    pygame3.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))
penguin_image = pygame3.transform.scale(
    pygame3.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
                                              SCREEN_HEIGHT // 2 - 30))
text = pygame3.font.Font(None, 36).render('Hello World ', True,
                                         pygame3.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
def game_loop():
  clock = pygame3.time.Clock()
  running = True
  while running:
    for event in pygame3.event.get():
      if event.type == pygame3.QUIT:
        running = False
    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)
    display_surface.blit(text, text_rect)
    pygame3.display.flip()
    clock.tick(30)
  pygame3.quit()
if __name__ == '__main__':
  game_loop()
