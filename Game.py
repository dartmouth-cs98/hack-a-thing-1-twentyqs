import pandas as pd
import random as rd
from DataScraper import DataScraper
from Information import Information

class Game:
    def __init__(self):
        customInfo = Information()
        self.positionMap = {'GoalKeeper': [0],
                           'Defender': [1, 2, 3],
                           'Midfielder': [4, 5, 6, 7, 8],
                           'Forward': [9, 10, 11, 12]}
        self.choiceDict = {0: customInfo.posDict, 
                           1: customInfo.basicList, 
                           2: customInfo.abilityList,
                          3: customInfo.posDetailedDict}
        self.knownPositives = {0: [], 1: [], 2: []}
        self.knownNegatives = {1: [], 2: []}
        self.dataScraper = DataScraper(self.positionMap)
    
    def execute_program(self):   
        counter = 0
        found = False
        playerTable = None
        crudePosFound = False
        while not found:
            counter += 1
            print(counter)
            dictChoice = -1
            valid = False
            while not valid:
                dictChoice = rd.randint(0, 2)
                if dictChoice == 0 and len(self.choiceDict[0]) == 1:
                    valid = False
                elif dictChoice == 1 and len(self.choiceDict[1]) == 1:
                    valid = False
                elif dictChoice == 2 and len(self.choiceDict[2]) == 1:
                    valid = False
                elif dictChoice not in [0, 1, 2]:
                    valid = False
                else:
                    valid = True   
                    
            keyword = rd.choice(self.choiceDict[dictChoice])
            self.choiceDict[dictChoice].remove(keyword)
            
            ###################
            # Jerry's Module
            ###################
            answer = rd.choice([True, False])
            print(keyword)
            print(answer)
            if answer:
                if dictChoice == 0: 
                    if crudePosFound:
                        self.knownPositives[0].append(keyword)
                        self.choiceDict[0] = [keyword]
                    else:
                        self.knownPositives[0] = self.positionMap[keyword]
                        self.choiceDict[0] = self.positionMap[keyword]
                        crudePosFound = True
                        
                else:
                    self.knownPositives[dictChoice].append(keyword)
                
            else:
                if dictChoice == 1 or dictChoice == 2:
                    self.knownNegatives[dictChoice].append(keyword)
            
            print(self.knownPositives)
            print(self.knownNegatives)
            playerTable = self.dataScraper.scrape(self.knownPositives, self.knownNegatives)
            if playerTable.shape[0] < 6:
                found = True
                print(playerTable)
            if playerTable.shape[0] == 0:
                print('Check your standards')