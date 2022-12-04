import pandas as pd
import requests
import time
import datetime

def skinwarsanfuegen(df):
    datum = time.strftime('%Y-%m-%d')
    df["date"] = datum
    ausgabe = pd.DataFrame(df.groupby(["name","rarity","date"])["PrizePerSkin"].mean())
    ausgabe.to_csv("skinwars/skinwars.csv", mode="a", decimal=",", header=False)

filenameMarketplace = 'marketplace-' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.csv'

filenameSkinWars = 'skinwars-' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.csv'


marketplace = requests.get('https://api.cryptoroyale.one/api/marketplace').json()

df = pd.DataFrame(marketplace['on_sale'])
df.to_csv('marketplace/' + filenameMarketplace, encoding='utf-8', index=False)

skinWarsDate = datetime.datetime.today() - datetime.timedelta(days=1)

parametersSkinWars = {
    'date' : skinWarsDate.strftime('%m-%d-%Y')
}

skinwars = requests.get('https://api.cryptoroyale.one/api/skinwars', params=parametersSkinWars).json()

df = pd.DataFrame(skinwars['clans']).transpose()
df.to_csv('skinwars/' + filenameSkinWars, encoding='utf-8', index=False)
skinwarsanfuegen(df)
