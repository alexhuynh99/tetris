import pygame


class Game:
    def __init__(self):
        pass

    def run(self):
        width = 400
        height = 800
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Tetris')
        clock = pygame.time.Clock()
        bg = pygame.image.load('board.png')
        bg = pygame.transform.scale(bg, (width, height))

        on = True
        while on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on = False
                print(event)

            display.blit(bg, (0, 0))
            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()


g = Game()
g.run()
