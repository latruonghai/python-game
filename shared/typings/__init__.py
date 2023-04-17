from dataclasses import dataclass, field
from typing import TypedDict
from abc import abstractmethod, ABC
from pygame.event import Event
from pygame.surface import Surface
import pygame
from pygame.rect import RectType


@dataclass
class Coordinate:
  x: int
  y: int

  def to_tuple(self) -> tuple:
    return (self.x, self.y)


@dataclass
class Player():
  player_path: str
  position: Coordinate
  player_detail: RectType = field(init=False)

  def __post_init__(self):
    self._position = self.position.to_tuple()

  def set_player_size(self, size: RectType) -> None:
    self.player_detail = size

  def __get_size__(self):
    return self.player_detail[2::]

  def __moving_area__(self, size: tuple[int, int]) -> tuple[int, int]:
    width, height = self.__get_size__()
    print('width, height: ', width, height)
    return (size[0] - width, size[1]-height)

  def move(self, event: Event, screen: Surface) -> None:
    # self.__get_size__()
    if event.type == pygame.KEYDOWN:
      self.width, self.height = self.__moving_area__(screen.get_size())
      match event.key:
        case pygame.K_RIGHT:
          self.move_to_right()
        case pygame.K_LEFT:
          self.move_to_left()
        case pygame.K_DOWN:
          self.move_backward()
        case pygame.K_UP:
          self.move_forward()
        case default:
          return

  def move_to_left(self):
    if self.position.x > 0:
      self.position.x -= 0.1

  def move_to_right(self):
    if self.position.x < self.width:
      self.position.x += 0.1

  def move_forward(self):
    if self.position.y > 0:
      self.position.y -= 0.1

  def move_backward(self):
    print('move_backward: ')
    if self.position.y < self.height:
      self.position.y += 0.1


@dataclass
class Size:
  width: int
  height: int

  def to_tuple(self) -> tuple:
    return (self.width, self.height)


class Configuration(TypedDict):
  caption: str
  icon_str: str
  player: Player
  background: tuple[int, int, int]
  size: Size
