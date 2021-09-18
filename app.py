import pygame
from pygame.locals import *


class App:
    """
        the main app
    """

    def __init__(self):
        """this constructor of  the class"""
        self.running = True
        self.display_surf = True
        self.size = self.weight, self.height = 640, 400
    # End

    def on_init(self):
        """ On load. tuning the parameters"""
        pygame.init()
        self.display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
    # End

    def on_event(self, event):
        """ on event handler """
        if event.type == pygame.QUIT:
            self.running = False
    # End

    def on_loop(slef):
        """ game loop """
        pass

    def on_render(self):
        """ render """
        pass

    def on_cleanup(self):
        """ clean up the memory"""
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
