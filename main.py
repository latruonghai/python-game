import pygame
from configuration import configuration
from features.players import PlayerSetup
from features.screen import ScreenSetup
import shared.typings
# Create new game


# Create the  screen


# Game Loop

# Player
# player_img = pygame.image.load(configuration['player'].player_path)


# def player():
#   screen.blit(player_img, configuration['player'].position.to_tuple())


if __name__ == '__main__':
  # Create Game
  pygame.init()
  running = True
  keyEvent = None
  screen_setup = ScreenSetup(
    configuration['icon_str'], configuration["caption"], configuration["size"])
  screen = screen_setup.to_surface()
  screen_setup.setup()
  player = configuration["player"]
  player_setup = PlayerSetup(player)
  while running:
    screen.fill(configuration['background'])
    for event in pygame.event.get():
      match event.type:
        case pygame.KEYDOWN:
          keyEvent = event
        case pygame.QUIT:
          running = False
        case pygame.KEYUP:
          keyEvent = None
        case default:
          pass
    if keyEvent != None:
      player.move(event=keyEvent, screen=screen)
    player_setup.setup(screen)
    pygame.display.update()
  # pygame.
