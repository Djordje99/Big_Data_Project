from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.diabetes_gui_view import Ui_MainWindow
from service.nnc import nnc_display
from service.pca import pca_display


COLUMN_NAMES = ['HighBP','HighChol','CholCheck','BMI','Smoker','Stroke','HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Income']


class DiabetesController(QMainWindow):
    def __init__(self)-> None:
        super(DiabetesController, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.nnc_fields_1.addItems(COLUMN_NAMES)
        self.ui.nnc_fields_2.addItems(COLUMN_NAMES)

        self.__connect_button()


    def __connect_button(self):
        self.ui.nnc_btn.clicked.connect(self.nnc_display)
        self.ui.pca_btn.clicked.connect(self.pca_display)


    def pca_display(self):
        pca_display()


    def nnc_display(self):
        first_field = self.ui.nnc_fields_1.currentText()
        second_field = self.ui.nnc_fields_2.currentText()

        if first_field == second_field:
            QMessageBox.critical(self, 'Error', 'Fields must be different value', QMessageBox.Ok)
            return

        nnc_display(first_field, second_field)