import random
import pygame

pygame.init()

# Constants
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 700

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

# Background
# Step 1: Set up the two different backgrounds main_background & battle_background
main_background = pygame.image.load('coluseumBackground.png').convert_alpha()
main_background = pygame.transform.scale(main_background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background image

battle_background = pygame.image.load('battlebackground.jpeg').convert_alpha()
battle_background = pygame.transform.scale(battle_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player movement variables 
player_x = 0
player_y = 0
player_input = {"left": False, "right": False, "up": False, "down": False}
player_velocity = [0, 0]
player_speed = 10


# Keybinds - Defined Fuction "check_input"
def check_input(key, value):
    if event.key == pygame.K_a:
        player_input["left"] = value
        return 2 #Left = 2
    elif event.key == pygame.K_d:
        player_input["right"] = value
        return 1 #Right =1
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()

# Class - objects
class Player:
  # Define a function that initalizes a "Player" object
    def __init__(self, x, y, image_path, scale_factor, health_value):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))
        self.health_value = health_value

        # Step 4: Manually adjust rect size to fit visible sprite
        self.rect.width = int(self.rect.width * 0.7)  # Adjust width
        self.rect.height = int(self.rect.height * 0.7)  # Adjust height
        self.rect = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height * 0.3)
        

    # Copying player image onto rectangle
    def draw(self, screen, directionImg):
        self.image = directionImg
        screen.blit(self.image, self.rect.topleft)

    # Updating player position
    def update(self):
        #Step 3: Separate Movement Update & Collision Detection:
        new_rect = self.rect.move(player_velocity[0] * player_speed, player_velocity[1] * player_speed)
        return new_rect
    

class Enemy:
    def __init__(self, x, y, image_path, scale_factor):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))
        
        # Manually adjust rect size to fit visible sprite better
        self.rect.width = int(self.rect.width * 0.7)  # Adjust width
        self.rect.height = int(self.rect.height * 0.7)  # Adjust height
        self.rect = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height * 0.3)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

class Heart:
  # Define a function that initalizes a "Heart" object
  def __init__(self, x, y, image_path, scale_factor):
      self.image = pygame.image.load(image_path)
      self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
    # Use center coordinates instead of topleft
      self.rect = self.image.get_rect(center=(x, y)) 

  # Copying player image onto rectangle
  def draw(self, screen):
      screen.blit(self.image, self.rect.topleft)


# Creating player image
image = pygame.image.load("wizardplayerRight.png")

# Centering player
surf_center = (
    SCREEN_WIDTH - image.get_width() / 2,
    SCREEN_HEIGHT - image.get_height() / 2
)

# Creating the player object
wizardPlayer = Player(500, 557, 'wizardplayerRight.png', 1.75, 5)

# Creating enemy goblin
goblinEnemy = Enemy(1000, 475, 'Goblin.png', 1.5)

# Creating heart
heart5 = Heart(225, 40, 'hearts5.png', 0.75)
heart4 = Heart(225, 40, 'hearts4.png', 0.75)
heart3 = Heart(225, 40, 'hearts3.png', 0.75)
heart2 = Heart(225, 40, 'hearts2.png', 0.75)
heart1 = Heart(225, 40, 'hearts1.png', 0.75)
heart0 = Heart(225, 40, 'hearts0.png', 0.75)

# Start of game loop
clock = pygame.time.Clock()
running = True
playerDirection = pygame.image.load("wizardplayerRight.png")
scene = "main" #Initialize the scene

while running:
    #Start of the game for when the player loads in
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            check_input(event.key, True)
            if check_input(event.key, True) == 1:
                playerDirection = pygame.image.load("wizardplayerRight.png")
            elif check_input(event.key, True) == 2:
                playerDirection = pygame.image.load("wizardplayerLeft.png")
        elif event.type == pygame.KEYUP:
            check_input(event.key, False)

        # Player Movement
        player_velocity[0] = player_input["right"] - player_input["left"]
        player_velocity[1] = player_input["down"] - player_input["up"]

    #Step 2: Scene Management:
    if scene == "main":
        # Update player position
        new_rect = wizardPlayer.update()

        # Collision Detection
        if new_rect.colliderect(goblinEnemy.rect):
            scene = "battle"
        else:
            wizardPlayer.rect = new_rect

        # Update and draw main scene
        screen.blit(main_background, (0,0))
        wizardPlayer.draw(screen, playerDirection)
        goblinEnemy.draw(screen)

    elif scene == "battle":
        # Draw battle scene
        screen.blit(battle_background, (0,0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
