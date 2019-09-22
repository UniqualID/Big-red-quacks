#### IMPORTS

class PlayerCountry:


    def __init__(self, name, population, cResources, gRate, GDP, gdpGrowth, nukeResearch, aaResearch,
      fProduction, treasury, nukes, faValues, cityDictionary):  #publicOp, education, arResarch

        self.name = name
        self.population = population
        self.startingPop = population
        self.cResources = cResources
        self.gRate = gRate
        self.GDP = GDP
        self.gdpGrowth = gdpGrowth
        self.nukeResearch = nukeResearch
        self.aaResearch = aaResearch
        #self.mProduction = mProduction
        self.fProduction = fProduction
        #self.arResarch = arResarch
        #self.publicOp = publicOp
        #self.education = education
        self.treasury = treasury
        self.nukes = nukes
        self.faValues = faValues
        self.cityDictionary = cityDictionary


    def update(self):  #publicOp

        oldPop = self.population
        oldGDP = self.GDP

        #Updates population
        self.population = ((self.cResources-self.population)*self.gRate) + self.population

        #Updates population in all cities
        for (k, v) in self.cityDictionary.items():
            v[0] = v[0] * (self.population/oldPop)

        #Updates GDP
        self.GDP = self.GDP + (self.population - startingPop)*self.gdpGrowth # ADD TRADE DEALS IN TURN

        #Refreshes Treasury
        self.treasury = self.treasury + self.GDP
