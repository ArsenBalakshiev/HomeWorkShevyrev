from City import City

def readData(count = 50):
    cities = []
    with open("../dataset/cities50.txt", "r")  as f:
        file = f.readlines()
        for i in range(count):
            line = file[i]
            cityData = line.split(' ')
            cities.append(City(float(cityData[1]), float(cityData[2]), cityData[0]))
    return cities