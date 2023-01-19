import numpy as np
from more_itertools import sort_together
import math
import time
from random import randint,choice
#candidate_set=wezly

def ForwardOrBackwardWithinVehicle(routes):
    trasy=routes
    print("trasy",trasy)
    lengthK=len(trasy)
    for i in range(0,lengthK-1):
        lengthW=len(trasy[i])
        if(lengthW<2):
            break
        losowy_W=randint(0,lengthW-1)
        if losowy_W==0:
            zmienna=trasy[i][0]
            trasy[i][0]=trasy[i][1]
            trasy[i][1]=zmienna
        else:
            zmienna=trasy[i][losowy_W]
            trasy[i][losowy_W]=trasy[i][losowy_W-1]
            trasy[i][losowy_W-1]=zmienna
    return trasy

def TransferringAcrossVehicles(routes):
    trasy1=routes
    lengthL=len(trasy1)
    print("lengthL",lengthL)
    for i in range(0,lengthL-1):
        if lengthL==1:
            break
        if i==lengthL-1:
            break
        lengthW=len(trasy1[i])
        lengthW1=len(trasy1[i+1])
        print(trasy1[i+1])
        losowy=randint(0,lengthW-1)
        print("rand int val",lengthW1-1)
        losowy2=randint(0,lengthW1-1)
        zmienna=trasy1[i][losowy]
        trasy1[i][losowy]=trasy1[i+1][losowy2]
        trasy1[i+1][losowy2]=zmienna
    return trasy1
    

def ExchangeWithinVehicle(routes):
    trasy2=routes
    lengthK=len(trasy2)
    for i in range(0, lengthK-1):
        lengthW=len(trasy2[i])
        if(lengthW<2):
            break
        losowy_W=randint(0,lengthW-1)
        losowy_W1=randint(0,lengthW-1)
        if losowy_W==losowy_W1:
            break
        zmienna=trasy2[i][losowy_W]
        trasy2[i][losowy_W]=trasy2[i][losowy_W1]
        trasy2[i][losowy_W1]=zmienna
    return trasy2
        

def ExchangeAcrossVehicles(routes):
    trasy3=routes
    lengthL=len(trasy3)
    for i in range(0,lengthL-1):
        if lengthL==1:
            break
        if i==lengthL-1:
            break
        lengthW=len(trasy3[i])
        lengthW1=len(trasy3[i+1])
        
        # losowy2=randint(0,lengthW1-1)
        if lengthW > lengthW1:
            losowy=randint(0,lengthW1-1)
        else:
            losowy=randint(0,lengthW-1)
        zmienna=trasy3[i][losowy]
        trasy3[i][losowy]=trasy3[i+1][losowy]
        trasy3[i+1][losowy]=zmienna
    return trasy3


# def InsertVehicle(routes):
#     trasy4=routes
#     lengthL=len(trasy4)
#     losowy=randint(0,lengthL-1)
#     lengthLT=len(trasy4[losowy])
#     losowy1=randint(0,lengthLT-1)
#     nowy=trasy4[losowy][losowy1]
#     trasy4.remove([losowy][losowy1])
#     trasy4.append(nowy)
#     return trasy4


def feasibility(x,blabla,q):
    Q=blabla[0]
    #print("Q",Q)
    #print("x",x)
    suma=0
    for i in x:
        suma=suma+i.zapotrzebowanie
        #print("i",i.zapotrzebowanie)
    #print(suma)
    if suma+q.zapotrzebowanie>Q:
        return False
    else:
        return True
    

def localsearchF(temp_pert,blabla,dziwnykoszt):
    stackkk=[]
    CurrentSolution=100
    NewSolution=0
    routes=temp_pert[0]
    stack=temp_pert[1]
    iterNotImp=1
    TrialStack=[]
    final_list=[]
    final_koszt=dziwnykoszt
    MaxNotImp=50 #ilość powtórzeń bez ulepszeń
