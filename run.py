import pygame
import random

# Zombie object
class Zombie:
    pass
    def __init__(self) -> None:
        pass
    
    # Constructor
    def __init__(self, screen, zom_sprites, x, y, width=65, height=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.zom_sprites = zom_sprites
        self.appear_frame = 0
        self.sprite_list = []

        # self.sprite_list.append(self.zom_sprites.get_sprite(31, 79, 56, 36))
        # self.sprite_list.append(self.zom_sprites.get_sprite(31 + 108 - 18, 59, 108, 68))
        # self.sprite_list.append(self.zom_sprites.get_sprite(31 + 108*2 - 18, 59, 108, 68))
        # self.sprite_list.append(self.zom_sprites.get_sprite(31 + 108*3 - 9, 35, 108, 92))
        # self.sprite_list.append(self.zom_sprites.get_sprite(31 + 108*4 - 3, 27, 108, 128))
        # self.sprite_list.append(self.zom_sprites.get_sprite(31 + 108*5 - 3, 27, 108, 128))
        # self.sprite_list.append(self.zom_sprites.get_sprite(41 + 108*6, 3, 108, 128))

        self.sprite_list.append(self.zom_sprites.get_sprite(0, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114 * 2, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114 * 3, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114 * 4, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114 * 5, 0, 114, 158))
        self.sprite_list.append(self.zom_sprites.get_sprite(114 * 6, 0, 114, 158))

        self.last_update = pygame.time.get_ticks()
        self.appear_time = pygame.time.get_ticks()
        self.disappear_time = random.randint(5000, 10000)
        self.head_rect = pygame.Rect(x, y, 103, 63)

    def display(self):
        pass
        current_time = pygame.time.get_ticks()
        animation_wait = 250
        if (current_time - self.appear_time < self.disappear_time):
            current_animate_time = pygame.time.get_ticks()
            if current_animate_time - self.last_update >= animation_wait:
                if self.appear_frame < 6: self.appear_frame += 1
                self.last_update = current_animate_time
            
            current_sprite = self.sprite_list[self.appear_frame]
            
            self.screen.blit(current_sprite, (self.x + 147 / 2 - current_sprite.get_size()[0] / 2, self.y + 155/2 - current_sprite.get_size()[1] / 2))
            # pygame.draw.rect(self.screen, (0, 0, 255), self.head_rect)
            return True
        else:
            return False
        

# Sprite Sheet processing
class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey((0,0,0))
        return sprite
    
def check_exits_zom_pos(zom_list, zom_pos):
    for zom in zom_list:
        if zom.x == zom_pos[0] and zom.y == zom_pos[1]: return False
    
    return True

def run():
    pass
    # Init pygame
    pygame.init()

    # Set up display
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # For set frame per second (FPS)
    pygame.display.set_caption("ZomBonk")
    pygame.display.update()

    #Set background image
    background = pygame.image.load("imgs/game_background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
    screen.blit(background, (0,0))
    # pygame.display.update()

    # Load sprite sheet zombie
    zom_sprites = Spritesheet("imgs/zom_sprite_2.png")

    # Define list to handle zombies
    zom_list = []
    tomb_pos_list = [(87, 326), (326, 326), (565, 326), (804, 326), (1043, 326),
                    (87, 550), (326, 550), (565, 550), (804, 550), (1043, 550)]
    zom_pos_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

        # Two line above for test each sprite
        sp1 = zom_sprites.get_sprite(114*6, 0, 114, 158)
        screen.blit(sp1, tomb_pos_list[0])

        """Uncomment this code to run general"""
        # Screen always have n zombies
        # if len(zom_list) < 1:
        #     zom_pos = random.randint(0, 9)
        #     if (zom_pos_list[zom_pos] == 1):
        #         zom_pos = random.randint(0, 9)
        #     zom = Zombie(screen, zom_sprites, tomb_pos_list[zom_pos][0], tomb_pos_list[zom_pos][1])
        #     zom_list.append(zom)

        # # Display zombie in zom_list
        # for zom in zom_list:
        #     if (not zom.display()):
        #         zom_list.remove(zom)

        pygame.display.update() # Update screen
        clock.tick(30) # FPS set to 30

run()