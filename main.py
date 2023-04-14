import pygame
from configuration import configuration
from features.players import PlayerSetup
from features.screen import ScreenSetup
import shared.typings
# Create new game
pygame.init()

# Create the  screen


# Game Loop

# Player
# player_img = pygame.image.load(configuration['player'].player_path)
running = True


# def player():
#   screen.blit(player_img, configuration['player'].position.to_tuple())


if __name__ == '__main__':
  player_setup = PlayerSetup(configuration["player"])
  screen_setup = ScreenSetup(
    configuration['icon_str'], configuration["caption"], configuration["size"])
  screen = screen_setup.to_surface()
  screen_setup.setup()
  while running:
    screen.fill(configuration['background'])
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    player_setup.setup(screen)
    pygame.display.update()
  # pygame.
