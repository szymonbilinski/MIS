
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class GetDataFromUserWindow(QWidget):
    def __init__(self):
        super(GetDataFromUserWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Enter Data")
        

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
    
        self.textbox = QLineEdit(self)
        self.textbox.move(500, 180)
        self.textbox.resize(200,40)
    
        self.textbox = QLineEdit(self)
        self.textbox.move(500, 280)
        self.textbox.resize(200,40)

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

        self.add_client_button = QtWidgets.QPushButton(self)
        self.add_client_button.setText("Dodaj klienta")
        self.add_client_button.setFont(QFont('Arial', 16))
        self.add_client_button.setGeometry(330,390,230,100)
        #self.add_client_button.move(370,400)
        self.add_client_button.clicked.connect(self.add_client_button_clicked)
    def go_back_button_clicked(self):
        self.close()
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

        self.textbox = QLineEdit(self)
        self.textbox.move(500, 60)
        self.textbox.resize(200,40)
    
        self.textbox = QLineEdit(self)
        self.textbox.move(500, 120)
        self.textbox.resize(200,40)

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

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("Poprzednik AND")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(250,340)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Poprzednik OR")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(250,410)
        self.Availability.adjustSize()

        self.textbox = QLineEdit(self)
        self.textbox.move(500, 330)
        self.textbox.resize(200,40)
    
        self.textbox = QLineEdit(self)
        self.textbox.move(500, 400)
        self.textbox.resize(200,40)

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("Min:")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(500,200)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Max:")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(600,200)
        self.Availability.adjustSize()

        self.textbox = QLineEdit(self)
        self.textbox.move(550, 195)
        self.textbox.resize(40,30)
    
        self.textbox = QLineEdit(self)
        self.textbox.move(650, 195)
        self.textbox.resize(40,30)

        self.Capacity = QtWidgets.QLabel(self)
        self.Capacity.setText("X:")
        self.Capacity.setFont(QFont('Arial', 13))
        self.Capacity.move(500,270)
        self.Capacity.adjustSize()
        
        self.Availability = QtWidgets.QLabel(self)
        self.Availability.setText("Y:")
        self.Availability.setFont(QFont('Arial', 13))
        self.Availability.move(600,270)
        self.Availability.adjustSize()

        self.textbox = QLineEdit(self)
        self.textbox.move(550, 260)
        self.textbox.resize(40,30)
    
        self.textbox = QLineEdit(self)
        self.textbox.move(650, 260)
        self.textbox.resize(40,30)
    def go_back_button_clicked(self):
        #self.continue_enterData_button.setEnabled(False)
        self.close()
    def continue_enterData_button_clicked(self):
        #self.go_back_button.setEnabled(False)
        self.close()
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
        self.MainTitleLabel.move(30,100)
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
        self.start_simulation_button.setEnabled(False)

    def get_data_from_user_button_clicked(self):
        self.w1=EnterDataWindow()
        self.w1.show()
        #self.w1=GetDataFromUserWindow()
        #self.w1.show()
        #self.get_data_from_user.setEnabled(False)

    def read_data_from_csv_button_clicked(self):
        self.read_data_from_csv.setEnabled(False)

    def show_graphs_and_values_button_clicked(self):
        self.show_graphs_and_values.setEnabled(False)

    def export_data_to_csv_button_clicked(self):
        self.export_data_to_csv.setEnabled(False)



 
def Window():
    app=QApplication(sys.argv)
    win = MainWindow()

    #wyswietlanie okna
    win.show()
    sys.exit(app.exec_())
Window()
    