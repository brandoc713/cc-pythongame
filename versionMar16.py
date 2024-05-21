import pygame

pygame.init()

#Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAME_RATE = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

'''
image = pygame.image.load('knight.png')
imagerect = image.get_rect()

surf_center = (
  (SCREEN_WIDTH-image.get_width())/2,
  (SCREEN_HEIGHT-image.get_height())/2
) 
'''

player_x = 0
player_y = 0
player_input = {"left": False, "right": False, "up": False, "down": False}
player_velocity = [0, 0]
player_speed = 20

def check_input(key, value):
  if event.key == pygame.K_LEFT:
    player_input["left"] = value
  elif event.key == pygame.K_RIGHT:
    player_input["right"] = value
  elif event.key == pygame.K_UP:
    player_input["up"] = value
  elif event.key == pygame.K_DOWN:
    player_input["down"] = value

#Class - objects
class Player:
  def __init__(self, x, y, image_path):
    self.x = x
    self.y = y
    self.image = pygame.image.load(image_path)
    self.rect = self.image.get_rect()

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def update(self):
    self.rect.topleft = (self.x, self.y)


knightPlayer = Player(100, 100, 'knight.png')

clock = pygame.time.Clock()
running = True
while running:
    screen.fill("white")
    #screen.blit(image, surf_center)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player_input["left"] = True
          elif event.key == pygame.K_RIGHT:
              player_input["right"] = True
          elif event.key == pygame.K_UP:
              player_input["up"] = True
          elif event.key == pygame.K_DOWN:
              player_input["down"] = True
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              player_input["left"] = False
          elif event.key == pygame.K_RIGHT:
              player_input["right"] = False
          elif event.key == pygame.K_UP:
              player_input["up"] = False
          elif event.key == pygame.K_DOWN:
              player_input["down"] = False

      player_velocity[0] = player_input["right"] - player_input["left"]
      player_velocity[1] = player_input["down"] - player_input["up"]

      player_x += player_velocity[0] * player_speed
      player_y += player_velocity[1] * player_speed

      knightPlayer.x = player_x
      knightPlayer.y = player_y

      knightPlayer.update()
      knightPlayer.draw(screen)

      pygame.display.flip()
      clock.tick(60)


pygame.quit()
