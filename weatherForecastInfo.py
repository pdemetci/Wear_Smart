import forecastio
import datetime
from operator import itemgetter

class WeatherForecast():

	def __init__(self, api_key, lat, lng):
		"""
		Initializes the WeatherForecast Class
		"""
		### Variables Taken ###
		self.api_key=api_key
		self.lat=lat
		self.lng= lng

		### Forecastio Related Variables to be Used ###
		self.forecast=forecastio.load_forecast(self.api_key, self.lat, self.lng)
		self.offset=self.forecast.offset()
		self.hourlyForecast = self.forecast.hourly()
		self.dailyForecast = self.forecast.daily()
		self.currentForecast = self.forecast.currently()

		### Initializing Variables to Return ###
		self.maxTemp = None
		self.minTemp = None
		self.currentTemp=None
		self.precipProb = None
		self.dailySummary=None
		self.currentTime = datetime.datetime.now().replace(second=0, microsecond=0)
		self.precipProbability=[]
		self.maxPrecipProb=None
	 	self.icon = None

	def getWeatherForecast(self):
		"""
		The main function of the class. Gets all the weather information we use.
		"""
		self.getTodaySummary()
		self.getTemperatureData()
		self.getPrecipitationInfo()

	def convert_localTime(self, utctime):
		"""
		Convert the utc time(common time worldwide) to local time using offset offered by API 
		"""
		local_time=utctime+datetime.timedelta(hours=self.offset)
		return local_time

	def getTodaySummary(self):
		"""
		Gets the summary and the icon for the day. e.g. summary="Mostly rainy in the morning" icon="rain"
		"""

	 	for data in self.dailyForecast.data:
	 		local_time=self.convert_localTime(data.time)
	 		if local_time.day == self.currentTime.day:
	 			self.dailySummary = str(data.summary)
	 	self.icon = str(self.dailyForecast.icon)

	def getTemperatureData(self):
		"""
		Gets max,min and current temperature
		"""
		listTemp=[]
		Time=[]

		for data in self.hourlyForecast.data:
	 		#change utc time to local time using offset
	 		local_time=self.convert_localTime(data.time)
	 		#only add the data corresponds to today
	 		#Without it, we get information for the next 24 hours, even if another day starts in the middle of it.
	 		if local_time.day == self.currentTime.day:
 				listTemp.append((str(local_time), data.temperature))
 		
 		##Compare only the second element of the tuple and get the minimum and maximum tuples.
 		self.minTemp=min(listTemp, key=itemgetter(1))
	 	self.maxTemp=max(listTemp, key=itemgetter(1))
	 	self.currentTemp=self.currentForecast.temperature

	def getPrecipitationInfo(self):
		"""
		Gets the precipitation probability information
		"""
	 	for data in self.hourlyForecast.data:
	 		#change utc time to local time using offset
	 		local_time=self.convert_localTime(data.time)
	 		##only add the data corresponds to today
	 		if local_time.day == self.currentTime.day:
	 			self.precipProbability.append((str(local_time), data.precipProbability))

	 	##get max precip probability during a day(today)
	 	self.maxPrecipProb=max(self.precipProbability, key=itemgetter(1))



if __name__ == '__main__':
	api_key= "18e78bb19491e1929765a1354c99d45a"
	#Latitude and Longitude information for Boston
	lat=42.27453
	lng=-71.243861
	weather = WeatherForecast(api_key=api_key, lat=lat, lng=lng)
	weather.getWeatherForecast()

