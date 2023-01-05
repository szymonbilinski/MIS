
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from PyQt5.QtGui import *

import sys

class GetDataFromUserWindow(QWidget):
    def __init__(self):
        super(GetDataFromUserWindow,self).__init__()
        self.setGeometry(200,200,900,500)
        self.setWindowTitle("Enter Data")
        


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
        self.w1=GetDataFromUserWindow()
        self.w1.show()
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
    