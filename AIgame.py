import pygame      
import sys      
import random    
  
# Initialize Pygame      
pygame.init()      
      
# Screen dimensions      
WIDTH, HEIGHT = 800, 600      
screen = pygame.display.set_mode((WIDTH, HEIGHT))      
pygame.display.set_caption("AI HOLE")      
      
# Colors      
WHITE = (255, 255, 255)      
BLACK = (0, 0, 0)      
GREEN = (0, 255, 0)      
    
# Character settings      
player_size = 50      
initial_player_pos = [WIDTH // 2, HEIGHT - player_size]      
player_pos = initial_player_pos[:]    
player_velocity = 0  # Initial vertical velocity    
    
# Gravity and Jumping    
gravity = 0.001    
jump_force = 0.9  
is_on_ground = True    
jump_key_released = True    
    
# Walls    
wall_width = 100      
wall_height = HEIGHT      
wall_x = WIDTH      
wall_speed = 0.1      
      
# Define hole properties      
hole_height = 230  
hole_position = 200      
  
# Define the game over screen  
def game_over():    
    font = pygame.font.SysFont('Arial', 50)    
    text_surface = font.render('Game Over!', True, BLACK)    
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))    
    screen.blit(text_surface, text_rect)       
  
# Game loop      
running = True    
game_over_state = False    
while running:      
    if not game_over_state:  
        screen.fill(WHITE)      
          
        # Event handling      
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:      
                running = False      
    
        # Movement logic    
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_a]:    
            player_pos[0] -= 0.5    
        if keys[pygame.K_d]:    
            player_pos[0] += 0.5    
        if keys[pygame.K_SPACE] and is_on_ground and jump_key_released:    
            player_velocity = -jump_force    
            is_on_ground = False    
            jump_key_released = False    
        if not keys[pygame.K_SPACE]:    
            jump_key_released = True    
    
        # Gravity    
        player_velocity += gravity    
        player_pos[1] += player_velocity    
    
        # Check if player is on the ground      
        if player_pos[1] >= HEIGHT - player_size:      
            player_pos[1] = HEIGHT - player_size      
            player_velocity = 0      
            is_on_ground = True      
    
        # Wall Movement    
        wall_x -= wall_speed      
        if wall_x < -wall_width:      
            wall_x = WIDTH      
            hole_position = random.randint(50, HEIGHT - hole_height - 50)    
    
        # Collision and game over    
        if player_pos[0] < wall_x + wall_width and player_pos[0] + player_size > wall_x:    
            if not (hole_position < player_pos[1] < hole_position + hole_height):    
                game_over_state = True  # Set game over state  
         
        # Draw the wall with the hole      
        pygame.draw.rect(screen, BLACK, (wall_x, 0, wall_width, hole_position))      
        pygame.draw.rect(screen, BLACK, (wall_x, hole_position + hole_height, wall_width, HEIGHT - hole_position - hole_height))      
    
        # Draw character      
        pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))      
      
    else:  
        game_over()  # Display game over screen  
  
    pygame.display.flip()      
  
pygame.quit()      
sys.exit()      
