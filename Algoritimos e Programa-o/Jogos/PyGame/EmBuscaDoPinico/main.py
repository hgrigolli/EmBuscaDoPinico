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

    def load_data(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'imagens')
        self.char_folder = path.join(image_folder, 'char')
        self.action_folder = path.join(image_folder, 'actions')
        self.ui_folder = path.join(image_folder, 'UI')
        self.anim_folder = path.join(image_folder, 'animations')
        map_folder = path.join(game_folder, 'mapas')
        self.map = TiledMap(path.join(map_folder, 'mapa.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_imgs = []
        self.player_actions_imgs = []
        self.mouse_img = []
        self.ui_popups = []
        self.animations = []
        
        #UI
        self.rectmov_img = pg.image.load(path.join(self.ui_folder, UI_RECT_ACTION_IMG)).convert_alpha()
        self.rectchoose_img = pg.image.load(path.join(self.ui_folder, UI_RECT_CHOOSER_IMG)).convert_alpha()
        self.ui_popups.append(pg.image.load(path.join(self.ui_folder, UI_N_LOOP_UNSEL_IMG)).convert_alpha())
        self.ui_popups.append(pg.image.load(path.join(self.ui_folder, UI_N_LOOP_SEL_IMG)).convert_alpha())
        self.mouse_img.append(pg.image.load(path.join(self.ui_folder, CURSOR)).convert_alpha())
        self.mouse_img.append(pg.image.load(path.join(self.ui_folder, CURSOR_GRAB)).convert_alpha())

        #ANIMATIONS
        self.animations.append(pg.image.load(path.join(self.anim_folder, UI_ANIM_BOX)).convert_alpha())

        #PLAYER ACTIONS
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, MOVER_CIMA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, MOVER_BAIXO)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, MOVER_DIREITA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, MOVER_ESQUERDA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, ABRIR_TORNEIRA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, FECHAR_TORNEIRA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, ABRIR_TAMPA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, DESCARGA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, FECHAR_TAMPA)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, DESENTUPIDOR)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, LAVAR_MAOS_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, SECAR_MAOS_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, PAPEL_ACTION)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, LOOP)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, PANTS_DOWN)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, PANTS_UP)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, PAUSE)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, PLAY)).convert_alpha())
        self.player_actions_imgs.append(pg.image.load(path.join(self.action_folder, RESET)).convert_alpha())

        #PLAYER CHAR SPRITES
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_UP1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_UP2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_UP3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_RIGHT1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_RIGHT2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_RIGHT3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_LEFT1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_LEFT2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_LEFT3)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_DOWN1)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_DOWN2)).convert_alpha())
        self.player_imgs.append(pg.image.load(path.join(self.char_folder, PLAYER_IMG_DOWN3)).convert_alpha())


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.actions = pg.sprite.Group()
        self.player_actions = pg.sprite.Group()
        self.player_movement = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.popups = pg.sprite.Group()
        self.mouse_img_active = self.mouse_img[0]
        self.mouse_pos = pg.mouse.get_pos()
        self.evento = 0
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
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000 # Amount of seconds between each loop.
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.player_actions.update()
        self.popups.update()

    def draw_grid(self):
        for x in range(0, self.map_rect.width , TILESIZE//2):
            pg.draw.line(self.screen, LIGHTGREY2, (MAP_SHIFT_X+x+6 , 0), (MAP_SHIFT_X+x+6, self.map_rect.height))
        for y in range(0, self.map_rect.height, TILESIZE//2):
            pg.draw.line(self.screen, LIGHTGREY2, (MAP_SHIFT_X, y), (MAP_SHIFT_X+self.map_rect.width, y))

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        pg.display.set_caption(TITLE + " - FPS: "+"{:.2f}".format(self.clock.get_fps()) + " - MOUSE POS: "+str(pg.mouse.get_pos() ))
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, (MAP_SHIFT_X, 0))
        # self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.map.render_acima(self.screen)
        self.playerActionHolder.show_action(self.screen)
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
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
