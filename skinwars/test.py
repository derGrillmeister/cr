import pandas as pd

def skinwarsanfuegen(datei):
    datum = datei[9:19]
    df = pd.read_csv(datei)
    df["date"] = datum
    ausgabe = pd.DataFrame(df.groupby(["name","rarity","date"])["PrizePerSkin"].mean())
    ausgabe.to_csv("skinwars.csv", mode="a", decimal=",", header=False)

skinwarsanfuegen("skinwars-2022-12-03-03-06-20.csv")
skinwarsanfuegen("skinwars-2022-12-04-03-07-51.csv")

