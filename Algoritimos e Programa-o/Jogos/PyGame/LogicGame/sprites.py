import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.index = 3
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
            collide_rect = pg.Rect(self.rect.x + 12, (self.rect.y + 36) , 24, 12)
            collide_rect.x += dx * TILESIZE//2
            collide_rect.y += dy * TILESIZE//2
            if collide_rect.colliderect(wall):
                return True
        return False
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups =  game.walls
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
        self.groups =  game.actions
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

    def do_action(self):
        keys = pg.key.get_pressed()
        if(keys[pg.K_SPACE]):
            if(self.rect.colliderect(self.game.player.rect)):
                if(self.action == LAVAR_MAOS):
                    for i in range(3):
                        print("Esfregando as mãos."+"."*i)
                    print("Limpo!")
                elif(self.action == SECAR_MAOS):
                    for i in range(3):
                        print("Secando as mãos."+"."*i)
                    print("Secas!")
                elif(self.action == DESCARGA):
                    for i in range(3):
                        print("Dando descarga."+"."*i)
                    print("Flusshhhhh")
                elif(self.action == USAR_PAPEL):
                    for i in range(3):
                        print("Limpando a sujeira."+"."*i)
                    print("Limpo!") 
                elif(self.action == DESENTUPIR):
                    for i in range(3):
                        print("Desentupindo."+"."*i)
                    print("Saiuuu!") 
                elif(self.action == TOMAR_BANHO):
                    for i in range(3):
                        print("Tomando banho."+"."*i)
                    print("Limpo!")
    def update(self):
        self.do_action()


class ChooseAction(pg.sprite.Sprite):
        def __init__(self, game, x, y, action_index):
            self.groups =  game.player_actions
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.drag = False
            self.image = game.player_actions_imgs[action_index]
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y

        def get_action(self):
            event = self.game.evento
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.collidepoint(event.pos):
                        self.drag = True
                        self.game.mouse_img_active = self.game.mouse_img[1]
                        mouse_x, mouse_y = event.pos
                        self.offset_x = self.rect.x - mouse_x
                        self.offset_y = self.rect.y - mouse_y
            elif(event.type == pg.MOUSEBUTTONUP):
                if(event.button == 1):
                    self.drag = False
                    self.game.mouse_img_active = self.game.mouse_img[0]
            elif(event.type == pg.MOUSEMOTION):
                if self.drag:
                    self.game.mouse_img_active = self.game.mouse_img[1]
                    mouse_x, mouse_y = event.pos
                    self.rect.x = mouse_x + self.offset_x
                    self.rect.y = mouse_y + self.offset_y


        
        def update(self):
            self.get_action()



class PlayPauseAction(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups =  game.player_actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.playing = False
        self.index = 15
        self.mouse_hold = False
        self.image = self.game.player_actions_imgs[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_action(self):
        event = self.game.evento
        if (event.type == pg.MOUSEBUTTONDOWN and not self.playing and not self.mouse_hold):
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.image = self.game.player_actions_imgs[self.index-1]
                    self.playing = True
                    self.mouse_hold = True
        elif(event.type == pg.MOUSEBUTTONDOWN and self.playing and not self.mouse_hold):
            if(event.button == 1):
                if self.rect.collidepoint(event.pos):
                    self.image = self.game.player_actions_imgs[self.index]
                    self.playing = False
                    self.mouse_hold = True
        elif(event.type == pg.MOUSEBUTTONUP):
            self.mouse_hold = False


    def update(self):
        self.get_action()



class PlayerAction(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.rectmov_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    # def update(self):
    #     self.draw.rect(self.game.screen, RED, self.rect)

    # def acao(self):
    #     keys = pg.key.get_pressed()
    #     if(keys[pg.KEYDOWN]):
    #         if keys[pg.K_LEFT]:
    #             self.game.player.move(dx=-1,index=6)
    #             #self.player.rotate(index=6)
    #         if keys[pg.K_RIGHT]:
    #             self.game.player.move(dx=1,index=3)
    #             #self.player.rotate(index=3)
    #         if keys[pg.K_UP]:
    #             self.game.player.move(dy=-1,index=0)
    #             # self.player.rotate(index=0)
    #         if keys[pg.K_DOWN]:
    #             self.game.player.move(dy=1,index=9)
    #             # self.player.rotate(index=9)        
