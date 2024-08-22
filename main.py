import pygame
pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
run = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walk1 = pygame.image.load("img/player/walk1.png")
        self.walk2 = pygame.image.load("img/player/walk2.png")
        self.walk = [self.walk1,self.walk2]
        self.walk_index = 0
        self.image = pygame.image.load("img/player/playerstand.png")
        self.rect = self.image.get_rect(center = (200,213))
        self.velocidad = 0
        self.direction = True
        self.gravedad = 0
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 263:
            self.gravedad = -15
        if keys[pygame.K_d]:
            self.velocidad = 6
            self.direction = True
        elif keys[pygame.K_a]:
            self.velocidad = -6
            self.direction = False
        else:
            self.velocidad = 0
    def movement(self):
        self.rect.x += self.velocidad
        if bg_rect.right != 600:
            if self.rect.right > 400:
                self.rect.right = 400
                bg_rect.x -= self.velocidad
        else:
            if self.rect.right > 600:
                self.rect.right = 600
                bg_rect.x -= self.velocidad

        if bg_rect.left != 0:
            if self.rect.left < 80:
                self.rect.left = 80
                bg_rect.x -= self.velocidad
        else:
            if self.rect.left < 0:
                self.rect.left = 0
                bg_rect.x -= self.velocidad
        
        if bg_rect.right < 600:
            bg_rect.right = 600
        if bg_rect.left > 0:
            bg_rect.left = 0
    def animation(self):
        if self.velocidad == 0:
            if self.direction:
                self.image = pygame.transform.flip(pygame.image.load("img/player/playerstand.png"),True,False)
            else:
                self.image = pygame.image.load("img/player/playerstand.png")
        if self.velocidad > 0:
            self.walk_index += 0.1
            if self.walk_index > len(self.walk):
                self.walk_index = 0
            self.image = pygame.transform.flip(self.walk[int(self.walk_index)],True,False)
        elif self.velocidad < 0:
            self.walk_index += 0.1
            if self.walk_index > len(self.walk):
                self.walk_index = 0
            self.image = self.walk[int(self.walk_index)]
    def gravity(self):
        self.gravedad += 1
        self.rect.y += self.gravedad
        if self.rect.bottom > 263:
            self.rect.bottom = 263
    def update(self):
        self.gravity()
        self.player_input()
        self.movement()
        self.animation()

player = pygame.sprite.GroupSingle()
player.add(Player())

bg = pygame.image.load("img/bg/bg.jpg")
bg_rect = bg.get_rect(topleft = (0,-400))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg,bg_rect)
    player.draw(screen)
    player.update()
    pygame.display.update()
    clock.tick(60)