# Импортируем наш интерфейс из файла
from datetime import timedelta

from PyQt5.QtWidgets import QMessageBox, QWidget

import add_report_row_to_db
from mainWindow import *
import sys


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.myFunction)
        self.ui.dateEdit_4.dateChanged.connect(self.delta_days_in_bt)
        self.ui.dateEdit_5.dateChanged.connect(self.delta_days_in_bt)
        self.ui.dateEdit_4.dateChanged.connect(self.salary_per_bt)
        self.ui.dateEdit_5.dateChanged.connect(self.salary_per_bt)
        self.ui.doubleSpinBox.valueChanged.connect(self.salary_per_bt)
        self.ui.comboBox.activated[str].connect(self.onActivated1)
        self.ui.comboBox_2.activated[str].connect(self.onActivated2)

    def onActivated1(self, str2):
        self.ui.comboBox_2.clear()
        list2 = Filling_comboBox.filter_comboBox_dep_where("db.db", "report", "name_of_reporter", "code_of_report",
                                                           str2)
        for elem2 in list2:
            self.ui.comboBox_2.addItem(elem2)
        self.ui.comboBox_2.addItem("--All--")

    def onActivated2(self, str1):
        self.ui.comboBox.clear()
        list2 = Filling_comboBox.filter_comboBox_dep_where("db.db", "report", "code_of_report", "name_of_reporter",
                                                           str1)
        for elem2 in list2:
            self.ui.comboBox.addItem(elem2)
        self.ui.comboBox.addItem("--All--")

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def myFunction(self):

        if self.ui.comboBox.currentText() != "--All--" and self.ui.comboBox_2.currentText() != "--All--":

            date_of_report = self.ui.dateEdit_3.date().toPyDate().strftime('%d.%m.%Y')
            code_of_report = self.ui.comboBox.currentText()
            name_of_reporter = self.ui.comboBox_2.currentText()
            date_of_start_bt = self.ui.dateEdit_4.date().toPyDate().strftime('%d.%m.%Y')
            date_of_end_bt = self.ui.dateEdit_5.date().toPyDate().strftime('%d.%m.%Y')

            name_of_payment = self.ui.lineEdit.text()
            sum_of_payment = self.ui.doubleSpinBox_2.value()
            date_of_payment = self.ui.dateEdit_6.date().toPyDate().strftime('%d.%m.%Y')
            sum_hotel = self.ui.checkBox.isChecked()
            sum_from_credit = self.ui.checkBox_2.isChecked()

            days_in_bt = self.delta_days_in_bt()
            salary_per_day = self.ui.doubleSpinBox.value()
            salary_per_bt = self.ui.label_16.text()
            sum_total = sum_of_payment
            sum_word = self.ui.lineEdit_2.text()

            add_report_row_to_db.add_rep_row_to_db(date_of_report, code_of_report, name_of_reporter, date_of_start_bt, date_of_end_bt, sum_total, sum_word)
            add_report_row_to_db.add_pay_row_to_db(days_in_bt, salary_per_day, salary_per_bt, name_of_payment, sum_of_payment, date_of_payment, sum_hotel, sum_from_credit)

            w = QWidget()
            w.move(600, 350)
            msg = QMessageBox.information(w, "Message", "Report " + code_of_report + " is saved!")

        else:

            w = QWidget()
            w.move(600, 350)
            msg1 = QMessageBox.information(w, "Message", "Error during filling!")



    def salary_per_bt(self):
        salary_per_bt = float(self.delta_days_in_bt()) * self.ui.doubleSpinBox.value()
        self.ui.label_16.setText(str(salary_per_bt))
        return salary_per_bt

    def delta_days_in_bt(self):
        delta_days = (self.ui.dateEdit_5.date().toPyDate() - self.ui.dateEdit_4.date().toPyDate() + timedelta(days=1))
        delta_days_int = strfdelta(delta_days, "{days}")
        self.ui.label_17.setText(delta_days_int)
        return delta_days_int

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())