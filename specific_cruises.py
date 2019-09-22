#program will check on prices of cruises out of a given zip code to find deals and discounts
# a goal of this code is to log cruise prices and send an alert when these prices drop as well as maybe
#predict the next price drop accordingly

#This is mostly to learn how to use git as well as learn some new technologies like...
  #web scraping
  #data management
  #sending alerts in python
    
#Celebrity Cruises URL
	#https://www.celebritycruises.com/itinerary-search?departures=FLL,MIA,TPA
#Royal Caribbean 
	#https://www.royalcaribbean.com/cruises/?country=USA&departureCode_MIA=true&departureCode_PCN=true&departureCode_TPA=true&sort-by=PRICE_LOW_TO_HIGH
#Norwegian Cruise Line
	#https://www.ncl.com/vacations/miami-florida-orlando-&-beaches-(port-canaveral)-tampa-florida-2-guests-?embarkationport=4294953464%204294953399%204294953412&cruise=1&cruiseTour=1&cruiseHotel=1&cruiseHotelAir=1&numberOfGuests=4294953449&state=undefined&pageSize=20&currentPage=1&sortBy=Price&autoPopulate=f&from=resultPage
#Carnival Cruise Line
	#https://www.carnival.com/?gclsrc=aw.ds&gclid=CjwKCAjw8NfrBRA7EiwAfiVJpXvjc1Z0YPAV3TiJUhFHeGJQ44AJqjpTMSarExdz9FDB7NPI8S3WqRoCP6cQAvD_BwE&gclsrc=aw.ds#?layout=grid&numAdults=2&pageNumber=2&pageSize=8&port=chs,fll,jax,mia,mob,pcv,tpa&showBest=true&sort=fromprice&useSuggestions=true
#Princess Cruises
	#https://www.princess.com/cruise-search/results
#Holland
	#https://www.hollandamerica.com/en_US/find-a-cruise.html#%7B!tag=destinationTag%7DdestinationIds=&%7B!tag=departTag%7DdepartDate=&%7B!tag=durationTag%7Dduration=&%7B!tag=embarkTag%7DembarkPortCode=FLL&%7B!tag=regionTag%7Dregions=&%7B!tag=cruisetypeTag%7DcruiseType=&%7B!tag=shipsTag%7DshipId=&%7B!tag=portsTag%7DportsOfCall=&soldOut=false&sort=price_USD_anonymous%20asc,departDate%20asc&group.sort=price_USD_anonymous%20asc,departDate%20asc&start=0
#MSC Cruises
	#https://www.msccruisesusa.com/webapp/wcs/stores/servlet/MSC_SearchCruiseManagerRedirectCmd?storeId=12264&langId=-1004&catalogId=10001&monthsResult=&areaFilter=&embarkFilter=MIA%40&lengthFilter=&departureFrom=03.01.2020&departureTo=05.31.2020&ships=&category=&onlyAvailableCruises=true&packageTrf=false&packageTpt=false&packageCrol=false&packageCrfl=false&noAdults=2&noChildren=0&noJChildren=0&noInfant=0&dealsInput=false&tripSpecificationPanel=true&shipPreferencesPanel=false&dealsPanel=false
#	
#
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
from re import sub
from decimal import Decimal
import tools
def check_methods(idk):
	object_methods = [method_name for method_name in dir(idk)
	                  if callable(getattr(idk, method_name))] 
	print(object_methods)	                  

good_cruises = {}
x=0
url = "https://www.ncl.com/cruises/7-day-western-caribbean-from-new-orleans-GETAWAY7MSYCZMRTBBPICMAMSY/Dates/March-2020-to-April-2020?cruiseTour=1&embarkationport=4294953361&destinations=4294961647&cruiseHotel=1&numberOfGuests=4294953449&pageSize=20&cruise=1&sortBy=Featured&state=undefined&sailmonths=4294941882%204294941891%204294941876%204294941875&currentPage=1&cruiseHotelAir=1&itineraryCode=GETAWAY7MSYCZMRTBBPICMAMSY"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
name = soup.h4.text
#gather the price of a given cruise on page
#Get prices of specific cruises and call them by their id on the cruise site.
#this makes price_html the resulting bs4 class value
price_html = soup.find_all(id="teaLeaf-value-text757")
#That returns  a long string of htlml, turn that into a list.
#then split that list at the Greater than sign.
price_html_as_list = ((str(price_html).split('>')))
#the price falls into the 2nd from last spot in the list so i set it as price_short
#it is then saved as a sting as price_short
price_short = (price_html_as_list[-2])
#split up price_short at the less than sign
#then take the first part of it containing the price
#this outputs the price as a list with the $ at the beginning
price_full = (price_short).split('<')[0]
value = Decimal(sub(r'[^\d.]', '', price_full))

print(value)

tools.check(value)

###   Whats the current thought process?   ###
"""



"""



'''for i in range(0, len(soup.findAll('h4'))):
	check = str(soup.findAll('h4')[i])
	this = check.split()
	if this[7] != "Bahamas":
		x=x+1
		good_cruises.update({x: this[7:-2]})
for x,y in good_cruises.items():
	print("Cruise number " + str(x) + " is going to " + str(' '.join(y)) + " cruise.")
'''

