from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.diabetes_gui_view import Ui_MainWindow
from service.nnc import nnc_display
from service.pca import pca_display
from service.lda import lda_display
from service.predictor import predict


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
        self.__init_predict_boxes()


    def __init_predict_boxes(self):
        self.ui.age_box.addItems([str(i) for i in range(1, 14)])
        self.ui.sex_box.addItems(['Male', 'Female'])
        self.ui.income_box.addItems([str(i) for i in range(1, 9)])
        self.ui.gen_hlth_box.addItems([str(i) for i in range(1, 6)])
        self.ui.ment_hlth_box.addItems([str(i) for i in range(1, 31)])
        self.ui.phys_hlth_box.addItems([str(i) for i in range(1, 31)])
        self.ui.education_box.addItems([str(i) for i in range(1, 7)])
        self.ui.bmi_box.addItems([str(i) for i in range(12, 99)])


    def __connect_button(self):
        self.ui.nnc_btn.clicked.connect(self.nnc_display)
        self.ui.pca_btn.clicked.connect(self.pca_display)
        self.ui.lda_btn.clicked.connect(self.lda_display)
        self.ui.predict_btn.clicked.connect(self.predict)


    def predict(self):
        age = int(self.ui.age_box.currentText())
        gen_hlth = int(self.ui.gen_hlth_box.currentText())
        ment_hlth = int(self.ui.ment_hlth_box.currentText())
        phys_hlth = int(self.ui.phys_hlth_box.currentText())
        income = int(self.ui.income_box.currentText())
        education = int(self.ui.education_box.currentText())
        sex = self.ui.sex_box.currentIndex()
        bmi = int(self.ui.bmi_box.currentText())
        high_bp = 1.0 if self.ui.high_bp_yes.isChecked() else 0.0
        high_chol = 1.0 if self.ui.high_chol_yes.isChecked() else 0.0
        chol_check = 1.0 if self.ui.chol_check_yes.isChecked() else 0.0
        smoker = 1.0 if self.ui.smoker_yes.isChecked() else 0.0
        heart_attack = 1.0 if self.ui.heart_attak_yes.isChecked() else 0.0
        phys_activity = 1.0 if self.ui.phys_activity_yes.isChecked() else 0.0
        fruits = 1.0 if self.ui.fruits_yes.isChecked() else 0.0
        veggies = 1.0 if self.ui.veggies_yes.isChecked() else 0.0
        alcohol = 1.0 if self.ui.alcohol_yes.isChecked() else 0.0
        healthcare = 1.0 if self.ui.heathcare_yes.isChecked() else 0.0
        no_cost_doctor = 1.0 if self.ui.doc_cost_yes.isChecked() else 0.0
        diff_walk = 1.0 if self.ui.diff_walk_yes.isChecked() else 0.0
        stroke = 1.0 if self.ui.stroke_yes.isChecked() else 0.0

        data_frame_row = {'HighBP': high_bp,'HighChol': high_chol,'CholCheck': chol_check,'BMI': bmi,'Smoker': smoker,'Stroke': stroke,'HeartDiseaseorAttack': heart_attack,
                            'PhysActivity': phys_activity,'Fruits': fruits,'Veggies': veggies,'HvyAlcoholConsump': alcohol,
                            'AnyHealthcare': healthcare,'NoDocbcCost': no_cost_doctor,'GenHlth': gen_hlth,'MentHlth': ment_hlth,
                            'PhysHlth': phys_hlth,'DiffWalk': diff_walk,'Sex': sex,'Age': age,'Education': education,'Income': income}

        prediction = predict(data_frame_row)

        print(f'Prediction: {prediction}')


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