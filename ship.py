import pygame
from laser import Laser
from window import HEIGHT


class Ship:
    RELOAD = 30

    def __init__(self,x: int ,y: int, speed: int, health=100, laser_damage=1) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.reload_counter = 0
        self.laser_damage = laser_damage
        self.speed = speed
        self.number_of_lasers = 1


    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel: int, obj: object) -> None:
        self.reload()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= laser.damage
                self.lasers.remove(laser)

    def reload(self) -> None:
        if self.reload_counter >= self.RELOAD:
            self.reload_counter = 0
        elif self.reload_counter > 0:
            self.reload_counter += 1

    def shoot(self, number_of_lasers=1) -> None:
        if self.reload_counter == 0:
            laser = Laser(self.x,self.y,self.laser_img, self.laser_damage)
            self.lasers.append(laser)
            self.reload_counter = 1

    def get_width(self) -> int:
        return self.ship_img.get_width()

    def get_height(self) -> int:
        return self.ship_img.get_height()