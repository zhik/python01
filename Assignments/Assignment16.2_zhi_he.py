#built on http://www.pythonlearn.com/code/emaildb.py
'''
results of mbox.txt
@iupui.edu 536
@umich.edu 491
@indiana.edu 178
@caret.cam.ac.uk 157
@vt.edu 110
@uct.ac.za 96
@media.berkeley.edu 56
@ufp.pt 28
@gmail.com 25
@et.gatech.edu 17
'''

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    email[email.find('@'):]
    domain = email[email.find('@'):]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( domain, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (domain, ))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
