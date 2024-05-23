import pygame
import random

# Initialize Pygame
pygame.init()

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

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Paddle setup
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball setup
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [random.choice([4, -4]), -4]

# Bricks setup
bricks = []
for row in range(ROWS):
    for col in range(COLUMNS):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5) + 35, row * (BRICK_HEIGHT + 5) + 35, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 6
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += 6

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= SCREEN_HEIGHT:
        running = False  # Game over if ball hits bottom

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, YELLOW, ball)
    for brick in bricks:
        pygame.draw.rect(screen, random.choice([RED, GREEN, BLUE, YELLOW]), brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
