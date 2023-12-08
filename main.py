import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((width / 2, height), width, player_speed)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(display)
        # update all sprite groups
        # draw all sprite groups

if __name__ == '__main__':
    pygame.init()

    FPS = 60
    width = 600
    height = 600
    display_color_default = (30, 30, 30)
    display = pygame.display.set_mode((width, height))

    player_speed = 5

    clock = pygame.time.Clock()
    game = Game() # instance for Game class

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display.fill('white')
        display.fill(display_color_default)
        game.run()


        pygame.display.flip()
        clock.tick(FPS)