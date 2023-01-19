import math



def calculate_solution(route):
    cost=[]
    cost_temp=[]
    for k in range(len(route)):
        cost_temp.append(0)
        for n in range(len(route[k])):
            cost_temp[k]+=route[k][n].czas_obslugi
        # print("cost temp",cost_temp)    

    for k in range(len(route)):
        cost.append(math.sqrt(math.pow(0-route[k][0].koordynat_x,2)+math.pow(0-route[k][0].koordynat_y,2)))
        for n in range(len(route[k])-1):
            # print(cost," ",k," ",n," ",(route[k][n].koordynat_x)," ",(route[k][n+1].koordynat_x)," ",(route[k][n].koordynat_y)," ",(route[k][n+1].koordynat_y))
            cost[k]+=math.sqrt(math.pow(route[k][n].koordynat_x-route[k][n+1].koordynat_x,2)+math.pow(route[k][n].koordynat_y-route[k][n+1].koordynat_y,2))
        # print("cost1231",cost)
        cost[k]+=cost_temp[k]

    solution=sum(cost)

    return(solution)