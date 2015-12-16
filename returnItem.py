from weatherForecastInfo import WeatherForecast
import serial
import time
import random
import GUI2

class returnItem():	
	def __init__ (self):
		self.weatherForecast = WeatherForecast(api_key= "18e78bb19491e1929765a1354c99d45a", lat=42.27453, lng=-71.243861)
		self.weatherForecastInfo = self.weatherForecast.getWeatherForecast()
		self.status = None	# status of table: 0 - default / 1- umbrella / 2 - cardigan / 3 - sun cap / 4 - scarf
		self.ser=serial.Serial("/dev/ttyACM1", 9600, timeout=5)
		self.gui=GUI2.returnGUI()

	def mainTable(self):
		self.communicateToSerial()

	def communicateToSerial(self):
		ser = serial.Serial(port = "/dev/ttyACM1", baudrate=9600)
		ser.close()
		ser.open()
		random.seed()
		while ser.isOpen():
			ser.write(self.gui.state)
			time.sleep(1)
			

if __name__ == '__main__':
	a=returnItem()
	a.mainTable()
