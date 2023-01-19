import pandas as pd





def ex_wyniku(routes):
    wynik=21
    czas_wyjazdu=[6,6]
    czas_przyjazdu=[10,10]
    laczny_czas=[4,4]
    laczne_zapotrzebowanie=[]
    nazwy_wezlow_na_trasie=[]
    for i in range(len(routes)):
        nazwy_wezlow_na_trasie.append('')
        laczne_zapotrzebowanie.append(0)
        for j in range(len(routes[i])):
            nazwy_wezlow_na_trasie[i]+=routes[i][j].nazwa_wezla
            laczne_zapotrzebowanie[i]+=routes[i][j].zapotrzebowanie
        
    data1={'wynik':wynik}

    data={
          'wezly':nazwy_wezlow_na_trasie,
          'godzina wyjazdu':czas_wyjazdu,
          'godzina przyjazdu':czas_przyjazdu,
          'laczny czas':laczny_czas,
          'zapotrzebowanie':laczne_zapotrzebowanie
          }
    # print(data)
    
    df=pd.DataFrame(data)
    df1=pd.DataFrame(data1,index=[0])
    dff=pd.concat([df1,df],axis=1)
    dff.to_excel(r'exportowany_wynik.xlsx',header=True)