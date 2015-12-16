from weatherForecastInfo import WeatherForecast
import pygame, math, time, sys, datetime, locale
from pygame.locals import *
import turnTable
import GUI2

class MainScreen():
    def __init__(self):
        locale.setlocale(locale.LC_TIME,'')
        pygame.init()
        self.SCREEN = pygame.display.set_mode((450, 320))
        self.weatherForecast = WeatherForecast(api_key= "18e78bb19491e1929765a1354c99d45a", lat=42.27453, lng=-71.243861)
        self.weatherForecast.getWeatherForecast()
        (self.maxTime,self.maxTemp) = self.weatherForecast.maxTemp
        self.maxTime= self.maxTime[10:]
        (self.minTime, self.minTemp) = self.weatherForecast.minTemp
        self.minTime= self.minTime[10:]
        (self.precipTime, self.maxPrecip) = self.weatherForecast.maxPrecipProb
        self.maxPrecip=float(self.maxPrecip)*100
        self.maxPrecip = str(self.maxPrecip)+"%"
        self.precipTime= self.precipTime[10:]
        self.currentTime = str(self.weatherForecast.currentTime)[10:16]
        self.state="turn"

    def main(self):
        TICKS = pygame.time.get_ticks()+1000
        self.fillScreen()
        while not pygame.event.peek(pygame.QUIT):
            self.fillScreen()
            self.handleEvents()
            pygame.time.delay(TICKS-pygame.time.get_ticks())
            TICKS += 1000
            # events = pygame.event.get()
            # for event in events:
            #     if event.type != QUIT and event.type == MOUSEBUTTONDOWN:
            #         mouseX, mouseY = pygame.mouse.get_pos()
            #         if 0<mouseX<220 and 265<mouseY<315:
            #             main()
            #         elif 230<mouseX<450 and 265<mouseY<315:
            #             pass    


    def handleEvents(self):
        # a=returnItem()
        mouseX,mouseY=pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            if 230<mouseX<450 and 265<mouseY<315 and event.type==MOUSEBUTTONDOWN:
                a=GUI2.returnGUI()
                a.main()
            if 0<mouseX<220 and 265<mouseY<315 and event.type==MOUSEBUTTONDOWN:
                a= turnTable.turnTable()
                a.mainTable()
                self.state="stop"


    def drawDate(self):
        dateUpdated = ''
        TIME = time.localtime()
        date=''
        for DATE in ('%a'),('%b'),('%Y'),('%d'):
            date += time.strftime(DATE,TIME)+ ' '

        dateUpdated+=date[:4]
        dateUpdated+= date[-3:]
        dateUpdated+= date[4:-3]

        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render(dateUpdated,1,(255,255,255)), (160,0))
    
    def drawImage(self):
        if self.weatherForecast.icon!= "clear-night" and "partly-cloudy-night":
            myimage = pygame.image.load(str(self.weatherForecast.icon)+".png")
        elif self.weatherForecast.icon=="clear-night":
            myimage = pygame.image.load("clear-day.png")
        elif self.weatherForecast.icon== "partly-cloudy-night":
            myimage = pygame.image.load("partly-cloudy-day.png")
        self.SCREEN.blit(myimage, (10,0))

    def drawButtons(self):
        pygame.draw.rect(self.SCREEN, (255,165,50), (0,265,220,50))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Receive Item", True, (50, 50, 50)), (50, 275))
        pygame.draw.rect(self.SCREEN, (255,165,50), (230,265,220,50))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Return Item", True, (50, 50, 50)), (285, 275))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 40, bold=True, italic=False).render(time.strftime('%H:%M:%S',time.localtime()), True, (255,165,0)), (160, 30))
        
    def fillScreen(self):
        # imagerect = myimage.get_rect()
        self.SCREEN.fill((18,151,147))
        pygame.draw.rect(self.SCREEN, (50,50,50), (0,0,450,120))
        # self.SCREEN.blit(pygame.font.SysFont('Arial', 18, bold=True, italic=False).render(dateUpdated, True, (255, 255, 255)), (150, 0))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Max:", True, (50, 50, 50)), (240, 180))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Min:", True, (50,50,50)), (30, 180))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render("Precip. Prob.:", True, (50,50,50)), (90, 210))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 18, bold=True, italic=False).render(str(self.weatherForecast.dailySummary), True, (255,255,255)), (160, 90))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render(str(self.maxTemp)+"F at " + str(self.maxTime)[0:6], True, (255,255,255)), (290, 180))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render(str(self.minTemp)+"F at " + str(self.minTime)[0:6], True, (255,255,255)), (80, 180))
        self.SCREEN.blit(pygame.font.SysFont('Arial', 20, bold=True, italic=False).render(str(self.maxPrecip)+ " at " + str(self.precipTime)[0:6], True, (255,255,255)), (240, 210))
        self.drawButtons()
        self.drawImage()
        self.drawDate()
        pygame.display.update()


if __name__ == '__main__':
    a=MainScreen()
    a.main()

