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
        pg.key.set_repeat(100, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'imagens')
        self.char_folder = path.join(image_folder, 'char')
        map_folder = path.join(game_folder, 'mapas')
        self.map = TiledMap(path.join(map_folder, 'mapa.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_imgs = []
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
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            else:
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption(TITLE + " - FPS: "+"{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, (0, 0))
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1,index=6)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1,index=3)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1,index=0)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1,index=9)

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
