"""
This is the main module
"""

import pygame
from constants import(
    SCREEN_SIZE,
    RUNNING,
)

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.init()

while RUNNING:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            break
        # actions = SCENE.event_logic(event, SCREEN)
        # SCENE.draw(SCREEN_SIZE, SCREEN)
        try:
            # scene_name = actions.get('scene')
            # SCENE = SCENES.get(scene_name)
            pygame.display.flip()
            continue
        except KeyError:
            print('Key error occurred')
    pygame.display.update()
