import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 10
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
ROWS = 5
COLUMNS = 10
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 6

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.right += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed = [random.choice([4, -4]), -4]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def bounce(self, axis):
        if axis == 'x':
            self.speed[0] = -self.speed[0]
        if axis == 'y':
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        pygame.draw.ellipse(screen, YELLOW, self.rect)


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = random.choice([RED, GREEN, BLUE, YELLOW])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout Game")
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = self.create_bricks()
        self.running = True

    def create_bricks(self):
        bricks = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = col * (BRICK_WIDTH + 5) + 35
                y = row * (BRICK_HEIGHT + 5) + 35
                bricks.append(Brick(x, y))
        return bricks

    def check_collisions(self):
        # Ball collision with walls
        if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.bounce('x')
        if self.ball.rect.top <= 0:
            self.ball.bounce('y')
        if self.ball.rect.bottom >= SCREEN_HEIGHT:
            self.running = False  # Game over if ball hits bottom

        # Ball collision with paddle
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce('y')

        # Ball collision with bricks
        for brick in self.bricks[:]:
            if self.ball.rect.colliderect(brick.rect):
                self.ball.bounce('y')
                self.bricks.remove(brick)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.paddle.move(keys)
            self.ball.move()
            self.check_collisions()

            self.screen.fill(BLACK)
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
