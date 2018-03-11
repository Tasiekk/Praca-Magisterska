# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:54:25 2018

@author: Tasiek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
names=['Typ','Liczba zdających','Średni wynik','Odchylenie standardowe']
namesP=['Liczba zdających','Średni wynik','Odchylenie standardowe']
GminyAngPodst = pd.read_excel('GDA - GMINY\GMINY - Angielski.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
GminyAngRozsz = pd.read_excel('GDA - GMINY\GMINY - Angielski.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
GminyPolski = pd.read_excel('GDA - GMINY\GMINY - Human.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
GminyWOS = pd.read_excel('GDA - GMINY\GMINY - Human.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
GminyMat = pd.read_excel('GDA - GMINY\GMINY - Matma.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
GminyPrz = pd.read_excel('GDA - GMINY\GMINY - Matma.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
GminyNiemPodst = pd.read_excel('GDA - GMINY\GMINY - Niemiecki.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
GminyNiemRozsz = pd.read_excel('GDA - GMINY\GMINY - Niemiecki.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)

PowiatyAngPodst = pd.read_excel('GDA - POWIATY\POWIATY - Angielski.xlsx',index_col=0,header=0,usecols=[0,1,2,3],names=namesP)
PowiatyAngRozsz = pd.read_excel('GDA - POWIATY\POWIATY - Angielski.xlsx',index_col=0,header=0,usecols=[0,4,5,6],names=namesP)
PowiatyPolski = pd.read_excel('GDA - POWIATY\POWIATY - Human.xlsx',index_col=0,header=0,usecols=[0,1,2,3],names=namesP)
PowiatyWOS = pd.read_excel('GDA - POWIATY\POWIATY - Human.xlsx',index_col=0,header=0,usecols=[0,4,5,6],names=namesP)
PowiatyMat = pd.read_excel('GDA - POWIATY\POWIATY - Matma.xlsx',index_col=0,header=0,usecols=[0,1,2,3],names=namesP)
PowiatyPrz = pd.read_excel('GDA - POWIATY\POWIATY - Matma.xlsx',index_col=0,header=0,usecols=[0,4,5,6],names=namesP)
PowiatyNiemPodst = pd.read_excel('GDA - POWIATY\POWIATY - Niemiecki.xlsx',index_col=0,header=0,usecols=[0,1,2,3],names=namesP)
PowiatyNiemRozsz = pd.read_excel('GDA - POWIATY\POWIATY - Niemiecki.xlsx',index_col=0,header=0,usecols=[0,4,5,6],names=namesP)

ParametryKrajAng = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-Ang.xlsx',index_col=0,header=0)
ParametryWojAng = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-Ang.xlsx',index_col=0,header=0)
ParametryKrajMat = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-Matma.xlsx',index_col=0,header=0)
ParametryWojMat = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-Matma.xlsx',index_col=0,header=0)
ParametryKrajNiem = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-Niem.xlsx',index_col=0,header=0)
ParametryWojNiem = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-Niem.xlsx',index_col=0,header=0)
ParametryKrajPolski = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-Polski.xlsx',index_col=0,header=0)
ParametryWojPolski = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-Polski.xlsx',index_col=0,header=0)
ParametryKrajPrz = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-Przyrka.xlsx',index_col=0,header=0)
ParametryWojPrz = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-Przyrka.xlsx',index_col=0,header=0)
ParametryKrajWOS = pd.read_excel('Parametry WOJ-KRAJ\Parametry-KRAJ-WOS.xlsx',index_col=0,header=0)
ParametryWojWOS = pd.read_excel('Parametry WOJ-KRAJ\Parametry-WOJ-WOS.xlsx',index_col=0,header=0)

#linie trendu
x = [2015,2016,2017]
y = [150,183,176]
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")

plt.show()
print(p(2018))