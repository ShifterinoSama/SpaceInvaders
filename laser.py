import pygame

class Laser:
    def __init__(self, x: int, y: int, img, damage=1) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.damage = damage

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))

    def move(self, vel: int) -> None:
        self.y += vel

    def off_screen(self, height: int) -> bool:
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj: object) -> bool:
        return collide(self, obj)

def collide(obj1: object, obj2: object) -> bool:
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None