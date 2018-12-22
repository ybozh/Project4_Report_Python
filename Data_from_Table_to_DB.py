import sqlite3

connections = sqlite3.connect('db.db')
query = "SELECT salary_per_bt  FROM  payments"
result = connections.execute(query)

self.tblTable.setRowCount(0)
for row, form in enumerate(cursor):
    self.tblTable.insertRow(row)
    for column, item in enumerate(form):
        print(str(item))
        self.tblTable.setItem(row, column, QtGui.QTableWidgetItem(str(item)))

connections.close()