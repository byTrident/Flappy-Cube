import pygame

class Score:
    def __init__(self, font, colour):
        self.score = 0
        with open('high_scores.txt', 'r') as file:
            self.high_score = int(file.read())

        self.surface = font.render("Score: " + str(self.score), 1, colour)
        self.rect = self.surface.get_rect()
        self.rect.center = (400, 50)

        self.hs_surface = font.render("High Score: " + str(self.high_score), 1, colour)
        self.hs_rect = self.surface.get_rect()
        self.hs_rect.center = (650, 550)

        self.detect_obstacle = False

    def draw(self, display, font, colour):
        self.surface = font.render("Score: " + str(self.score), 1, colour)
        display.blit(self.surface, self.rect)

        self.hs_surface = font.render("High Score: " + str(self.high_score), 1, colour)
        display.blit(self.hs_surface, self.hs_rect)

    def update(self, player_x, obstacles_x):
        for obstacle in obstacles_x:
            if ((obstacle - 24) < (player_x + 16)) and ((obstacle + 24) > (player_x + 16)):
                self.detect_obstacle = True
            if ((player_x + 16) > (obstacle + 24)) and ((player_x - 16) < (obstacle + 24)) and self.detect_obstacle:
                self.detect_obstacle = False
                self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        self.score = 0
        self.detect_obstacle = False