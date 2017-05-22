from PyQt5.QtWidgets import QApplication

from Calculator import Calculator

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())