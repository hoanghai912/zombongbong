import pygame
import random

# Zombie object
class Zombie:
    pass
    def __init__(self) -> None:
        pass
    
    # Constructor
    def __init__(self, screen, x, y, width=100, height=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.appear_time = pygame.time.get_ticks()
        self.disappear_time = random.randint(2000, 4000)

    def display(self):
        pass
        current_time = pygame.time.get_ticks()
        if (current_time - self.appear_time < self.disappear_time):
            zombie_image = pygame.image.load("imgs\zom.png")
            zombie_image = pygame.transform.smoothscale(zombie_image, (self.width, self.height))
            self.screen.blit(zombie_image, (self.x, self.y))
            return True
        else:
            return False
        

def run():
    pass
    # Init pygame
    pygame.init()

    # Set up display
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # For set frame per second (FPS)
    pygame.display.set_caption("ZomBonk")
    pygame.display.update()

    #Set background image
    background = pygame.image.load("imgs/background.jpg")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (0,0))
    pygame.display.update()

    # Define list to handle zombies
    zom_list = []
    
    """Running Game Loop"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(zom_list)

        screen.blit(background, (0,0))
        
        if len(zom_list) < 10:
            zom = Zombie(screen, random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 100))
            zom_list.append(zom)

        
        for zom in zom_list:
            if (not zom.display()):
                zom_list.remove(zom)

        pygame.display.update()
        clock.tick(30) # FPS set to 30

run()