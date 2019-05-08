import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.index = 0
        self.image = game.player_imgs[self.index]
        self.rect = self.image.get_rect()
        # Rect de Colisão
        # self.rect = pg.Rect(self.rect.x + 12, (self.rect.y + 24) , 24, 24)
        # self.image = pg.Surface((self.rect.width, self.rect.height))
        # self.image.fill(YELLOW)
        # self.image.set_alpha(100)
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0, index=0):
        if not self.collide_with_walls(dx,dy):
            if(dx==0 and dy==0):
                self.image = self.game.player_imgs[index]
            elif(self.image == self.game.player_imgs[index+1]):
                self.image = self.game.player_imgs[index+2]
            elif(self.image == self.game.player_imgs[index+2]):
                self.image = self.game.player_imgs[index+1]
            else:
                self.image =  random.choice([self.game.player_imgs[index+1], self.game.player_imgs[index+2]])
            self.x += dx * TILESIZE//2
            self.y += dy * TILESIZE//2
        else:
            self.image = self.game.player_imgs[index]

    def rotate(self, index):
        self.image = self.game.player_imgs[index]

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            collide_rect = pg.Rect(self.rect.x + 12, (self.rect.y + 24) , 24, 24)
            collide_rect.x += dx * TILESIZE//2
            collide_rect.y += dy * TILESIZE//2
            if collide_rect.colliderect(wall):
                return True
        return False
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class PlayerAction(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.player_actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.action_img
        self.rect = self.image.get_rect()

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

class ActionObstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, action):
        self.groups = game.all_sprites, game.walls, game.actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.action = action
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.image.set_alpha(100)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    # def do_action(self, action):
    #     if(action == 'towel'):


