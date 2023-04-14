from dataclasses import dataclass
import pygame
from pygame.surface import Surface
from shared.typings import Size


@dataclass
class ScreenSetup:
  icon: str
  caption: str
  size: Size

  def setup(self):
    pygame.display.set_caption(self.caption)
    pygame.display.set_icon(self._icon)

  def __post_init__(self):
    self._icon = pygame.image.load(self.icon)
    self._screen = pygame.display.set_mode(self.size.to_tuple())

  def to_surface(self) -> Surface:
    return self._screen
