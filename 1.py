from appJar import gui
import sqlite3

# APP GUI

app = gui()

#------

# SQLITE --

conn = sqlite3.connect('test.db')
c = conn.cursor()

#------


app.addEntry('searche',0,0)
app.setEntryDefault('searche','Search Item')
app.addButton('Search',None,0,1)

app.addEntry('e2')
app.addEntry('e3')
app.addEntry('e4')

app.setEntryDefault('e2','Isim')
app.setEntryDefault('e3','Fiyat')
app.setEntryDefault('e4','Adet')

# TEST ---
def printb(pp):
    if pp == 'print':
         e22 = app.getEntry('e2')

         print e22
app.addButton('print',printb)

#-----
def add(addb):
    if addb == 'Add':
        edb1=app.getEntry('e2')
        edb2=app.getEntry('e3')
        edb3=app.getEntry('e4')
        

        c.execute("INSERT INTO items VALUES(?,?,?)",(edb1,edb2,edb3))
        
        conn.commit()


def printse(prntf):
    if prntf == 'printb2':
        searchi=app.getEntry('searche')
        print searchi

        c.execute("SELECT * FROM items WHERE name=(?)",searchi)
        
        row1 = c.fetchone()
        r1 = row1[0]
        r2 = row1[1]
        r3 = row1[2]
        print r1
        print r2
        print r3
           
app.addButton('Add',add,2,1)
app.addButton('printb2',printse,4,1)



def deleb(delb):
    if delb == 'Del':
        c.execute("DELETE FROM items WHERE name=('kratosc2')")
app.addButton('Del',deleb,3,1)
app.go()

