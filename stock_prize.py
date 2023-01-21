import requests
from bs4 import BeautifulSoup

def get_stock_price(stock_symbol):
  # Send an HTTP GET request to the Yahoo Finance API
  response = requests.get(f'https://finance.yahoo.com/quote/{stock_symbol}')

  # Parse the HTML of the response
  soup = BeautifulSoup(response.text, 'html.parser')
	price_element = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})
	if price_element:
  	price_element = price_element.find('span')
		else:
  # Handle the case where the element is not found
  raise Exception('Could not find stock price element')

  # Find the element containing the current stock price
  price_element = soup.find('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span')

  # Extract the current stock price
  price = float(price_element.text.replace(',', ''))

  return price

# Test the function
print(get_stock_price('AAPL')) # Outputs the current price of Apple stock
print(get_stock_price('GOOGL')) # Outputs the current price of Google stock
