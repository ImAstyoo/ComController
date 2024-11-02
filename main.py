import sys
import json
import pygame

WHITE = (255,255,255)
BLUE = (0,0,255)
PERIWINKLE = (100, 100, 255)

# Button class
class Button:
    def __init__(self, x, y, width, height, color, hover_color, pygame, name='', font_size=30, onClick=lambda x: None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.name = name
        self.text = f"{self.name}: off"
        self.font = pygame.font.Font(None, font_size)
        self.text_surf = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.pygame = pygame
        self.isOn = False
        self.OnClick = onClick

    def draw(self, screen):
        # Change color on hover
        current_color = self.hover_color if self.rect.collidepoint(self.pygame.mouse.get_pos()) else self.color
        self.pygame.draw.rect(screen, current_color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        return event.type == self.pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
    
    def swap_status(self):
        self.isOn = not self.isOn
        if self.isOn:
            self.text = f"{self.name}: on"
        else:
            self.text = f"{self.name}: off"
        self.text_surf = self.font.render(self.text, True, WHITE)

def create_button(x, y, width, height, color, hover_color, pygame,text='', font_size=30, ):
    # TODO: Take colors from config
    return Button(x, y, width, height, color, hover_color, pygame, text, font_size)

def update_button(_button):
    # Update the button after click (ex: change text on/off)
    _button.swap_status()

def get_button_position(pos, window_size, padding, heigth):
    # Border touched? Increment y and set x to 0
    if pos["x"] >= window_size[0]:
            pos["y"] += padding + heigth
            pos["x"] = 0 # Reset x position
    return pos

# Create button dynamically from configuration file
def get_button_list(pygame, commands, _window_configuration):
    # Get button parameters from configuration
    window_size = pygame.display.get_window_size()
    buttons_config = _window_configuration["buttons"]
    width = buttons_config["width"]
    heigth = buttons_config["heigth"]
    padding = buttons_config["padding"]

    # Current draw position
    pos = { 
        "x": 0,
        "y": 0
    }

    buttons = []
    # Cycle all names from configuration file and create the associated button
    for command in commands:
        # Get x,y position
        pos = get_button_position(pos, window_size, padding, heigth)
        # Create button
        buttons.append(create_button(pos["x"], pos["y"], width, heigth, BLUE, PERIWINKLE, pygame, command))

        # Update X value
        pos["x"] += padding + width

    # Return the list of buttons ready to be drawn
    return buttons

def init_configuration(file):
    with open(file, "r") as file:
        return json.load(file)
    config_file.close()

def onClick(_button, _event):
    # TODO: Add the serial port controller function 
    update_button(_button) # Invert the isOn boolean # TODO: change this invert to 'request status and update interface'

def bind_onClick(command):
    # TODO: implement com port controller
    return command 

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
        
        # Request port status
        # TODO: request port status

        # Modify button status
        # TODO: modify button status

        # Drawing all the buttons
        [button.draw(screen) for button in commands]

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()
