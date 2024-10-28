from Button import Button
from Colors import BLUE, PERIWINKLE

def create_button(x, y, width, height, color, hover_color, pygame, text='', font_size=30):
    # TODO: Take colors from config
    return Button(x, y, width, height, color, hover_color, pygame, text, font_size)

def update_button(_button, isOn):
    # Update the button after click (ex: change text on/off)
    if isOn:
        _button.text = "on"
    else: _button.text = "off"

def get_button_position(pos, window_size, padding, heigth):
    # Border touched? Increment y and set x to 0
    if pos["x"] >= window_size[0]:
            pos["y"] += padding + heigth
            pos["x"] = 0 # Reset x position
    return pos

# Create button dynamically from configuration file
def get_button_list(pygame,_configuration, _window_configuration, key):
    # Get buttons name
    _button_list = [ command for command in _configuration[key]]
    _buttons = []

    # Get button parameters from configuration
    _window_size = pygame.display.get_window_size()
    _width = _window_configuration["buttons"]["width"]
    _heigth = _window_configuration["buttons"]["heigth"]
    _padding = _window_configuration["buttons"]["padding"]

    # Current draw position
    pos = { 
        "x": 0,
        "y": 0
    }

    for _button in _button_list:
        # Get x,y position
        pos = get_button_position(pos, _window_size, _padding, _heigth) 

        # Create button
        _buttons.append(create_button(pos["x"], pos["y"], _width, _heigth, BLUE, PERIWINKLE, pygame, text=_button))

        # Update X value
        pos["x"] += _padding + _width
    return _buttons