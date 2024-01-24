import pygame

def run():
    pass
    # Init pygame
    pygame.init()

    # Set up display
    SCREEN_WIDTH = 750
    SCREEN_HEIGHT = 520
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ZomBonkBonk")
    pygame.display.update()


    """Running Game Loop"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

run()