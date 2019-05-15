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
        self.startpos = (x, y)
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

    def reset_pos(self):
        self.rect.x = self.startpos[0]
        self.rect.y = self.startpos[1]

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

    # def do_action(self):
    #     keys = pg.key.get_pressed()
    #     # if(keys[pg.K_SPACE]):
    #     #     if(self.rect.colliderect(self.game.player.rect)):
    #     #         if(self.action == LAVAR_MAOS):
    #     #             for i in range(3):
    #     #                 print("Esfregando as mãos."+"."*i)
    #     #             print("Limpo!")
    #     #         elif(self.action == SECAR_MAOS):
    #     #             for i in range(3):
    #     #                 print("Secando as mãos."+"."*i)
    #     #             print("Secas!")
    #     #         elif(self.action == DESCARGA):
    #     #             for i in range(3):
    #     #                 print("Dando descarga."+"."*i)
    #     #             print("Flusshhhhh")
    #     #         elif(self.action == USAR_PAPEL):
    #     #             for i in range(3):
    #     #                 print("Limpando a sujeira."+"."*i)
    #     #             print("Limpo!") 
    #     #         elif(self.action == DESENTUPIR):
    #     #             for i in range(3):
    #     #                 print("Desentupindo."+"."*i)
    #     #             print("Saiuuu!") 
    #     #         elif(self.action == TOMAR_BANHO):
    #     #             for i in range(3):
    #     #                 print("Tomando banho."+"."*i)
    #     #             print("Limpo!")

    # def update(self):
    #     self.do_action()


class ChooseAction(pg.sprite.Sprite):
    def __init__(self, game, x, y, action_index):
        self.groups =  game.player_actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.drag = False
        self.action_index = action_index
        self.image = game.player_actions_imgs[action_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startpos = (x, y)
        self.added = False

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
                    self.added = False
        elif(event.type == pg.MOUSEBUTTONUP):
            if(event.button == 1):
                self.drag = False
                self.game.mouse_img_active = self.game.mouse_img[0]
                if self.rect.colliderect(self.game.playerActionHolder.rect):
                    if(not self.added):
                        self.game.playerActionHolder.add_action(self)
                        self.added = True
        elif(event.type == pg.MOUSEMOTION):
            if self.drag:
                self.game.mouse_img_active = self.game.mouse_img[1]
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y


        
    def update(self):
        self.get_action()

    
    def reset_pos(self):
        if(self.action_index == LOOP_IND):
            self.rect.x = 2000
            self.rect.y = 2000 #paliativo para destruir o loop antigo
            LoopAction(self.game, self.startpos[0], self.startpos[1])
        else:
            self.rect.x = self.startpos[0]
            self.rect.y = self.startpos[1]

    def execute(self):
        if(self.action_index == MOVER_CIMA_IND):
            self.game.player.move(dy=-1,index=0)
        if(self.action_index == MOVER_BAIXO_IND):
            self.game.player.move(dy=1,index=9)
        if(self.action_index == MOVER_ESQUERDA_IND):
            self.game.player.move(dx=-1,index=6)
        if(self.action_index == MOVER_DIREITA_IND):
            self.game.player.move(dx=1,index=3)
        # if(self.action_index == ABRIR_TORNEIRA_IND):

        # if(self.action_index == FECHAR_TORNEIRA_IND):

        # if(self.action_index == ABRIR_TAMPA_IND):

        # if(self.action_index == DAR_DESCARGA_IND):

        # if(self.action_index == FECHAR_TAMPA_IND):

        # if(self.action_index == DESENTUPIDOR_IND):

        # if(self.action_index == LAVAR_MAOS_ACTION_IND):

        # if(self.action_index == SECAR_MAOS_ACTION_IND):

        # if(self.action_index == PAPEL_ACTION_IND):

        if(self.action_index == LOOP_IND):
            n = self.loop_cycles
            for i in range(n):
                if(self.loop_action == MOVER_CIMA_IND):
                    self.game.player.move(dy=-1,index=0)
                if(self.loop_action == MOVER_BAIXO_IND):
                    self.game.player.move(dy=1,index=9)
                if(self.loop_action == MOVER_ESQUERDA_IND):
                    self.game.player.move(dx=-1,index=6)
                if(self.loop_action == MOVER_DIREITA_IND):
                    self.game.player.move(dx=1,index=3)
                self.game.update()
                self.game.draw()
                pg.time.wait(80)
            





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
                    self.play()
        elif(event.type == pg.MOUSEBUTTONDOWN and self.playing and not self.mouse_hold):
            if(event.button == 1):
                if self.rect.collidepoint(event.pos):
                    self.image = self.game.player_actions_imgs[self.index]
                    self.playing = False
                    self.mouse_hold = True
                    self.pause()
        elif(event.type == pg.MOUSEBUTTONUP):
            self.mouse_hold = False
        


    def update(self):
        self.get_action()

    def play(self):
        self.game.playerActionHolder.execute_action()

    
    def pause(self):
        print("reset")
        self.game.playerActionHolder.actions_list = []
        self.game.player.reset_pos()




class PlayerActionHolder(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.rectmov_img
        self.rect = self.image.get_rect()
        self.actions_list = []
        self.after_loop = False
        self.index = 0
        self.x = x
        self.y = y

    def add_action(self, action):
        if(action.action_index == LOOP_IND):
            self.after_loop = True
            self.actions_list.append(action)
            self.index = len(self.actions_list)-1
        elif(self.after_loop):
            self.after_loop = False
            loop = self.actions_list[self.index]
            print(loop)
            loop.loop_action = action.action_index
            loop = None
            self.actions_list.append(action)
        else:
            self.actions_list.append(action)
        action.reset_pos()

    def show_action(self, surface):
        posx = 30
        posy = 135
        self.loopImage = False
        self.is_loop = False
        for action in self.actions_list:
            self.imagem = action.image
            self.imagem_rect = self.imagem.get_rect()
            self.imagem_rect.x = posx
            self.imagem_rect.y = posy
            if(self.is_loop):
                self.is_loop = False
                self.imagem_rect.x = self.loop_pos[0] + 8
                self.imagem_rect.y = self.loop_pos[1] + 4
                self.loopImage = True

            if(self.imagem == self.game.player_actions_imgs[LOOP_IND]):
                self.is_loop = True
                self.loop_pos = (posx , posy)
                self.loop_rect = self.imagem_rect

            
            if(not self.is_loop and not self.loopImage):
                posy += 51
                if(posy > 552):
                    posy = 135
                    posx += 104
                if(posx >= 104*4):
                    posx = 30
            else:
                posy += 36
                if(posy > 552):
                    posy = 135
                    posx += 104
                if(posx >= 104*4):
                    posx = 30   

            surface.blit(self.imagem, self.imagem_rect)
            if(self.loopImage):
                surface.blit(self.game.player_actions_imgs[LOOP_IND], self.loop_rect)
                self.loopImage = False

    def execute_action(self):
        if(self.game.playPauseAction.playing):
            for action in self.actions_list:
                action.execute()
                self.game.update()
                self.game.draw()
                pg.time.wait(80)
            self.game.playPauseAction.playing = False
            self.game.playPauseAction.image =  self.game.player_actions_imgs[15]




class PlayerActionChooser(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups =  game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.rectchoose_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class LoopAction(ChooseAction):
    def __init__(self, game, x, y, action_index = LOOP_IND):
        ChooseAction.__init__(self, game, x, y, action_index)
        self.loop_action = 0
        self.loop_cycles = 5
        





class ActionAnimation(pg.sprite.Sprite):
    pass