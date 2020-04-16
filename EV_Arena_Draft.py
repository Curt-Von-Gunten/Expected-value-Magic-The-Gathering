# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:44:57 2020

@author: Curt
"""
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline

### Combination function ###
def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))


# =============================================================================
# Premier draft
# =============================================================================    
### Calculating the number of wins by win % probability table ###
winPerc = list(np.array(range(5,96,5))/100)
winNumb = list(range(0,8,1))

percProbs = []
for perc in winPerc:
    winNumbProb = []
    for wins in winNumb:
        if wins < 7:
            prob = (perc**wins)*(1-perc)**2*(nCr(wins+2,2))*(1-perc)
            winNumbProb.append(prob)
        else:
            prob = (perc**wins) + ((perc**(wins-1))*((1-perc)**1)*(nCr((wins-1)+1,1))*perc) + ((perc**(wins-1))*((1-perc)**2)*(nCr((wins-1)+2,2))*perc)  
            winNumbProb.append(prob)
    percProbs.append(winNumbProb)

varNames = []
for i in range(8):
    name = str(i) + '_wins'
    varNames.append(name)

df = pd.DataFrame(percProbs, columns=varNames)
df['perc'] = np.array(winPerc) * 100

gemTot = [50, 100, 250, 1000, 1400, 1600, 1800, 2200]
gemNet = np.array(gemTot) - 1500
gemPacks = [200, 200, 400, 400, 600, 800, 1000, 1200]
totNet = np.array(gemPacks) + gemNet

### Multiplying the probability and the value of each win number ###
### Gems only ###
dfPremUtils = pd.DataFrame()
for wins, gems in zip(varNames, gemNet):
    temp = df[wins] * gems
    temp.rename(wins + '_gems', inplace=True)
    dfPremUtils = pd.concat([dfPremUtils, temp], axis=1)
### Total ###
for wins, gems in zip(varNames, totNet):
    temp = df[wins] * gems
    temp.rename(wins + '_tot', inplace=True)
    dfPremUtils = pd.concat([dfPremUtils, temp], axis=1)

### Summing the utilities from each win number ###    
dfPremUtils['GemNet'] = dfPremUtils['0_wins_gems'] + dfPremUtils['1_wins_gems'] + dfPremUtils['2_wins_gems'] + dfPremUtils['3_wins_gems'] + dfPremUtils['4_wins_gems'] + dfPremUtils['5_wins_gems'] + dfPremUtils['6_wins_gems'] + dfPremUtils['7_wins_gems']
dfPremUtils['TotalNet'] = dfPremUtils['0_wins_tot'] + dfPremUtils['1_wins_tot'] + dfPremUtils['2_wins_tot'] + dfPremUtils['3_wins_tot'] + dfPremUtils['4_wins_tot'] + dfPremUtils['5_wins_tot'] + dfPremUtils['6_wins_tot'] + dfPremUtils['7_wins_tot']
dfPremUtils['perc']  = df['perc'] 


# =============================================================================
# Traditional Draft
# =============================================================================   
### Calculating the number of wins by win % probability table ###
winPerc = list(np.array(range(5,96,5))/100)
winNumb = list(range(0,4,1))

### Modifying win %s for games ###
matchPerc = []
for game in winPerc:
    match = (game**2) + (2 * (game**2) * (1-game))
    matchPerc.append(match)

### Calculating the number of wins by win % probability table ###
percProbs = []
for perc in matchPerc:
    winNumbProb = []
    for wins in winNumb:
        losses = 3 - wins
        prob = (perc**wins)*(1-perc)**losses*(nCr(3,wins))
        winNumbProb.append(prob)
    percProbs.append(winNumbProb)

varNames = []
for i in range(4):
    name = str(i) + '_wins'
    varNames.append(name)
    
dfTrad = pd.DataFrame(percProbs, columns=varNames)
dfTrad['perc'] = np.array(matchPerc) * 100

gemTot = [0, 0, 1000, 3000]
gemNet = np.array(gemTot) - 1500
gemPacks = [200, 200, 800, 1200]
totNet = np.array(gemPacks) + gemNet

### Multiplying the probability and the value of each win number ###
### Gems only ###
dfTradUtils = pd.DataFrame()
for wins, gems in zip(varNames, gemNet):
    temp = dfTrad[wins] * gems
    temp.rename(wins + '_gems', inplace=True)
    dfTradUtils = pd.concat([dfTradUtils, temp], axis=1)
### Total ###
for wins, gems in zip(varNames, totNet):
    temp = dfTrad[wins] * gems
    temp.rename(wins + '_tot', inplace=True)
    dfTradUtils = pd.concat([dfTradUtils, temp], axis=1)

### Summing the utilities from each win number ###
dfTradUtils['GemNet'] = dfTradUtils['0_wins_gems'] + dfTradUtils['1_wins_gems'] + dfTradUtils['2_wins_gems'] + dfTradUtils['3_wins_gems']
dfTradUtils['TotalNet'] = dfTradUtils['0_wins_tot'] + dfTradUtils['1_wins_tot'] + dfTradUtils['2_wins_tot'] + dfTradUtils['3_wins_tot']
dfTradUtils['perc']  = dfTrad['perc'] 


# =============================================================================
# Ranked draft
# =============================================================================
### Calculating the number of wins by win % probability table ###
winPerc = list(np.array(range(5,96,5))/100)
winNumb = list(range(0,8,1))

percProbs = []
for perc in winPerc:
    winNumbProb = []
    for wins in winNumb:
        if wins < 7:
            prob = (perc**wins)*(1-perc)**2*(nCr(wins+2,2))*(1-perc)
            winNumbProb.append(prob)
        else:
            prob = (perc**wins) + ((perc**(wins-1))*((1-perc)**1)*(nCr((wins-1)+1,1))*perc) + ((perc**(wins-1))*((1-perc)**2)*(nCr((wins-1)+2,2))*perc)  
            winNumbProb.append(prob)
    percProbs.append(winNumbProb)

varNames = []
for i in range(8):
    name = str(i) + '_wins'
    varNames.append(name)

df = pd.DataFrame(percProbs, columns=varNames)
df['perc'] = np.array(winPerc) * 100

gemTot = [50, 100, 200, 300, 450, 650, 850, 950]
gemNet = np.array(gemTot) - 750
gemPacks = [200+200*.20, 200+200*.22, 200+200*.24, 200+200*.26, 200+200*.30, 200+200*.35, 200+200*.40, 400]
totNet = np.array(gemPacks) + gemNet

### Multiplying the probability and the value of each win number ###
### Gems only ###
dfRankUtils = pd.DataFrame()
for wins, gems in zip(varNames, gemNet):
    temp = df[wins] * gems
    temp.rename(wins + '_gems', inplace=True)
    dfRankUtils = pd.concat([dfRankUtils, temp], axis=1)
### Total ###
for wins, gems in zip(varNames, totNet):
    temp = df[wins] * gems
    temp.rename(wins + '_tot', inplace=True)
    dfRankUtils = pd.concat([dfRankUtils, temp], axis=1)

### Summing the utilities from each win number ###
dfRankUtils['GemNet'] = dfRankUtils['0_wins_gems'] + dfRankUtils['1_wins_gems'] + dfRankUtils['2_wins_gems'] + dfRankUtils['3_wins_gems'] + dfRankUtils['4_wins_gems'] + dfRankUtils['5_wins_gems'] + dfRankUtils['6_wins_gems'] + dfRankUtils['7_wins_gems']
dfRankUtils['TotalNet'] = dfRankUtils['0_wins_tot'] + dfRankUtils['1_wins_tot'] + dfRankUtils['2_wins_tot'] + dfRankUtils['3_wins_tot'] + dfRankUtils['4_wins_tot'] + dfRankUtils['5_wins_tot'] + dfRankUtils['6_wins_tot'] + dfRankUtils['7_wins_tot']
dfRankUtils['perc']  = df['perc'] 


# =============================================================================
# Plotting
# =============================================================================
### Plotting ###
fig = plt.figure(figsize=(18,10))
fig.add_subplot(111)
plt.plot(dfRankUtils['perc'], dfRankUtils['TotalNet'], 'gs--', linewidth=2.0, markersize=8, label='Ranked: Gems+Packs (1 pack = 200 gems)')
plt.plot(dfTradUtils['perc'], dfTradUtils['TotalNet'], 'gv-', linewidth=2.0, markersize=8, label='Traditional: Gems+Packs (1 pack = 200 gems)')
plt.plot(dfPremUtils['perc'], dfPremUtils['TotalNet'], 'gx:', linewidth=2.0, markersize=8, label='Premium: Gems+Packs (1 pack = 200 gems)')
plt.plot(dfRankUtils['perc'], dfRankUtils['GemNet'], 'ys--', linewidth=2.0, markersize=8, label='Ranked: Gems Only')
plt.plot(dfTradUtils['perc'], dfTradUtils['GemNet'], 'yv:', linewidth=2.0, markersize=8, label='Traditional: Gems Only')
plt.plot(dfPremUtils['perc'], dfPremUtils['GemNet'], 'yx-', linewidth=2.0, markersize=8, label='Premium: Gems Only')
plt.xlabel('Win %', fontsize=20)
plt.ylabel('Net value in gem units', fontsize=20)
plt.legend(fontsize=16)
plt.xlim(5, 95)
plt.ylim(-1500, 2500)
plt.xticks(fontsize=16, rotation=0)
plt.yticks(fontsize=16, rotation=0)
plt.title('All Draft Types: Average Reward in Gem Units Based on Win %', fontsize=24)
plt.axhline(y=0, linewidth=2, color='b')
#plt.axvline(x=53.5, linewidth=3, color='b')
#plt.axvline(x=67.5, linewidth=3, color='b')
plt.show()