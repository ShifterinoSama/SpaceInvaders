import pygame

from data.data import DROPS

class Drop:
    DROP_LIST = ["lasers", "speed", "reload", "hp", "heart", "explosion"]
    NUMBER_OF_LASERS = 3
    SPEED_BOOST = 10
    RELOAD_BOOST = 5
    EXPLOSION_DAMAGE = 10
    HP_GAIN = 5
    HEART_GAIN = 2

    DROP_MAP = {
                "lasers": (DROPS["lasers"], NUMBER_OF_LASERS),
                "speed": (DROPS["speed"], SPEED_BOOST),
                "reload": (DROPS["reload"], RELOAD_BOOST),
                "hp": (DROPS["hp"], HP_GAIN),
                "heart": (DROPS["heart"], HEART_GAIN),
                "explosion": (DROPS["explosion"], EXPLOSION_DAMAGE)
                }

    def __init__(self, x: int, y: int, value: int) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.drop_name = self.DROP_LIST[self.value]
        self.drop_img, self.drop_effect = self.DROP_MAP[self.drop_name]
        self.mask = pygame.mask.from_surface(self.drop_img)      

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.drop_img, (self.x, self.y))

    def move(self, vel: int) -> None:
        self.y += vel

    def get_width(self) -> int:
        return self.drop_img.get_width()

    def get_height(self) -> int:
        return self.drop_img.get_height()