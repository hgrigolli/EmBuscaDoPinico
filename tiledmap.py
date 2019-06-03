import pygame as pg
import pytmx
from settings import *

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

        for layer in self.tmxdata.layers:
            if(layer.name == 'vaso_up'):
                self.vaso_up = layer
            elif(layer.name == 'vaso_down'):
                self.vaso_down = layer
            elif(layer.name == 'pia_c_agua'):
                self.pia_c_agua = layer
            elif(layer.name == 'pia_s_agua'):
                self.pia_s_agua = layer
            elif(layer.name == 'toalha_umida'):
                self.toalha_umida = layer
            elif(layer.name == 'toalha_seca'):
                self.toalha_seca = layer
    
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
        if(tampa_aberta):
            self.vaso_down.visible = False
            self.vaso_up.visible = True
        else:
            self.vaso_down.visible = True
            self.vaso_up.visible = False

    def toggle_pia(self, torneira_aberta):
        if(torneira_aberta):
            self.pia_c_agua.visible = True
            self.pia_s_agua.visible = False
        else:
            self.pia_c_agua.visible = False
            self.pia_s_agua.visible = True   

    def toggle_toalha(self, secou_maos):
        if(secou_maos):
            self.toalha_umida.visible = True
            self.toalha_seca.visible = False
        else:
            self.toalha_umida.visible = False
            self.toalha_seca.visible = True                    

    def reset_map(self):
        self.vaso_up.visible = False
        self.vaso_down.visible = True

        self.pia_c_agua.visible = False
        self.pia_s_agua.visible = True  
        
        self.toalha_umida.visible = False
        self.toalha_seca.visible = True 

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface