
# Determine how to parse the doc
# How are the elements labeled within the HTML? 
# Once determined, write functions to go and retrieve each data point 
# Write out to CSV (will surely have to do more clean up here) 


'''

Table is initiated with the <table class="table0 "> tags
Table contents are within the <tbody> and </tbody> tags 
Meal-parts are within <tr class="meal_header">
Item entries are within <td class="first alt"> 




'''


from bs4 import BeautifulSoup 
import urllib.request 

# the URL we want to scrape 
my_url = 'http://www.myfitnesspal.com/food/diary/camflawless?date=2016-10-24'
s = urllib.request.urlopen(my_url)

soup = BeautifulSoup(s,'html.parser')

tables = soup.findAll("table")

entries = soup.findAll('td', {'class' : 'first alt'})
meals = soup.findAll('tr', {'class' : 'meal_header'})

print(meals)
		

