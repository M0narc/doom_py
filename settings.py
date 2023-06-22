import math

# main game settings
# screen resolution
RES = WIDTH, HEIGHT = 1600, 900
FPS = 60

# Settings for the player
PLAYER_POS = 1.5, 5 # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROTATION_SPEED = 0.002

# Raycasting
FOV = math.pi / 3 # field of view
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20