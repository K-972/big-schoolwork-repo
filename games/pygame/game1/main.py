import pygame
import random

pygame.init()

# Define game window dimensions
screen_width = 288
screen_height = 512

# Set up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load images
bg_img = pygame.image.load("bg.png").convert_alpha()
bird_img = pygame.image.load("bird.png").convert_alpha()
pipe_img = pygame.image.load("pipe.png").convert_alpha()

# Define bird properties
bird_x = 50
bird_y = 200
bird_y_speed = 0
bird_gravity = 0.25

# Define pipe properties
pipe_x = screen_width
pipe_gap = 100
pipe_speed = 2
pipe_width = 52
pipe_height = 320
pipe_gap_height = 150
pipe_color = (0, 255, 0)

# Define game over message properties
game_over_font = pygame.font.Font("freesansbold.ttf", 32)
game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))

# Define score properties
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)

# Define game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_speed = -6
    
    # Move the bird
    bird_y_speed += bird_gravity
    bird_y += bird_y_speed
    
    # Move the pipes
    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = screen_width
        pipe_gap_top = random.randint(50, screen_height - pipe_gap_height - 50)
        pipe_gap_bottom = pipe_gap_top + pipe_gap_height
    
    # Detect collisions
    bird_rect = pygame.Rect(bird_x, bird_y, bird_img.get_width(), bird_img.get_height())
    pipe_top_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_gap_top)
    pipe_bottom_rect = pygame.Rect(pipe_x, pipe_gap_bottom, pipe_width, screen_height - pipe_gap_bottom)
    if bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(pipe_bottom_rect) or bird_y < 0 or bird_y > screen_height:
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        game_running = False
    
    # Draw the game
    screen.blit(bg_img, (0, 0))
    screen.blit(bird_img, (bird_x, bird_y))
    pygame.draw.rect(screen, pipe_color, (pipe_x, 0, pipe_width, pipe_gap_top))
    pygame.draw.rect(screen, pipe_color, (pipe_x, pipe_gap_bottom, pipe_width, screen_height - pipe_gap_bottom))
    score_text = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 50))
    pygame.display.flip()
    
    # Update the score
    if pipe_x < bird_x and pipe_x + pipe_speed >= bird_x:
        score += 1

# Clean up and quit
