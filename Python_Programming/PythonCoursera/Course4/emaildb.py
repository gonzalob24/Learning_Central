import sqlite3

# make a connection
connection = sqlite3.connect('emaildb.sqlite')

# kind of like the handle
cur = connection.cursor()

# create table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
fname = input('Enter file name: ')
fh = open(fname)
pair = dict()

for line in fh:
    if not line.startswith('From: '):
        continue
    else:
        emailfull = line.split('@')
        org = emailfull[1].rstrip()
        pair[org] = pair.get(org, 0) + 1

for key in pair:
    cur.execute('INSERT INTO Counts (org, count) VALUES (?,?)', (key, pair[key]))

res_table = cur.execute('SELECT*FROM Counts ORDER BY count DESC')

for item in res_table:
    print(item[0], item[1])
connection.commit()
'''
for line in fh:
    # makes sure that we only get From lines
    if not line.startswith('From: '):
        continue
    pieces = line.split('@')
    org = pieces[1]
    org = org.rstrip()
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    connection.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
s
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

'''
