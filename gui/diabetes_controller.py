from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.diabetes_gui_view import Ui_MainWindow
from service.nnc import nnc_display
from service.pca import pca_display
from service.lda import lda_display


COLUMN_NAMES = ['HighBP','HighChol','CholCheck','BMI','Smoker','Stroke','HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','HvyAlcoholConsump',
                    'AnyHealthcare','NoDocbcCost','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Income']

DIMENSIONS = ([str(i) for i in range(2, 21)])

class DiabetesController(QMainWindow):
    def __init__(self)-> None:
        super(DiabetesController, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.nnc_fields_1.addItems(COLUMN_NAMES)
        self.ui.nnc_fields_2.addItems(COLUMN_NAMES)
        self.ui.pca_dimensions.addItems(DIMENSIONS)

        self.__connect_button()


    def __connect_button(self):
        self.ui.nnc_btn.clicked.connect(self.nnc_display)
        self.ui.pca_btn.clicked.connect(self.pca_display)
        self.ui.lda_btn.clicked.connect(self.lda_display)


    def lda_display(self):
        lda_display()


    def pca_display(self):
        dimensions = self.ui.pca_dimensions.currentIndex() + 2
        first_field = self.ui.field_1.value()
        second_field = self.ui.field_2.value()

        if dimensions <= first_field or dimensions <= second_field:
            QMessageBox.critical(self, 'Error', 'Field value cant be greater than dimension', QMessageBox.Ok)
            return

        if second_field == first_field:
            QMessageBox.critical(self, 'Error', 'Fields cant have same value', QMessageBox.Ok)
            return

        pca_display(dimensions, first_field, second_field)


    def nnc_display(self):
        first_field = self.ui.nnc_fields_1.currentText()
        second_field = self.ui.nnc_fields_2.currentText()

        if first_field == second_field:
            QMessageBox.critical(self, 'Error', 'Fields must be different value', QMessageBox.Ok)
            return

        nnc_display(first_field, second_field)