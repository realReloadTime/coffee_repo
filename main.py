import sys
import sqlite3

from PyQt5 import uic
help(uic)
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Cappuccino(QMainWindow):
    def __init__(self):
        self.editor_screen = QMainWindow()
        super().__init__()
        uic.loadUi('main.ui', self)
        uic.loadUi('addEditCoffeeForm.ui', self.editor_screen)
        self.data_base = sqlite3.connect('coffee.sqlite')
        self.size_of_base = 0
        all_data = self.data_base.cursor().execute('''SELECT * from main_table''').fetchall()
        for i, row in enumerate(all_data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.size_of_base += 1
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
        self.pushButton.clicked.connect(self.editor)

    def editor(self):
        self.editor_screen.show()
        self.editor_screen.spinBox_id.setValue(self.size_of_base + 1)
        self.editor_screen.comboBox_roast.addItems(('light roast', 'medium roast', 'dark roast', 'italian roast', 'continental roast'))
        self.editor_screen.comboBox_type.addItems(('ground', 'in grains'))
        self.editor_screen.comboBox_volume.addItems(('0.25', '0.3', '0.5', '1'))
        self.editor_screen.comboBox_item.addItems(('ID', 'variety', 'roasting', 'ground/in grains', 'taste', 'cost', 'volume'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cappuccino()
    ex.show()
    sys.exit(app.exec())
