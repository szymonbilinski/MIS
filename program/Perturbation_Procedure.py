import math
from more_itertools import sort_together

def pert_proc(routes,blabla):
    #1 - obliczenie kosztow tras 
    nbVehicles=blabla[1]
    print("P_P")
    #koszt start
    cost=[]
    print("pert routes",routes)
    cost_temp=[]
    for k in range(len(routes)):
        cost_temp.append(0)
        for n in range(len(routes[k])):
            cost_temp[k]+=routes[k][n].czas_obslugi
        # print("cost temp",cost_temp)    

    for k in range(len(routes)):
        
        cost.append(math.sqrt(math.pow(0-routes[k][0].koordynat_x,2)+math.pow(0-routes[k][0].koordynat_y,2)))
        for n in range(len(routes[k])-1):
            print(cost," ",k," ",n," ",(routes[k][n].koordynat_x)," ",(routes[k][n+1].koordynat_x)," ",(routes[k][n].koordynat_y)," ",(routes[k][n+1].koordynat_y))
            cost[k]+=math.sqrt(math.pow(routes[k][n].koordynat_x-routes[k][n+1].koordynat_x,2)+math.pow(routes[k][n].koordynat_y-routes[k][n+1].koordynat_y,2))
        # print("cost1231",cost)
        cost[k]+=cost_temp[k]
        # print("cost",cost)  koszt koniec
    
    
    #2 - obliczenie ocen tras
    I=[]
    for k in range(len(routes)):
        I.append(cost[k]/len(routes[k]))

    #3 - posortowanie tego czegos 
    # print("I",I)
    # print("routes",routes)
    temp=sort_together([I,routes],reverse=True)
    I=temp[0]
    routes=list(temp[1])
    # print("I",I)
    # print("routes",routes)
    # usuwanie odpowiedniej ilosci oraz zapisywanie usunietych w stosie
    stack=[]
    print("co tu jest",nbVehicles,len(routes))
    if(int(nbVehicles)==len(routes)):
        
        routes_to_remove=int(len(routes)/2)
        for i in range(routes_to_remove):
            for j in range(len(routes[i])):
                stack.append(routes[i].pop(0))
                # print("popppppppppped")
            routes=routes[1:]


    elif(int(nbVehicles)>len(routes)):
        
        routes_to_remove=int(nbVehicles-len(routes))
        for i in range(routes_to_remove):
            for j in range(len(routes[i])):
                stack.append(routes[i].pop(0))
                # print("popppppppppped")
            routes=routes[1:]


    elif(int(nbVehicles)<len(routes)):
        
        routes_to_remove=int(nbVehicles/2)
        for i in range(routes_to_remove):
            for j in range(len(routes[i])):
                stack.append(routes[i].pop(0))
                # print("popppppppppped")
            routes=routes[1:]

    # print("routes popped",routes)
    # print("stack",stack)
    
    # print("P_P")
    return([routes,stack])

# pert_proc(0)