# Example file for Advanced Python: Hands On by Joe Marini
# Count items using a default dictionary

import json
import pprint
from collections import defaultdict

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# The defaultdict collection provides a cleaner way of initializing key values
# TODO: Count th number of data points for each year we have data


# TODO: defaultdict can use more complex objects, like lists
years = defaultdict(int)
for d in weatherdata:
    key = d['date'][0:4]
    years[key] += 1
pprint.pp(years)

# TODO: create a dictionary with year-month keys and lists for each day in the month
years_month = defaultdict(list)

for d in weatherdata: 
    key = d['date'][0:7]
    years_month[key].append(d)
# pprint.pp(years_month)

# What were the coldest and warmest days of each month?
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])

# TODO: loop over the keys of the dictionary and find each warmest and coldest day
for years_month, day_list in years_month.items():
    print(f"warmest day in {years_month}: {warmest_day(day_list)}")
    print(f"coldest day in {years_month}: {coldest_day(day_list)}")