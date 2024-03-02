import pygame
import math

# Constants for window dimensions
WIDTH, HEIGHT = 1000, 300

# Constants for colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (192, 192, 192)

# Constants for planetary data
# The values are not to scale
PLANETS = [
    {"name": "Mercury", "semi_major_axis": 50, "semi_minor_axis": 45, "color": GRAY, "speed": 2},
    {"name": "Venus", "semi_major_axis": 100, "semi_minor_axis": 95, "color": (255, 165, 0), "speed": 1.5},
    {"name": "Earth", "semi_major_axis": 150, "semi_minor_axis": 145, "color": (0, 0, 255), "speed": 1},
    {"name": "Mars", "semi_major_axis": 200, "semi_minor_axis": 195, "color": (255, 0, 0), "speed": 0.8},
    {"name": "Jupiter", "semi_major_axis": 300, "semi_minor_axis": 295, "color": (255, 140, 0), "speed": 0.5},
    {"name": "Saturn", "semi_major_axis": 400, "semi_minor_axis": 395, "color": (255, 215, 0), "speed": 0.3},
    {"name": "Uranus", "semi_major_axis": 500, "semi_minor_axis": 495, "color": (0, 255, 255), "speed": 0.2},
    {"name": "Neptune", "semi_major_axis": 600, "semi_minor_axis": 595, "color": (0, 0, 128), "speed": 0.15}
]

# Function to calculate planet positions
def calculate_position(angle, semi_major_axis, semi_minor_axis):
    x = WIDTH // 2 + semi_major_axis * math.cos(math.radians(angle))
    y = HEIGHT // 2 + semi_minor_axis * math.sin(math.radians(angle))
    return int(x), int(y)

# Function to draw planets and orbits
def draw_planets(screen, angle):
    for planet in PLANETS:
        semi_major_axis = planet["semi_major_axis"]
        semi_minor_axis = planet["semi_minor_axis"]
        color = planet["color"]
        speed = planet["speed"]
        x, y = calculate_position(angle * speed, semi_major_axis, semi_minor_axis)
        pygame.draw.circle(screen, color, (x, y), 5)
        pygame.draw.ellipse(screen, WHITE, (WIDTH // 2 - semi_major_axis, HEIGHT // 2 - semi_minor_axis, 2 * semi_major_axis, 2 * semi_minor_axis), 1)

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((450, 300))
    pygame.display.set_caption("Solar System Simulator")
    clock = pygame.time.Clock()

    angle = 0  # Initial angle for planet positions
    # dragging = False
    # offset_x = 0
    # offset_y = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:  # Left mouse button
            #         dragging = True
            #         mouse_x, mouse_y = event.pos
            #         offset_x = mouse_x - WIDTH // 2
            #         offset_y = mouse_y - HEIGHT // 2
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     if event.button == 1:
            #         dragging = False
            # elif event.type == pygame.MOUSEMOTION:
            #     if dragging:
            #         mouse_x, mouse_y = event.pos
            #         WIDTH, HEIGHT = pygame.display.get_surface().get_size()
            #         new_center_x = mouse_x - offset_x
            #         new_center_y = mouse_y - offset_y
            #         screen.fill((0, 0, 0))  # Clear the screen
            #         screen.blit(screen, (new_center_x - WIDTH // 2, new_center_y - HEIGHT // 2))
            #         pygame.display.flip()

        screen.fill((0, 0, 0))  # Clear the screen

        draw_planets(screen, angle)
        angle += 0.5  # Update angle for next frame (controls planet movement speed)

        pygame.display.flip()
        clock.tick(60)  # Limit frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
