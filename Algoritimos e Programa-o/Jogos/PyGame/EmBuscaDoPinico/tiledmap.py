import pygame as pg
import pytmx
from settings import *

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
    
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if(layer.name != 'objetoquatoacima'):
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth + MAP_SHIFT_X, 
                                                y * self.tmxdata.tileheight))

    def render_acima(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if(layer.name == 'objetoquatoacima'):
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth + MAP_SHIFT_X, 
                                                y * self.tmxdata.tileheight))        
    

    def toggle_vaso(self, tampa_aberta):
        vaso_down = self.tmxdata.layers[2]
        vaso_up = self.tmxdata.layers[3]

        if(tampa_aberta):
            vaso_down.visible = False
            vaso_up.visible = True
        else:
            vaso_down.visible = True
            vaso_up.visible = False

    def reset_map(self):
        vaso_down = self.tmxdata.layers[2]
        vaso_up = self.tmxdata.layers[3]

        vaso_down.visible = True
        vaso_up.visible = False
        

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface