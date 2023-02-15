import re
import sys
from urllib.request import urlopen


def fetch_USD_quote(value: float):
    url = "https://www.google.com/finance/quote/USD-BRL"
    content = urlopen(url).read()
    search = re.search('class="YMlKec fxKbKc">(.*?)<', content.decode('utf-8'))
    if not search or not search.group(1):
        raise Exception('Not possible to get USD Quote, try again later')

    usd_value = float(search.group(1))
    brl_currency = value * usd_value
    return brl_currency 

if __name__ == '__main__':
    try:
        input_val = sys.argv[1]
    except:
        input_val = '1.0'
    
    value_number = float(re.sub("[^0-9.]", "", re.sub( ",", ".", input_val)))
    result = fetch_USD_quote(value_number)
    print('\nOutput: {:.2f}'.format(result))
