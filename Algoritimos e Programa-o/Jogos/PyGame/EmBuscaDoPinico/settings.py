# COLORS (R,G,B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
LIGHTGREY2 = (176,176,176)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
COLOR_INACTIVE = (40, 40, 40)
COLOR_ACTIVE = (176,176,176)
TEXT_BLUE = (137,194,212)
TEXT_DARK_BLUE = (25,75,184)

# GAME SETTINGS
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Em busca do Pinico"
BGCOLOR = DARKGREY


#PLAYER SETTINGS
PLAYER_IMG_UP1 = 'char_01 (12).png'
PLAYER_IMG_UP2 = 'char_01 (1).png'
PLAYER_IMG_UP3 = 'char_01 (11).png'
PLAYER_IMG_RIGHT1 = 'char_01 (9).png'
PLAYER_IMG_RIGHT2 = 'char_01 (8).png'
PLAYER_IMG_RIGHT3 = 'char_01 (10).png'
PLAYER_IMG_LEFT1 = 'char_01 (6).png'
PLAYER_IMG_LEFT2 = 'char_01 (5).png'
PLAYER_IMG_LEFT3 = 'char_01 (7).png'
PLAYER_IMG_DOWN1 = 'char_01 (3).png'
PLAYER_IMG_DOWN2 = 'char_01 (2).png'
PLAYER_IMG_DOWN3 = 'char_01 (4).png'

#PLAYER MOVEMENT
PLAYER_TIME_WAIT = 100

#MAP SETTINGS
MAP_SHIFT_X = 424
MAP_SHIFT_Y = 84
TILESIZE = 24
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#PLAYER ACTION OBJECTS
LAVAR_MAOS = 'sink_action'
ABRIR_TORNEIRA_ACTION = 'sink_action'
FECHAR_TORNEIRA_ACTION = 'sink_action'

SECAR_MAOS = 'towel_action'

DAR_DESCARGA = 'vaso_action'
ABAIXAR_CALCAS_ACTION = 'vaso_action'
LEVANTAR_CALCAS_ACTION = 'vaso_action'
ABRIR_TAMPA_ACTION = 'vaso_action'
FECHAR_TAMPA_ACTION = 'vaso_action'

USAR_PAPEL = 'papel'

DESENTUPIR = 'desentupidor'

TOMAR_BANHO = 'shower_action' # AINDA NÃO IMPLEMENTADO


# ACTION IMAGENS
MOVER_CIMA = 'up-arrow.png'
MOVER_BAIXO = 'down-arrow.png'
MOVER_DIREITA = 'right-arrow.png'
MOVER_ESQUERDA = 'left-arrow.png'
ABRIR_TORNEIRA = 'abrir_torneira.png'
FECHAR_TORNEIRA = 'fechar_torneira.png'
ABRIR_TAMPA = 'tampa_aberta.png'
DESCARGA = 'descarga.png'
FECHAR_TAMPA = 'tampa_fechada.png'
DESENTUPIDOR = 'desentupidor.png'
LAVAR_MAOS_ACTION = 'lavar_maos.png'
SECAR_MAOS_ACTION = 'secar_maos.png'
LOOP = 'loop.png'
PAPEL_ACTION = 'papel.png'
PANTS_DOWN = 'pants_down.png'
PANTS_UP = 'pants_up.png'
PAUSE = 'pause-button.png'
PLAY = 'play-button.png'
RESET = 'reload-button.png'

#ACTION INDEX

MOVER_CIMA_IND = 0
MOVER_BAIXO_IND = 1
MOVER_DIREITA_IND = 2
MOVER_ESQUERDA_IND = 3
ABRIR_TORNEIRA_IND = 4
FECHAR_TORNEIRA_IND = 5
ABRIR_TAMPA_IND = 6
DAR_DESCARGA_IND = 7
FECHAR_TAMPA_IND = 8
DESENTUPIDOR_IND = 9
LAVAR_MAOS_ACTION_IND = 10
SECAR_MAOS_ACTION_IND = 11
PAPEL_ACTION_IND = 12
LOOP_IND = 13
PANTS_DOWN_IND = 14
PANTS_UP_IND = 15
PAUSE_IND = 16
PLAY_IND = 17
RESET_IND = 18



#UI

## UI POP UPS
UI_N_LOOP_UNSEL = 0
UI_N_LOOP_SEL = 1


## UI CURSOR
CURSOR_GRAB = 'cursor_hand.png'
CURSOR = 'cursor_pointerFlat.png'

## UI POPUP CONFIGS
UI_N_LOOP_UNSEL_IMG = 'UI_repet_loop_unsel.png'
UI_N_LOOP_SEL_IMG = 'UI_repet_loop_sel.png'

UI_RECT_ACTION_IMG = 'rect_movement.png'
UI_RECT_CHOOSER_IMG = 'rect_chooser.png'

## UI ANIMATIONS
UI_ANIM_BOX = 'anim_box.png'



