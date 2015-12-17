from weatherForecastInfo import WeatherForecast
import serial
import time
import random
import returnItemGUI

class returnItem():	
	"""
	This class handles the communication to the serial port while returning an item.
	returnItemGUI implements its state depending on the mouse action on the GUI.
	"""
	def __init__ (self):
		self.status = None	# status of table: 0 - default / 1- umbrella / 2 - cardigan / 3 - sun cap / 4 - scarf
		self.ser=serial.Serial("/dev/ttyACM1", 9600, timeout=5)
		self.gui=returnItemGUI.returnGUI()

	def mainTable(self):
		self.communicateToSerial()

	def communicateToSerial(self):
		if self.ser.isOpen():
			self.ser.write(self.gui.state)
			time.sleep(1)
			

if __name__ == '__main__':
	a=returnItem()
	a.mainTable()
