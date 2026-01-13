import pygame
import random
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game variables
GRAVITY = 0.35
JUMP = -7
PIPE_GAP = 150
PIPE_WIDTH = 70
PIPE_SPEED = 3

FONT = pygame.font.SysFont("Arial", 32)

clock = pygame.time.Clock()

# Bird settings
bird_x = 60
bird_y = HEIGHT // 2
bird_velocity = 0
bird_radius = 16

# Pipes list
pipes = []  # each pipe is [x, top_height]
SPAWN_PIPE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_PIPE_EVENT, 1500)

score = 0


def draw_bird():
    pygame.draw.circle(WIN, (255, 255, 0), (bird_x, int(bird_y)), bird_radius)


def draw_pipes():
    for pipe in pipes:
        x, top_height = pipe
        # Top pipe
        pygame.draw.rect(WIN, (0, 200, 0), (x, 0, PIPE_WIDTH, top_height))
        # Bottom pipe
        bottom_y = top_height + PIPE_GAP
        pygame.draw.rect(WIN, (0, 200, 0), (x, bottom_y, PIPE_WIDTH, HEIGHT - bottom_y))


def check_collision():
    # Check ground / ceiling
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True

    # Check pipes
    for x, top_height in pipes:
        bottom_y = top_height + PIPE_GAP
        if x < bird_x + bird_radius < x + PIPE_WIDTH:
            if bird_y - bird_radius < top_height or bird_y + bird_radius > bottom_y:
                return True

    return False


def show_score():
    txt = FONT.render(f"Score: {score}", True, (255, 255, 255))
    WIN.blit(txt, (10, 10))


def game_over_screen():
    txt = FONT.render("GAME OVER!", True, (255, 0, 0))
    WIN.blit(txt, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    pygame.display.update()
    pygame.time.wait(2000)


# Main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN_PIPE_EVENT:
            top_height = random.randint(50, HEIGHT - PIPE_GAP - 50)
            pipes.append([WIDTH, top_height])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP

    # Bird physics
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # Move pipes
    for pipe in pipes:
        pipe[0] -= PIPE_SPEED

    # Score + pipe cleanup
    for pipe in pipes:
        if pipe[0] + PIPE_WIDTH == bird_x:
            score += 1
    pipes = [p for p in pipes if p[0] + PIPE_WIDTH > 0]

    # Check collisions
    if check_collision():
        game_over_screen()
        pygame.quit()
        sys.exit()

    # Draw everything
    WIN.fill((0, 0, 120))
    draw_bird()
    draw_pipes()
    show_score()
    pygame.display.update()

pygame.quit()
