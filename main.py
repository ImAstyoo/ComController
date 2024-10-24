import sys
import pygame
import json

config = "../Configuration.json"
window_config = "../WindowConfiguration.json"

def init_configuration(file):
    with open(file, "r") as file:
        return json.load(file)
    config_file.close()

if __name__ == "__main__":
    configuration = init_configuration(config)
    window_configuration = init_configuration(window_config)

    # Required
    pygame.init()   

    # Set screen properties
    screen = pygame.display.set_mode((window_configuration["width"], window_configuration["heigth"]))
    pygame.display.set_caption(window_configuration["title"])

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color (RGB)
        screen.fill((0, 0, 0))  # Fill with black

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()