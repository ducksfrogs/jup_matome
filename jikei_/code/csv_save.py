import requests

url = 'https://www.mizuhobank.co.jp/market/csv/m_quote.csv'

try :
    r = requests.get(url)
    with open("momo.csv", mode='w') as f:
        f.write(r.text)
except requests.exceptions.RequestException as err:
    print(err)
