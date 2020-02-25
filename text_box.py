import pygame
class text_box:
    
    def __init__(self, position, unactive_color, active_color):
        self.position = position
        self.UAC = unactive_color
        self.AC = active_color
        self.text = ''
        self.is_active = False
    
    def change_position(self, new_position):
        self.position = new_position

    def return_position(self):
        return self.position

    def change_unactive_color(self, new_unactive_color):
        self.UAC = new_unactive_color

    def return_unactive_color(self):
        return self.UAC

    def change_active_color(self, new_active_color):
        self.AC = new_active_color

    def return_active_color(self):
        return self.AC

    def change_text(self, new_text):
        self.text = new_text

    def add_text(self, letter):
        self.text += letter

    def delete_text(self):
        self.text = self.text[:-1]
        
    def return_text(self):
        return self.text

    def change_is_active(self, boolean):
        self.is_active = boolean

    def return_is_active(self):
        return self.is_active

    def draw_unactive_box(self, environment):
        pygame.draw.rect(environment, self.UAC, self.position, 0)

    def draw_active_box(self, environment):
        pygame.draw.rect(environment, self.AC, self.position, 0)

    def box_is_press(self, environment, mouse):
        if(self.return_position().collidepoint(mouse)):
            self.draw_active_box(environment)
            self.is_active = True
            if(pygame.mouse.get_pressed()[0]):
                return True
        else:
            self.draw_unactive_box(environment)
            self.is_active = False
        return False

    def write_in_box(self, environment, font):
        text_surface = font.render(self.return_text(), False, (0, 0, 0))
        environment.blit(text_surface, (self.return_position()[0] + 2, self.return_position()[1] + 4))

    def write_in_box_with_text(self, environment, font, input_text):
        text_surface = font.render(input_text, False, (0, 0, 0))
        environment.blit(text_surface, (self.return_position()[0] + 2, self.return_position()[1] + 4))
