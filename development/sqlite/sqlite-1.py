import sqlite3, time, datetime, random

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table(tname, expression):
    c.execute(f'CREATE TABLE IF NOT EXISTS {tname}({expression})')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(6353625, '2018-01-01', 'Python', 65)")
    conn.commit()

def dynamic_data_entry():
    date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = float(format(random.uniform(0.5, 10.0), '.2f'))
    d = {'datestamp': 'date', 'keyword': 'keyword', 'value': 'value'}
    x = 'datestamp, keyword, value'
    k = 'date, keyword, value'
    eval(f"""c.execute('INSERT INTO stuffToPlot ({x}) VALUES (?, ?, ?)',
    ({k}))""")
    conn.commit()

def read_from_db():
    c.execute("SELECT datestamp FROM stuffToPlot WHERE 3 < value AND value < 5")
    for row in c.fetchall(): print(row)

create_table('stuffToPlot', 'datestamp TEXT, keyword TEXT, value REAL')
dynamic_data_entry()
c.close()
conn.close()

