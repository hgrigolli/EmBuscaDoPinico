import pygame
import random
 
class Bloco(pygame.sprite.Sprite):
    #def __init__(self, color, x, y, width, height):
    def __init__(self, imagem,x,y):
        # chama a classe (Sprite) 
        super().__init__()
##        self.image = pygame.Surface([width, height])
##        
##        self.image.fill(color)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
 
class Player(Bloco): 
    # carrega os blocos
    carry_block_list = []
    
    def update(self):
 
        # Obtem a posição do mouse
        pos = pygame.mouse.get_pos()
 
        # Verifica a posição do mouse
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]
 
       #cria o loop que carreguei
        for block in self.carry_block_list:
            block.rect.x -= diff_x
            block.rect.y -= diff_y

        self.image.set_alpha(1)  
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
# Inicializa o Pygame
pygame.init()
 
# cria a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Em busca do Pinico")
 
# Esta é a lista de 'sprites'
# a lista é add e gerenciada pela classe grupo
block_list = pygame.sprite.Group()
 
# cria a lista de todos os sprites
# cria os blocos e o bloco do jogador tb
all_sprites_list = pygame.sprite.Group()

 # for que cria os blocos
for i in range(5):
    # aqui cria o bloco
    #block = Bloco(preto, 70, 100*i, 50, 50) # logica antiga
    block = Bloco(seta_baixo, 70, 100)
    block1 =  Bloco(seta_direita, 120, 200)
 
    # Define um local aleatorio ao bloco
    #block.rect.x = random.randrange(screen_width)
    #block.rect.y = random.randrange(screen_height)
 
    # seta o bloco em objetos
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(5):
    # aqui cria o bloco
    #block = Bloco(preto, 70, 100*i, 50, 50) # logica antiga
    block1 =  Bloco(seta_direita, 120, 200)

      # seta o bloco em objetos
    block_list.add(block1)
    all_sprites_list.add(block1)
 
# cria o que seleciona o mouse
player = Player(seta_cima, 0,0)
all_sprites_list.add(player)
 
# faz o loop atpe o jogador clicar em fechar
done = False
 
# gerenciador de atualização de tela
clock = pygame.time.Clock()
 
# oculta o cursor do mouse
pygame.mouse.set_visible(True) # False oculta :)
 
# -------- Main Programa loop -----------

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando clicar e pressionar verifique 
            blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
 
            # Define a lista de blocos e verifica se esta em contato com blocos
            player.carry_block_list = blocks_hit_list
 
        elif event.type == pygame.MOUSEBUTTONUP:
            # Qdo não deixamos de clicar carrega como vazio
            player.carry_block_list = []
 
    all_sprites_list.update()
 
    # Limpa a tela
    screen.fill(amarelo)
 
    # desenha os spites
    all_sprites_list.draw(screen)
##    screen.blit(seta_cima, (10, 140))    
##    screen.blit(seta_baixo,(10, 80))
##    screen.blit(seta_direita,(8, 155))
##    screen.blit(seta_esquerda,(8, 220))

    # limita 60 quadros por segundo
    clock.tick(60)
 
    # atualiza a tela
    pygame.display.flip()
 
pygame.quit()
