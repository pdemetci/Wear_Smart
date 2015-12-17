from weatherForecastInfo import WeatherForecast
import serial
import time
import random
import pygame
import MainScreen
import goodWeatherGUI
class turnTable:	
	def __init__ (self):
		self.weatherForecast = WeatherForecast(api_key= "18e78bb19491e1929765a1354c99d45a", lat=42.27453, lng=-71.243861)
		self.weatherForecastInfo = self.weatherForecast.getWeatherForecast()
		self.status = None	# status of table: 0 - default / 1- umbrella / 2 - cardigan / 3 - sun cap / 4 - scarf
		self.ser=serial.Serial("/dev/ttyACM0", 9600, timeout=5)

	def mainTable(self):
		"""
		The main function of the class. 
		Gets weather info and communicates commands to the serial port accordingly 
		in order to turn the disk and give the appropriate item to the user.
		"""
		self.weatherForecast.getWeatherForecast()
		self.checkWeather()
		self.communicateToSerial()

	def checkWeather(self):
		"""
		Firstly checks whether the weather is rainy or sunny. If not either of those, runs the checkTemp code.
		"""
		(self.precipTime, self.maxPrecip) = self.weatherForecast.maxPrecipProb
		if self.maxPrecip> 0.5: 			# if it rains
			self.status = "1" 		# hands umbrella
		elif self.weatherForecast.icon=="clear-day" or self.weatherForecast.icon=="clear-night" or self.weatherForecast.icon=="partly-cloudy-day" or self.weatherForecast.icon=="partly-cloudy-night":					# if sunny is true
				self.status = "3" 		# hands sun cap
		else:
			self.checkTemp() 

	def checkTemp(self):
		"""
		Checks temperature and changes self.status according to the appropriate item for the temperature.
		"""
		(self.maxTime,self.maxTemp) = self.weatherForecast.maxTemp # maxTemp data in WeatherForecastInfo is a tuple that also contains the time of max Temp. 
		(self.minTime,self.minTemp) = self.weatherForecast.minTemp
		if self.maxTemp - self.minTemp > 18: 		# if the temperature difference is large
			self.status = "2"				# hands cardigan
		elif self.weatherForecast.currentTemp < 10 or self.weatherForecast.averageTemp < 10: 		# if it's cold
			self.status = "4"							# hands scarf
		else:
			a=goodWeatherGUI.goodWeatherGUI()  #<-- if the weather is good enough that the user does not need any of the items, this is displayed in the "goodWeatherGUI"
			a.main()
			
	def communicateToSerial(self):
		"""
		Writes self.state to the serial port for Arduino to read.
		"""
		ser = serial.Serial(port = "/dev/ttyACM0", baudrate=9600)
		if ser.isOpen():
			ser.write(self.status)
			time.sleep(1)

if __name__ == '__main__':
	a=turnTable()
	a.mainTable()
