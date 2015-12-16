import forecastio
import datetime
from operator import itemgetter
# import pyserial

api_key= "18e78bb19491e1929765a1354c99d45a"
lat=42.27453
lng=-71.243861

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
		self.averageTemp = None
		self.maxTemp = None
		self.minTemp = None
		self.precipProb = None
		self.dailySummary=None
		self.currentTime = datetime.datetime.now().replace(second=0, microsecond=0)
		self.listHourlyTemp = None
		self.precipProbability=[]
		self.precipIntensity=[]
		self.maxPrecipProb=None
	 	self.currentPrecipProb=None
	 	self.maxPrecipInt= None
	 	self.currentPrecipInt=None
	 	self.weeklySummary=[]
	 	self.icon = None

	def getWeatherForecast(self):
		"""
		DocString
		"""
		self.getTodaySummary()
		self.getTemperatureData()
		self.getPrecipitationInfo()
		self.getWeeklyInfo()

	def convert_localTime(self, utctime):
		"""
		Convert the utc time(common time worldwide) to local time using offset offered by API 
		"""
		local_time=utctime+datetime.timedelta(hours=self.offset)
		return local_time

	def getTodaySummary(self):
		"""
		DocString
		"""

	 	for data in self.dailyForecast.data:
	 		local_time=self.convert_localTime(data.time)
	 		if local_time.day == self.currentTime.day:
	 			self.dailySummary = str(data.summary)
	 	self.icon = str(self.dailyForecast.icon)
	 	print self.icon

	def getTemperatureData(self):
		"""
		DocString
		"""

		sumTemp =0
		listTemp=[]
		count=0

		avg_sumTemp=0
		avg_count=0
		Time=[]


		for data in self.hourlyForecast.data:
	 		sumTemp+=data.temperature
	 		count+=1

	 		#change utc time to local time using offset
	 		local_time=self.convert_localTime(data.time)
	 		if local_time.day == self.currentTime.day:
 				listTemp.append((str(local_time), data.temperature))

 				avg_sumTemp+=data.temperature
 				avg_count+=1
 		
 		##Compare only the second element of the tuple and get the minimum and maximum tuples.
 		self.minTemp=min(listTemp, key=itemgetter(1))
	 	self.maxTemp=max(listTemp, key=itemgetter(1))
	 	self.currentTemp=self.currentForecast.temperature
	 	##Jake changed the count used in average because it returned average of 48hours--> I changed it to daily average.
	 	self.averageTemp= avg_sumTemp/avg_count
	 	self.listHourlyTemp = listTemp

	def getPrecipitationInfo(self):
		"""
		DocString
		"""
	 	for data in self.hourlyForecast.data:
	 		#change utc time to local time using offset
	 		local_time=self.convert_localTime(data.time)
	 		##only add the data corresponds to today
	 		if local_time.day == self.currentTime.day:
	 			self.precipProbability.append((str(local_time), data.precipProbability))
	 			self.precipIntensity.append((str(local_time), data.precipIntensity))

	 	##get max precip probability during a day(today)
	 	#compare precipProbability in the lists and get the tuple
	 	self.maxPrecipProb=max(self.precipProbability, key=itemgetter(1))
	 	self.currentPrecipProb=(self.currentTime,self.currentForecast.precipProbability)
	 	self.maxPrecipInt= max(self.precipIntensity, key=itemgetter(1))
	 	self.currentPrecipInt=(self.currentTime,self.currentForecast.precipProbability)

	def getWeeklyInfo(self):
		"""
		DocString
		"""
		##this function returns summary or icon of daily weather 
	 	for data in self.dailyForecast.data:
	 		local_time= self.convert_localTime(data.time)
	 		self.weeklySummary.append((local_time,str(data.summary)))


# if __name__ == '__main__':
weather = WeatherForecast(api_key = "18e78bb19491e1929765a1354c99d45a", lat=lat, lng=lng)

weather.getTemperatureData()
weather.getPrecipitationInfo()
weather.getWeeklyInfo()
weather.getWeatherForecast()
print weather.icon

