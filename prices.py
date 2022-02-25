import requests

#API key
headers = {
    'X-CMC_PRO_API_KEY' : '90130b7e-8a50-4e47-8da5-ba1d5c056101', 'Accepts' : 'application/json'
}

#specify the coins needed from the API
parameters = {
    'start' : '1', 'limit' : '200', 'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#make a request
response = requests.get(url, params=parameters, headers=headers).json()

coins = response['data']

#iterate through all the data and print the specified ones
for coin in coins:
    print("Rank:" + str(coin['cmc_rank']), str(coin['name']) + "(" + str(coin['symbol']) + ")", "Price:" + "$" + str("{:.2f}".format(coin['quote']['USD']['price'])), "MarketCap= " + "$" + str("{:.2f}".format(coin['quote']['USD']['market_cap'])), "Circulating Supply = " + str(int(coin['circulating_supply'])) + " " + str(coin['symbol']))
