distances = {1:[0,10,15,20] , 2:[10,0,35,25], 3:[15,35,0,30], 4:[20,25,30,0]}
bestAnswer = 100
bestPath = ""
cities = []

def calcDistance(i , j):
    return distances[i][j - 1]

for i in range(0,3):
    cities = [2 , 3 , 4]
    city1 = cities[i]
    distance = calcDistance(1 , city1)
    if(distance >= bestAnswer):
        continue
    else:
        cities_2 = cities.copy()
        cities_2.remove(city1)
        for j in range(0,2):
            city2 = cities_2[j]
            distance = calcDistance(1 , city1) + calcDistance(city1 , city2)
            if(distance >= bestAnswer):
                continue
            else:
                cities_3 = cities_2.copy()
                cities_3.remove(city2)
                city3 = cities_3[0]
                finalDistance = calcDistance(1 , city1) + calcDistance(city1 , city2) + calcDistance(city2 , city3) + calcDistance(city3 , 1)
                if(finalDistance <= bestAnswer):
                    bestAnswer = finalDistance
                    bestPath = "1 -> " + str(city1) + "-> " + str(city2) + "-> " + str(city3) + "-> " + "1"

print(bestAnswer)
print(bestPath)