
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import sys
from pyqtgraph import PlotWidget,plot
import pyqtgraph as pg
from initsolution import initsolution
from Perturbation_Procedure import pert_proc
from LocalSearch import localsearchF
import time
from random import randint
from export_wyniku import ex_wyniku
from calc_solution import calculate_solution

# capacity=None
# available=None
# time=None




class costam():
    def __init__(self,capacity,available,time):
        self.capacity=capacity
        self.available=available
        self.time=time

class Node():
    def __init__(self,zapotrzebowanie,czas_obslugi,okno_czasowe_min,okno_czasowe_max,koordynat_x,koordynat_y,ANDpre,ORpre,nazwa_wezla=""):
        self.nazwa_wezla=nazwa_wezla
        self.zapotrzebowanie = zapotrzebowanie
        self.czas_obslugi = czas_obslugi
        self.okno_czasowe_min = okno_czasowe_min
        self.okno_czasowe_max = okno_czasowe_max
        self.koordynat_x = koordynat_x
        self.koordynat_y = koordynat_y
        self.ANDpre = ANDpre
        self.ORpre = ORpre


wezly = []
blabla = []
routes_koncowy=[]

class GetDataFromUserWindow(QWidget):
    def __init__(self):
        super(GetDataFromUserWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Enter Data")
        
class ExportDataToExcell(QWidget):
    def __init__(self):
        super(ExportDataToExcell,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Export Data to Excell")
        self.ExpData()
    def ExpData(self):
        self.tekst = QtWidgets.QLabel(self)
        self.tekst.setText("Dane zostały poprawnie wyeksportowane")
        self.tekst.setFont(QFont('Arial', 13))
        self.tekst.move(300,100)
        self.tekst.adjustSize()
        #for i in range(len(route)):
        #for j in range(len(route[i])):
        #    print(route[i][j].nazwa_wezla)

        
        capacity=blabla[0]
        available=blabla[1]
        time=blabla[2]
        print(capacity, available, time)
        #df=pd.DataFrame(blabla)
        #dd=pd.DataFrame(wezly)
        #print(df)
        #print(dd)
        #dd.to_excel('C:/Users/Uzytkownik/Desktop/MIS/MIS/program/exportowane.xlsx', sheet_name='Dane klientów')
        #df.to_excel('C:/Users/Uzytkownik/Desktop/MIS/MIS/program/exportowane.xlsx', sheet_name='Dane Pojazdów')
        Zapotrzebowanie=[]
        Czas_Obsługi=[]
        Okno_czasowe_min=[]
        Okno_czasowe_max=[]
        Koordynaty_x=[]
        Koordynaty_y=[]
        Poprzednik_And=[]
        Poprzednik_Or=[]
        for i in range(len(wezly)):
            Zapotrzebowanie.append(wezly[i].zapotrzebowanie)
            Czas_Obsługi.append(wezly[i].czas_obslugi)
            Okno_czasowe_min.append(wezly[i].okno_czasowe_min)
            Okno_czasowe_max.append(wezly[i].okno_czasowe_max)
            Koordynaty_x.append(wezly[i].koordynat_x)
            Koordynaty_y.append(wezly[i].koordynat_y)
            Poprzednik_And.append(wezly[i].ANDpre)
            Poprzednik_Or.append(wezly[i].ORpre)
        #print(Zapotrzebowanie, Czas_Obsługi, Okno_czasowe_min, Okno_czasowe_max, Koordynaty_x, Koordynaty_y, Poprzednik_And, Poprzednik_Or)

        slownik={'Capacity':[capacity],'Available':[available],'Time':[time],'Zapotrzebowanie':[Zapotrzebowanie],'Czas Obslugi':[Czas_Obsługi],'Okno czasowe min':[Okno_czasowe_min],'Okno czasowe max':[Okno_czasowe_max],'Koordynaty x':[Koordynaty_x],'Koordynaty y':[Koordynaty_y],'Poprzednik AND':[Poprzednik_And],'Poprzednik OR':[Poprzednik_Or]}
        df=pd.DataFrame(slownik)
        excel_url='exportowane.xlsx'
        df.to_excel(excel_url, sheet_name='Dane eksportowane')
        

class GetDataFromExcell(QWidget):
    def __init__(self):
        super(GetDataFromExcell,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Get Data From Excell")
        self.gData()

    def gData(self):
        self.tekst = QtWidgets.QLabel(self)
        self.tekst.setText("Dane zostały wczytane poprawnie")
        self.tekst.setFont(QFont('Arial', 13))
        self.tekst.move(300,100)
        self.tekst.adjustSize()
        wb=pd.read_excel('dane.xlsx')
    
        Capacity=int(wb.at[0,'Capacity'])
        Available=int(wb.at[0,'Available'])
        Time=int(wb.at[0,'Time'])
        #self.obiekt=costam(Capacity, Available, Time)
        blabla.clear()
        blabla.append(Capacity)
        blabla.append(Available)
        blabla.append(Time)
        print(blabla)

        zmienna=wb['Zapotrzebowanie']
        licznik=zmienna.size
        wezly.clear()
        for x in range(licznik):
            # Zapotrzebowanie.append(wb.at[x,'Zapotrzebowanie'])     
            # Czas_Obsługi.append(wb.at[x,'Czas Obslugi'])
            # Okno_czasowe_min.append(wb.at[x,'Okno czasowe min'])
            # Okno_czasowe_max.append(wb.at[x,'Okno czasowe max'])
            # Koordynaty_x.append(wb.at[x,'Koordynaty x'])
            # Koordynaty_y.append(wb.at[x,'Koordynaty y'])
            # Poprzednik_And.append(wb.at[x,'Poprzednik AND'])
            
            # Poprzednik_Or.append(wb.at[x,'Poprzednik OR'])
            wezly.append(Node(float(wb.at[x,'Zapotrzebowanie']),float(wb.at[x,'Czas Obslugi']),float(wb.at[x,'Okno czasowe min']),float(wb.at[x,'Okno czasowe max']),float(wb.at[x,'Koordynaty x']),float(wb.at[x,'Koordynaty y']),str(wb.at[x,'Poprzednik AND']),str(wb.at[x,'Poprzednik OR'])))
            if wezly[x].ANDpre =="nan":
                wezly[x].ANDpre=""
            if wezly[x].ORpre=="nan":
                wezly[x].ORpre=""

            #self.obiekt1=Node(Zapotrzebowanie,Czas_Obsługi,Okno_czasowe_min,Okno_czasowe_max,Koordynaty_x,Koordynaty_y, Poprzednik_And, Poprzednik_Or )
        print("and",wezly[1].ANDpre)
    
class EnterDataWindow(QMainWindow):
    def __init__(self):
        super(EnterDataWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Wprowadzanie danych")
        self.initData()

    def initData(self):
        self.MainTitleLabel = QtWidgets.QLabel(self)
        self.MainTitleLabel.setText("Wprowadz dane")
        self.MainTitleLabel.setFont(QFont('Arial', 16))
        self.MainTitleLabel.move(350,20)
        self.MainTitleLabel.adjustSize()

        self.textbox = QLineEdit(self)
        self.textbox.move(500, 80)
        self.textbox.resize(200,40)
    
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(500, 180)
        self.textbox1.resize(200,40)
    
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(500, 280)
        self.textbox2.resize(200,40)

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("Pojemność pojazdów")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(250,100)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Dostępna liczba pojazdów")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(250,200)
        self.Availability.adjustSize()
 
        self.Time = QtWidgets.QLabel(self)
        self.Time.setText("Czas podróży w ciągu dnia")
        self.Time.setFont(QFont('Arial', 13))
        self.Time.move(250,300)
        self.Time.adjustSize()

        self.go_back_button = QtWidgets.QPushButton(self)
        self.go_back_button.setText("Wstecz")
        self.go_back_button.move(0,0)
        self.go_back_button.clicked.connect(self.go_back_button_clicked)

        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText("zapisz")
        self.save_button.move(800,0)
        self.save_button.clicked.connect(self.save_button_button_clicked)

        self.add_client_button = QtWidgets.QPushButton(self)
        self.add_client_button.setText("Dodaj klienta")
        self.add_client_button.setFont(QFont('Arial', 16))
        self.add_client_button.setGeometry(330,390,230,100)
        #self.add_client_button.move(370,400)
        self.add_client_button.clicked.connect(self.add_client_button_clicked)

    def go_back_button_clicked(self):
        self.close()

    def save_button_button_clicked(self):
        # capacity=int(self.textbox.text())
        # available=int(self.textbox1.text())
        # time=int(self.textbox2.text())
        blabla.append(int(self.textbox.text()))
        blabla.append(int(self.textbox1.text()))
        blabla.append(int(self.textbox2.text()))
        #print(capacity, available, time)


    def add_client_button_clicked(self):
        #self.add_client_button.setEnabled(False)
        
        
        self.w2=EnterClientWindow()
        self.w2.show()

class EnterClientWindow(QMainWindow):
    def __init__(self):
        super(EnterClientWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Dodaj klienta")
        self.initClient()

    def initClient(self):
        self.MainTitleLabel = QtWidgets.QLabel(self)
        self.MainTitleLabel.setText("Wprowadz dane węzła")
        self.MainTitleLabel.setFont(QFont('Arial', 16))
        self.MainTitleLabel.move(350,20)
        self.MainTitleLabel.adjustSize()

        self.go_back_button = QtWidgets.QPushButton(self)
        self.go_back_button.setText("Wstecz")
        self.go_back_button.move(0,0)
        self.go_back_button.clicked.connect(self.go_back_button_clicked)

        self.continue_enterData_button = QtWidgets.QPushButton(self)
        self.continue_enterData_button.setText("Kontynuuj")
        self.continue_enterData_button.move(800,0)
        self.continue_enterData_button.clicked.connect(self.continue_enterData_button_clicked)

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("Zapotrzebowanie")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(250,70)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Czas obsługi")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(250,130)
        self.Availability.adjustSize()

        self.textboxZ = QLineEdit(self)
        self.textboxZ.move(500, 60)
        self.textboxZ.resize(200,40)
    
        self.textboxC = QLineEdit(self)
        self.textboxC.move(500, 120)
        self.textboxC.resize(200,40)

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("Okno czasowe")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(250,200)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Koordynaty")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(250,270)
        self.Availability.adjustSize()

        self.And = QtWidgets.QLabel(self)
        self.And.setText("Poprzednik AND")
        self.And.setFont(QFont('Arial', 13))
        self.And.move(250,340)
        self.And.adjustSize()
        
        self.Or = QtWidgets.QLabel(self)
        self.Or.setText("Poprzednik OR")
        self.Or.setFont(QFont('Arial', 13))
        self.Or.move(250,410)
        self.Or.adjustSize()

        self.textboxA = QLineEdit(self)
        self.textboxA.move(500, 330)
        self.textboxA.resize(200,40)
    
        self.textboxO = QLineEdit(self)
        self.textboxO.move(500, 400)
        self.textboxO.resize(200,40)

        self.Min = QtWidgets.QLabel(self)
        self.Min.setText("Min:")
        self.Min.setFont(QFont('Arial', 13))
        self.Min.move(500,200)
        self.Min.adjustSize()
        
        self.Max = QtWidgets.QLabel(self)
        self.Max.setText("Max:")
        self.Max.setFont(QFont('Arial', 13))
        self.Max.move(600,200)
        self.Max.adjustSize()

        self.textboxMa = QLineEdit(self)
        self.textboxMa.move(550, 195)
        self.textboxMa.resize(40,30)
    
        self.textboxMin = QLineEdit(self)
        self.textboxMin.move(650, 195)
        self.textboxMin.resize(40,30)

        self.X = QtWidgets.QLabel(self)
        self.X.setText("X:")
        self.X.setFont(QFont('Arial', 13))
        self.X.move(500,270)
        self.X.adjustSize()
        
        self.Y = QtWidgets.QLabel(self)
        self.Y.setText("Y:")
        self.Y.setFont(QFont('Arial', 13))
        self.Y.move(600,270)
        self.Y.adjustSize()

        self.textboxX = QLineEdit(self)
        self.textboxX.move(550, 260)
        self.textboxX.resize(40,30)
    
        self.textboxY = QLineEdit(self)
        self.textboxY.move(650, 260)
        self.textboxY.resize(40,30)
    def go_back_button_clicked(self):
        #self.continue_enterData_button.setEnabled(False)
        self.close()
    def continue_enterData_button_clicked(self):
        #self.go_back_button.setEnabled(False)
        wezly.append(Node(int(self.textboxZ.text()),int(self.textboxC.text()),int(self.textboxMin.text()),int(self.textboxMa.text()),int(self.textboxX.text()),int(self.textboxY.text()),self.textboxA.text(),self.textboxO.text()))
        print(wezly[0].ANDpre)
        #Zapotrzebowanie.append(self.textboxZ.text())
        #Czas_Obsługi.append(self.textboxC.text())
        #Okno_czasowe_min.append(self.textboxMin.text())
        #Okno_czasowe_max.append(self.textboxMa.text())
        #Koordynaty_x.append(self.textboxX.text())
        #Koordynaty_y.append(self.textboxY.text())
        #Poprzednik_And.append(self.textboxA.text())
        #Poprzednik_Or.append(self.textboxO.text())
        print(wezly)
        self.close()

class nodes_table(QMainWindow):
    def __init__(self):
        super(nodes_table,self).__init__
        #wyswietlanie tabeli

class ShowGraph(QMainWindow):
    def __init__(self):
        super(ShowGraph,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Metody Inzynierii Systemow")
        self.showgraphwindow()

    def showgraphwindow(self):
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        rutes=[]
        rutes=routes_koncowy[0]
        #self.graphWidget.setBackground('w')

        for i in range(len(rutes)):
            zmienna_x=[]
            zmienna_y=[]
            zmienna_x.append(0)
            zmienna_y.append(0)
            #time.sleep(3)
            for j in range(len(rutes[i])):
                zmienna_x.append(rutes[i][j].koordynat_x)
                zmienna_y.append(rutes[i][j].koordynat_y)
                print(rutes[i][j].nazwa_wezla)

            zmienna_x.append(0)
            zmienna_y.append(0)
            temp_col=randint(50,200)
            temp_col2=randint(50,200)
            temp_col3=randint(50,200)
            pen = pg.mkPen(color=(temp_col, temp_col2, temp_col3))
            self.graphWidget.plot(zmienna_x,zmienna_y,pen=pen,symbol='+')
        # print("rzeczy ",routes[0].koordynat_x,routes[0].koordynat_y)
        print(rutes)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Metody Inzynierii Systemow")
        self.initUI()

    def initUI(self):
        self.MainTitleLabel = QtWidgets.QLabel(self)
        self.MainTitleLabel.setText("A hybrid algorithm for the CRP with AND/OR Precedence Constraints and time windows")
        self.MainTitleLabel.setFont(QFont('Arial', 13))
        self.MainTitleLabel.move(130,100)
        self.MainTitleLabel.adjustSize()

        self.start_simulation_button = QtWidgets.QPushButton(self)
        self.start_simulation_button.setText("Start")
        self.start_simulation_button.move(800,0)
        self.start_simulation_button.clicked.connect(self.start_simulation_button_clicked)

        self.get_data_from_user = QtWidgets.QPushButton(self)
        self.get_data_from_user.setText("Input Values")
        self.get_data_from_user.setGeometry(125,200,250,100)
        self.get_data_from_user.clicked.connect(self.get_data_from_user_button_clicked)

        self.read_data_from_csv = QtWidgets.QPushButton(self)
        self.read_data_from_csv.setText("Load Data")
        self.read_data_from_csv.setGeometry(125,350,250,100)
        self.read_data_from_csv.clicked.connect(self.read_data_from_csv_button_clicked)

        self.show_graphs_and_values = QtWidgets.QPushButton(self)
        self.show_graphs_and_values.setText("Show Graphs")
        self.show_graphs_and_values.setGeometry(525,200,250,100)
        self.show_graphs_and_values.clicked.connect(self.show_graphs_and_values_button_clicked)

        self.export_data_to_csv = QtWidgets.QPushButton(self)
        self.export_data_to_csv.setText("Export Data")
        self.export_data_to_csv.setGeometry(525,350,250,100)
        self.export_data_to_csv.clicked.connect(self.export_data_to_csv_button_clicked)

    def start_simulation_button_clicked(self):
        #self.start_simulation_button.setEnabled(False)
        routes =[]
        stack =[]
        temp_routes=[]
        temp_routes.append(initsolution(wezly,blabla))
        routes=temp_routes[0].copy()
        # routes_koncowy.append(routes.copy())
        # self.w69=ShowGraph()
        # self.w69.show()
        # routes.clear()
        # temp_pert=pert_proc(routes[0],blabla)
        
        # LocalSearch1=localsearchF(temp_pert,blabla)
        # print("routes",LocalSearch1[0])
        # print("stack",LocalSearch1[1])
        # print("cost",LocalSearch1[2])
        # stack=temp_pert[1]
        #print("routessss",temp_pert[0])
        #print("stackkkk",temp_pert[1])
        #print(routes[0])
        Max_iter=120
        S_best=calculate_solution(routes)    #do tej zmiennej ma isc najlepsze teraz rozwiazanie
        New_S_best=calculate_solution(routes) #do tej zmiennej nowe rozwiazanie ma isc 
        iter=1
        while(iter<Max_iter):
            temp_pert=pert_proc(routes,blabla)
            routes.clear()
            stack.clear()
            
            # print("routessss",routes)
            # print("stackkkk",stack)
            LocalSearch1=localsearchF(temp_pert,blabla,S_best)
            if(len(LocalSearch1)==3):
                routes=LocalSearch1[0].copy()
                stack=LocalSearch1[2].copy()
                New_S_best=LocalSearch1[1]
                print("routes",LocalSearch1[0])
                print("stack",LocalSearch1[2])
            else:
                routes=LocalSearch1[0].copy()
                New_S_best=LocalSearch1[1]
                print("routes",LocalSearch1[0])
                # print("stack",LocalSearch1[2])
            # print("cost",LocalSearch1[1])
            print("len stack",len(stack))
            if(len(stack)>0):
                print("nbveh",blabla[1])
                print("lenroutes",len(routes))
                if(blabla[1]>len(routes)):
                    print("staczek",stack)
                    
                    routes.append(stack.copy())
                    
                    print("roteeeeeeee",routes)
                    stack.clear()
                    print("routesssssewaew",routes)
                    print("staczek2222",stack)
                    temp_pert.clear()
                    temp_pert=[routes,stack]
                    print("tempeprokeappr",temp_pert)
                    LocalSearch1=localsearchF(temp_pert,blabla,S_best)
                    if(len(LocalSearch1)==3):
                        routes=LocalSearch1[0].copy()
                        stack=LocalSearch1[2].copy()
                        New_S_best=LocalSearch1[1]
                    else:
                        routes=LocalSearch1[0].copy()
                        New_S_best=LocalSearch1[1]
                    print("routessssssssssssssssssssssss ",iter,routes)
                else:
                    temp_pert=pert_proc(routes,blabla)
                    routes.clear()
                    stack.clear()
                    routes=temp_pert[0].copy()
                    stack=temp_pert[1].copy()
                    print("routessssssssssssssssssssssssss ",iter,routes)

            if(S_best>New_S_best):
                S_best=New_S_best
            iter+=1
        # stack=temp_pert[1]
        # print("routessss",temp_pert[0])
        # print("stackkkk",temp_pert[1])
        # print(routes)
        #export wynikow
        routes_koncowy.append(routes)
        ex_wyniku(routes,S_best)              #do odkomentowania i wrzucenia wynikow wszystich

    def get_data_from_user_button_clicked(self):
        self.w1=EnterDataWindow()
        self.w1.show()
        #self.w1=GetDataFromUserWindow()
        #self.w1.show()
        #self.get_data_from_user.setEnabled(False)

    def read_data_from_csv_button_clicked(self):
        self.w3=GetDataFromExcell()
        self.w3.show()
        #print(blabla[0],blabla[1],blabla[2])
        self.read_data_from_csv.setEnabled(False)

    def show_graphs_and_values_button_clicked(self):
        #self.show_graphs_and_values.setEnabled(False)
        self.w1=ShowGraph()
        self.w1.show()

    def export_data_to_csv_button_clicked(self):
        self.w4=ExportDataToExcell()
        self.w4.show()



 
def Window():
    app=QApplication(sys.argv)
    win = MainWindow()

    #wyswietlanie okna
    win.show()
    sys.exit(app.exec_())
Window()
    