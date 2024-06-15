import random
import pygame

pygame.init()

# Constants

# Step 1: Make a bottom_panel constant
bottom_panel = 200

WHITE = (255, 255, 255)
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 700

# Creating player image
wizardImage = pygame.image.load("wizardplayerRight.png")
goblinImage = pygame.image.load('Goblin.png')

# Screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

# Backgrounds
start_background = pygame.image.load('TitleScreen.png').convert_alpha()

main_background = pygame.image.load('coluseumBackground.png').convert_alpha()
main_background = pygame.transform.scale(main_background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale the background image

battle_background = pygame.image.load('battlebackground.jpeg').convert_alpha()
battle_background = pygame.transform.scale(battle_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Step 2: Load wooden panel image + function for drawing the panel
panel_img = pygame.image.load('wooden_panel.png').convert_alpha()
panel_img = pygame.transform.scale(panel_img, (1440, bottom_panel))

def drawPanel():
    screen.blit(panel_img, (0, SCREEN_HEIGHT - bottom_panel))

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
    def __init__(self, x, y, image_path, scale_factor):
        self.image = pygame.image.load(image_path)
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.image, (1000, 400))
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.width = int(self.rect.width * 0.7)  # Adjust width
        self.rect.height = int(self.rect.height * 0.7)  # Adjust height
        self.rect = self.rect.inflate(-self.rect.width * 1.75, -self.rect.height * 0.3)
        

    # Copying player image onto rectangle
    def draw(self, screen, directionImg):
        self.image = directionImg
        screen.blit(self.image, self.rect)

    # Updating player position
    def update(self):
        new_rect = self.rect.move(player_velocity[0] * player_speed, player_velocity[1] * player_speed)
        return new_rect
    
class Enemy:
    def __init__(self, x, y, image_path, scale_factor):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.rect.width = int(self.rect.width * 0.7)  # Adjust width
        self.rect.height = int(self.rect.height * 0.7)  # Adjust height
        self.rect = self.rect.inflate(-self.rect.width * 1.01, -self.rect.height * 0.3)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

# Step 3: Create new classes for battle portion of game
class BattlePlayer:
    def __init__(self, x, y, att_val, def_val, hp_val):
        self.att_val = att_val
        self.def_val = def_val
        self.hp_val = hp_val
        self.alive = True
        self.image = pygame.transform.scale(wizardImage, (600,300))
        self.rect = self.image.get_rect() #Note: Rect is a hidden property which takes width and height of picture and position it on screen
        self.rect.center = (x,y) # Position rectangle @ (x,y) coordinate

    def draw(self): # Note: Whenever creating methods within a class you need to include "self" in the parameter as a minimum
        screen.blit(self.image, self.rect)

class BattleEnemy:
    def __init__(self, x, y, att_val, hp_val, imagePath):
        self.att_val = att_val
        self.hp_val = hp_val
        self.image = imagePath
        self.image = pygame.transform.scale(self.image, (500,700))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Button():
    def __init__(self, x, y, image_path, scale):
        # Load the image using pygame.image.load()
        self.image = pygame.image.load(image_path)
        
        # Get the size of the image and apply the scaling
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))

        # Set the rect attributes for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        print(f"Button initialized at position: {self.rect.topleft} with size: {self.rect.size}")

        self.clicked = False

    def draw(self, surface):
        #Draw Button on screen
        surface.blit(self.image, (600, 350))

    def utility(self):
        action = False
        #Get mouse position
        pos = pygame.mouse.get_pos()
        #print(f"Mouse position: {pos}")

        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            #print("Mouse is over the button")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                #print("Clicked")
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        return action


# Creating buttons needed through game
start_button = Button(600, 350, 'startButton.png', 0.5)

# Creating the "player" and "goblin" for the initial interaction.
wizardPlayer = Player(150, 500, 'wizardplayerRight.png', 1.75)
goblinEnemy = Enemy(1000, 375, 'Goblin.png', 2)

# Step 4: Create the "battlePlayer" and "battleEnemy" for battle sequence
battleWizard = BattlePlayer(250, SCREEN_HEIGHT - bottom_panel - 85, 1, 1, 15)
battleGoblin = BattleEnemy(1150, (SCREEN_HEIGHT - bottom_panel - 135), 5, 10, goblinImage)

# Creating heart Note(5/21): Commenting these out first maybe turn this into a loop when in the battle screen?
'''
heart5 = Heart(225, 40, 'hearts5.png', 0.75)
heart4 = Heart(225, 40, 'hearts4.png', 0.75)
heart3 = Heart(225, 40, 'hearts3.png', 0.75)
heart2 = Heart(225, 40, 'hearts2.png', 0.75)
heart1 = Heart(225, 40, 'hearts1.png', 0.75)
heart0 = Heart(225, 40, 'hearts0.png', 0.75)
'''

# Start of game loop
clock = pygame.time.Clock()
running = True
playerDirection = pygame.image.load("wizardplayerRight.png")
scene = "startScreen" #Initialize the scene

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

    #Scene Management:
    if scene == "startScreen":
        start_button_clicked = start_button.utility()
        #Load Title Screen
        screen.blit(start_background, (0,0))
        start_button.draw(screen)
        if start_button_clicked:
            scene = "main"

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

        # Draw the wooden panel at the bottom
        drawPanel()

        # Draw the scaled enemies
        battleWizard.draw()
        battleGoblin.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
