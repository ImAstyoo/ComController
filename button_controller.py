from button import Button
from colors import BLUE, PERIWINKLE

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