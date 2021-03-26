STOCKS = []

def getAllStocks():
    file = open("data/all_symbols.txt", "r")

    for line in file:
        line = line[:-1]
        STOCKS.append(line)

def chooseStock():
    stock = input("Choose a stock: \n")
    print("You choosed " + stock);

def main():
    getAllStocks()
    chooseStock()

if __name__ == "__main__":
    main()
