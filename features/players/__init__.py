from dataclasses import dataclass, InitVar
import pygame
from pygame.surface import Surface
from shared.typings import Player


@dataclass
class PlayerSetup():
  player: Player

  def setup(self, screen: Surface, **kwargs) -> None:
    if not kwargs:
      if not "player_img" in kwargs or not kwargs["player_img"]:
        kwargs["player_img"] = pygame.image.load(self.player.player_path)
      if not "position" in kwargs or not kwargs["position"]:
        kwargs["position"] = self.player.position.to_tuple()
    screen.blit(kwargs['player_img'], kwargs["position"])
  # def create
