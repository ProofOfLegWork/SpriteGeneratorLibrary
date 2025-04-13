import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Mario character
mario = pygame.Rect(50, 300, 40, 40)  # x, y, width, height
mario_color = RED
mario_speed = 5
mario_jump = -15
gravity = 1
velocity_y = 0
is_jumping = False

# Platform
platform = pygame.Rect(0, 350, SCREEN_WIDTH, 50)  # x, y, width, height

# Game loop
def game_loop():
    global velocity_y, is_jumping

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mario.x -= mario_speed
        if keys[pygame.K_RIGHT]:
            mario.x += mario_speed
        if keys[pygame.K_SPACE] and not is_jumping:
            velocity_y = mario_jump
            is_jumping = True

        # Apply gravity
        velocity_y += gravity
        mario.y += velocity_y

        # Check for collision with the platform
        if mario.colliderect(platform):
            mario.y = platform.y - mario.height
            velocity_y = 0
            is_jumping = False

        # Prevent Mario from going off-screen
        if mario.x < 0:
            mario.x = 0
        if mario.x > SCREEN_WIDTH - mario.width:
            mario.x = SCREEN_WIDTH - mario.width

        # Draw everything
        screen.fill(WHITE)  # Clear screen
        pygame.draw.rect(screen, GREEN, platform)  # Draw platform
        pygame.draw.rect(screen, mario_color, mario)  # Draw Mario

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    game_loop()