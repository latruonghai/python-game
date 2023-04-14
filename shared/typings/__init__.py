from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Coordinate:
  x: int
  y: int

  def to_tuple(self) -> tuple:
    return (self.x, self.y)


@dataclass
class Player:
  player_path: str
  position: Coordinate


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
