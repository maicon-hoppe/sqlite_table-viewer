import database
from PyQt5 import QtWidgets, uic


def loadData(tela):
    tela.tableWidget.setColumnCount(len(database.showData(only_keys=True)))
    tela.tableWidget.setRowCount(len(database.showData()))
    cont = tela.tableWidget.rowCount()
    table = database.showData()
    for pessoa in table:
        for column, data in pessoa.items():
            num_col = database.showData(only_keys=True)
            num_col = num_col.index(column)
            num_lin = tela.tableWidget.rowCount() - cont
            tela.tableWidget.setHorizontalHeaderItem(num_col,
                                                     QtWidgets.QTableWidgetItem(str(column)))
            tela.tableWidget.setItem(num_lin,
                                     num_col,
                                     QtWidgets.QTableWidgetItem(str(data)))
        cont -= 1
    tela.tableWidget.resizeColumnsToContents()


def fechar():
    tela.close()


if __name__ == '__main__':
    database.createTab()
    # database.insert('pessoas', 'Pedro', 'Maria', 'João',
    #                 'Carlos Fernandes da Silva', 'Ana')

    app = QtWidgets.QApplication([])
    tela = uic.loadUi('interface/main_window.ui')

    tela.pushButton.clicked.connect(fechar)
    loadData(tela)
    tela.show()
    app.exec()
