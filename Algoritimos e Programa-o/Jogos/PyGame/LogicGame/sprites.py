import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_imgs[1]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0, index=0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx * TILESIZE
            self.y += dy * TILESIZE
            self.image = self.game.player_imgs[index]

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            collide_rect = pg.Rect(self.rect.x, self.rect.y + self.rect.height/2, self.rect.width, self.rect.height/2)
            collide_rect.x += dx * TILESIZE
            collide_rect.y += dy * TILESIZE
            if collide_rect.colliderect(wall):
                return True
        return False
        

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class PlayerActions(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.action_img
        self.rect = self.image.get_rect()

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites,game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.image.set_alpha(100)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
