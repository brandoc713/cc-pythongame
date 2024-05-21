import pygame

pygame.init()

# Constants
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

# Background
background = pygame.image.load('coluseumBackround.png').convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background image

# Player movement variables 
player_x = 0
player_y = 0
player_input = {"left": False, "right": False, "up": False, "down": False}
player_velocity = [0, 0]
player_speed = 10



# Keybinds - Defined Fuction "check_input"
def check_input(key, value):
    if event.key == pygame.K_LEFT:
        player_input["left"] = value
        return 2 #Left = 2
    elif event.key == pygame.K_RIGHT:
        player_input["right"] = value
        return 1 #Right =1
    elif event.key == pygame.K_UP:
        player_input["up"] = value
    elif event.key == pygame.K_DOWN:
        player_input["down"] = value
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()

# Class - objects
class Player:
    # Define a function that initalizes a "Player" object
    def __init__(self, x, y, image_path, scale_factor):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        # Use center coordinates instead of topleft
        self.rect = self.image.get_rect(center=(x, y)) 

    # Copying player image onto rectangle
    def draw(self, screen, directionImg):
        self.image = directionImg
        screen.blit(self.image, self.rect.topleft)

    # Updating player position
    def update(self):
        self.rect.move_ip(player_velocity[0] * player_speed, player_velocity[1] * player_speed)

class Enemy:
    def __init__(self, x, y, image_path, scale_factor):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))

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
wizardPlayer = Player(500, 500, 'wizardplayerRight.png', 1.5)

# Creating the enemy object
enemyGoblin = Enemy(750, 500, 'goblin.png', 1.5)

# Start of game loop
clock = pygame.time.Clock()
running = True
playerDirection = pygame.image.load("wizardplayerRight.png")
check_collison = 0

while running:
    #screen.fill(WHITE)
    check_collison = 0
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

    # Collision Detection
    if pygame.sprite.collide_rect(wizardPlayer, enemyGoblin):
        check_collison = 1
        if check_collison == 1:
            print("Encounter Here!")
    else:
        check_collison = 0    

    #Calling an the Update function to adjust where player is and then Draw function to put it onto the screen
    screen.blit(background, (0, 0))
    wizardPlayer.update()
    wizardPlayer.draw(screen, playerDirection)

    enemyGoblin.draw(screen)


    # pygame.display.flip() after the call to blit(). This updates the entire screen with everything that’s been drawn since the last flip.  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()