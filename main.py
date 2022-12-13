from PyQt5.QtWidgets import QApplication
import sys
from gui.diabetes_controller import DiabetesController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DiabetesController()

    main_window.show()
    sys.exit(app.exec_())

