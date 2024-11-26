import pygame

class Player:
    def __init__(self):
        self.textures = ['textures/player/player_down.png', 'textures/player/player_mid.png', 'textures/player/player_up.png']
        self.surface = pygame.image.load(self.textures[1]).convert()
        self.surface = pygame.transform.scale_by(self.surface, 2)

        self.rect = self.surface.get_rect()
        self.rect.x = 50
        self.rect.y = 284
        self.velocity = -450

    def draw(self, display):
        # Draw the Player on screen
        display.blit(self.surface, self.rect)

        # Animation
        if self.velocity < 0:
            self.surface = pygame.image.load(self.textures[2]).convert()
        elif self.velocity == 0:
            self.surface = pygame.image.load(self.textures[1]).convert()
        else:
            self.surface = pygame.image.load(self.textures[0]).convert()
        self.surface = pygame.transform.scale_by(self.surface, 2)

    def update(self, dt):
        # Implement Gravity
        self.velocity += 20
        self.rect.y += self.velocity * dt

    def jump(self):
        self.velocity = -450

    def reset(self):
        self.rect.x = 50
        self.rect.y = 284
        self.velocity = -450

        self.surface = pygame.image.load(self.textures[1]).convert()
        self.surface = pygame.transform.scale_by(self.surface, 2)