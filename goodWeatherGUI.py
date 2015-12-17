import pygame
from pygame.locals import *
import MainScreen


class returnGUI():
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((800, 600))

    def GUI_display(self):
        self.SCREEN.fill((18,151,147))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=False, italic=False).render("Today the weather is nice", True, (255, 255, 255)), (50, 150))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=False, italic=False).render("You don't need anything, just go outside!", True, (255, 255, 255)), (50, 250))
        pygame.draw.rect(self.SCREEN, (255,165,50), (0,500,400,70))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Okay", True, (255, 255, 255)), (120, 520))

        pygame.display.update()
        

    def handleEvents(self):
        mouseX,mouseY=pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if 0<mouseX<400 and 500<mouseY<570 and event.type==MOUSEBUTTONDOWN:
                b=MainScreen.MainScreen()
                b.main()

    def main(self):
        self.GUI_display()
        TICKS = pygame.time.get_ticks()+1000
        while not pygame.event.peek(pygame.QUIT):
            self.GUI_display()
            self.handleEvents()
            pygame.time.delay(TICKS-pygame.time.get_ticks())
            TICKS += 1000

if __name__ == '__main__':
    a=returnGUI()
    a.main()
