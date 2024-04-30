import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uimain_ui import Ui_MainWindow
from conection import Connect
import res_icon_qrc_rc
from  operation_windows_ui import Ui_Dialog
from PySide6.QtSql import QSqlTableModel

class Disik(QMainWindow):
    def __init__(self):
        super(Disik, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = Connect()


    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('info_res')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Dialog":
            self.ui_window.operation_windows_ui.connect(self.add_new_transaction)
        else:
            self.ui_window.operation_windows_ui.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        self.name = self.ui_window.lineEdit.text()
        self.surname = self.ui_window.lineEdit_2.text()
        self.age = self.ui_window.lineEdit_3.text()
        self.phone = self.ui_window.lineEdit_4.text()
        self.address = self.ui_window.lineEdit_5.text()
        self.bio = self.ui_window.lineEdit_6.text()

        self.data.add_info(self.name, self.surname, self.age, self.phone, self.address, self.bio)
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.name = self.ui_window.lineEdit.text()
        self.surname = self.ui_window.lineEdit_2.text()
        self.age = self.ui_window.lineEdit_3.text()
        self.phone = self.ui_window.lineEdit_4.text()
        self.address = self.ui_window.lineEdit_5.text()
        self.bio = self.ui_window.lineEdit_6.text()

        self.data.update_info(self.name, self.surname, self.age, self.phone, self.address, self.bio)
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.data.delete_info(id)
        self.view_data()



if __name__ == "__main__":
    app = QApplication([])
    window = Disik()
    window.show()
    sys.exit(app.exec())