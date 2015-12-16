from weatherForecastInfo import WeatherForecast
import pygame, math, time, syslog, sys, glob, datetime, locale
from pygame.locals import *
from turnTable import main
import serial
# from returnItem import returnItem
# from flip_ticks import MainScreen

def GUI_display():
    pygame.init()
    SCREEN = pygame.display.set_mode((450, 320))
    SCREEN.fill((18,151,147))
    SCREEN.blit(pygame.font.SysFont('Arial', 18, bold=False, italic=False).render("Please select the item you'd like to return", True, (50, 50, 50)), (50, 50))
    pygame.draw.rect(SCREEN, (50,50,50), (50,100,150,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Umbrella", True, (255, 255, 255)), (70, 110))
    pygame.draw.rect(SCREEN, (50,50,50), (50,180,150,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Sun Cap", True, (255,255,255)), (70, 180))
    pygame.draw.rect(SCREEN, (50,50,50), (250,100,150,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Cardigan", True, (255,255,255)), (300, 110))
    pygame.draw.rect(SCREEN, (50,50,50), (250,180,150,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Scarf", True, (255,255,255)), (300, 180))
    pygame.draw.rect(SCREEN, (255,165,50), (0,270,220,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("< Go Back", True, (255, 255, 255)), (50, 275))
    pygame.draw.rect(SCREEN, (255,165,50), (250,270,220,40))
    SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Done >", True, (255, 255, 255)), (300, 275))
    pygame.display.update()
    

def handleEvents():
    # a=returnItem()
    mouseX,mouseY=pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if 50<mouseX<200 and 100<mouseY<140 and event.type==MOUSEBUTTONDOWN:
            # a.state="5"
            print "5"
        if 50<mouseX<200 and 180<mouseY<220 and event.type==MOUSEBUTTONDOWN:
            # a.state="6"
            print "6"
        if 250<mouseX<400 and 100<mouseY<140 and event.type==MOUSEBUTTONDOWN:
            # a.state="7"
            print "7"
        if 250<mouseX<400 and 180<mouseY<220 and event.type==MOUSEBUTTONDOWN:
            # a.state="8"
            print "8"
        if 250<mouseX<470 and 270<mouseY<310 and event.type==MOUSEBUTTONDOWN:
            pass
            #default
        # if 0<mouseX<220 and 270<mouseY<310 and event.type==MOUSEBUTTONDOWN:
        #     TICKS = pygame.time.get_ticks()+1000
        #     a = MainScreen()
        #     a.fillScreen()
        #     while not pygame.event.peek(pygame.QUIT):
        #         pygame.event.clear()
        #         a.fillScreen()
        #         pygame.time.delay(TICKS-pygame.time.get_ticks())
        #         TICKS += 1000


GUI_display()
TICKS = pygame.time.get_ticks()+1000
while not pygame.event.peek(pygame.QUIT):
    GUI_display()
    handleEvents()
    pygame.time.delay(TICKS-pygame.time.get_ticks())
    TICKS += 1000

# def handleItem():
#     if state==5:
#         #Umbrella
#     elif state ==2:
#         #Sun Cap
#     elif state == 3:
#         #
