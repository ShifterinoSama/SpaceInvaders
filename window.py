import pygame

WIDTH, HEIGHT = 750,750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KENNY'S SPACE INVADERS")

class Window:
    def __init__(self, x: int ,y: int, img: object) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)