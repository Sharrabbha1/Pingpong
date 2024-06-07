import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player1 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
player2 = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

ball_speed_x = 7 * (-1 if pygame.time.get_ticks() % 2 else 1)
ball_speed_y = 7 * (-1 if pygame.time.get_ticks() % 2 else 1)
player_speed = 0
opponent_speed = 7

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Player movement
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT

    # Opponent movement
    if player2.top < ball.y:
        player2.top += opponent_speed
    if player2.bottom > ball.y:
        player2.bottom -= opponent_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
