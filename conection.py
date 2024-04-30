from PySide6 import QtWidgets, QtSql

class Connect:
    def __init__(self):
        self.create_connect()

    def create_connect(self):
        db = QtSql.QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('hostname')
        db.setDatabaseName('dbname')
        db.setUserName('username')
        db.setPassword('password')
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        self.query = QtSql.QSqlQuery()

        self.query.exec(
                """CREATE TABLE IF NOT EXISTS users_info (
                    id serial PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    surname varchar(50) NOT NULL,
                    age int NOT NULL,
                    phone_number int NOT NULL,
                    address varchar(50) NOT NULL,
                    bio varchar(100)
                );"""
            )

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()

        return query

    def add_info(self, name, surname, age, phone_number, address, bio):
        sql_query = """INSERT INTO users_info (name, surname, age, phone_number, address, bio) VALUES (?, ?, ?, ?, ?, ?);"""
        self.execute_query_with_params(sql_query, [name, surname, age, phone_number, address, bio])

    def delete_info(self, user_id):
        sql_query = """DELETE FROM users_info WHERE id = ?;"""
        self.execute_query_with_params(sql_query, [user_id])

    def update_info(self, user_id, name, surname, age, phone_number, address, bio):
        sql_query = """UPDATE users_info SET name = ?, surname = ?, age = ?, phone_number = ?, address = ?, bio = ? WHERE id = ?;"""
        self.execute_query_with_params(sql_query, [name, surname, age, phone_number, address, bio, user_id])
