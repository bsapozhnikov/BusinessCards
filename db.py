import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()

def dropTable(tablename):
    c.execute("DROP TABLE %s" % (tablename))
    conn.commit()
    print ("DROP TABLE %s" % (tablename))

def createTable(tablename, attr):
    """Creates a table in the database \'blog.db\'
    1st parameter - name of table (string)
    2nd parameter - Dictionary with keys and types as values'
    """
    print tablename
    L = [k[0]+' '+k[1] for k in attr]
##    L = [k+' '+attr[k] for k in attr.keys()]
    s = ','.join(L)
    c.execute("CREATE TABLE %s(%s)" % (tablename, s))
    conn.commit()
    print ("CREATE TABLE %s(%s)") % (tablename, s)

def createTables():
    createTable('cards',[('name','text')])

def dropTables():
    dropTable('cards')

def getCards():
    'returns a collection of trips'
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    cards = []
    for row in c.execute('SELECT rowid,* FROM cards'):
        cards.append({"id":row[0], "name":row[1]})
    print 'cards: '+`cards`
    return cards    
     
def addCard(name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    t = (name, )
    c.execute("INSERT INTO cards VALUES (?)",t)
    conn.commit()
    print "added %s" %(name)
    return True   

def deleteCard(cardID):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    t = (cardID, )
    c.execute("DELETE FROM cards WHERE oid=?",t)
    conn.commit()
    print "deleted card %s" %(cardID)
    return True   
