import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

STOCKS = []
STOCK = ""

def getAllStocks():
    file = open("data/all_symbols.txt", "r")

    for line in file:
        line = line[:-1]
        STOCKS.append(line)



def getStock():
    df = pd.read_csv("data/full_history/" + STOCK + ".csv")
    df = df.drop(columns=["volume", "high", "low", "adjclose"])
    df = df.reindex(index=df.index[::-1])
    df['date'] = pd.to_datetime(df['date'])
    #print(df.to_string())

    return df



def findCloseStockName(wantedStock):
    similarStocks = []
    for stock in STOCKS:
        if (stock[:len(wantedStock)] == wantedStock):
            similarStocks.append(stock)

    return similarStocks



def chooseStock():
    global STOCK
    stock = input("Choose a stock: \n").upper();
    if stock in STOCKS:
        print("You choosed " + stock);
        STOCK = stock
        return stock
    else:
        print("Did you mean: " + str(findCloseStockName(stock)))
        return chooseStock()



def plotStock(df):
    plt.figure(figsize=(10,10))
    plt.plot(df["date"], df['close'])
    #plt.plot(df['close'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title(STOCK + " Stock Price")
    plt.show()


def main():
    getAllStocks()
    chooseStock()
    plotStock(getStock())

if __name__ == "__main__":
    main()
