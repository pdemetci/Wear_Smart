from weatherForecastInfo import WeatherForecast
import serial
import time
import random
import pygame
import MainScreen

class turnTable:	
	def __init__ (self):
		self.weatherForecast = WeatherForecast(api_key= "18e78bb19491e1929765a1354c99d45a", lat=42.27453, lng=-71.243861)
		self.weatherForecastInfo = self.weatherForecast.getWeatherForecast()
		self.status = None	# status of table: 0 - default / 1- umbrella / 2 - cardigan / 3 - sun cap / 4 - scarf
		self.ser=serial.Serial("/dev/ttyACM0", 9600, timeout=5)
	def mainTable(self):
		self.weatherForecast.getWeatherForecast()
		self.checkPrecip()
		self.communicateToSerial()
		while True:
			print self.ser.readline()
			if self.ser.readline()=="check temp":
				self.checkTemp()
				self.communicateToSerial()
				break
	def checkPrecip(self):
		(self.precipTime, self.maxPrecip) = self.weatherForecast.maxPrecipProb
		if True: 			# if it rains
			self.status = "1" 		# hands umbrella
		else:	
			if self.weatherForecast.icon=="clear-day" or self.weatherForecast.icon=="clear-night" or self.weatherForecast.icon=="partly-cloudy-day" or self.weatherForecast.icon=="partly-cloudy-night":					# if sunny is true
				self.status = "3" 		# hands sun cap
			else:
				self.status = "0" 		# goes to default

	def checkTemp(self):
		(self.maxTime,self.maxTemp) = self.weatherForecast.maxTemp
		(self.minTime,self.minTemp) = self.weatherForecast.minTemp
		if True: 		# if the temperature difference is large
			self.status = "2"
						# hands cardigan
		elif self.weatherForecast.currentTemp < 10 or self.weatherForecast.averageTemp < 10: 		# if it's cold
			self.status = "4"							# hands scarf
		else:
			self.status = "0"							# goes to default

	def communicateToSerial(self):
		ser = serial.Serial(port = "/dev/ttyACM0", baudrate=9600)
		ser.close()
		ser.open()
		random.seed()
		a=[]
		while ser.isOpen() and len(a)<2:
			print True
			ser.write(self.status)
			a.append(self.status)
			time.sleep(1)

if __name__ == '__main__':
	a=turnTable()
	a.mainTable()
