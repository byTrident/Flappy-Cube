import pygame
from random import randint

class Obstacles:
    def __init__(self, display, colour):
        self.width = 48
        self.height = 480
        self.x_positions = []
        self.y_positions = []

        self.spawn_timer = 0
        self.req_time = randint(0, 1)

        self.death = False

    def draw(self, display, player_rect, colour = "black"):
        # Draw obstacles
        for x in self.x_positions:
            if pygame.draw.rect(display, colour, ((x, self.y_positions[self.x_positions.index(x)]), (self.width, self.height))).colliderect(player_rect):
                self.death = True
            elif pygame.draw.rect(display, colour, ((x, self.y_positions[self.x_positions.index(x)] + 600), (self.width, self.height))).colliderect(player_rect):
                self.death = True

    def update(self, dt): 
        # Create new obstacles upon time end
        if self.spawn_timer >= self.req_time:
            self.spawn_timer = 0
            self.req_time = randint(10, 15) / 10
            self.x_positions.append(799)
            self.y_positions.append(randint(-480, 0))
        else:
            self.spawn_timer += 1 * dt

        for x in self.x_positions:
            # Move obstacle
            self.x_positions[self.x_positions.index(x)] -= 300 * dt

    def reset(self):
        self.x_positions = []
        self.y_positions = []

        self.spawn_timer = 0
        self.req_time = randint(0, 1)

        self.death = False