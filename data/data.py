import pygame, os

from window import HEIGHT, WIDTH


# Load enemy ship images
RED_SPACE_SHIP = pygame.image.load(os.path.join("data\images", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("data\images", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("data\images", "pixel_ship_green_small.png"))
SHIPS = dict()
SHIPS["red"] = RED_SPACE_SHIP
SHIPS["blue"] = BLUE_SPACE_SHIP
SHIPS["green"] = GREEN_SPACE_SHIP

# Load player ship image
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("data\images", "pixel_ship_yellow.png"))
SHIPS["yellow"] = YELLOW_SPACE_SHIP

# Load Laser images
RED_LASER = pygame.image.load(os.path.join("data\images", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("data\images", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("data\images", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("data\images", "pixel_laser_yellow.png"))
LASERS = dict()
LASERS["red"] = RED_LASER
LASERS["blue"] = BLUE_LASER
LASERS["green"] = GREEN_LASER
LASERS["yellow"] = YELLOW_LASER


# Load Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("data\images", "background-black.png")), (WIDTH, HEIGHT))

# Load Drops
LASERS_DROP = pygame.image.load(os.path.join("data\images", "pixel_lasers_drop.png"))
SPEED_DROP = pygame.image.load(os.path.join("data\images", "pixel_speed_drop.png"))
RELOAD_DROP = pygame.image.load(os.path.join("data\images", "pixel_reload_drop.png"))
EXPLOSION_DROP = pygame.image.load(os.path.join("data\images", "pixel_explosion_drop.png"))
HP_DROP = pygame.image.load(os.path.join("data\images", "pixel_hp_drop.png"))
HEART_DROP = pygame.image.load(os.path.join("data\images", "pixel_heart_drop.png"))
DROPS = dict()
DROPS["lasers"] = LASERS_DROP
DROPS["speed"] = SPEED_DROP
DROPS["reload"] = RELOAD_DROP
DROPS["explosion"] = EXPLOSION_DROP
DROPS["hp"] = HP_DROP
DROPS["heart"] = HEART_DROP