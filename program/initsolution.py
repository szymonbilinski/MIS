import numpy as np
from more_itertools import sort_together
import math
import time
#from program import Node



def initsolution(wezly,blabla):
#def initsolution():
    #parametry z palca
    CD=0
    print("ile wezlow",len(wezly))
    Q=blabla[0]
    T=blabla[2]
    route_counter=0
    #q=[2,2,1,1,2]
    #Koordynaty_x=[0,2,5,2,1]
    #Koordynaty_y=[0,1,1,2,3]
    #ANDpre=['0','5', '2', '', '9']
    #ORpre=['0','5', '', '1', '9']
    #N=[]
    routed=[]
    route=[[]]
    
    new_candidate_set=[]
    for i in range(len(wezly)):
        wezly[i].nazwa_wezla=str(i)
    AllPRE=[]
    for i in range(len(wezly)):
        AllPRE.append(len(wezly[i].ANDpre)+len(wezly[i].ORpre))
        routed.append(0)
        
    candidate_set=wezly
    
    
    #print("candidate set: ",candidate_set)
    #print("allpre ",AllPRE)
    numberbofvehicles=1
    while(candidate_set):
        
        temp=sort_together([AllPRE,candidate_set])
        
        candidate_set=temp[1]
        AllPRE=temp[0]
        insertionprocess=0
        for i in range(len(candidate_set)):
            if(CD+candidate_set[0].zapotrzebowanie>Q):
                #time.sleep(3)
                print("move is infeasible"+str(CD)+" "+str(candidate_set[0].zapotrzebowanie)+" "+str(Q))
                break
            if(wezly[0].okno_czasowe_min>wezly[0].okno_czasowe_max):
                print("move is infeasible")
                break
            
            #if(A[i]+s[i]+math.dist(route[-1],))

            route[route_counter].append(candidate_set[0])
            CD+=candidate_set[0].zapotrzebowanie
            insertionprocess=1
            
            # print("allpre",AllPRE)
            # print("candidate_set",candidate_set[i].nazwa_wezla)
            # print("routed",routed)
            candidate_set=candidate_set[1:]
            AllPRE=AllPRE[1:]
            routed=routed[1:]
            
            
            #print(i)
            #usuwanie z AND OR PC
            
            #time.sleep(5)
            
        if(insertionprocess==0):
            route_counter+=1
            route.append([])
            for i in range(len(candidate_set)):
                if(routed[i]==0):
                    print("last_candidate_set",candidate_set[i].nazwa_wezla)
                    new_candidate_set.append(candidate_set[i])
                    print("new_candidate_set",new_candidate_set[i].nazwa_wezla)
            candidate_set=new_candidate_set
            #routed=[]
            CD=0
            new_candidate_set=[]
        

        
    print(candidate_set)
    print(route)
    for i in range(len(route)):
        for j in range(len(route[i])):
            print(route[i][j].nazwa_wezla)
    

    #print(AllPRE)   
    return(route)
#initsolution()