import PlayerCountry

def treasryChange(country, nChange):
    country.treasury = country.treasury + nChange

def cResourceChange(country, nChange):
    country.cResources = coutry.cResources + nChange

def changeGDP(country, nChange):
    country.GDP = country.GDP + nChange

def changeNukeResearch(country, nChange):
    country.nukeResearch = country.nukeResearch + nChange

def changeAAResearch(country, nChange):
    country.aaResearch = country.aaResearch + nChange

def changeMProduction(country, nChange):
    country.mProduction = country.mProduction + nChange

def changeFProduction(country, nChange):
    country.fProduction = country.fProduction  + nChange

def changeARResearch(country, nChange):
    country.ARResearch = country.ARResearch + nChange

def changeEducation(country, nChange):
    country.education = country.education + nChange

def changeFaValues(country, nChange):
    country.faValues = country.faValues + nChange

def fTrage(country1, country2, resource1, amount1, resource2, amount2): #f = food, t = treasury, n = nukes
    if(resource1 == f and resouce2 == n):
        country1.cResources = country1.cResources - amount1
        country1.nukes = country1.nukes + amount2
        country2.nukes = country2.nukes - amount2
        country2.cResources = country2.cResources + amount1
    elif(resources1 == f and resource2 == t):
        country1.cResources = country1.cResources - amount1
        country1.treasury = country1.treasury + amount2
        country2.treasury = country2.treasury - amount2
        country2.cResources = country2.cResources + amount1
    elif(resources1 == n and resource2 == t):
        country1.nukes = country1.nukes - amount1
        country1.treasury = country1.treasury + amount2
        country2.treasury = country2.treasury - amount2
        country2.nukes = country2.nukes + amount1
        ########3 OPPOSITE FUNCTIONS ##########
    elif(resource1 == n and resouce2 == f):
        country2.cResources = country2.cResources - amount2
        country2.nukes = country2.nukes + amount1
        country1.nukes = country1.nukes - amount1
        country1.cResources = country1.cResources + amount2
    elif(resources1 == t and resource2 == f):
        country2.cResources = country2.cResources - amount1
        country2.treasury = country2.treasury + amount2
        country1.treasury = country1.treasury - amount2
        country1.cResources = country1.cResources + amount1
    elif(resources1 == t and resource2 == n):
        country2.nukes = country2.nukes - amount1
        country2.treasury = country2.treasury + amount2
        country1.treasury = country1.treasury - amount2
        country1.nukes = country1.nukes + amount1

def launchNuke(c1, c2, target): # c1 is your own country, c2 is the opposing country, target is the specific city
<<<<<<< HEAD
    if (c1):
=======
    if (c1.faValues.get(c2.name) == 0):
>>>>>>> 07e6cac5c0785460a6cbf78ffea6f881226dddcc
        if (c1.nuke > 0):
            c1.nuke = c1.nuke - 1
            if (c2.cityDictionary.get(target)[1] != 0):
                c2.cityDictionary.get(target)[1] = c2.cityDictionary.get(target)[1] - 1
                if (c1.nukeResearch > c2.aaResearch):
                    diff = c1.nukeResearch - c2.aaResearch
                    initPop = c2.cityDictionary.get(target)[0]
                    if(diff > 14):
                        c2.cityDictionary.get(target)[0] = 0;
                        c2.population -= initPop
                    elif(diff == 14):
                        c2.cityDictionary.get(target)[0] = initPop*.01;
                        c2.population -= initPop*.99
                    elif(diff == 13):
                        c2.cityDictionary.get(target)[0] = initPop*.02;
                        c2.population -= initPop*.98
                    elif(diff == 12):
                        c2.cityDictionary.get(target)[0] = initPop*.03;
                        c2.population -= initPop*.97
                    elif(diff == 11):
                        c2.cityDictionary.get(target)[0] = initPop*.04;
                        c2.population -= initPop*.96
                    elif(diff == 10):
                        c2.cityDictionary.get(target)[0] = initPop*.05;
                        c2.population -= initPop*.95
                    elif(diff == 9):
                        c2.cityDictionary.get(target)[0] = initPop*.15;
                        c2.population -= initPop*.85
                    elif(diff == 8):
                        c2.cityDictionary.get(target)[0] = initPop*.25;
                        c2.population -= initPop*.75
                    elif(diff == 7):
                        c2.cityDictionary.get(target)[0] = initPop*.35;
                        c2.population -= initPop*.65
                    elif(diff == 6):
                        c2.cityDictionary.get(target)[0] = initPop*.45;
                        c2.population -= initPop*.55
                    elif(diff == 5):
                        c2.cityDictionary.get(target)[0] = initPop*.6;
                        c2.population -= initPop*.4
                    elif(diff == 4):
                        c2.cityDictionary.get(target)[0] = initPop*.7;
                        c2.population -= initPop*.3
                    elif(diff == 3):
                        c2.cityDictionary.get(target)[0] = initPop*.8;
                        c2.population -= initPop*.2
                    elif(diff == 2):
                        c2.cityDictionary.get(target)[0] = initPop*.9;
                        c2.population -= initPop*.1
                    elif(diff == 1):
                        c2.cityDictionary.get(target)[0] = initPop*.95;
                        c2.population -= initPop*.05
    else:
        return False


def researchPurchase(country, researchType):
    if(researchType == "Anti-Air"):
        stock = 0
        for (k, v) in country.cityDictionary.items():
            stock += v[1]
        cost = country.aaResearch * 25000 * (1.025**stock)
        if(treasury > cost):
            country.treasury = country.treasury - cost
            country.aaResearch += 1
    elif(researchType == "Nuclear"):
        costs = country.nukeResearch * 25000 * (1.025**country.nukes)
        if(treasury > cost):
            country.treasury = country.treasury - cost
            country.nukeResearch += 1
    elif(researchType == "Food Production"):
        costs = country.fProduction * 12500
        if(treasury > cost):
            country.treasury -= costs
            country.fProduction += 1


def makeNuke(c1):
    if (c1.treasury >= 3000000):
        c1.treasury -= 3000000
        c1.nukes += 1

def makeAntiAir(c1, city):
    if (c1.treasury >= 1500000):
        c1.treasury -= 1500000
        c1.cityDictionary.get(city)[1] + 1
