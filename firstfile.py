from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

# Lookup WOEID via http://weather.yahoo.com.

city=input()

lookup = weather.lookup(560743)
condition = lookup.condition
print(condition.text)

# Lookup via location name.

location = weather.lookup_by_location(city)
condition = location.condition
print(condition.text)

# Get weather forecasts for the upcoming days.

forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)
