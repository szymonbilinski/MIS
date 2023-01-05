from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
def Window():
    app=QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,900,500)
    win.window
    win.show()
    sys.exit(app.exec_())

 
print('tak')
window = Window()
    