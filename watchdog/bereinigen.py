import pandas as pd
import os
import time
import datetime

files = os.listdir()



watchdog = ['ufo', 'moon','bomb','football','cherry','pizza']

def marketplaceanfuegen(file):
    df = pd.read_csv(file)
    datum = file[12:22] + " " + file[23:25] + ":" + file[26:28] + ":" + file[29:31]
    df['date'] = datum
    df['on_sale_price'].astype('float')
    ausgabe = pd.DataFrame(df.sort_values(['on_sale_price'], ascending=True).groupby('name', as_index=False).first())
    ausgabe[['rarity','name','date','on_sale_price']].to_csv('marketplace.csv', mode='a', decimal=',', header=False, index=False)

for f in files:
    marketplaceanfuegen(f)
#    print(f[12:22] + " " + f[23:25] + ":" + f[26:28] + ":" + f[29:31])
