import zoopla
import pandas as pd

api = zoopla.api(version=1, api_key='gh2q9a6bkwk6req537gngfe5')

CSV_FILE = 'test.csv'

def read_postcodes(CSV_FILE):
	df = pd.read_csv(CSV_FILE)
	return df

def write_to_file():
        pass

data = read_postcodes(CSV_FILE)

house_price_list = []	
for pc in data['postcode']:
	print pc	
	out = api.average_sold_prices(postcode=pc, output_type='outcode', area_type='postcodes')
	average_sold_price_list = []
	for item in out['areas']:
		# building in some redundancy by having the 3 year price as well
		item_price_1year = int(item['average_sold_price_1year'])
		item_price_3year = int(item['average_sold_price_3year'])
		if item_price_1year != 0:
			average_sold_price_list.append(item_price_1year)
		if item_price_3year != 0:
			average_sold_price_list.append(item_price_3year)

	if len(average_sold_price_list) == 0:
		raise ValueError("No house prices found for postcode: " + pc)

	house_price_list.append(sum(average_sold_price_list)/float(len(average_sold_price_list)))

data['house_price'] = pd.Series(house_price_list)
print data		
