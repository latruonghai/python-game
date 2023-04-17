import pygame
from shared.typings import Player
from dataclasses import dataclass
from pygame.event import Event


@dataclass
class SpaceShip(Player):
  player_path: str = './spaceship.png'
