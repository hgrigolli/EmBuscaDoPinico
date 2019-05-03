import pygame as pg


pg.init()
screen = pg.display.set_mode((1024, 768))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_GREEN = pg.Color('green')
BLOCK_LEFT = "Move left"
BLOCK_RIGHT = "Move right"
BLOCK_UP = "Move up"
BLOCK_DOWN = "Move down"
FONT = pg.font.Font(None, 16)
pg.display.set_caption("jogo maneiro")


class ActionBox:

    def __init__(self, x, y, w, h, player, lista_action, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.player = player
        self.lista_action = lista_action
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                for action in self.lista_action:
                    if(action == BLOCK_LEFT):
                        andarFrente(self.player)
                        pg.draw.rect(screen, COLOR_GREEN, self.player, 2)
                        pg.draw.rect(screen, self.color, self.rect, 2)
                        pg.time.wait(100)
                    elif(action == BLOCK_RIGHT):
                        andarTras(self.player)

                        pg.draw.rect(screen, COLOR_GREEN, self.player, 2)
                        pg.draw.rect(screen, self.color, self.rect, 2)
                        pg.time.wait(100)
                    elif(action == BLOCK_DOWN):
                        andarBaixo(self.player)
                        pg.draw.rect(screen, COLOR_GREEN, self.player, 2)
                        pg.draw.rect(screen, self.color, self.rect, 2)
                        pg.time.wait(100)
                    else:
                        andarCima(self.player)
                        pg.draw.rect(screen, COLOR_GREEN, self.player, 2)
                        pg.draw.rect(screen, self.color, self.rect, 2)
                        pg.time.wait(100)
                        
                    pg.display.flip()
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

    def update(self):
        # Resize the box if the text is too long.
        width = min(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        pg.draw.rect(screen, COLOR_GREEN, self.player, 2)



def main():
    clock = pg.time.Clock()
    player = pg.Rect(20,20,30,30)
    lista_action = []
    lista_action.append(BLOCK_RIGHT)
    lista_action.append(BLOCK_RIGHT)
    lista_action.append(BLOCK_RIGHT)
    lista_action.append(BLOCK_RIGHT)
    lista_action.append(BLOCK_DOWN)
    lista_action.append(BLOCK_DOWN)
    lista_action.append(BLOCK_DOWN)
    lista_action.append(BLOCK_DOWN)
    lista_action.append(BLOCK_LEFT)
    lista_action.append(BLOCK_LEFT)
    lista_action.append(BLOCK_LEFT)
    lista_action.append(BLOCK_LEFT)
    lista_action.append(BLOCK_UP)
    lista_action.append(BLOCK_UP)
    lista_action.append(BLOCK_UP)
    lista_action.append(BLOCK_UP)
    
    action_box1 = ActionBox(100, 50, 140, 32, player, lista_action, "Start")
    action_boxes = [action_box1]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in action_boxes:
                box.handle_event(event)
                
                
        screen.fill((30, 30, 30))
        for box in action_boxes:
            box.update()

        for box in action_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


def andarFrente(rect):
    rect.move_ip(-20,0)
    screen.fill((30, 30, 30))
    
def andarCima(rect):
    rect.move_ip(0,-20)
    screen.fill((30, 30, 30))
    
def andarBaixo(rect):
    rect.move_ip(0,20)
    screen.fill((30, 30, 30))
    
def andarTras(rect):
    rect.move_ip(20,0)
    screen.fill((30, 30, 30))
    
if __name__ == '__main__':
    main()
    pg.quit()
