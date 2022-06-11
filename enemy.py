import pygame
from data.data import LASERS, SHIPS  
from laser import Laser
from ship import Ship


class Enemy(Ship):
    COLOR_MAP = {
                "red": (SHIPS["red"], LASERS["red"]),
                "blue": (SHIPS["blue"], LASERS["blue"]),
                "green": (SHIPS["green"], LASERS["green"])
                }


    def __init__(self, x: int, y: int,speed:int, color: str, health=10, laser_damage=1) -> None:
        super().__init__(x, y,speed, health, laser_damage)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel: int) -> None:
        self.y += vel
    
    def shoot(self) -> None:
        if self.reload_counter == 0:
            laser = Laser(self.x-20,self.y,self.laser_img, self.laser_damage)
            self.lasers.append(laser)
            self.reload_counter = 1


class Boss(Enemy):

    COLOR_MAP = {
                "red": (SHIPS["red"], LASERS["red"]),
                "blue": (SHIPS["blue"], LASERS["blue"]),
                "green": (SHIPS["green"], LASERS["green"])
                }

    def __init__(self, x: int, y: int,speed:int, color: str, health: int, laser_damage: int, number_of_lasers: int) -> None:
        super().__init__(x,y,speed,color,health, laser_damage)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.ship_img = pygame.transform.scale2x(self.ship_img)
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.number_of_lasers = number_of_lasers

    def shoot(self) -> None:
        if self.reload_counter == 0:
            laser = Laser(self.x-10,self.y,self.laser_img, self.laser_damage)
            self.lasers.append(laser)
            laser = Laser(self.x-40,self.y,self.laser_img, self.laser_damage)
            self.lasers.append(laser)
            laser = Laser(self.x+20,self.y,self.laser_img, self.laser_damage)
            self.lasers.append(laser)
            self.reload_counter = 1