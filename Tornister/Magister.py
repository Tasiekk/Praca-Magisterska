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

e=np.zeros(4)
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
        
        

        
#linie trendu
#x = [2015,2016,2017]
#y = [150,183,176]
#plt.scatter(x, y)
#z = np.polyfit(x, y, 1)
#p = np.poly1d(z)
#plt.plot(x,p(x),"r--")
#plt.show()
#print(p(2018))

oceny=np.zeros(9)
punkty=np.zeros(9)
procenty=np.zeros(5)
oceny[0]=input("Proszę podać ocenę z języka polskiego: ")
oceny[1]=input("Proszę podać ocenę z matematyki: ")
oceny[2]=input("Proszę podać ocenę z wiedzy o społeczeństwie: ")
oceny[3]=input("Proszę podać ocenę z języka angielskiego: ")
oceny[4]=input("Proszę podać ocenę z języka niemieckiego: ")
oceny[5]=input("Proszę podać ocenę z fizyki: ")
oceny[6]=input("Proszę podać ocenę z chemii: ")
oceny[7]=input("Proszę podać ocenę z biologii: ")
oceny[8]=input("Proszę podać ocenę z geografii: ")

for i in range(0,9):
    if oceny[i] in range(1,7):
        if oceny[i]==1:
            print("Dziecko nie ukończyło gimnazjum.")
        if oceny[i]==2:
            punkty[i]=2
        if oceny[i]==3:
            punkty[i]=8
        if oceny[i]==4:
            punkty[i]=14
        if oceny[i]==5:
            punkty[i]=17
        if oceny[i]==6:
            punkty[i]=18
    else:
        print("Podano złą ocenę!")

print('Proszę wybrać sposób przewidywań wyników końcowych.')
print('1 - przewidywanie na podstawie wyników egzaminów próbnych,')
print('2 - przewidywanie na podstawie ocen,')
print('3 - przewidywanie na podstawie wyników egzaminów głównych.')

wybor=input('Twój wybór: ')
if wybor==1 or wybor==3:
    procenty[0]=input('Proszę podać wynik procentowy egzaminu z języka polskiego: ')
    procenty[1]=input('Proszę podać wynik procentowy egzaminu z matematyki: ')
    procenty[2]=input('Proszę podać wynik procentowy egzaminu z wiedzy o społeczeństwie: ')
    procenty[3]=input('Proszę podać wynik procentowy egzaminu z przedmiotów przyrodniczych: ')
    procenty[4]=input('Proszę podać wynik procentowy egzaminu z języka obcego: ')    
if wybor==2:   

else:
    print('Nie ma takiej opcji!')

#print("Przejdźmy do analizy przybliżonych wyników egzaminu gimnazjalnego.")
#oceny[4]=input("Proszę podać ocenę z języka obcego nowożytnego, który będzie zdawany: ")
#oceny[5]=input("Proszę podać ocenę z biologii: ")
#oceny[6]=input("Proszę podać ocenę z geografii: ")
#oceny[7]=input("Proszę podać ocenę z chemii: ")
#oceny[8]=input("Proszę podać ocenę z fizyki: ")
#oceny[9]=input("Proszę podać ocenę z wiedzy o społeczeństwie: ")
#przyrka=(oceny[5]+oceny[6]+oceny[7]+oceny[8])/4



        
