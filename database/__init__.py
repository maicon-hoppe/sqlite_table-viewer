import sqlite3


def connectTab(db_name: str = 'dados.db') -> sqlite3.Connection:

    conexao = sqlite3.connect(f'../{db_name}')
    conexao.row_factory = sqlite3.Row

    return conexao


def createTab(tab_name: str = 'pessoas'):

    conexao = connectTab()
    print(type(conexao))

    with conexao:
        cursor = conexao.cursor()
        sql = f'CREATE TABLE IF NOT EXISTS {tab_name}(' \
              f'id INTEGER NOT NULL PRIMARY KEY,' \
              f'nome TEXT NOT NULL' \
              f');'
        cursor.execute(sql)
        conexao.commit()


def insert(tab_name: str = 'pessoas', *args: str):

    conexao = connectTab()

    with conexao:
        cursor = conexao.cursor()
        sql = f'INSERT INTO {tab_name} VALUES \n'

        c, ids = len(args), list()
        for arg in args:
            sql += f"(?, '{arg}')"
            if c > 1:
                sql += ', \n'
            ids.append(None)
            c -= 1
        sql += ';'
        cursor.execute(sql, ids)
        conexao.commit()


def remove(tab_name: str = 'pessoas', ident: int):

    conexao = connectTab()

    with conexao:
        cursor = conexao.cursor()
        sql = f'DELETE FROM {tab_name} WHERE id={ident};'
        cursor.execute(sql)
        conexao.commit()


def showData(tab_name: str = 'pessoas', only_keys: bool = False):

    conexao = connectTab()

    with conexao:
        cursor = conexao.cursor()
        sql = f'SELECT * FROM {tab_name};'
        cursor.execute(sql)
        result = cursor.fetchall()

        pessoas = list()
        for data in result:
            data = dict(data)
            if only_keys:
                data = data.keys()
                pessoas = list(data)
            else:
                pessoas.append(data)
        return pessoas
