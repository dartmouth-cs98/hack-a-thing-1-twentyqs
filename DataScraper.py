#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from Information import Information


# In[2]:


class DataScraper:
    def __init__(self, positionMap):
        self.base_url = 'http://pesdb.net/pes2019/?feature=0'
        self.positionMap = positionMap
        self.customInfo = Information()
    
    def scrape(self, positives, negatives):
        featureURL = self.formFeatureURL(positives, negatives)
        print(self.base_url + featureURL)
        response = requests.get(self.base_url + featureURL)
        html = response.content
        table = pd.read_html(html)
        return table[0]
    
    def formFeatureURL(self, positives, negatives):
        res = ''
        if positives[0]:
            res += '&pos='
            isFirst = True
            for pos in positives[0]:
                if isFirst:
                    res += str(pos)
                    isFirst = False
                else:
                    res += ',' + str(pos)
        
        if positives[1]:
            if 'Tall' in positives[1]:
                res += '&height=185-227'
            if 'Over 30' in positives[1]:
                res += '&age=31-78'
        
        if positives[2]:
            for ability in positives[2]:
                res += '&' + ability + '=80-99'
        
        if negatives[1]:
            if 'Tall' in negatives[1]:
                res += '&height=100-185'
            if 'Over 30' in negatives[1]:
                res += '&age=15-30'
        
        if negatives[2]:
            for ability in negatives[2]:
                res += '&' + ability + '=40-79'
        return res