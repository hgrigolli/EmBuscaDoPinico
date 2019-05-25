import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tiledmap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        pg.mouse.set_visible(False)
        self.elapsed = 0

    def load_data(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'imagens')
        char_folder = path.join(image_folder, 'char')
        action_folder = path.join(image_folder, 'actions')
        ui_folder = path.join(image_folder, 'UI')
        anim_folder = path.join(image_folder, 'animations')
        map_folder = path.join(game_folder, 'mapas')
        font_folder = path.join(image_folder, 'font')
        self.sound_folder = path.join(game_folder, 'sounds')
        self.font_name = path.join(font_folder, UI_FONT)
        self.font = pg.font.Font(self.font_name, 28)
        self.map = TiledMap(path.join(map_folder, 'mapa.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_imgs = []
        self.player_actions_imgs = []
        self.player_actions_done = []
        self.mouse_img = []
        self.ui_popups = []
        self.animations = []
        self.buttons_sprites = pg.sprite.Group()

        #SFX SOUNDS
        self.sink_sound = pg.mixer.Sound(path.join(self.sound_folder, 'sink_on.ogg'))
        self.open_lid = pg.mixer.Sound(path.join(self.sound_folder, 'open_lid.ogg'))
        self.papel_sound = pg.mixer.Sound(path.join(self.sound_folder, 'toilet_paper.ogg'))
        self.vaso_flush = pg.mixer.Sound(path.join(self.sound_folder, 'vaso_flush.ogg'))
        self.lava_mao_sound = pg.mixer.Sound(path.join(self.sound_folder, 'hands-with-soap.ogg'))
        self.wrong_sound = pg.mixer.Sound(path.join(self.sound_folder, 'wrong.ogg'))
        self.alert_sound = pg.mixer.Sound(path.join(self.sound_folder, 'alert.ogg'))
        self.vaso_poop_sound = pg.mixer.Sound(path.join(self.sound_folder, 'vaso_poop_sound.ogg'))
        self.lose_sound = pg.mixer.Sound(path.join(self.sound_folder, 'aww.ogg'))
        self.win_sound = pg.mixer.Sound(path.join(self.sound_folder, 'applause.ogg'))
        self.towel_sound = pg.mixer.Sound(path.join(self.sound_folder, 'towel_sound.ogg'))
        self.pants_up_sound = pg.mixer.Sound(path.join(self.sound_folder, 'pants_up_sound.ogg'))
        self.pants_down_sound = pg.mixer.Sound(path.join(self.sound_folder, 'pants_down_sound.ogg'))
        
        #UI
        self.rectmov_img = pg.image.load(path.join(ui_folder, UI_RECT_ACTION_IMG)).convert_alpha()
        self.rectchoose_img = pg.image.load(path.join(ui_folder, UI_RECT_CHOOSER_IMG)).convert_alpha()

        self.pendente_img = pg.image.load(path.join(ui_folder, UI_PENDENTE)).convert_alpha()
        self.done_img = pg.image.load(path.join(ui_folder, UI_DONE)).convert_alpha()

        self.win_img = pg.image.load(path.join(ui_folder, UI_WINNER)).convert_alpha()
        self.lose_img = pg.image.load(path.join(ui_folder, UI_LOST)).convert_alpha()

        self.ui_popups.append(pg.image.load(path.join(ui_folder, UI_N_LOOP_UNSEL_IMG)).convert_alpha())
        self.ui_popups.append(pg.image.load(path.join(ui_folder, UI_N_LOOP_SEL_IMG)).convert_alpha())
        self.ui_popups.append(pg.image.load(path.join(ui_folder, UI_MSG_BOX)).convert_alpha())
        self.ui_popups.append(pg.image.load(path.join(ui_folder, UI_PLAYER_BLOCKED)).convert_alpha())

        self.start_bg_img = pg.image.load(path.join(ui_folder, 'bg_home.png')).convert_alpha()
        self.credits_bg_img = pg.image.load(path.join(ui_folder, 'credit_bg.png')).convert_alpha()

        self.start_button_img = pg.image.load(path.join(ui_folder, 'start_button.png')).convert_alpha()
        self.start_button_hover_img  = pg.image.load(path.join(ui_folder, 'start_button_hover.png')).convert_alpha()
        
        self.how_to_play_button_img = pg.image.load(path.join(ui_folder, 'how_to_play_button.png')).convert_alpha()
        self.how_to_play_button_hover_img  = pg.image.load(path.join(ui_folder, 'how_to_play_button_hover.png')).convert_alpha()
        self.how_to_play_img = pg.image.load(path.join(ui_folder, 'comojogar.png')).convert_alpha()

        self.back_button_img  = pg.image.load(path.join(ui_folder, 'back_button.png')).convert_alpha()
        self.back_button_hover_img  = pg.image.load(path.join(ui_folder, 'back_button_hover.png')).convert_alpha()
        self.back_button = None

        self.creditos_button_img  = pg.image.load(path.join(ui_folder, 'creditos_button.png')).convert_alpha()
        self.creditos_button_hover_img  = pg.image.load(path.join(ui_folder, 'creditos_button_hover.png')).convert_alpha()


        self.mouse_img.append(pg.image.load(path.join(ui_folder, CURSOR)).convert_alpha())
        self.mouse_img.append(pg.image.load(path.join(ui_folder, CURSOR_GRAB)).convert_alpha())

        #ANIMATIONS
        self.animations.append(pg.image.load(path.join(anim_folder, UI_ANIM_BOX)).convert_alpha())
        self.animations.append(pg.image.load(path.join(anim_folder, UI_BOX_NOT_ALLOWED)).convert_alpha())
        
        
        #PLAYER ACTIONS
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, MOVER_CIMA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, MOVER_BAIXO)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, MOVER_DIREITA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, MOVER_ESQUERDA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, LOOP)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, ABRIR_TORNEIRA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, FECHAR_TORNEIRA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, ABRIR_TAMPA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, DESCARGA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, FECHAR_TAMPA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, LAVAR_MAOS_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, SECAR_MAOS_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, PAPEL_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, PANTS_DOWN)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, PANTS_UP)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, PAUSE)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, PLAY)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(action_folder, RESET)).convert_alpha())

        for i in range(5, len(self.player_actions_imgs)-3):
            img = self.player_actions_imgs[i]
            new_img = pg.transform.scale(img, (24,24))
            self.player_actions_done.append(new_img)

        #PLAYER CHAR SPRITES
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_UP1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_UP2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_UP3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_RIGHT1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_RIGHT2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_RIGHT3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_LEFT1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_LEFT2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_LEFT3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_DOWN1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_DOWN2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(char_folder, PLAYER_IMG_DOWN3)).convert_alpha())
        
        self.mouse_img_active = self.mouse_img[0]

        
    
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.actions = pg.sprite.Group()
        self.player_actions = pg.sprite.Group()
        self.player_movement = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.popups = pg.sprite.Group()
        self.scores = pg.sprite.Group()
        
        self.mouse_pos = pg.mouse.get_pos()
        self.evento = pg.event.poll()
        pg.mixer.music.load(path.join(self.sound_folder, 'playing_sound.ogg'))

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x + MAP_SHIFT_X, tile_object.y)
            elif(tile_object.name == 'towel_action' or tile_object.name == 'desentupidor' 
                    or tile_object.name == 'vaso_action' or tile_object.name == 'papel' 
                    or tile_object.name == 'sink_action' or tile_object.name == 'shower_action'):
                ActionObstacle(self, tile_object.x + MAP_SHIFT_X, tile_object.y, tile_object.width, tile_object.height, tile_object.name)
            else:
                Obstacle(self, tile_object.x + MAP_SHIFT_X, tile_object.y, tile_object.width, tile_object.height)
        self.playPauseAction = PlayPauseAction(self, 350, 10)
        self.playerActionHolder = PlayerActionHolder(self,0,0)
        self.playerActionChooser = PlayerActionChooser(self, 0,600)
        self.scoreBoard = PlayerScoreBoard(self)
        k = 0
        const = 10
        posy = 640
        for i in range(len(self.player_actions_imgs)-3):
            posx = const + k*3*TILESIZE
            if(posx >= WIDTH - 3*TILESIZE):
                posy += 64
                posx = 10
                k = 0
            if(i != LOOP_IND):
                ChooseAction(self, posx, posy, i)
            else:
                LoopAction(self, posx, posy)
                # loop.handle_event()
            k += 1
            

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Amount of seconds between each loop.
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.player_sprite.update()
        self.player_actions.update()
        self.popups.update()
        self.scores.update()
    
    def draw_grid(self):
        for x in range(0, self.map_rect.width , TILESIZE//2):
            vertical_line = pg.Surface((self.map_rect.height, 1), pg.SRCALPHA)
            vertical_line.fill(LIGHTGREY2_ALPHA)
            self.screen.blit(vertical_line, (MAP_SHIFT_X+6, x))
        for y in range(0, self.map_rect.height, TILESIZE//2):
            horizontal_line = pg.Surface((1, self.map_rect.width), pg.SRCALPHA)
            horizontal_line.fill(LIGHTGREY2_ALPHA)
            self.screen.blit(horizontal_line, (MAP_SHIFT_X+y+6, 0))

    def draw_text(self, text, size, color, x, y, align="topleft"):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        pg.display.set_caption(TITLE + " - FPS: "+"{:.2f}".format(self.clock.get_fps()) + " - MOUSE POS: "+str(pg.mouse.get_pos() ))
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, (MAP_SHIFT_X, 0))
        self.map.render(self.screen)
        self.all_sprites.draw(self.screen)
        self.player_sprite.draw(self.screen)
        self.map.render_acima(self.screen)
        self.playerActionHolder.show_action(self.screen)
        # self.draw_grid()
        self.draw_text("Pontos: {}".format(self.player.score),16,TEXT_DARK_BLUE,10,10)
        self.scores.draw(self.screen)
        self.player_actions.draw(self.screen)
        self.popups.draw(self.screen)
        for action in self.playerActionHolder.actions_list:
            if(action.inputbox is not None):
                action.inputbox.render(self.screen)
        self.screen.blit(self.mouse_img_active, ( pg.mouse.get_pos() ))
    

        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            self.evento = event
            

    def show_start_screen(self):
        pg.mixer.music.load(path.join(self.sound_folder, 'home_sound.ogg'))
        mouse_hold = False
        waiting = True
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(loops=-1)
        self.start_button = Buttons(self, self.start_button_img, WIDTH/2, HEIGHT * 2 /4)
        self.how_to_play_button = Buttons(self, self.how_to_play_button_img, 200, HEIGHT * 3 /4)
        self.credits_button = Buttons(self, self.creditos_button_img, WIDTH - 200, HEIGHT * 3 /4)
        if(self.back_button != None):
            self.back_button.kill()
            self.back_button = None
        while waiting:
            self.screen.blit(self.start_bg_img, (0, 0))
            self.screen.blit(self.mouse_img_active, ( pg.mouse.get_pos() )) 
            self.buttons_sprites.update()
            self.buttons_sprites.draw(self.screen)
            self.clock.tick(FPS)
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    self.quit()
                if(event.type == pg.MOUSEBUTTONDOWN and not mouse_hold):
                    if event.button == 1:
                        if self.start_button.rect.collidepoint(event.pos):
                            waiting = False
                            mouse_hold = True
                            pg.mixer.music.fadeout(500)
                        elif self.credits_button.rect.collidepoint(event.pos):
                            mouse_hold = True
                            self.show_credits_screen()
                        elif self.how_to_play_button.rect.collidepoint(event.pos):
                            mouse_hold = True
                            self.show_how_to_play_screen()
                elif(event.type == pg.MOUSEMOTION):
                    if self.start_button.rect.collidepoint(event.pos):
                        self.start_button.image = self.start_button_hover_img
                    else:
                        self.start_button.image = self.start_button_img
                    if self.credits_button.rect.collidepoint(event.pos):
                        self.credits_button.image = self.creditos_button_hover_img
                    else:
                         self.credits_button.image = self.creditos_button_img
                    if self.how_to_play_button.rect.collidepoint(event.pos):
                        self.how_to_play_button.image = self.how_to_play_button_hover_img
                    else:
                         self.how_to_play_button.image = self.how_to_play_button_img        
                elif(event.type == pg.MOUSEBUTTONUP):
                    mouse_hold = False
            pg.display.flip()
    


    def show_credits_screen(self):
        mouse_hold = False
        voltar = False
        self.back_button = Buttons(self, self.back_button_img, WIDTH-150, HEIGHT * 3 /4)
        self.start_button.kill()
        self.credits_button.kill()
        self.how_to_play_button.kill()
        while not voltar:
            self.screen.blit(self.credits_bg_img, (0, 0))
            self.screen.blit(self.mouse_img_active, ( pg.mouse.get_pos() ))
            self.buttons_sprites.update()
            self.buttons_sprites.draw(self.screen)
            self.clock.tick(FPS)
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    self.quit()

                if(event.type == pg.MOUSEBUTTONDOWN and not mouse_hold):
                    if event.button == 1:
                        if self.back_button.rect.collidepoint(event.pos):
                            voltar = True
                            mouse_hold = True
                            self.show_start_screen()
                elif(event.type == pg.MOUSEMOTION):
                        if self.back_button.rect.collidepoint(event.pos):
                            self.back_button.image = self.back_button_hover_img
                        else:
                            self.back_button.image = self.back_button_img
                elif(event.type == pg.MOUSEBUTTONUP):
                    mouse_hold = False
            pg.display.flip()
    
    def show_how_to_play_screen(self):
        mouse_hold = False
        voltar = False
        self.back_button = Buttons(self, self.back_button_img, WIDTH-100, HEIGHT * 2 /4)
        self.start_button.kill()
        self.credits_button.kill()
        self.how_to_play_button.kill()
        while not voltar:
            self.screen.blit(self.how_to_play_img, (0, 0))
            self.screen.blit(self.mouse_img_active, ( pg.mouse.get_pos() ))
            self.buttons_sprites.update()
            self.buttons_sprites.draw(self.screen)
            self.clock.tick(FPS)
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    self.quit()
                if(event.type == pg.MOUSEBUTTONDOWN and not mouse_hold):
                    if event.button == 1:
                        if self.back_button.rect.collidepoint(event.pos):
                            voltar = True
                            mouse_hold = True
                            self.show_start_screen()
                elif(event.type == pg.MOUSEMOTION):
                        if self.back_button.rect.collidepoint(event.pos):
                            self.back_button.image = self.back_button_hover_img
                        else:
                            self.back_button.image = self.back_button_img
                elif(event.type == pg.MOUSEBUTTONUP):
                    mouse_hold = False
            pg.display.flip()      

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()

pg.quit()