import requests
import os
from datetime import datetime


DOWNLOAD_SAVE_DIR = os.getenv("DOWNLOAD_SAVE_DIR")


def main():
    url = 'https://www.mizuhobank.co.jp/market/csv/m_quote.csv'
    response = requests.get(url)

    contentType = response.headers['Content-Type']
    contentDispositon = response.headers['Content-Disposition']
    ATTRIBUTE = 'filename='
    filename = contentDispositon[contentDispositon.find(ATTRIBUTE) + len(ATTRIBUTE):]



if __name__ == "__main__":
    main()
