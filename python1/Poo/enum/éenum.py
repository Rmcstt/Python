from enum import Enum, auto

class Directions(Enum):
  right = auto()
  left = auto()
  up = auto()
  down = auto()

def move(directions):
  if not isinstance(directions, Directions):
    raise TypeError(f'expected Directions not {type(directions).__name__}')
  
  return f'moving {directions.name}'

if __name__ == '__main__': # serve para executar o codigo apenas se o arquivo for executado diretamente
  print(move(Directions.right))
  print(move(Directions.left))
  print(move(Directions.up))
  print(move(Directions.down))

  print()

  for direction in Directions:
    print(direction, direction.value, direction.name)