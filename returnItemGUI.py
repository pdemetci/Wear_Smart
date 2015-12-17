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
        self.SCREEN = pygame.display.set_mode((800, 600))
        self.state=None
        self.ser=serial.Serial("/dev/ttyACM0", 9600, timeout=5)

    def GUI_display(self):
        self.SCREEN.fill((18,151,147))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=False, italic=False).render("Please select the item you'd like to return", True, (255, 255, 255)), (50, 50))
        pygame.draw.rect(self.SCREEN, (50,50,50), (50,180,300,80))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Umbrella", True, (255, 255, 255)), (130, 200))
        pygame.draw.rect(self.SCREEN, (50,50,50), (50,350,300,80))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Sun Cap", True, (255,255,255)), (130, 370))
        pygame.draw.rect(self.SCREEN, (50,50,50), (450,180,300,80))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Cardigan", True, (255,255,255)), (530, 200))
        pygame.draw.rect(self.SCREEN, (50,50,50), (450,350,300,80))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Scarf", True, (255,255,255)), (530, 370))
        pygame.draw.rect(self.SCREEN, (255,165,50), (0,500,400,70))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("< Go Back", True, (255, 255, 255)), (70, 520))
        pygame.draw.rect(self.SCREEN, (255,165,50), (420,500,380,70))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Done >", True, (255, 255, 255)), (600, 520))
        pygame.display.update()


    def handleEvents(self):
        mouseX,mouseY=pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:

            if 50<mouseX<300 and 180<mouseY<260 and event.type==MOUSEBUTTONDOWN:
                pygame.draw.rect(self.SCREEN, (255,255,255), (50,180,300,80))
                self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Umbrella", True, (50, 50, 50)), (130, 200))
                pygame.display.update()	
                if self.ser.isOpen():
                    self.ser.write("5")
                    time.sleep(1)
            if 50<mouseX<350 and 350<mouseY<430 and event.type==MOUSEBUTTONDOWN:
                pygame.draw.rect(self.SCREEN, (255,255,255), (50,350,300,80))
                self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Sun Cap", True, (50, 50, 50)), (130, 370))
                pygame.display.update()
                if self.ser.isOpen():
                    self.ser.write("6")
                    time.sleep(1)
            if 450<mouseX<750 and 180<mouseY<260 and event.type==MOUSEBUTTONDOWN:
                pygame.draw.rect(self.SCREEN, (255,255,255), (45,180,300,80))
                self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Cardigan", True, (50, 50, 50)), (530, 200))
                pygame.display.update()
                if self.ser.isOpen():
                    self.ser.write("7")
                    time.sleep(1)
            if 450<mouseX<750 and 350<mouseY<430 and event.type==MOUSEBUTTONDOWN:
                pygame.draw.rect(self.SCREEN, (255,255,255), (450,350,300,80))
                self.SCREEN.blit(pygame.font.SysFont('Arial', 30, bold=True, italic=False).render("Scarf", True, (50, 50, 50)), (530, 370))
                pygame.display.update()
                if self.ser.isOpen():
                    self.ser.write("8")
                    time.sleep(1)
            if 420<mouseX<800 and 500<mouseY<570 and event.type==MOUSEBUTTONDOWN:
                if self.ser.isOpen():
                    self.ser.write("0")
                    time.sleep(1)
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
