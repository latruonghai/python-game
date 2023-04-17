from dataclasses import dataclass, InitVar, field
import pygame
from pygame.surface import Surface
from shared.typings import Player
from pygame.rect import RectType


@dataclass
class PlayerSetup():
  player: Player

  def setup(self, screen: Surface, **kwargs) -> None:
    if not kwargs:
      if not "player_img" in kwargs or not kwargs["player_img"]:
        kwargs["player_img"] = pygame.image.load(self.player.player_path)
      if not "position" in kwargs or not kwargs["position"]:
        kwargs["position"] = self.player.position.to_tuple()
    player_rect = screen.blit(kwargs['player_img'], kwargs["position"])
    self.set_player_size(player_rect)

  def set_player_size(self, size: RectType) -> None:
    self.player.set_player_size(size=size)
  # def create
