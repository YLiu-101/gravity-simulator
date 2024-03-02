import pygame
import math

# Constants for window dimensions
WIDTH, HEIGHT = 1500, 1500

# Constants for colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
REDORANGE = (255, 25, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Constants for planetary data
# The values are not to scale
PLANETS = [
    {"name": "Sun", "semi_major_axis": 0, "semi_minor_axis": 0, "color": YELLOW, "speed": 0, "size": 17.5},
    {"name": "Mercury", "semi_major_axis": 50, "semi_minor_axis": 45, "color": GRAY, "speed": 2, "size": 7},
    {"name": "Venus", "semi_major_axis": 100, "semi_minor_axis": 95, "color": (255, 165, 0), "speed": 1.5, "size": 8},
    {"name": "Earth", "semi_major_axis": 150, "semi_minor_axis": 145, "color": (100, 100, 255), "speed": 1, "size": 8},
    {"name": "Mars", "semi_major_axis": 200, "semi_minor_axis": 195, "color": (255, 0, 0), "speed": 0.8, "size": 7.5},
    {"name": "Jupiter", "semi_major_axis": 300, "semi_minor_axis": 295, "color": (255, 140, 0), "speed": 0.5, "size": 12},
    {"name": "Saturn", "semi_major_axis": 400, "semi_minor_axis": 395, "color": (255, 215, 0), "speed": 0.3, "size": 11.5},
    {"name": "Uranus", "semi_major_axis": 500, "semi_minor_axis": 495, "color": (0, 255, 255), "speed": 0.2, "size": 11},
    {"name": "Neptune", "semi_major_axis": 600, "semi_minor_axis": 595, "color": (0, 0, 255), "speed": 0.15, "size": 11}
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
        size = planet["size"]
        x, y = calculate_position(angle * speed, semi_major_axis, semi_minor_axis)
        pygame.draw.circle(screen, color, (x, y), size)
        if planet["name"] == "Jupiter":
            pygame.draw.line(screen, REDORANGE, (x - (size / 2), y), (x + (size / 2), y))
            pygame.draw.line(screen, REDORANGE, (x - ((size / 2) * (math.sqrt(3)) / 2), y + (size / 2)), (x + ((size / 2) * (math.sqrt(3)) / 2), y + (size / 2)))
            pygame.draw.line(screen, REDORANGE, (x - ((size / 2) * (math.sqrt(3)) / 2), y - (size / 2)), (x + ((size / 2) * (math.sqrt(3)) / 2), y - (size / 2)))
            ellipse_rect = pygame.Rect(x - (size / 3), y + (size / 3), size / 1.5, size / 3)
            pygame.draw.ellipse(screen, REDORANGE, ellipse_rect, 5)
        if planet["name"] == "Uranus":
            pygame.draw.line(screen, WHITE, (x, y - (5 * size / 3)), (x, y + (5 * size / 3)))
        if planet["name"] == "Saturn":
            pygame.draw.line(screen, GRAY, (x - (3 * size / 2), y - size), (x + (3 * size / 2), y + size))
        if planet["name"] == "Earth":
            pygame.draw.circle(screen, GREEN, (x - (size / 2), y + (size / 8)), size / 3)
            pygame.draw.circle(screen, GREEN, (x + (size / 2), y + (size / 8)), size / 3)
            pygame.draw.circle(screen, GREEN, (x, y - (size / 2)), size / 3)
            pygame.draw.circle(screen, GREEN, (x, y + (size / 2)), size / 3)
        pygame.draw.ellipse(screen, WHITE, (WIDTH // 2 - semi_major_axis, HEIGHT // 2 - semi_minor_axis, 2 * semi_major_axis, 2 * semi_minor_axis), 1)

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((2000, 2000))
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
