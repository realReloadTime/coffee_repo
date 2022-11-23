import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from main import Ui_MainWindow as MainForm
from addEditCoffeeForm import Ui_MainWindow as EditForm


class Cappuccino(QMainWindow, MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.editor_screen = EditDelete()
        self.data_base = sqlite3.connect('data\coffee.sqlite')
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
        self.editor_screen.comboBox_roast.addItems(('light roast', 'medium roast',
                                                    'dark roast', 'italian roast', 'continental roast'))
        self.editor_screen.comboBox_type.addItems(('ground', 'in grains'))
        self.editor_screen.comboBox_volume.addItems(('0.25', '0.3', '0.5', '1'))
        self.editor_screen.comboBox_item.addItems(('ID', 'variety', 'roasting',
                                                   'ground/in grains', 'taste', 'cost', 'volume'))
        self.editor_screen.pushButton_add.clicked.connect(self.add_or_edit)
        self.editor_screen.pushButton_delete.clicked.connect(self.delete_record)

    def add_or_edit(self):
        self.editor_screen.statusBar().hide()
        try:
            volume_size = self.data_base.cursor().execute('''SELECT ID FROM volume WHERE volume_size = (?)''',
                                                          (float(self.editor_screen.comboBox_volume.currentText()),
                                                           )).fetchall()[0][0]
            if self.size_of_base < self.editor_screen.spinBox_id.value():
                self.data_base.cursor().execute('''INSERT INTO main_table VALUES(?, ?, ?, ?, ?, ?, ?)''',
                                                (self.editor_screen.spinBox_id.value(),
                                                 self.editor_screen.lineEdit_name.text().strip(),
                                                 self.editor_screen.comboBox_roast.currentIndex() + 1,
                                                 self.editor_screen.comboBox_type.currentIndex() + 1,
                                                 self.editor_screen.lineEdit_taste.text().strip(),
                                                 float(self.editor_screen.lineEdit_cost.text().strip()),
                                                 float(volume_size)))
            elif self.size_of_base >= self.editor_screen.spinBox_id.value():
                self.data_base.cursor().execute('''UPDATE main_table
                                                   SET variety = ?, 
                                                       roasting = ?,
                                                       "ground/in grains" = ?,
                                                       taste = ?,
                                                       cost = ?,
                                                       volume = ?
                                                   WHERE ID = ?''',
                                                (self.editor_screen.lineEdit_name.text().strip(),
                                                 self.editor_screen.comboBox_roast.currentIndex() + 1,
                                                 self.editor_screen.comboBox_type.currentIndex() + 1,
                                                 self.editor_screen.lineEdit_taste.text().strip(),
                                                 float(self.editor_screen.lineEdit_cost.text().strip()),
                                                 float(volume_size),
                                                 int(self.editor_screen.spinBox_id.value())))
            self.data_base.commit()
            self.upd_table()
        except ValueError:
            self.editor_screen.statusBar().show()
            self.editor_screen.statusBar().showMessage('Введены неверные данные, повторите попытку!')

    def delete_record(self):
        self.editor_screen.statusBar().hide()
        try:
            search_val = self.editor_screen.lineEdit_value.text()
            self.data_base.cursor().execute('''DELETE FROM main_table WHERE '''
                                            + self.editor_screen.comboBox_item.currentText()
                                            + ' = ' + str(search_val))
            self.data_base.commit()
            self.upd_table()
        except ValueError or sqlite3.OperationalError:
            self.editor_screen.statusBar().show()
            self.editor_screen.statusBar().showMessage('Введены неверные данные для удаления, повторите попытку!')

    def upd_table(self):
        all_data = self.data_base.cursor().execute('''SELECT * from main_table''').fetchall()
        self.size_of_base = 0
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        for i, row in enumerate(all_data):
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class EditDelete(QMainWindow, EditForm):
    def __init__(self):
        super(EditDelete, self).__init__()
        self.setupUi2(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cappuccino()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
