class Converter():
    def __init__(self):
        self.__names = []
        self.__quantitiesMult = []

    def addQuantities(self, name, arrFromQuant):
        if len(self.__quantitiesMult) == 0:
            self.__quantitiesMult.append([1])
        else:
            arrFromQuant = self.__checkSimilarWay(arrFromQuant)
            if len(arrFromQuant) > len(self.__quantitiesMult):
                arrFromQuant[len(arrFromQuant) - 1] = 1
            else:
                arrFromQuant.append(1)
            self.__quantitiesMult.append(arrFromQuant)
            self.__appendNewWay(arrFromQuant)
        self.__names.append(name)

    def __checkSimilarWay(self, arrFromQuant):
        for i in range(len(arrFromQuant)):
            if arrFromQuant[i] == 0:
                for j in range(len(arrFromQuant)):
                    if arrFromQuant[j] != 0 and self.__quantitiesMult[i][j] != 0:
                        arrFromQuant[i] = arrFromQuant[j] / self.__quantitiesMult[i][j]
                        break
        return arrFromQuant

    def __appendNewWay(self, arrFromQuant):
        for i in range(len(self.__quantitiesMult) - 1):
            if len(arrFromQuant) > i and arrFromQuant[i] != 0:
                self.__quantitiesMult[i].append(1 / arrFromQuant[i])
            else:
                self.__quantitiesMult[i].append(0)

    def getNames(self):
        return self.__names

    def getQuantities(self):
        return self.__quantitiesMult

