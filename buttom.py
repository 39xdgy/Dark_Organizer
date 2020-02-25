import pygame
class buttom:

    def __init__(self, position, unactive_color, active_color):
        self.position = position
        self.UAC = unactive_color
        self.AC = active_color

    def change_position(self, new_position):
        self.position = new_position

    def return_position(self):
        return self.position

    def change_unactive_color(self, NUAC):
        self.UAC = NUAC

    def return_unactive_color(self):
        return self.UAC

    def change_active_color(self, NAC):
        self.AC = NAC

    def return_active_color(self):
        return self.AC

    def draw_unactive_buttom(self, environment):
        pygame.draw.rect(environment, self.UAC, self.position, 0)

    def draw_active_buttom(self, environment):
        pygame.draw.rect(environment, self.AC, self.position, 0)

    def buttom_is_press(self, environment,  mouse):
        if(self.return_position().collidepoint(mouse)):
            self.draw_active_buttom(environment)
            if(pygame.mouse.get_pressed()[0]):
                return True
            
        else:
            self.draw_unactive_buttom(environment)
        return False

    def text_in_buttom(self, environment, font, text):
        text_surface = font.render(text, False, (0, 0, 0))
        environment.blit(text_surface, (self.return_position()[0]+2, self.return_position()[1]+4))
