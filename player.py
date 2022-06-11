import pygame
from data.data import LASERS, SHIPS
from laser import Laser
from enemy import Boss
from ship import Ship
from window import HEIGHT


class Player(Ship):
    def __init__(self, x: int, y: int,speed: int, health=100, laser_damage=1) -> None:
        super().__init__(x,y,speed,health,laser_damage)
        self.ship_img = SHIPS["yellow"]
        self.laser_img = LASERS["yellow"]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health 
        self.number_of_lasers_default = 1
        self.speed_default = speed
        self.reload_default = self.RELOAD
        self.number_of_lasers = self.number_of_lasers_default

    def move_lasers(self, vel: int, objs: list) -> None:
        self.reload()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else: 
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= self.laser_damage
                        if obj.health <= 0:
                            if type(obj) == Boss:
                                self.max_health += 10
                                self.speed_default += 1
                                self.RELOAD -= 5
                                self.reload_default = self.RELOAD
                            objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    def shoot(self) -> None:
        if self.reload_counter == 0:
            for i in range(self.number_of_lasers):
                if i == 0:
                    laser = Laser(self.x, self.y, self.laser_img, self.laser_damage)
                    self.lasers.append(laser)
                if i == 1:
                    laser = Laser(self.x-30, self.y, self.laser_img, self.laser_damage)
                    self.lasers.append(laser)
                if i == 2:
                    laser = Laser(self.x+30, self.y, self.laser_img, self.laser_damage)
                    self.lasers.append(laser)
            self.reload_counter = 1
        pass

    def drop_use(self, drop: object) -> None:
        if drop.drop_name == "lasers":
            self.number_of_lasers = drop.drop_effect
        elif drop.drop_name == "speed":
            self.speed = drop.drop_effect
        elif drop.drop_name == "reload":
            self.RELOAD = drop.drop_effect
        elif drop.drop_name == "hp":
            self.health = self.max_health

    def drop_timer(self, drop: object) -> None:
        pass
        
    def drop_expired(self, drop: object) -> None:
        if drop.drop_name == "lasers":
            self.number_of_lasers = self.number_of_lasers_default
        elif drop.drop_name == "speed":
            self.speed = self.speed_default
        elif drop.drop_name == "reload":
            self.RELOAD = self.reload_default


    def healthbar(self, window: pygame.Surface) -> None:
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

    def draw(self, window: pygame.Surface) -> None:
        super().draw(window)
        self.healthbar(window)