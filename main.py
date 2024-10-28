import sys
import pygame
import json
from button_controller import *
from Colors import *

def init_configuration(file):
    with open(file, "r") as file:
        return json.load(file)
    config_file.close()

def onClick(_button, _event):
    # TODO: Add the serial port controller function 
    update_button(_button, not _button.isOn) # Invert the isOn boolean

if __name__ == "__main__":
    # Get configuration files
    configuration = init_configuration(".\src\Config\Configuration.json")
    window_configuration = init_configuration(".\src\Config\WindowConfiguration.json")

    # Required
    pygame.init()   

    # Set screen properties
    screen = pygame.display.set_mode((window_configuration["width"], window_configuration["heigth"]))
    pygame.display.set_caption(window_configuration["title"])
    
    # Fetch and create buttons from configuration file
    buttons = get_button_list(pygame, configuration, window_configuration,"commands")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in buttons:
                if button.is_clicked(event):
                    onClick(button, event)

        # Fill the screen with a color (RGB)
        screen.fill((WHITE))  # Fill with white

        # Drawing all the buttons
        [button.draw(screen) for button in buttons]
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
