import numpy as np
from more_itertools import sort_together
import math
import time
#from program import wezly
from random import *
#candidate_set=wezly
candidate_set=2
final_list=[]
MaxNotImp=50 #ilość powtórzeń bez ulepszeń


def ForwardOrBackwardWithinVehicle():
    print('tak')
def TransferringAcrossVehicles():
    print('tak')
def ExchangeWithinVehicle():
    print('tak')
def ExchangeAcrossVehicles():
    print('tak')
def InsertVehicle():
    print('tak')

lista=[ForwardOrBackwardWithinVehicle(),TransferringAcrossVehicles(),ExchangeWithinVehicle(),ExchangeAcrossVehicles(),InsertVehicle()]
def LocalSearch():
    iterNotImp=1
    while(len(candidate_set)!=0 and iterNotImp<MaxNotImp):
            improve=False #logiczny parametr mówiący o tym czy wynik został ulepszony w danej iteracji
            for x in range(1,5): #pętla tworząca listę losowych elementów
                zmienna=choice(lista)
                lista.remove(zmienna)
                final_list.append(zmienna)
                if len(lista)==1:
                    zmienna=lista[0]
                    lista.remove(zmienna)
                    final_list.append(zmienna)  
            
            for n in range(1,5):
                final_list[n]
            candidate_set=candidate_set-1

                
