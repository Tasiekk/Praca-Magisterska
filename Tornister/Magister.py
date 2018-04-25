# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:54:25 2018

@author: Tasiek
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Interpolacja import interpolation, error
names=['Typ','Liczba zdających','Średni wynik','Odchylenie standardowe']
namesP=['Liczba zdających','Średni wynik','Odchylenie standardowe']
indexPowiaty=['bytowski','chojnicki','człuchowski','gdański','kartuski','kościerski','kwidzyński','lęborski','Gdańsk','Gdynia','Słupsk','Sopot','malborski','nowodworski','pucki','słupski','starogardzki','sztumski','tczewski','wejherowski']

#GminyAngPodst = pd.read_excel('GDA - GMINY\GMINY - Angielski.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
#GminyAngRozsz = pd.read_excel('GDA - GMINY\GMINY - Angielski.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
#GminyPolski = pd.read_excel('GDA - GMINY\GMINY - Human.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
#GminyWOS = pd.read_excel('GDA - GMINY\GMINY - Human.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
#GminyMat = pd.read_excel('GDA - GMINY\GMINY - Matma.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
#GminyPrz = pd.read_excel('GDA - GMINY\GMINY - Matma.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)
#GminyNiemPodst = pd.read_excel('GDA - GMINY\GMINY - Niemiecki.xlsx',index_col=0, header=0,usecols=[0,1,2,3,4],names=names)
#GminyNiemRozsz = pd.read_excel('GDA - GMINY\GMINY - Niemiecki.xlsx',index_col=0, header=0,usecols=[0,1,5,6,7],names=names)

PowiatyAngLiczbaZd = pd.read_excel('GDA - POWIATY\POWIATY - Angielski - Liczba zdajacych.xlsx',index_col=0,header=0)
PowiatyAngSredni = pd.read_excel('GDA - POWIATY\POWIATY - Angielski - Średni wynik.xlsx',index_col=0,header=0)
PowiatyAngOdchSt = pd.read_excel('GDA - POWIATY\POWIATY - Angielski - Odch st.xlsx',index_col=0,header=0)

PowiatyJPLiczbaZd = pd.read_excel('GDA - POWIATY\POWIATY - JP - Liczba zdajacych.xlsx',index_col=0,header=0)
PowiatyJPSredni = pd.read_excel('GDA - POWIATY\POWIATY - JP - Średni wynik.xlsx',index_col=0,header=0)
PowiatyJPOdchSt = pd.read_excel('GDA - POWIATY\POWIATY - JP - Odch st.xlsx',index_col=0,header=0)

PowiatyWOSLiczbaZd = pd.read_excel('GDA - POWIATY\POWIATY - WOS - Liczba zdajacych.xlsx',index_col=0,header=0)
PowiatyWOSSredni = pd.read_excel('GDA - POWIATY\POWIATY - WOS - Średni wynik.xlsx',index_col=0,header=0)
PowiatyWOSOdchSt = pd.read_excel('GDA - POWIATY\POWIATY - WOS - Odch st.xlsx',index_col=0,header=0)

PowiatyMATLiczbaZd = pd.read_excel('GDA - POWIATY\POWIATY - MAT - Liczba zdających.xlsx',index_col=0,header=0)
PowiatyMATSredni = pd.read_excel('GDA - POWIATY\POWIATY - MAT - Średni wynik.xlsx',index_col=0,header=0)
PowiatyMATOdchSt = pd.read_excel('GDA - POWIATY\POWIATY - MAT - Odch st.xlsx',index_col=0,header=0)

PowiatyPRZLiczbaZd = pd.read_excel('GDA - POWIATY\POWIATY - PRZ - Liczba zdajacych.xlsx',index_col=0,header=0)
PowiatyPRZSredni = pd.read_excel('GDA - POWIATY\POWIATY - PRZ - Średni wynik.xlsx',index_col=0,header=0)
PowiatyPRZOdchSt = pd.read_excel('GDA - POWIATY\POWIATY - PRZ - Odch st.xlsx',index_col=0,header=0)

Srednie=[PowiatyAngSredni,PowiatyJPSredni,PowiatyWOSSredni,PowiatyMATSredni,PowiatyPRZSredni]

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

Parametry = [ParametryKrajAng,ParametryWojAng,ParametryKrajMat,ParametryWojMat,ParametryKrajNiem,ParametryWojNiem,ParametryKrajPolski,ParametryWojPolski,ParametryKrajPrz,ParametryWojPrz,ParametryKrajWOS,ParametryWojWOS]
for l in Parametry:
    l.insert(len(l.columns),'2018-liniowo',np.zeros(len(l)))
    l.insert(len(l.columns),'2018-kwadratowo',np.zeros(len(l)))
    l.insert(len(l.columns),'Błąd-liniowo',np.zeros(len(l)))
    l.insert(len(l.columns),'Błąd-kwadratowo',np.zeros(len(l)))
    for i in range(0,len(l)):        
        b=l[i:i+1]
        g=np.zeros(5)
        for j in range(0,5):
            g[j]=b.iat[0,j] 
        l.iat[i,5]=interpolation([2013,2014,2015,2016,2017],g,1)
        l.iat[i,6]=interpolation([2013,2014,2015,2016,2017],g,2)
        l.iat[i,7]=error([2013,2014,2015,2016,2017],g,1)
        l.iat[i,8]=error([2013,2014,2015,2016,2017],g,2)



