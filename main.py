import sys
import pygame
import json
from button_controller import *
from colors import *

def init_configuration(file):
    with open(file, "r") as file:
        return json.load(file)
    config_file.close()

def onClick(_button, _event):
    # TODO: Add the serial port controller function 
    update_button(_button) # Invert the isOn boolean

def bind_onClick(command):
    return

if __name__ == "__main__":
    # Get configuration files
    configuration = init_configuration(".\src\Config\Configuration.json")
    window_configuration = init_configuration(".\src\Config\WindowConfiguration.json")

    # Required
    pygame.init()   

    # Set screen properties
    screen = pygame.display.set_mode((window_configuration["width"], window_configuration["heigth"]))
    pygame.display.set_caption(window_configuration["title"])
    
    commands_dict = configuration["commands"]

    # Fetch and create buttons from configuration file
    commands = get_button_list(pygame, commands_dict.keys(), window_configuration)

    commands = [bind_onClick(command) for command in commands]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for button in commands:
                if button.is_clicked(event):
                    onClick(button, event)

        # Fill the screen with a color (RGB)
        screen.fill((WHITE))  # Fill with white

        # Drawing all the buttons
        [button.draw(screen) for button in commands]
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