#MaxIter=600 
    Temp=100 #dana z artykułu
    alfa=0.95 #dana z artykułu
    lista1=ForwardOrBackwardWithinVehicle(routes)
    lista=[lista1,TransferringAcrossVehicles(routes),ExchangeWithinVehicle(routes),ExchangeAcrossVehicles(routes)]
    #ActiveVehicles=[] #tu ma być dostepna liczba pojazdow - roboczo wartosc 2
    TrialStack=stack
    while(len(stack)!=0 and iterNotImp<MaxNotImp):
            improve=False #logiczny parametr mówiący o tym czy wynik został ulepszony w danej iteracji
            for x in range(len(lista)-1): #pętla tworząca listę losowych elementów
                #print("lista",len(lista))
                zmienna=choice(lista)
                print(len(lista))
                lista.remove(zmienna)
                final_list.append(zmienna)
                if len(lista)==1:
                    zmienna=lista[0]
                    lista.remove(zmienna)
                    final_list.append(zmienna)  
            
            for n in range(0,3):
                wynik=final_list[n]
                #print("Wynik123",wynik)
                # do exploracji sąsiedztwa potrzebuję dostępu do pojedycznego węzła i jego pozycji? 
                # if feasible==False: #jak sprawdzić czy coś jest wykonalne?
                #     continue
                #Tu powinna być linia 10 z pseudokodu z artykułu ale nwm jak to połączyć ze sobą te symultaniczne wyżażanie - pomijam ten krok
                #New Solution powinno być wyliczane od Routes
               
               
                 #1 - obliczenie kosztow tras 
                nbVehicles=blabla[1]
                #koszt start
                cost=[]
                cost_temp=[]
                for k in range(len(wynik)):
                    cost_temp.append(0)
                    for n in range(len(wynik[k])):
                        cost_temp[k]+=wynik[k][n].czas_obslugi
                # print("cost temp",cost_temp)    

                for k in range(len(wynik)):
                    cost.append(math.sqrt(math.pow(0-wynik[k][0].koordynat_x,2)+math.pow(0-wynik[k][0].koordynat_y,2)))
                    for n in range(len(wynik[k])-1):
                        # print(cost," ",k," ",n," ",(routes[k][n].koordynat_x)," ",(routes[k][n+1].koordynat_x)," ",(routes[k][n].koordynat_y)," ",(routes[k][n+1].koordynat_y))
                        cost[k]+=math.sqrt(math.pow(wynik[k][n].koordynat_x-wynik[k][n+1].koordynat_x,2)+math.pow(wynik[k][n].koordynat_y-wynik[k][n+1].koordynat_y,2))
                    # print("cost1231",cost)
                    cost[k]+=cost_temp[k]
                NewSolution=sum(cost)
                    # print("cost",cost)  koszt koniec                
                if CurrentSolution>NewSolution:
                    routes=wynik
                    #print("wynik155",wynik)
                    #print("routes156",routes)
                    final_koszt=NewSolution
                    improve=True
                else:
                    final_koszt=CurrentSolution
            #TrialStack.append(candidate_set[iterNotImp]) 
            TrialStack=stack
            print("TRIAL",TrialStack)
            stackkk=[]
            for i in range(0,len(stack)):
                
                q=randint(0,len(TrialStack)-1)
                qq=TrialStack[q]
                print("QQ",qq)
                TrialVehicles=routes 
                #print("TrialVehicles", TrialVehicles)
                for z in range(len(routes)):
                    #print("STack1",stack)
                    #vv=randint(0,len(TrialVehicles)-1)

                    for x in TrialVehicles[z]:
                        #print("routes173",routes)
                        #if feasible==True:
                            #insert node q
                        #print("Z",routes[z])
                        #print("q",q)
                        sprawdz=feasibility(TrialVehicles[z],blabla,qq)
                        
                        if sprawdz==True:
                            #print("STACK",stack)
                            print("Q",qq)
                            print("RoutesZ",routes[z])
                            routes[z].append(qq)
                            print("ROUTESZ",routes[z])
                            #print("routes177",routes)
                            improve=True
                            #stack.remove(qq) #remove node q from Stack
                            break
                        else:
                            print("qq przed dodaniem else",qq)
                            stackkk.append(qq)
                            break
                    if improve==True:
                        break
                    TrialVehicles.remove(z)
                print("STACK przed usunieciem",stack)
                
                TrialStack.remove(qq)
                print("TrialStack po usunieciu",TrialStack)
            if improve==False:
                iterNotImp=iterNotImp+1
            #Temp=alfa*Temp
    #temp_pert[0]=routes
    #temp_pert[1]=stack
    if(stackkk!=[]):
        return([routes, final_koszt, stackkk])
    else:
        return([routes,final_koszt])



                
