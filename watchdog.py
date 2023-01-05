import pandas as pd
import requests
import time
import datetime

watchdog = ['ufo', 'moon','bomb','football']

def marketplaceanfuegen(df):
    datum = time.strftime('%Y-%m-%d %H:%M:%S')
    df['date'] = datum
    df['on_sale_price'] = pd.to_numeric(df['on_sale_price'],errors = 'coerce')
    ausgabe = df.loc[df.groupby('name')['on_sale_price'].idxmin()]
    ausgabe[['rarity','name','date','on_sale_price']].to_csv('watchdog/marketplace.csv', mode='a', decimal=',', header=False, index=False)

filenameMarketplace = 'marketplace-' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.csv'

marketplace = requests.get('https://api.cryptoroyale.one/api/marketplace').json()

df = pd.DataFrame(marketplace['on_sale'])

df = df[df['filename'].isin(watchdog)]

df.to_csv('watchdog/' + filenameMarketplace, encoding='utf-8', index=False)
marketplaceanfuegen(df)
