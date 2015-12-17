
from weatherForecastInfo import WeatherForecast
import pygame, math, time, syslog, sys, glob, datetime, locale
from pygame.locals import *
import serial
import MainScreen
import serial
import time
import random

class returnGUI():
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((450, 320))
        self.state=None
        self.ser=serial.Serial("/dev/ttyACM0", 9600, timeout=5)

    def GUI_display(self):
        self.SCREEN.fill((18,151,147))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 18, bold=False, italic=False).render("Please select the item you'd like to return", True, (50, 50, 50)), (50, 50))
        pygame.draw.rect(self.SCREEN, (50,50,50), (50,100,150,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Umbrella", True, (255, 255, 255)), (70, 110))
        pygame.draw.rect(self.SCREEN, (50,50,50), (50,180,150,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Sun Cap", True, (255,255,255)), (70, 180))
        pygame.draw.rect(self.SCREEN, (50,50,50), (250,100,150,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Cardigan", True, (255,255,255)), (300, 110))
        pygame.draw.rect(self.SCREEN, (50,50,50), (250,180,150,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Scarf", True, (255,255,255)), (300, 180))
        pygame.draw.rect(self.SCREEN, (255,165,50), (0,270,220,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("< Go Back", True, (255, 255, 255)), (50, 275))
        pygame.draw.rect(self.SCREEN, (255,165,50), (250,270,220,40))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Done >", True, (255, 255, 255)), (300, 275))
        pygame.display.update()
        

    def handleEvents(self):
        mouseX,mouseY=pygame.mouse.get_pos()
        events = pygame.event.get()
        ser = serial.Serial(port = "/dev/ttyACM0", baudrate=9600)
        ser.close()
        ser.open()
        random.seed()
        for event in events:
            if 50<mouseX<200 and 100<mouseY<140 and event.type==MOUSEBUTTONDOWN:
		pygame.draw.rect(self.SCREEN, (255,255,255), (50,100,150,40))
        	self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Umbrella", True, (50, 50, 50)), (70, 110))
		pygame.display.update()	
		if ser.isOpen():
                    ser.write("5")
                    time.sleep(1)
            if 50<mouseX<200 and 180<mouseY<220 and event.type==MOUSEBUTTONDOWN:
                if ser.isOpen():
                    ser.write("6")
                    time.sleep(1)
            if 250<mouseX<400 and 100<mouseY<140 and event.type==MOUSEBUTTONDOWN:
                if ser.isOpen():
                    ser.write("7")
                    time.sleep(1)
            if 250<mouseX<400 and 180<mouseY<220 and event.type==MOUSEBUTTONDOWN:
                if ser.isOpen():
                    ser.write("8")
                    time.sleep(1)
            if 250<mouseX<470 and 270<mouseY<310 and event.type==MOUSEBUTTONDOWN:
                if ser.isOpen():
                    ser.write("0")
                    time.sleep(1)
            if 0<mouseX<220 and 270<mouseY<310 and event.type==MOUSEBUTTONDOWN:
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
