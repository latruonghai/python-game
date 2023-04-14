from shared.typings import Configuration, Player, Coordinate, Size


configuration: Configuration = {
  'caption': "Space Invader",
  'icon_str': './assets/img/spaceship.png',
  'player': Player('./assets/img/players.png', Coordinate(370, 30)),
  'background': (0, 0, 0),
  'size': Size(800, 600)
}
