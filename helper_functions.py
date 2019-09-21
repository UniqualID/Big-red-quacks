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
    if(resource1 == f && resouce2 == n):
        country1.cResources = country1.cResources - amount1
        country1.nukes = country1.nukes + amount2
        country2.nukes = country2.nukes - amount2
        country2.cResources = country2.cResources + amount1
    elif(resources1 == f && resource2 == t):
        country1.cResources = country1.cResources - amount1
        country1.treasury = country1.treasury + amount2
        country2.treasury = country2.treasury - amount2
        country2.cResources = country2.cResources + amount1
    elif(resources1 == n && resource2 == t):
        country1.nukes = country1.nukes - amount1
        country1.treasury = country1.treasury + amount2
        country2.treasury = country2.treasury - amount2
        country2.nukes = country2.nukes + amount1
        ########3 OPPOSITE FUNCTIONS ##########
    elif(resource1 == n && resouce2 == f):
        country2.cResources = country2.cResources - amount2
        country2.nukes = country2.nukes + amount1
        country1.nukes = country1.nukes - amount1
        country1.cResources = country1.cResources + amount2
    elif(resources1 == t && resource2 == f):
        country2.cResources = country2.cResources - amount1
        country2.treasury = country2.treasury + amount2
        country1.treasury = country1.treasury - amount2
        country1.cResources = country1.cResources + amount1
    elif(resources1 == t && resource2 == n):
        country2.nukes = country2.nukes - amount1
        country2.treasury = country2.treasury + amount2
        country1.treasury = country1.treasury - amount2
        country1.nukes = country1.nukes + amount1

def launchNuke(c1, target, nResearch):
    if (c1.nuke > 0):
        if (c1.nResearch >= x):
            alskdjf
        elif (c1.nResearch >= y):
            asldfkj;
