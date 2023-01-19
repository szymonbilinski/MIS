import pandas as pd
import math




def ex_wyniku(routes,SBest):
    wynik=21
    czas_wyjazdu=[]
    czas_przyjazdu=[]
    laczny_czas=[]
    laczne_zapotrzebowanie=[]
    nazwy_wezlow_na_trasie=[]

    
    cost_temp=[]
    for k in range(len(routes)):
        cost_temp.append(0)
        for n in range(len(routes[k])):
            cost_temp[k]+=routes[k][n].czas_obslugi
        # print("cost temp",cost_temp)    

    for k in range(len(routes)):
        laczny_czas.append(math.sqrt(math.pow(0-routes[k][0].koordynat_x,2)+math.pow(0-routes[k][0].koordynat_y,2)))
        for n in range(len(routes[k])-1):
            # print(cost," ",k," ",n," ",(route[k][n].koordynat_x)," ",(route[k][n+1].koordynat_x)," ",(route[k][n].koordynat_y)," ",(route[k][n+1].koordynat_y))
            laczny_czas[k]+=math.sqrt(math.pow(routes[k][n].koordynat_x-routes[k][n+1].koordynat_x,2)+math.pow(routes[k][n].koordynat_y-routes[k][n+1].koordynat_y,2))
        # print("cost1231",cost)
        laczny_czas[k]+=cost_temp[k]



    print("len trasa",routes)
    for i in range(len(routes)):
        nazwy_wezlow_na_trasie.append('')
        laczne_zapotrzebowanie.append(0)
        
        czas_wyjazdu.append(routes[i][0].okno_czasowe_min-(math.sqrt(math.pow(0-routes[i][0].koordynat_x,2)+math.pow(0-routes[i][0].koordynat_y,2))))
        for j in range(len(routes[i])):
            nazwy_wezlow_na_trasie[i]+=routes[i][j].nazwa_wezla
            print("nazwy_wezlow_na_trasie",nazwy_wezlow_na_trasie)
            laczne_zapotrzebowanie[i]+=routes[i][j].zapotrzebowanie
        czas_przyjazdu.append(czas_wyjazdu[i]+laczny_czas[i])
        
    data1={'wynik':SBest}
    
    data={
          'wezly':nazwy_wezlow_na_trasie,
          'godzina wyjazdu':czas_wyjazdu,
          'godzina przyjazdu':czas_przyjazdu,
          'laczny czas':laczny_czas,
          'zapotrzebowanie':laczne_zapotrzebowanie
          }
    print("data",data)
    
    df=pd.DataFrame(data)
    df1=pd.DataFrame(data1,index=[0])
    dff=pd.concat([df1,df],axis=1)
    dff.to_excel(r'exportowany_wynik.xlsx',header=True)