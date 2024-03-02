import pygame
import math
import numpy as np
# import numpy as np
# Constants for window dimensions
WIDTH, HEIGHT = 2000, 2000

# Constants for colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (192, 192, 192)

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




def calculate_accel(masses, x_positions, y_positions):
    a_vec_x = list(np.zeros(len(masses)))
    a_vec_y=list(np.zeros(len(masses)))
    a_vec = [0,0]
    for i in range(len(masses)):
        for j in range(len(masses)):
            # print(i,j)
            a_vec = [0,0]
            if j != i:
                angle = math.atan2((y_positions[j]-y_positions[i]),(x_positions[j]-x_positions[i]))
                dist = math.sqrt((x_positions[0]-x_positions[1])**2 + (y_positions[0]-y_positions[1])**2)
                accel = G_CONSTANT*masses[j]/(dist**2)
                new_vec_x = accel*math.cos(angle)
                new_vec_y = accel*math.sin(angle)
                a_vec[0] += new_vec_x
                a_vec[1] += new_vec_y
            a_vec_x[i] += a_vec[0]
            a_vec_y[i] += a_vec[1]
    return a_vec_x,a_vec_y
def update_vel(accel_x, accel_y, current_vel_x, current_vel_y):
  vel_x = list(np.zeros(len(accel_x)))
  vel_y = list(np.zeros(len(accel_x)))
  for i in range(len(current_vel_x)):
    vel_x[i] = current_vel_x[i] + accel_x[i]*DELTA_TIME
    vel_y[i] = current_vel_y[i] + accel_y[i]*DELTA_TIME

  return vel_x, vel_y
def update_pos(accel_x, accel_y, current_vel_x, current_vel_y):
  vel_x = list(np.zeros(len(accel_x)))
  vel_y = list(np.zeros(len(accel_x)))
  for i in range(len(current_vel_x)):
    vel_x[i] = current_vel_x[i] + accel_x[i]*DELTA_TIME
    vel_y[i] = current_vel_y[i] + accel_y[i]*DELTA_TIME

  return vel_x, vel_y
# Function to draw planets and orbits
def draw_planets(screen, angle):
    global YEAR
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 15)
    
    global pos_x, pos_y
    pygame.draw.circle(screen, (255,255,0), (250, 250), 10) 

    a_x, a_y = calculate_accel(MASS,pos_x,pos_y)
    v_x, v_y = update_vel(a_x,a_y,vel_x,vel_y)
    pos_x, pos_y = update_pos(v_x,v_y,pos_x,pos_y)
    iterator = 0
    for planet in PLANETS:
        semi_major_axis = planet["semi_major_axis"]
        semi_minor_axis = planet["semi_minor_axis"]
        color = planet["color"]
        speed = planet["speed"]
        x, y = calculate_position(angle * speed, semi_major_axis, semi_minor_axis)
        pygame.draw.circle(screen, color, (x, y), 5)
        pygame.draw.ellipse(screen, WHITE, (WIDTH // 2 - semi_major_axis, HEIGHT // 2 - semi_minor_axis, 2 * semi_major_axis, 2 * semi_minor_axis), 1)
        iterator+=1
    YEAR += 110
# # Function to calculate planet positions
# def calculate_position(angle, semi_major_axis, semi_minor_axis):
#     x = WIDTH // 2 + semi_major_axis * math.cos(math.radians(angle))
#     y = HEIGHT // 2 + semi_minor_axis * math.sin(math.radians(angle))
#     return int(x), int(y)
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
        screen.fill((0, 0, 0))  # Clear the screen

        draw_planets(screen, angle)
        angle += 0.5  # Update angle for next frame (controls planet movement speed)

        pygame.display.flip()
        clock.tick(60)  # Limit frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
