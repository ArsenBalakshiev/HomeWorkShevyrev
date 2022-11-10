from City import City

def readData(count = 50):
    cities = []
    with open("cities50.txt", "r")  as f:
        for line in f.readlines():
            cityData = line.split(' ')
            cities.append(City(cityData[1], cityData[2], cityData[0]))
    return cities

print(readData())