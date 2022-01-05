import pymysql


def mysqlconnect():
    conn = pymysql.connect(host='localhost', user='root', password='0909', db='pdb')

    cur = conn.cursor()

    cur.execute('show tables')
    op = cur.fetchall()

    for i in op:
        print(i)

if __name__ == "__main__" :
    mysqlconnect()