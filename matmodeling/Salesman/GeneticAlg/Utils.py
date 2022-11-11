from City import City

def readData(count = 50):
    cities = []
    with open("../dataset/cities50.txt", "r")  as f:
        for line in f.readlines():
            cityData = line.split(' ')
            cities.append(City(float(cityData[1]), float(cityData[2]), cityData[0]))
    return cities