import json
from urllib.request import urlopen

count = 0

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
da = json.loads(source)

with open("states.json") as fl:
    data_state = json.load(fl)

print(type(data_state))
print(type(data_state["states"]))

for st in data_state['states']:
    print(st['name'])
    del st['abbreviation']

new_state = json.dumps(data_state)
print(len(data_state['states']))

try:
    print(new_state['abbreviation'])
except:
    print('No abbreviation data exists')

with open('new_states.json', 'w') as f:
    json.dump(new_state, f)


usd_rates = dict()
for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))