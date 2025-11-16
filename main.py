from logic.converter import Converter

if __name__ == "__main__":
    c = Converter("./examples/record.xlsx", "./assets/coordinates.csv")
    print(c.reader.map)
    # c.test()
    print(c.get_from_to())
    c.loader.close()
    exit(0)
