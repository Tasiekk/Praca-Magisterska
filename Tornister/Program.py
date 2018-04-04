# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:37:22 2018

@author: Tasiek
"""
import Magister as mgr
import numpy as np
mgr.oceny[0]=input("Proszę podać ocenę z języka polskiego: ")
while mgr.oceny[0] not in range (1,7):
    mgr.oceny[0]=input("Podano złą ocenę! \nProszę podać ocenę z języka polskiego: ")
    
mgr.oceny[1]=input("Proszę podać ocenę z matematyki: ")
while mgr.oceny[1] not in range (1,7):
    mgr.oceny[1]=input("Podano złą ocenę! \nProszę podać ocenę z matematyki: ")
    
mgr.oceny[2]=input("Proszę podać ocenę z wiedzy o społeczeństwie: ")
while mgr.oceny[2] not in range (1,7):
    mgr.oceny[2]=input("Podano złą ocenę! \nProszę podać ocenę z wiedzy o społeczeństwie: ")
    
mgr.oceny[3]=input("Proszę podać ocenę z języka angielskiego: ")
while mgr.oceny[3] not in range (1,7):
    mgr.oceny[3]=input("Podano złą ocenę! \nProszę podać ocenę z języka angielskiego: ")
    
mgr.oceny[4]=input("Proszę podać ocenę z języka niemieckiego: ")
while mgr.oceny[4] not in range (1,7):
    mgr.oceny[4]=input("Podano złą ocenę! \nProszę podać ocenę z języka niemieckiego: ")
    
mgr.oceny[5]=input("Proszę podać ocenę z fizyki: ")
while mgr.oceny[5] not in range (1,7):
    mgr.oceny[5]=input("Podano złą ocenę! \nProszę podać ocenę z fizyki: ")
    
mgr.oceny[6]=input("Proszę podać ocenę z chemii: ")
while mgr.oceny[6] not in range (1,7):
    mgr.oceny[6]=input("Podano złą ocenę! \nProszę podać ocenę z chemii: ")
    
mgr.oceny[7]=input("Proszę podać ocenę z biologii: ")
while mgr.oceny[7] not in range (1,7):
    mgr.oceny[7]=input("Podano złą ocenę! \nProszę podać ocenę z biologii: ")
    
mgr.oceny[8]=input("Proszę podać ocenę z geografii: ")
while mgr.oceny[8] not in range (1,7):
    mgr.oceny[8]=input("Podano złą ocenę! \nProszę podać ocenę z geografii: ")
    
mgr.oceny[9]=input("Proszę podać ocenę z historii: ")
while mgr.oceny[9] not in range (1,7):
    mgr.oceny[9]=input("Podano złą ocenę! \nProszę podać ocenę z historii: ")
    
mgr.oceny[10]=input("Proszę podać ocenę z informatyki: ")
while mgr.oceny[10] not in range (1,7):
    mgr.oceny[10]=input("Podano złą ocenę! \nProszę podać ocenę z informatyki: ")
    
if 1 in mgr.oceny:
    print('Dziecko nie ukończyło gimnazjum!')
#    break
   
else:
    for i in range(0,11):
        if mgr.oceny[i]==2:
            mgr.punkty[i]=2
            mgr.punkty_proc[i]=2
        if mgr.oceny[i]==3:
            mgr.punkty[i]=8
            mgr.punkty_proc[i]=8
        if mgr.oceny[i]==4:
            mgr.punkty[i]=14
            mgr.punkty_proc[i]=13
        if mgr.oceny[i]==5:
            mgr.punkty[i]=17
            mgr.punkty_proc[i]=18
        if mgr.oceny[i]==6:
            mgr.punkty[i]=18
            mgr.punkty_proc[i]=20
    print('Proszę wybrać sposób przewidywań wyników końcowych.')
    print('1 - przewidywanie na podstawie wyników egzaminów próbnych,')
    print('2 - przewidywanie na podstawie ocen,')
    print('3 - przewidywanie na podstawie wyników egzaminów głównych.')
    wybor=int(input('Twój wybór: '))
    while wybor not in [1,2,3]:
        wybor=int(input('Wybierz 1,2 lub 3! \nTwój wybór: '))
    dodatek=0
    if wybor==1 or wybor==3:
        print('Który z języków obcych będzie zdawał uczeń?')
        print('1 - angielski')
        print('2 - niemiecki')
        jezyk=int(input('Proszę podać liczbę 1 lub 2: '))
        while jezyk not in [1,2]:
            jezyk=int(input('Proszę podać liczbę 1 lub 2: '))
        print('W kolejnych krokach prosimy o podanie wyników procentowych z testów. Jeżeli uczeń był zwolniony z egzaminu proszę wpisać: zwolniony.')
        pytania=['Proszę podać wynik procentowy egzaminu z języka polskiego: ',
                'Proszę podać wynik procentowy egzaminu z matematyki: ',
                'Proszę podać wynik procentowy egzaminu z wiedzy o społeczeństwie: ',
                'Proszę podać wynik procentowy egzaminu z przedmiotów przyrodniczych: ',
                'Proszę podać wynik procentowy egzaminu z języka obcego: ']
        for i in range(0,5):
               odp=input(pytania[i])
               if odp=='zwolniony': 
                   if i in [0,1]:
                      mgr.procenty[i]=mgr.punkty_proc[i]*5
                   if i==2:
                      mgr.procenty[i]=(mgr.punkty_proc[2]+mgr.punkty_proc[9])*5/2
                   if i==3:
                      mgr.procenty[i]=(mgr.punkty_proc[5]+mgr.punkty_proc[6]+mgr.punkty_proc[7]+mgr.punkty_proc[8])*5/4
                   if jezyk==1 and i==4:
                      mgr.procenty[i]=mgr.punkty_proc[3]*5
                   if jezyk==2 and i==4:
                      mgr.procenty[i]=mgr.punkty_proc[4]*5
               else:
                   odp=int(odp)    
                   while odp not in list(range(0,101)):
                       odp=int(input(pytania[i]))
                   mgr.procenty[i]=odp
#        mgr.procenty[0]=input('Proszę podać wynik procentowy egzaminu z języka polskiego: ')
#        while mgr.procenty[0] not in range (0,101):
#            mgr.procenty[0]=input('Proszę podać poprawny wynik procentowy egzaminu z języka polskiego: ')
#        mgr.procenty[1]=input('Proszę podać wynik procentowy egzaminu z matematyki: ')
#        while mgr.procenty[1] not in range (0,101):
#            mgr.procenty[1]=input('Proszę podać poprawny wynik procentowy egzaminu z matematyki: ')
#        mgr.procenty[2]=input('Proszę podać wynik procentowy egzaminu z wiedzy o społeczeństwie: ')
#        while mgr.procenty[2] not in range (0,101):
#            mgr.procenty[2]=input('Proszę podać poprawny wynik procentowy egzaminu z wiedzy o społeczeństwie: ')
#        mgr.procenty[3]=input('Proszę podać wynik procentowy egzaminu z przedmiotów przyrodniczych: ')
#        while mgr.procenty[3] not in range (0,101):
#            mgr.procenty[3]=input('Proszę podać poprawny wynik procentowy egzaminu z przedmiotów przyrodniczych: ')
#        mgr.procenty[4]=input('Proszę podać wynik procentowy egzaminu z języka obcego: ')
#        while mgr.procenty[4] not in range (0,101):
#            mgr.procenty[4]=input('Proszę podać poprawny wynik procentowy egzaminu z języka obcego: ')
        WspProcentowy=np.sum(mgr.procenty)*(0.2)
        sumy=[WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[3]+mgr.punkty[4],
              WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[2]+mgr.punkty[9],WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[7]+mgr.punkty[6],
              WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[10],WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[7],
              WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[8],WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[3],
              WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[6]+mgr.punkty[8],WspProcentowy+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[10]+mgr.punkty[3]]
        
    else:
        print('Wyniki egzaminu gimnazjalnego będą przewidywane na podstawie ocen ucznia.')
        print('Proszę mieć na uwadze, że jest to luźne przewidywanie i może być bardzo niedokładne.')
       
        for i in range(0,11):
            if mgr.oceny[i]==2:
                mgr.procentyMIN[i]=0
                mgr.procentyMAX[i]=10
            if mgr.oceny[i]==3:
                mgr.procentyMIN[i]=10
                mgr.procentyMAX[i]=40
            if mgr.oceny[i]==4:
                mgr.procentyMIN[i]=40
                mgr.procentyMAX[i]=65
            if mgr.oceny[i]==5:
                mgr.procentyMIN[i]=65
                mgr.procentyMAX[i]=90
            if mgr.oceny[i]==6:
                mgr.procentyMIN[i]=90
                mgr.procentyMAX[i]=100
        print('Który z języków obcych będzie zdawał uczeń?')
        print('1 - angielski')
        print('2 - niemiecki')
        jezyk=int(input('Proszę podać liczbę 1 lub 2: '))
        while jezyk not in [1,2]:
            jezyk=int(input('Proszę podać liczbę 1 lub 2: '))
        if jezyk==1:
            WspProcentowyMIN=(mgr.procentyMIN[0]+mgr.procentyMIN[1]+((mgr.procentyMIN[2]+mgr.procentyMIN[9])/2)+((mgr.procentyMIN[5]+mgr.procentyMIN[6]+mgr.procentyMIN[7]+mgr.procentyMIN[8])/4)+mgr.procentyMIN[3])*(0.2)
            WspProcentowyMAX=(mgr.procentyMAX[0]+mgr.procentyMAX[1]+((mgr.procentyMAX[2]+mgr.procentyMAX[9])/2)+((mgr.procentyMAX[5]+mgr.procentyMAX[6]+mgr.procentyMAX[7]+mgr.procentyMAX[8])/4)+mgr.procentyMAX[3])*(0.2)
        else:
            WspProcentowyMIN=(mgr.procentyMIN[0]+mgr.procentyMIN[1]+((mgr.procentyMIN[2]+mgr.procentyMIN[9])/2)+((mgr.procentyMIN[5]+mgr.procentyMIN[6]+mgr.procentyMIN[7]+mgr.procentyMIN[8])/4)+mgr.procentyMIN[4])*(0.2)
            WspProcentowyMAX=(mgr.procentyMAX[0]+mgr.procentyMAX[1]+((mgr.procentyMAX[2]+mgr.procentyMAX[9])/2)+((mgr.procentyMAX[5]+mgr.procentyMAX[6]+mgr.procentyMAX[7]+mgr.procentyMAX[8])/4)+mgr.procentyMAX[4])*(0.2)    
            
        sumyMIN=[WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[3]+mgr.punkty[4],
              WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[2]+mgr.punkty[9],WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[7]+mgr.punkty[6],
              WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[10],WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[7],
              WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[8],WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[3],
              WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[6]+mgr.punkty[8],WspProcentowyMIN+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[10]+mgr.punkty[3]]
        WspProcentowyMAX=(mgr.procentyMAX[0]+mgr.procentyMAX[1]+((mgr.procentyMAX[2]+mgr.procentyMAX[9])/2)+((mgr.procentyMAX[5]+mgr.procentyMAX[6]+mgr.procentyMAX[7]+mgr.procentyMAX[8])/4)+mgr.procentyMAX[3])*(0.2)
        sumyMAX=[WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[3]+mgr.punkty[4],
              WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[2]+mgr.punkty[9],WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[7]+mgr.punkty[6],
              WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[10],WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[7],
              WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[8],WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[5]+mgr.punkty[3],
              WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[6]+mgr.punkty[8],WspProcentowyMAX+mgr.punkty[0]+mgr.punkty[1]+mgr.punkty[10]+mgr.punkty[3]]
        print('Wnioskując z ocen ucznia możliwe wyniki z testów gimnazjalnych prezentują się następująco: ')
        print('- z języka polskiego od',mgr.procentyMIN[0],'% do',mgr.procentyMAX[0],'%')
        print('- z matematyki od',mgr.procentyMIN[1],'% do',mgr.procentyMAX[1],'%')
        print('- z wiedzy o społeczeństwie od',(mgr.procentyMIN[2]+mgr.procentyMIN[9])/2,'% do',(mgr.procentyMAX[2]+mgr.procentyMAX[9])/2,'%')
        print('- z przedmiotów przyrodniczych od',(mgr.procentyMIN[5]+mgr.procentyMIN[6]+mgr.procentyMIN[7]+mgr.procentyMIN[8])/4,'% do',(mgr.procentyMAX[5]+mgr.procentyMAX[6]+mgr.procentyMAX[7]+mgr.procentyMAX[8])/4,'%')
        if jezyk==1:
            print('- z języka angielskiego od',mgr.procentyMIN[3],'% do',mgr.procentyMAX[3],'%')
        else:
            print('- z języka niemieckiego od',mgr.procentyMIN[4],'% do',mgr.procentyMAX[4],'% ')
        
    wyroznienie=input('Czy uczeń ukończył szkołę z wyróźnieniem? ')
    while wyroznienie not in ['tak','Tak','nie','Nie','t','T','n','N']:
        wyroznienie=input('Czy uczeń ukończył szkołę z wyróźnieniem? ')
    if wyroznienie in ['tak','Tak','t','T']:
        dodatek+=7
    konkurs=input('Czy uczeń brał udział w konkursie o zasięgu ponadwojewódzkim? ')
    while konkurs not in ['tak','Tak','nie','Nie','t','T','n','N']:
        konkurs=input('Czy uczeń brał udział w konkursie o zasięgu ponadwojewódzkim? ')
    if konkurs in ['tak','Tak','t','T']:
        odp1=input('Czy został finalistą konkursu przedmiotowego? ')
        while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp1=input('Czy został finalistą konkursu przedmiotowego? ')
        if odp1 in ['tak','Tak','t','T']:
            dodatek+=10
        odp2=input('Czy został laureatem konkursu tematycznego lub interdyscyplinarnego? ')
        while odp2 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp2=input('Czy został laureatem konkursu tematycznego lub interdyscyplinarnego? ')
        if odp2 in ['tak','Tak','t','T']:
            dodatek+=7
        else:
            odp3=input('Czy został finalistą konkursu tematycznego lub interdyscyplinarnego? ')
            while odp3 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                odp3=input('Czy został finalistą konkursu tematycznego lub interdyscyplinarnego? ')
            if odp3 in ['tak','Tak','t','T']:
                dodatek+=5
                    
    konkurs=input('Czy uczeń brał udział w konkursie o zasięgu międzynarodowym lub ogólnopolskim? ')
    while konkurs not in ['tak','Tak','nie','Nie','t','T','n','N']:
        konkurs=input('Czy uczeń brał udział w konkursie o zasięgu międzynarodowym lub ogólnopolskim? ')
    if konkurs in ['tak','Tak','t','T']:
        odp1=input('Czy został finalistą konkursu z przedmiotu lub przedmiotów artystycznych objętych ramowym planem nauczania szkoły artystycznej? ')
        while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp1=input('Czy został finalistą konkursu z przedmiotu lub przedmiotów artystycznych objętych ramowym planem nauczania szkoły artystycznej? ')
        if odp1 in ['tak','Tak','t','T']:
            dodatek+=10
        odp2=input('Czy został laureatem konkursu z przedmiotu lub przedmiotów artystycznych nieobjętych ramowym planem nauczania szkoły artystycznej? ')
        while odp2 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp2=input('Czy został laureatem konkursu z przedmiotu lub przedmiotów artystycznych nieobjętych ramowym planem nauczania szkoły artystycznej? ')
        if odp2 in ['tak','Tak','t','T']:
            dodatek+=4
        else:
            odp3=input('Czy został finalistą konkursu z przedmiotu lub przedmiotów artystycznych nieobjętych ramowym planem nauczania szkoły artystycznej? ')
            while odp3 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                odp3=input('Czy został finalistą konkursu z przedmiotu lub przedmiotów artystycznych nieobjętych ramowym planem nauczania szkoły artystycznej? ')
            if odp3 in ['tak','Tak','t','T']:
                dodatek+=3
    
    konkurs=input('Czy uczeń brał udział w konkursie o zasięgu wojewódzkim? ')
    while konkurs not in ['tak','Tak','nie','Nie','t','T','n','N']:
        konkurs=input('Czy uczeń brał udział w konkursie o zasięgu wojewódzkim? ')
    if konkurs in ['tak','Tak','t','T']:
        odp1=input('Czy został finalistą dwóch lub więcej konkursów przedmiotowych? ')
        while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp1=input('Czy został finalistą dwóch lub więcej konkursów przedmiotowych? ')
        if odp1 in ['tak','Tak','t','T']:
            dodatek+=10
        else:
            odp4=input('Czy został finalistą jednego konkursu przedmiotowego? ')
            while odp4 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                odp4=input('Czy został finalistą jednego konkursu przedmiotowego? ')
            if odp4 in ['tak','Tak','t','T']:
                dodatek+=7
        odp2=input('Czy został laureatem dwóch lub więcej konkursów interdyscyplinarnych lub tematycznych? ')
        while odp2 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp2=input('Czy został laureatem dwóch lub więcej konkursów interdyscyplinarnych lub tematycznych? ')
        if odp2 in ['tak','Tak','t','T']:
            dodatek+=7
        else:
            odp5=input('Czy został laureatem jednego konkursu interdyscyplinarnego lub tematycznego? ')
            while odp5 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                odp5=input('Czy został laureatem jednego konkursu interdyscyplinarnego lub tematycznego? ')
            if odp5 in ['tak','Tak','t','T']:
                dodatek+=5
            else:
                odp3=input('Czy został finalistą dwóch lub więcej konkursów interdyscyplinarnych lub tematycznych? ')
                while odp3 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                    odp3=input('Czy został finalistą dwóch lub więcej konkursów interdyscyplinarnych lub tematycznych? ')
                if odp3 in ['tak','Tak','t','T']:
                    dodatek+=5
                else:
                    odp6=input('Czy został finalistą jednego konkursu interdyscyplinarnego lub tematycznego? ')
                    while odp6 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                        odp6=input('Czy został finalistą jednego konkursu interdyscyplinarnego lub tematycznego? ')
                        if odp6 in ['tak','Tak','t','T']:
                            dodatek+=3
    print('Czy uczeń uzyskał wysokie miejsce w zawodach wiedzy innych niż wyżej wymienione, artystycznych lub sportowych organizowanych przez kuratora oswiaty na szczeblu: ')
    odp1=input('międzynarodowym? ')
    while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
        odp1=input('międzynarodowym? ')
    if odp1 in ['tak','Tak','t','T']:
        dodatek+=4
    else:
        odp1=input('krajowym? ')
        while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
            odp1=input('krajowym? ')
        if odp1 in ['tak','Tak','t','T']:
            dodatek+=3
        else:
            odp1=input('wojewódzkim? ')
            while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                odp1=input('wojewódzkim? ')
            if odp1 in ['tak','Tak','t','T']:
                dodatek+=2
            else:
                odp1=input('powiatowym? ')
                while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
                    odp1=input('powiatowym? ')
                if odp1 in ['tak','Tak','t','T']:
                    dodatek+=1            
    odp1=input('Czy uczeń udzielał się na rzecz srodowiska szkolnego i był aktywny w życiu społecznym szkoły?')
    while odp1 not in ['tak','Tak','nie','Nie','t','T','n','N']:
        odp1=input('Czy uczeń udzielał się na rzecz srodowiska szkolnego i był aktywny w życiu społecznym szkoły? ')
    if odp1 in ['tak','Tak','t','T']:
        dodatek+=3

if wybor==1 or wybor==3:
        for i in range(0,9):
            sumy[i]+=dodatek
            if sumy[i]>200:
                sumy[i]=200
        print('Liczba punktów zdobyta poprzez oceny oraz wyniki testu może różnić się w zależnosci od profilu klasy oraz szkoły wybranej przez ucznia')
        print('Każda szkoła bierze pod uwagę oceny z języka polskiego i matematyki. Pozostałe dwie oceny dobierane są na podstawie profilu klasy.')
        print('Jeżeli szkoła będzie wymagała ocen z języków obcych to uczeń będzie miał',sumy[0],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z wiedzy o społeczeństwie i historii to uczeń będzie miał',sumy[1],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z biologii i chemii to uczeń będzie miał',sumy[2],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z fizyki i informatyki to uczeń będzie miał',sumy[3],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z fizyki i biologii to uczeń będzie miał',sumy[4],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z fizyki i geografii to uczeń będzie miał',sumy[5],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z fizyki i języka angielskiego to uczeń będzie miał',sumy[6],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z chemii i języka angielskiego i to uczeń będzie miał',sumy[7],'punktów.')
        print('Jeżeli szkoła będzie wymagała ocen z informatyki i języka angielskiego to uczeń będzie miał',sumy[8],'punktów.')
else:
    for i in range(0,9):
            sumyMIN[i]+=dodatek
            sumyMAX[i]+=dodatek
            if sumyMIN[i]>200:
                sumyMIN[i]=200
            if sumyMAX[i]>200:
                sumyMAX[i]=200
                
    print('Liczba punktów zdobyta poprzez oceny oraz wyniki testu może różnić się w zależnosci od profilu klasy oraz szkoły wybranej przez ucznia')
    print('Każda szkoła bierze pod uwagę oceny z języka polskiego i matematyki. Pozostałe dwie oceny dobierane są na podstawie profilu klasy.')
    print('Jeżeli szkoła będzie wymagała ocen z języków obcych to uczeń będzie zdobędzie od ',sumyMIN[0],'do',sumyMAX[0],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z wiedzy o społeczeństwie i historii to uczeń zdobędzie od ',sumyMIN[1],'do',sumyMAX[1],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z biologii i chemii to uczeń zdobędzie od ',sumyMIN[2],'do',sumyMAX[2],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z fizyki i informatyki to uczeń zdobędzie od ',sumyMIN[3],'do',sumyMAX[3],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z fizyki i biologii to uczeń zdobędzie od ',sumyMIN[4],'do',sumyMAX[4],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z fizyki i geografii to uczeń zdobędzie od ',sumyMIN[5],'do',sumyMAX[5],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z fizyki i języka angielskiego to uczeń zdobędzie od ',sumyMIN[6],'do',sumyMAX[6],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z chemii i języka angielskiego i to uczeń zdobędzie od ',sumyMIN[7],'do',sumyMAX[7],'punktów.')
    print('Jeżeli szkoła będzie wymagała ocen z informatyki i języka angielskiego to uczeń zdobędzie od ',sumyMIN[8],'do',sumyMAX[8],'punktów.')
#    break