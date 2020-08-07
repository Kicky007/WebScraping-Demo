import datetime

# Ziua cu care lucrez.
day = 1973
zile = {
    "1983": str(datetime.datetime(2020, 6, 14)),
    "1982": str(datetime.datetime(2020, 6, 13)),
    "1981": str(datetime.datetime(2020, 6, 12)),
    "1980": str(datetime.datetime(2020, 6, 11)),
    "1979": str(datetime.datetime(2020, 6, 10)),
    "1978": str(datetime.datetime(2020, 6, 9)),
    "1977": str(datetime.datetime(2020, 6, 8)),
    "1976": str(datetime.datetime(2020, 6, 7)),
    "1975": str(datetime.datetime(2020, 6, 6)),
    "1974": str(datetime.datetime(2020, 6, 5)),
    "1973": str(datetime.datetime(2020, 6, 4)),
    "1972": str(datetime.datetime(2020, 6, 3)),
    "1971": str(datetime.datetime(2020, 6, 2)),
    "1970": str(datetime.datetime(2020, 6, 1)),
    "1969": str(datetime.datetime(2020, 5, 31)),
    "1968": str(datetime.datetime(2020, 5, 30)),
    "1967": str(datetime.datetime(2020, 5, 29)),
    "1966": str(datetime.datetime(2020, 5, 28)),
    "1965": str(datetime.datetime(2020, 5, 27)),
    "1964": str(datetime.datetime(2020, 5, 26)),
    "1963": str(datetime.datetime(2020, 5, 25)),
    "1962": str(datetime.datetime(2020, 5, 24)),
    "1961": str(datetime.datetime(2020, 5, 23)),
    "1960": str(datetime.datetime(2020, 5, 22)),
    "1959": str(datetime.datetime(2020, 5, 21)),
    "1958": str(datetime.datetime(2020, 5, 20)),
    "1957": str(datetime.datetime(2020, 5, 19)),
    "1956": str(datetime.datetime(2020, 5, 18)),
    "1955": str(datetime.datetime(2020, 5, 17)),
    "1954": str(datetime.datetime(2020, 5, 16)),
    "1953": str(datetime.datetime(2020, 5, 15)),
    "1952": str(datetime.datetime(2020, 5, 14)),
    "1951": str(datetime.datetime(2020, 5, 13)),
    "1950": str(datetime.datetime(2020, 5, 12)),
    "1949": str(datetime.datetime(2020, 5, 11)),
    "1948": str(datetime.datetime(2020, 5, 10)),
    "1947": str(datetime.datetime(2020, 5, 9)),
    "1946": str(datetime.datetime(2020, 5, 8)),
    "1945": str(datetime.datetime(2020, 5, 7)),
}


def days(day):
    # Cast din int in string
    daystr = str(day)
    # Deschiderea fisierului cu care lucrez in continuare.
    f = open('CSGOEMPIRE_'+daystr+'.txt', 'r')
    zero = 0
    rosu = 0
    negru = 0
    jackpot = 0
    for x in f:
        new = x.split(" - ")
        number = int(new[1])
        if (number >= 1 and number <= 7):
            # print("Rosu")
            rosu += 1
            pass
        elif (number <= 14 and number >= 8):
            # print("Negru")
            negru += 1
            pass
        elif (number == 0):
            # pass
            zero += 1
        else:
            # print("Jackpot")
            pass
            jackpot += 1
    print("Ziua: " + zile[daystr])
    print("Rosu: " + str(rosu))
    print("Negru: " + str(negru))
    print("Zero: " + str(zero))
    print("Jackpot: " + str(jackpot))
    print("Total: " + str(rosu+negru+zero+jackpot)+"\n")
    f.close()


def main():
    start = 1975
    stop = 1977
    for i in range(start, stop):
        days(i)


if __name__ == "__main__":
    main()
