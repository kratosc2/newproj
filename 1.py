from appJar import gui
import sqlite3
import random
import string
import time
# APP GUI

app = gui()
app.setSticky('nwes')
#------

# SQLITE --

conn = sqlite3.connect('test.db')
c = conn.cursor()

#------
app.addLabel('w','Welcome Program',8,0)
app.setLabelBg('w','black')
app.setLabelFg('w','white')
app.setLabelFont('w',10)
app.setLabelWidth('w','30')
app.setLabelHeight('w','1')
app.setLabelAnchor('w','sw')
app.addLabel('s',' ',8,1)
app.setLabelBg('s','black')
app.setLabelPadding('w',[50,1])


app.addLabel('lab','Search Items In DB',0,0)
app.addLabel('lab1','',0,1)
app.setLabelBg('lab1','green')
app.setLabelBg('lab','green')


app.addEntry('searche',1,0)
app.setEntryDefault('searche','Search Item')
searchi = app.getEntry('searche')
app.setEntryFg('searche','green')
app.setEntryBg('searche','honeydew')
app.addLabel('label3','Add Item To DB ',2,0)
app.addLabel('label4',' ',2,1)
app.setLabelBg('label4','green')
app.setLabelBg('label3','green')
app.addLabel('l5','Searched Items',6,0)
app.addLabel('l6',' ',6,1)
app.setLabelBg('l6','green')
app.setLabelBg('l5','green')

random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
app.addGrid('g1',[['Name','Price','Qty']],7,0)
app.setGridSticky('g1','both')
app.setGridBg('g1','mediumseagreen')


def searchb(src):
    if src == 'Search':

        
        searchi = app.getEntry('searche')
        if not searchi == '':

            c.execute("SELECT * FROM items WHERE name=(?)",(searchi,))
            row = c.fetchone()
            r1=row[0]
            r2=row[1]
            r3=row[2] 
            app.addGridRow('g1',[r1,r2,r3]) 
            app.clearEntry('searche')

            
             







app.addButton('Search',searchb,1,1)
app.setButtonFg('Search','green')
app.addEntry('e2',3,0)
app.addEntry('e3',4,0)
app.addNumericEntry('e4',5,0)

app.setEntryDefault('e2','Isim')
app.setEntryDefault('e3','Fiyat')
app.setEntryDefault('e4','Adet')

def add(addb):
    if addb == 'Add':
        edb1=app.getEntry('e2')
        edb2=app.getEntry('e3')
        edb3=app.getEntry('e4')
        

        c.execute("INSERT INTO items VALUES(?,?,?)",(edb1,edb2,edb3))
        
        conn.commit()
               
app.addButton('Add',add,3,1)
app.setButtonHeight('Add','1')
def deleb(delb):
    searchd = app.getEntry('searche')
    if delb == 'Del':
        c.execute("DELETE FROM items WHERE name=(?)",(searchd,))
        app.warningBox('Delete',"".join(searchd) +' '+ 'Deleted !!!',parent=None)




def update(upd):
    if upd == 'Update':
        searchu = app.getEntry('searche')
        upde2 = app.getEntry('e2')
        upde3 = app.getEntry('e3')
        upde4 = app.getEntry('e4')
        c.execute('UPDATE items SET name = (?), price = (?), qty = (?) WHERE name =(?)',(upde2, upde3, upde4, searchu))




app.addButton('Del',deleb,4,1)
app.addButton('Update',update,5,1)
app.addButton('upd',None,0,3)



app.go()

