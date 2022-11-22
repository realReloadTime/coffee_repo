import sqlite3
import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget


class Espresso(QMainWindow):
    def __init__(self):
        super(Espresso, self).__init__()
        uic.loadUi('main.ui', self)
        self.data_base = sqlite3.connect('coffee.sqlite')
        all_data = self.data_base.cursor().execute('''SELECT * from main_table''').fetchall()
        for i, row in enumerate(all_data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 2:
                    elem = self.data_base.cursor().execute('''SELECT roasting_name FROM roasting WHERE id=(?)''',
                                                           (elem,)).fetchall()[0][0]
                if j == 3:
                    elem = self.data_base.cursor().execute('''SELECT type FROM type_of_coffee WHERE id=(?)''',
                                                           (elem,)).fetchall()[0][0]
                if j == 6:
                    elem = str(self.data_base.cursor().execute('''SELECT volume_size FROM volume WHERE id=(?)''',
                                                           (elem,)).fetchall()[0][0]) + 'л'
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Espresso()
    ex.show()
    sys.exit(app.exec())
