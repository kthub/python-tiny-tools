import requests
import json

def get_price(code):
  url = 'https://finance.yahoo.co.jp/quote/' + code
  row_response = requests.get(url).text

  # extract JSON
  start_str = 'window.__PRELOADED_STATE__ ='
  end_str = '</script>'

  start = row_response.find(start_str)
  if start != -1:
    start += len(start_str)
  else:
    print('PARSE FAILED : start string [' + start_str + '] not found')

  end = row_response.find(end_str, start)
  if (end != -1):
    json_response = row_response[start:end]
  else:
    print('PARSE FAILED : end string [' + end_str + '] not found')

  # parse JSON
  data = json.loads(json_response)
  price = data['mainFundPriceBoard']['fundPrices']['price']

  return int(price.replace(",",""))