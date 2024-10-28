# Button class
class Button:
    def __init__(self, x, y, width, height, color, hover_color, pygame, text='', font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_surf = self.font.render(text, True, (255,255,255)) # TODO: get from config file
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.pygame = pygame

    def draw(self, screen):
        # Change color on hover
        current_color = self.hover_color if self.rect.collidepoint(self.pygame.mouse.get_pos()) else self.color
        self.pygame.draw.rect(screen, current_color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        return event.type == self.pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
