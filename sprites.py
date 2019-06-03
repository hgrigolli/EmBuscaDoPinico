import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.player_sprite
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.index = 3
        self.image = game.player_imgs[self.index]
        self.rect = self.image.get_rect()
        self.startpos = (x, y)

        #player actions
        self.tampa_aberta = False
        self.toneira_aberta = False
        self.deu_descarga = False
        self.evacuou = False
        self.lavou_maos = False
        self.secou_maos = False
        self.calcas_abaixadas = False
        self.usou_papel = False
        self.score = 0
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0, index=0, loop=False):
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
            if(loop):
                self.score += ANDAR_COM_LOOP_SCORE
            else:
                self.score += ANDAR_SCORE
        else:
            ActionAnimation(self.game).blocked()
            self.score -= ANDAR_COM_LOOP_SCORE
            self.image = self.game.player_imgs[index]

    def rotate(self, index):
        self.image = self.game.player_imgs[index]

    def reset_pos(self):
        self.x = self.startpos[0]
        self.y = self.startpos[1]

        self.tampa_aberta = False
        self.toneira_aberta = False
        self.deu_descarga = False
        self.evacuou = False
        self.lavou_maos = False
        self.secou_maos = False
        self.calcas_abaixadas = False
        self.usou_papel = False

        self.score = 0
        self.image = self.game.player_imgs[self.index]

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
        self.inputbox = None



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
                        if(self.action_index == LOOP_IND):
                            self.inputbox = InputBox(self.game)
                        self.game.playerActionHolder.add_action(self)
                        self.added = True
                        if(self.inputbox is not None and self.inputbox.valid):
                            self.inputbox.kill()
                # elif(not self.rect.colliderect(self.game.playerActionHolder.rect)):
                #     self.reset_pos()
                # comentado pois está quebrando o fps.
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
            self.kill()
            LoopAction(self.game, self.startpos[0], self.startpos[1])
        else:
            self.rect.x = self.startpos[0]
            self.rect.y = self.startpos[1]


    def nao_pode_exec_acao(self):
        ActionAnimation(self.game, txt="Ação Não Permitida").action_not_allowed()

    def execute(self, posx, posy):
        acoes_do_player = pg.sprite.groupcollide(self.game.actions, self.game.player_sprite, False, False)
        fez_acao = False
        
        #AÇÕES
        if(not self.game.player.calcas_abaixadas):
            if(self.action_index == MOVER_CIMA_IND):
                i = 0
                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                while(i < PLAYER_STEPS):
                    if(pg.time.get_ticks() >= next_move):
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        self.game.player.move(dy=-1,index=0)
                        self.game.update()
                        self.game.draw()
                        i += 1
                        print("Andando cima sem loop ", (posx,posy) )
                        
                    pg.draw.circle(self.game.screen, WHITE, (posx, posy), RADIUS, 3)
                    pg.display.flip()


            if(self.action_index == MOVER_BAIXO_IND):
                i = 0
                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                while(i < PLAYER_STEPS):
                    if(pg.time.get_ticks() >= next_move):
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        self.game.player.move(dy=1,index=9)
                        self.game.update()
                        self.game.draw()
                        i += 1
                        print("Andando Baixo sem loop ", (posx,posy) )

                    pg.draw.circle(self.game.screen, LIGHTGREY, (posx, posy), RADIUS, 3)
                    pg.display.flip()


            if(self.action_index == MOVER_ESQUERDA_IND):
                i = 0
                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                while(i < PLAYER_STEPS):
                    if(pg.time.get_ticks() >= next_move):
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        self.game.player.move(dx=-1,index=6)
                        self.game.update()
                        self.game.draw()
                        print("Andando Esquerda sem loop ", (posx,posy) )
                        i += 1
                    pg.draw.circle(self.game.screen, YELLOW, (posx, posy), RADIUS, 3)
                    pg.display.flip()


            if(self.action_index == MOVER_DIREITA_IND):
                i = 0
                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                while(i < PLAYER_STEPS):
                    if(pg.time.get_ticks() >= next_move):
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        self.game.player.move(dx=1,index=3)
                        self.game.update()
                        self.game.draw()
                        i += 1
                        print("Andando Direita sem loop ", (posx,posy) )

                    pg.draw.circle(self.game.screen, GREEN, (posx, posy), RADIUS, 3)
                    pg.display.flip()
        else:
            print("levante as calças antes de andar")

        if(self.action_index == ABRIR_TORNEIRA_IND):
            for acao in acoes_do_player:
                if acao.action == ABRIR_TORNEIRA_ACTION and not self.game.player.toneira_aberta:
                    print("Abrindo torneira...")
                    fez_acao = True

                    pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
                    
                    self.game.player.toneira_aberta = True
                    self.game.map.toggle_pia(self.game.player.toneira_aberta)
                    self.game.sink_sound.play(loops=1)
                    self.game.player.score += ABRIR_TORNEIRA_SCORE
                    self.game.scoreBoard.player_scores[1].done = True
                    break
                elif(acao.action == ABRIR_TORNEIRA_ACTION):
                    print("A torneira ja está aberta!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.game.player.score -= ABRIR_TORNEIRA_SCORE
                self.nao_pode_exec_acao()

        if(self.action_index == FECHAR_TORNEIRA_IND):
            for acao in acoes_do_player:
                if acao.action == FECHAR_TORNEIRA_ACTION and self.game.player.toneira_aberta:
                    print("Fechando torneira...")
                    fez_acao = True
                    self.game.player.toneira_aberta = False
                    self.game.map.toggle_pia(self.game.player.toneira_aberta)
                    self.game.player.score += FECHAR_TORNEIRA_SCORE
                    self.game.scoreBoard.player_scores[3].done = True
                    break
                elif(acao.action == FECHAR_TORNEIRA_ACTION):
                    print("A torneira ja está fechada!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.game.player.score -= FECHAR_TORNEIRA_SCORE
                self.nao_pode_exec_acao()
            
            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == ABRIR_TAMPA_IND):
            for acao in acoes_do_player:
                if acao.action == ABRIR_TAMPA_ACTION and not self.game.player.tampa_aberta:
                    self.game.player.tampa_aberta = True
                    fez_acao = True
                    self.game.map.toggle_vaso(self.game.player.tampa_aberta)
                    self.game.open_lid.play()
                    self.game.vaso_poop_sound.play(loops=2)
                    self.game.player.score += ABRIR_TAMPA_SCORE
                    self.game.scoreBoard.player_scores[5].done = True
                    break
                elif(acao.action == ABRIR_TAMPA_ACTION):
                    print("A tampa já está aberta!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= ABRIR_TAMPA_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == FECHAR_TAMPA_IND):
            for acao in acoes_do_player:
                if acao.action == FECHAR_TAMPA_ACTION and self.game.player.tampa_aberta:
                    self.game.player.tampa_aberta = False
                    fez_acao = True
                    self.game.open_lid.play()
                    self.game.map.toggle_vaso(self.game.player.tampa_aberta)
                    self.game.player.score += FECHAR_TAMPA_SCORE
                    self.game.scoreBoard.player_scores[7].done = True
                    break
                elif(acao.action == FECHAR_TAMPA_ACTION):
                    print("A tampa já está fechada!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= FECHAR_TAMPA_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()


        if(self.action_index == DAR_DESCARGA_IND):
            for acao in acoes_do_player:
                if acao.action == DAR_DESCARGA and not self.game.player.deu_descarga:
                    print("Dando descarga...\nFlushhhhhh")
                    fez_acao = True
                    self.game.player.deu_descarga = True
                    self.game.vaso_flush.play()
                    self.game.player.score += DAR_DESCARGA_SCORE
                    self.game.scoreBoard.player_scores[9].done = True
                    break
                elif(acao.action == DAR_DESCARGA) and self.game.player.deu_descarga:
                    print("Você já deu descarga, economize água!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= DAR_DESCARGA_SCORE
            
            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()


        if(self.action_index == LAVAR_MAOS_ACTION_IND):
            for acao in acoes_do_player:
                if acao.action == LAVAR_MAOS and self.game.player.toneira_aberta:
                    self.game.player.lavou_maos = True
                    print("Lava uma mão..\nLava outra, lava uma mão..")
                    fez_acao = True
                    self.game.lava_mao_sound.play()
                    self.game.player.score += LAVAR_MAOS_SCORE
                    self.game.scoreBoard.player_scores[11].done = True
                    break
                elif(acao.action == LAVAR_MAOS and not self.game.player.toneira_aberta):
                    print("Você precisa abrir a torneira antes de lavar as mãos.")
                    fez_acao = True
                    self.game.player.score -= LAVAR_MAOS_SCORE
                    break
                elif(acao.action == LAVAR_MAOS):
                    print("Suas mãos já estão limpas.\nEconomize água")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= LAVAR_MAOS_SCORE
            
            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == SECAR_MAOS_ACTION_IND):
            for acao in acoes_do_player:
                if acao.action == SECAR_MAOS and self.game.player.lavou_maos and not self.game.player.secou_maos:
                    self.game.player.secou_maos = True
                    self.game.towel_sound.play()
                    self.game.map.toggle_toalha(self.game.player.secou_maos)
                    self.game.player.score += SECAR_MAOS_SCORE
                    self.game.scoreBoard.player_scores[13].done = True
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= SECAR_MAOS_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == PAPEL_ACTION_IND):
            for acao in acoes_do_player:
                if acao.action == USAR_PAPEL and not self.game.player.usou_papel:
                    print("Papel!")
                    self.game.papel_sound.play()
                    self.game.player.usou_papel = True
                    self.game.player.score += USAR_PAPEL_SCORE
                    self.game.scoreBoard.player_scores[15].done = True
                    fez_acao = True
                    break
                elif(acao.action == USAR_PAPEL):
                    print("Você já se limpou, não disperdice papel!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= USAR_PAPEL_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == PANTS_DOWN_IND):
            for acao in acoes_do_player:
                if acao.action == ABAIXAR_CALCAS_ACTION and not self.game.player.calcas_abaixadas:
                    self.game.player.calcas_abaixadas = True
                    self.game.player.score += ABAIXAR_CALCAS_SCORE
                    self.game.pants_down_sound.play()
                    self.game.scoreBoard.player_scores[17].done = True
                    print("Tirando a calça..")
                    fez_acao = True
                    break
                elif(acao.action == ABAIXAR_CALCAS_ACTION):
                    print("Você já está sem calças!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= ABAIXAR_CALCAS_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == PANTS_UP_IND):
            for acao in acoes_do_player:
                if acao.action == LEVANTAR_CALCAS_ACTION and self.game.player.calcas_abaixadas:
                    self.game.player.calcas_abaixadas = False
                    self.game.pants_up_sound.play()
                    self.game.player.score += LEVANTAR_CALCAS_SCORE
                    self.game.scoreBoard.player_scores[19].done = True
                    print("Colocando a calça...\nZip!")
                    fez_acao = True
                    break
                elif(acao.action == LEVANTAR_CALCAS_ACTION):
                    print("Você já está de calças!")
                    fez_acao = True
                    break
            if(not fez_acao):
                self.nao_pode_exec_acao()
                self.game.player.score -= LEVANTAR_CALCAS_SCORE

            pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
            pg.display.flip()

        if(self.action_index == LOOP_IND):
            n = self.loop_cycles
            if(not self.game.player.calcas_abaixadas): #não pode andar de calças abaixadas
                for i in range(1,n):
                    if(self.loop_action == MOVER_CIMA_IND):
                        j = 0
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        while(j < PLAYER_STEPS):
                            if(pg.time.get_ticks() >= next_move):
                                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                                self.game.player.move(dy=-1,index=0,loop=True)
                                self.game.update()
                                self.game.draw()
                                self.game.draw_text('Repetições restantes: {}'.format(n-i), 16, TEXT_DARK_BLUE, 120, 10)
                                pg.display.flip()
                                print("Andando cima com loop ", (posx,posy) )
                                j += 1
                            pg.draw.circle(self.game.screen, RED, (posx+8, posy+4), RADIUS, 3)
                            pg.display.flip()

                    elif(self.loop_action == MOVER_BAIXO_IND):
                        j = 0
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        while(j < PLAYER_STEPS):
                            if(pg.time.get_ticks() >= next_move):
                                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                                self.game.player.move(dy=1,index=9,loop=True)
                                self.game.update()
                                self.game.draw()
                                self.game.draw_text('Repetições restantes: {}'.format(n-i), 16, TEXT_DARK_BLUE, 120, 10)
                                pg.display.flip()
                                print("Andando baixo com loop ", (posx,posy) ) 
                                j += 1
                            pg.draw.circle(self.game.screen, RED, (posx+8, posy+4), RADIUS, 3)
                            pg.display.flip()
                    
                    elif(self.loop_action == MOVER_ESQUERDA_IND):
                        j = 0
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        while(j < PLAYER_STEPS):
                            if(pg.time.get_ticks() >= next_move):
                                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                                self.game.player.move(dx=-1,index=6,loop=True)
                                self.game.update()
                                self.game.draw()
                                self.game.draw_text('Repetições restantes: {}'.format(n-i), 16, TEXT_DARK_BLUE, 120, 10)
                                pg.display.flip()
                                print("Andando direita esquerda loop ", (posx,posy) )
                                j += 1
                            pg.draw.circle(self.game.screen, RED, (posx+8, posy+4), RADIUS, 3)
                            pg.display.flip()

                    elif(self.loop_action == MOVER_DIREITA_IND):
                        j = 0
                        next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                        while(j < PLAYER_STEPS):
                            if(pg.time.get_ticks() >= next_move):
                                next_move = pg.time.get_ticks() + PLAYER_TIME_WAIT
                                self.game.player.move(dx=1,index=3,loop=True)
                                self.game.update()
                                self.game.draw()
                                self.game.draw_text('Repetições restantes: {}'.format(n-i), 16, TEXT_DARK_BLUE, 120, 10)
                                pg.display.flip()
                                print("Andando direita com loop ", (posx,posy) )
                                j += 1
                            pg.draw.circle(self.game.screen, RED, (posx+8, posy+4), RADIUS, 3)
                            pg.display.flip()
                    else:
                        break

                    self.game.update()
                    self.game.draw()
                    self.game.draw_text('Repetições restantes: {}'.format(n-i), 16, TEXT_DARK_BLUE, 120, 10)
                    pg.display.flip()
            else:
                print("não pode andar de calças abaixadas. Levante as calças")
        
            

class PlayPauseAction(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups =  game.player_actions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.playing = False
        self.index = PLAY_IND
        self.mouse_hold = False
        self.image = self.game.player_actions_imgs[self.index]
        self.rect = self.image.get_rect()
        self.played = False
        self.rect.x = x
        self.rect.y = y

    def get_action(self):
        pg.event.pump()
        event = self.game.evento
        if (event.type == pg.MOUSEBUTTONDOWN and not self.mouse_hold and not self.played):
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.image = self.game.player_actions_imgs[PAUSE_IND]
                    self.playing = True
                    self.mouse_hold = True
                    self.played = True
                    self.play()
        elif(event.type == pg.MOUSEBUTTONDOWN and not self.mouse_hold and self.played):
            if(event.button == 1):
                if self.rect.collidepoint(event.pos):
                    self.image = self.game.player_actions_imgs[PLAY_IND]
                    self.played = False
                    self.mouse_hold = True
                    self.reset()
        elif(event.type == pg.MOUSEBUTTONUP):
            self.mouse_hold = False
        


    def update(self):
        self.get_action()

    def play(self):
        self.game.playerActionHolder.execute_action()

    
    def reset(self):
        self.game.playerActionHolder.actions_list = []
        self.game.player.reset_pos()
        self.game.map.reset_map()
        self.game.scoreBoard.reset()
        self.game.update()
        self.game.draw()




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
            if(self.after_loop):
                action.reset_pos()
            else:
                self.after_loop = True
                self.actions_list.append(action)
                self.index = len(self.actions_list)-1
        elif(self.after_loop):
            self.after_loop = False
            loop = self.actions_list[self.index]
            loop.loop_action = action.action_index
            loop = None
            self.actions_list.append(action)
        else:
            self.actions_list.append(action)
        action.reset_pos()

    def show_action(self, surface):
        posx = 30
        posy = 95
        
        loopImage = False
        is_loop = False
        for action in self.actions_list:
            self.imagem = action.image
            self.imagem_rect = self.imagem.get_rect()
            self.imagem_rect.x = posx
            self.imagem_rect.y = posy
            if(is_loop):
                is_loop = False
                self.imagem_rect.x = self.loop_pos[0] + 8
                self.imagem_rect.y = self.loop_pos[1] + 4
                loopImage = True

            if(self.imagem == self.game.player_actions_imgs[LOOP_IND]):
                is_loop = True
                self.loop_pos = (posx , posy)
                self.loop_rect = self.imagem_rect

            if(not is_loop and not loopImage):
                posy += 51
                if(posy > 552):
                    posy = 95
                    posx += 104
                if(posx >= 104*4):
                    posx = 35
            else:
                posy += 36
                if(posy > 552):
                    posy = 95
                    posx += 104
                if(posx >= 104*4):
                    posx = 35   

            surface.blit(self.imagem, self.imagem_rect)

            # Blit para loop aparecer por cima da imagem de ação.
            if(loopImage):
                surface.blit(self.game.player_actions_imgs[LOOP_IND], self.loop_rect)
                loopImage = False

    def execute_action(self):
        posx = 54
        posy = 119

        proximo = False
        is_loop = False
        after_loop = False
        if(self.game.playPauseAction.playing):
            for action in self.actions_list:
                # pg.draw.circle(self.game.screen, RED, (posx, posy), RADIUS, 3)
                # pg.display.flip()
                imagem = action.image

                while(pg.mixer.get_busy()):
                    self.game.update()
                    self.game.draw()
                    
                action.execute(posx,posy)
                self.game.update()
                self.game.draw()

                if(after_loop):
                    posx -= 8
                    posy -= 4

                if(is_loop):
                    is_loop = False
                    after_loop = False

                if(imagem == self.game.player_actions_imgs[LOOP_IND]):
                    is_loop = True
                    after_loop = True
                

                if(not is_loop and not proximo):
                    posy += 51
                    if(posy > 552):
                        posy = 119
                        posx += 104
                    if(posx >= 104*4):
                        posx = 35
                elif(proximo):
                    posy += 68
                    posx -= 8
                    proximo = False
                    if(posy > 552):
                        posy = 119
                        posx += 104
                    if(posx >= 104*4):
                        posx = 35
                elif(not after_loop):
                    posy += 36
                    if(posy > 552):
                        posy = 119
                        posx += 104
                    if(posx >= 104*4):
                        posx = 35
                
                elif(after_loop):
                    after_loop = False
                    proximo = True
                    posy += 4
                    posx += 8 

                # if(action.action_index != LOOP_IND and not after_loop):
                #     posy += 51
                #     if(posy > 552):
                #         posy = 95
                #         posx += 104
                #     if(posx >= 104*4):
                #         posx = 35
                # elif(after_loop):
                #     after_loop = False
                # elif(action.action_index == LOOP_IND and not after_loop):
                #     posy += 36
                #     after_loop = True
                #     if(posy > 552):
                #         posy = 95
                #         posx += 104
                #     if(posx >= 104*4):
                #         posx = 35

            while(pg.mixer.get_busy()):
                self.game.update()
                self.game.draw()
                # continue   
            self.game.playPauseAction.playing = False
            self.game.playPauseAction.image =  self.game.player_actions_imgs[RESET_IND]
        
        qtde_acoes = 10
        count = 0
        for i in range(len(self.game.scoreBoard.player_scores)):
            if(i%2 == 1):
                if(self.game.scoreBoard.player_scores[i].done):
                    count += 1
        if(count == qtde_acoes):
            ActionAnimation(self.game).winner10()
        else:
            ActionAnimation(self.game).game_over()






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
    def __init__(self, game, x, y, action_index = LOOP_IND ):
        ChooseAction.__init__(self, game, x, y, action_index)
        self.loop_action = 0
        self.loop_cycles = 0
        



class InputBox(pg.sprite.Sprite):

    def __init__(self, game, text='1'):
        self.groups =  game.popups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.ui_popups[UI_N_LOOP_UNSEL]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2 - 100
        self.pressed = False
        self.mouse_clicked = False
        self.text = text
        self.txt_surface = self.game.font.render(self.text, True, TEXT_BLUE)
        self.active = False
        self.valid = False

    def handle_event(self):
        validKeys = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_RETURN, pg.K_KP0, pg.K_KP1, pg.K_KP2, pg.K_KP3, pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9, pg.K_BACKSPACE]
        event = self.game.evento
        if event.type == pg.MOUSEBUTTONDOWN and not self.mouse_clicked:
            self.mouse_clicked = True
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.image = self.game.ui_popups[UI_N_LOOP_SEL]
                self.active = not self.active
            else:
                self.image = self.game.ui_popups[UI_N_LOOP_UNSEL]
                self.active = False
            # Change the current color of the input box.
        if event.type == pg.KEYDOWN:
            if(event.key in validKeys):
                if self.active and not self.pressed:
                    if event.key == pg.K_RETURN:
                        self.pressed = True
                        try:
                            self.game.playerActionHolder.actions_list[self.game.playerActionHolder.index].loop_cycles = int(self.text)
                        except:
                            self.game.playerActionHolder.actions_list[self.game.playerActionHolder.index].loop_cycles = 0
                        self.text = ''
                        self.valid = True
                    elif event.key == pg.K_BACKSPACE:
                        self.pressed = True
                        self.text = self.text[:-1]
                    else:
                        self.pressed = True
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.game.font.render(self.text, True, TEXT_BLUE)
        if event.type == pg.KEYUP:
            self.pressed = False
        if event.type == pg.MOUSEBUTTONUP:
            self.mouse_clicked = False

    def update(self):
        self.handle_event()

    def render(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+30, self.rect.y+50))
        if(self.valid):
            self.kill()




class ActionAnimation(pg.sprite.Sprite):
    def __init__(self, game, action=0, txt=''):
        self.groups =  game.popups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.animations[UI_BOX_NOT_ALLOWED_IND] #ANIM BOX
        self.rect = self.image.get_rect()
        self.action = action
        self.txt = txt
        self.rect.centerx = WIDTH/2 #512
        self.rect.centery = HEIGHT/2 - 100 #284

    def action_not_allowed(self):
        j = 0
        next_move = pg.time.get_ticks()
        self.game.alert_sound.play()
        while(j < 10):
            if(pg.time.get_ticks() >= next_move):
                next_move = pg.time.get_ticks() + NOT_ALLOWED_ANIM_DELAY
                self.game.update()
                self.game.draw()
                pg.display.flip()
                j += 1
        
        self.kill()

    def blocked(self):
        self.game.wrong_sound.play()
        next_move = pg.time.get_ticks()
        j = 0
        while(j < 10):
            if(pg.time.get_ticks() >= next_move):
                next_move = pg.time.get_ticks() + BLOCKED_DELAY
                self.image = self.game.ui_popups[UI_PLAYER_BLOCKED_IND]
                self.rect.x = self.game.player.rect.x + 12
                self.rect.y = self.game.player.rect.y - 24
                self.game.update()
                self.game.draw()
                pg.display.flip()
                j += 1
        self.game.update()
        self.game.draw()
        pg.display.flip()

        self.kill()

    def winner10(self):
        j = 0
        next_move = pg.time.get_ticks()
        self.game.win_sound.play()
        while(j < 10):
            if(pg.time.get_ticks() >= next_move):
                next_move = pg.time.get_ticks() + GAME_OVER_DELAY
                self.image = self.game.win_img
                j += 1
            self.game.update()
            self.game.draw()
            pg.display.flip()

        self.kill()

    def game_over(self):
        j = 0
        self.game.lose_sound.play()
        next_move = pg.time.get_ticks()
        while(j < 10):
            if(pg.time.get_ticks() >= next_move):
                next_move = pg.time.get_ticks() + GAME_OVER_DELAY
                self.image = self.game.lose_img
                j += 1
            self.game.update()
            self.game.draw()
            pg.display.flip()

        self.kill()


class PlayerScoresItem(pg.sprite.Sprite):
    def __init__(self, game, image, index, x, y):
        self.groups =  game.scores
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.done = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.action_index = index


    def update(self):
        if(self.action_index % 2 == 0):
            if(self.done):
                self.image = self.game.done_img
            else:
                self.image = self.game.pendente_img

    def reset(self):
        self.done = False
        if(self.image == self.game.done_img):
            self.image = self.game.pendente_img



class PlayerScoreBoard():
    def __init__(self, game):
        self.game = game
        x = 10
        y = 30
        self.player_scores = []

        i = 5
        for img in self.game.player_actions_done:
            self.player_scores.append(PlayerScoresItem(self.game, img, i, x, y))
            self.player_scores.append(PlayerScoresItem(self.game, self.game.pendente_img, i+1, x+24, y))
            i += 2
            x += 65
            if(x > 300):
                x = 10
                y += 30

    def reset(self):
        for scoreItem in self.player_scores:
            scoreItem.reset()





class Buttons(pg.sprite.Sprite):

    def __init__(self, game, image, x, y):
        self.groups =  game.buttons_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
