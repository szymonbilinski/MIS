
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import sys
from pyqtgraph import PlotWidget,plot
import pyqtgraph as pg
from initsolution import initsolution
import time
from random import randint



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
routes =[]

class GetDataFromUserWindow(QWidget):
    def __init__(self):
        super(GetDataFromUserWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Enter Data")
        
class GetDataFromExcell(QWidget):
    def __init__(self):
        super(GetDataFromExcell,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Get Data From Excell")
        self.gData()

    def gData(self):
        wb=pd.read_excel('C:/Users/Uzytkownik/Desktop/MIS/MIS/program/dane.xlsx')
        Capacity=(wb[0:1][['Capacity']])
        Available=(wb[0:1][['Available']])
        Time=(wb[0:1][['Time']])
        Czas_Obsługi=wb['Czas Obslugi']
        Okno_czasowe_min=wb['Okno czasowe min']
        Okno_czasowe_max=wb['Okno czasowe max']
        Koordynaty_x=wb['Koordynaty x']
        Koordynaty_y=wb['Koordynaty y']
        Poprzednik_And=wb['Poprzednik AND']
        Poprzednik_Or=wb['Poprzednik OR']
        print(Capacity)
        print(Available)
        print(Time)
        print(Czas_Obsługi)
        print(Okno_czasowe_min)
        print(Okno_czasowe_max)
        print(Koordynaty_x)
        print(Koordynaty_y)
        print(Poprzednik_And)
        print(Poprzednik_Or)
        #print(Capacity)
        #print(Available)
        #print(Time)
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
        print(wezly[0].zapotrzebowanie)
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
        rutes=routes[0]
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

            zmienna_x.append(0)
            zmienna_y.append(0)
            temp_col=randint(5,200)
            pen = pg.mkPen(color=(temp_col, 0, 0))
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
        routes.append(initsolution(wezly,blabla))
        
        print(routes[0])

    def get_data_from_user_button_clicked(self):
        self.w1=EnterDataWindow()
        self.w1.show()
        #self.w1=GetDataFromUserWindow()
        #self.w1.show()
        #self.get_data_from_user.setEnabled(False)

    def read_data_from_csv_button_clicked(self):
        print(blabla[0],blabla[1],blabla[2])
        self.read_data_from_csv.setEnabled(False)

    def show_graphs_and_values_button_clicked(self):
        #self.show_graphs_and_values.setEnabled(False)
        self.w1=ShowGraph()
        self.w1.show()

    def export_data_to_csv_button_clicked(self):
        self.export_data_to_csv.setEnabled(False)



 
def Window():
    app=QApplication(sys.argv)
    win = MainWindow()

    #wyswietlanie okna
    win.show()
    sys.exit(app.exec_())
Window()
    