SzkolySredniLimit3 = pd.read_excel('SZKOŁY\LICEA - Średni limit punktowy.xlsx',index_col=0,header=0,skip_footer=5)
SzkolySredniLimit2 = pd.read_excel('SZKOŁY\LICEA - Średni limit punktowy.xlsx',index_col=0,header=0, skiprows=27, usecols=2)

SzkolySredniLimit3.insert(len(SzkolySredniLimit3.columns),'2018-liniowo',np.zeros(len(SzkolySredniLimit3)))
SzkolySredniLimit3.insert(len(SzkolySredniLimit3.columns),'2018-kwadratowo',np.zeros(len(SzkolySredniLimit3)))
SzkolySredniLimit3.insert(len(SzkolySredniLimit3.columns),'Błąd-liniowo',np.zeros(len(SzkolySredniLimit3)))
SzkolySredniLimit3.insert(len(SzkolySredniLimit3.columns),'Błąd-kwadratowo',np.zeros(len(SzkolySredniLimit3)))

SzkolySredniLimit2.insert(len(SzkolySredniLimit2.columns),'2018-liniowo',np.zeros(len(SzkolySredniLimit2)))
SzkolySredniLimit2.insert(len(SzkolySredniLimit2.columns),'2018-kwadratowo',np.zeros(len(SzkolySredniLimit2)))
SzkolySredniLimit2.insert(len(SzkolySredniLimit2.columns),'Błąd-liniowo',np.zeros(len(SzkolySredniLimit2)))
SzkolySredniLimit2.insert(len(SzkolySredniLimit2.columns),'Błąd-kwadratowo',np.zeros(len(SzkolySredniLimit2)))

f=np.zeros(3)
for i in range(0,len(SzkolySredniLimit3)):        
       b=SzkolySredniLimit3[i:i+1]
       for j in range(0,3):
                f[j]=b.iat[0,j] 
       SzkolySredniLimit3.iat[i,3]=interpolation([2015,2016,2017],f,1)
       SzkolySredniLimit3.iat[i,4]=interpolation([2015,2016,2017],f,2)
       SzkolySredniLimit3.iat[i,5]=error([2015,2016,2017],f,1)
       SzkolySredniLimit3.iat[i,6]=error([2015,2016,2017],f,2)

g=np.zeros(2)
for i in range(0,len(SzkolySredniLimit2)):        
       b=SzkolySredniLimit3[i:i+1]
       for j in range(0,2):
                g[j]=b.iat[0,j] 
       SzkolySredniLimit2.iat[i,2]=interpolation([2015,2016],g,1)
       SzkolySredniLimit2.iat[i,3]=interpolation([2015,2016],g,2)
       SzkolySredniLimit2.iat[i,4]=error([2015,2016],g,1)
       SzkolySredniLimit2.iat[i,5]=error([2015,2016],g,2)
       
PowiatyAngSredni['2018-liniowo']=np.zeros(20)
PowiatyJPSredni['2018-liniowo']=np.zeros(20)
PowiatyWOSSredni['2018-liniowo']=np.zeros(20)
PowiatyMATSredni['2018-liniowo']=np.zeros(20)
PowiatyPRZSredni['2018-liniowo']=np.zeros(20)

PowiatyAngSredni['2018-kwadratowo']=np.zeros(20)
PowiatyJPSredni['2018-kwadratowo']=np.zeros(20)
PowiatyWOSSredni['2018-kwadratowo']=np.zeros(20)
PowiatyMATSredni['2018-kwadratowo']=np.zeros(20)
PowiatyPRZSredni['2018-kwadratowo']=np.zeros(20)

PowiatyAngSredni['Błąd-liniowo']=np.zeros(20)
PowiatyJPSredni['Błąd-liniowo']=np.zeros(20)
PowiatyWOSSredni['Błąd-liniowo']=np.zeros(20)
PowiatyMATSredni['Błąd-liniowo']=np.zeros(20)
PowiatyPRZSredni['Błąd-liniowo']=np.zeros(20)

PowiatyAngSredni['Błąd-kwadratowo']=np.zeros(20)
PowiatyJPSredni['Błąd-kwadratowo']=np.zeros(20)
PowiatyWOSSredni['Błąd-kwadratowo']=np.zeros(20)
PowiatyMATSredni['Błąd-kwadratowo']=np.zeros(20)
PowiatyPRZSredni['Błąd-kwadratowo']=np.zeros(20)

e=np.zeros(4)
a=[2014,2015,2016,2017]
for k in Srednie:
    for i in range(0,20):        
        b=k[i:i+1]
        for j in range(0,4):
            e[j]=b.iat[0,j] 
        k.iat[i,4]=interpolation(a,e,1)
        k.iat[i,5]=interpolation(a,e,2)
        k.iat[i,6]=error(a,e,1)
        k.iat[i,7]=error(a,e,2)
    

oceny=np.zeros(11)
punkty=np.zeros(11)
punkty_proc=np.zeros(11)
procenty=np.zeros(5)
procentyMIN=np.zeros(11)
procentyMAX=np.zeros(11)