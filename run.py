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
        self.disappear_time = random.randint(5000, 10000)
        self.head_rect = pygame.Rect(x + self.width / 6, y, self.width / 1.5, self.height / 1.8)

    def display(self):
        pass
        current_time = pygame.time.get_ticks()
        if (current_time - self.appear_time < self.disappear_time):
            zombie_image = pygame.image.load("imgs\zom.png")
            zombie_image = pygame.transform.smoothscale(zombie_image, (self.width, self.height))
            self.screen.blit(zombie_image, (self.x, self.y))
            # pygame.draw.rect(self.screen, (0, 0, 255), self.head_rect)
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

            if (event.type == pygame.MOUSEBUTTONDOWN):
                """Check collision and remove zombie form zom list
                ** Use method ``collidepoint`` in pygame.Rect to check collision with mouse's position
                ** Find the last object (zombie) collision and delete it. Because the last object is in front of.
                """
                zom_delete = None
                for zom in reversed(zom_list):
                    if zom.head_rect.collidepoint(event.pos):
                        zom_delete = zom
                        break

                if (zom_delete): zom_list.remove(zom_delete)



        screen.blit(background, (0,0))
        
        # Screen always have 10 zombies
        if len(zom_list) < 10:
            zom = Zombie(screen, random.randint(0, SCREEN_WIDTH - 100), random.randint(0, SCREEN_HEIGHT - 100))
            zom_list.append(zom)

        # Display zombie in zom_list
        for zom in zom_list:
            if (not zom.display()):
                zom_list.remove(zom)

        pygame.display.update() # Update screen
        clock.tick(30) # FPS set to 30

run()