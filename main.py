import pygame, time
from sys import exit
from player import Player
from obstacles import Obstacles
from score import Score
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_CAPTION)

        self.player = Player()
        self.obstacle = Obstacles(self.display, "black")

        self.clock = pygame.time.Clock()
        self.prev_time = time.time()
        self.dt = 0
        self.now = 0

        self.font = pygame.font.SysFont("Arial", 22, True)
        self.score = Score(self.font, 'black')

    def main_loop(self):
        while True:
            self.event_loop()
            self.draw()
            self.update()

    def draw(self):
        self.display.fill("white")
        self.player.draw(self.display)
        self.obstacle.draw(self.display, self.player.rect)
        self.score.draw(self.display, self.font, 'black')

    def update(self):  
        self.score.update(self.player.rect.x, self.obstacle.x_positions)

        # Update Player 
        self.player.update(self.dt)
        if self.player.rect.bottom >= 600 or self.player.rect.top <= 0:
            self.reset_game()
 

        # Update Obstacles
        self.obstacle.update(self.dt)
        if self.obstacle.death == True:
            self.reset_game()
        # Update display
        pygame.display.flip()

        # Manage Time 
        self.clock.tick(FPS)
        self.now = time.time()
        self.dt = self.now - self.prev_time
        self.prev_time = self.now

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                    self.player.jump()

    def quit_game(self):
        with open('high_scores.txt', 'r') as file:
            if int(file.read()) < self.score.high_score:
                with open('high_scores.txt', 'w') as f:
                    f.write(str(self.score.high_score))
        pygame.quit()
        exit()

    def reset_game(self):
        self.player.reset()
        self.obstacle.reset()
        self.score.reset()

if __name__ == "__main__":
    game = Game()
    game.main_loop()