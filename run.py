import pygame
import random

# Zombie object
class Zombie:
    pass
    def __init__(self) -> None:
        pass
    
    # Constructor
    def __init__(self, screen, x, y, width=65, height=100, sprite_list_appear = [], sprite_list_dead = []):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.appear_frame = 0
        self.dead_frame = 0
        
        self.sprite_list_appear = sprite_list_appear
        self.sprite_list_dead = sprite_list_dead

        self.last_update = pygame.time.get_ticks()
        self.appear_time = pygame.time.get_ticks()
        self.disappear_time = random.randint(2000, 3000)
        self.head_rect = None
        
        # Flag
        self.is_killed = False

    def display(self):
        pass
        current_time = pygame.time.get_ticks()
        animation_wait = 100
        animation_dead_wait = 175
        if (self.is_killed):
            current_animate_time = pygame.time.get_ticks()
            if current_animate_time - self.last_update >= animation_dead_wait:
                if self.dead_frame < 5: self.dead_frame += 1
                self.last_update = current_animate_time
            
            current_sprite = self.sprite_list_dead[self.dead_frame]

            self.screen.blit(current_sprite, (self.x + 147 / 2 - current_sprite.get_size()[0] / 2, self.y + 80/2 - current_sprite.get_size()[1] / 2))
            if (self.dead_frame == 5): return False
            else: return True
        else:
            if (current_time - self.appear_time < self.disappear_time):
                current_animate_time = pygame.time.get_ticks()
                if current_animate_time - self.last_update >= animation_wait:
                    if self.appear_frame < 6: self.appear_frame += 1
                    self.last_update = current_animate_time
                
                current_sprite = self.sprite_list_appear[self.appear_frame]

                self.screen.blit(current_sprite, (self.x + 147 / 2 - current_sprite.get_size()[0] / 2, self.y + 155/2 - current_sprite.get_size()[1] / 2))
                if (self.appear_frame == 6): 
                    self.head_rect = pygame.Rect(self.x + self.sprite_list_appear[-1].get_size()[0] / 4.1, self.y + self.sprite_list_appear[-1].get_size()[0] / 8, 103, 73)
                    # pygame.draw.rect(self.screen, (0, 0, 255), self.head_rect)
                return True
            elif (current_time - self.appear_time > self.disappear_time + 1000):
                return False
            else:
                current_animate_time = pygame.time.get_ticks()
                if current_animate_time - self.last_update >= animation_wait:
                    if self.appear_frame > 0: self.appear_frame -= 1
                    self.last_update = current_animate_time
                
                current_sprite = self.sprite_list_appear[self.appear_frame]
                self.screen.blit(current_sprite, (self.x + 147 / 2 - current_sprite.get_size()[0] / 2, self.y + 155/2 - current_sprite.get_size()[1] / 2))
                return True
        

        

# Sprite Sheet processing
class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey((0,0,0))
        return sprite
    
class Text():
    def __init__(self, screen, font_name, size, outFont=False):
        self.font_name = font_name
        self.size = size
        self.font = None
        self.rect = None
        self.outFont = outFont
        self.screen = screen

    def render(self, text, left=0, top=0, center=None, color="white"):
        self.font = pygame.font.SysFont(self.font_name, self.size) if (self.outFont == False) else pygame.font.Font(self.font_name, self.size)
        display = self.font.render(text, True, color)
        self.rect = display.get_rect()
        self.rect.topleft = (left, top)
        if (center):
            self.rect.center = center
        self.screen.blit(display, self.rect)
    
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

    #Set background image
    background = pygame.image.load("imgs/game_background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
    screen.blit(background, (0,0))

    # Load sprite sheet zombie
    zom_sprites_appear = Spritesheet("imgs/zom_sprite_2.png")
    sprite_list_appear = []
    sprite_list_appear.append(zom_sprites_appear.get_sprite(0, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114 * 2, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114 * 3, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114 * 4, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114 * 5, 0, 114, 158))
    sprite_list_appear.append(zom_sprites_appear.get_sprite(114 * 6, 0, 114, 158))
    
    zom_sprites_dead = Spritesheet("imgs/zom_sprite_3.png")
    sprite_list_dead = []
    sprite_list_dead.append(zom_sprites_dead.get_sprite(0, 0, 133, 203))
    sprite_list_dead.append(zom_sprites_dead.get_sprite(133, 0, 133, 203))
    sprite_list_dead.append(zom_sprites_dead.get_sprite(133 * 2, 0, 133, 203))
    sprite_list_dead.append(zom_sprites_dead.get_sprite(133 * 3, 0, 133, 203))
    sprite_list_dead.append(zom_sprites_dead.get_sprite(133 * 4, 0, 133, 203))
    sprite_list_dead.append(zom_sprites_dead.get_sprite(133 * 5, 0, 133, 203))

    # Define list to handle zombies
    zom_list = []
    tomb_pos_list = [(87, 326), (326, 326), (565, 326), (804, 326), (1043, 326),
                    (87, 550), (326, 550), (565, 550), (804, 550), (1043, 550)]


    point = 0
    miss = 0

    #Define text in game
    text = Text(screen, r'assets\04B_19.TTF', 30, True)

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
                    if (zom.head_rect):
                        if zom.head_rect.collidepoint(event.pos):
                            zom_delete = zom
                            zom.is_killed = True
                            break

                if (zom_delete): 
                    # zom_list.remove(zom_delete)
                    point += 1
                else: miss += 1

        screen.blit(background, (0,0))
        
        text.render('SCORE: ' + str(point), 10, 10, color='green')
        text.render('MISS: ' + str(miss), 250, 10, color="red")
        accuracy = (point*1.0 / (point + miss)) * 100 if point+miss != 0 else 0
        if round(accuracy,2) == 100.00 and miss > 0 : accuracy = 99.99
        text.render('ACCURACY: ' + str(round(accuracy, 2)) + " %", 10, 50, color="Yellow")

        # sp1 = sprite_list_dead[6]
        # screen.blit(sp1, (720, 50))
        
        # Screen always have n zombies
        if len(zom_list) < 5:
            zom_pos = random.choice(tomb_pos_list)
            while (not check_exits_zom_pos(zom_list, zom_pos)):
                zom_pos = random.choice(tomb_pos_list)
            zom = Zombie(screen, zom_pos[0], zom_pos[1], sprite_list_appear=sprite_list_appear, sprite_list_dead=sprite_list_dead)
            zom_list.append(zom)

        # Display zombie in zom_list
        for zom in zom_list:
            if (not zom.display()):
                zom_list.remove(zom)

        pygame.display.flip() # Update screen
        clock.tick(240) # FPS set to 60

run()