import pygame
import sys

from models import Ball, Paddle


class Game:
    def __init__(self):
        pygame.init()

        size = (600, 400)
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode(size)
        pygame.draw.circle(self.window, (244,0,0), (10, 10), 9)    

        self.ball = Ball(10, 0, (80, 80, 80))
        self.left_paddle = Paddle(50, 20, (80, 0, 0))
        self.right_paddle = Paddle(50, 20, (0, 0, 80))

    def render_ball(self, x, y):
        ball = self.ball
        pygame.draw.circle(
            self.window, ball.colour, (x, y), ball.radius, ball.width
        )    
        
    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            self.render_ball(30, 30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pass

            self.clock.tick(100)
            pygame.display.flip()

Game().run()
