from appJar import gui
import sqlite3
import random
import string
import time
# APP GUI

app = gui()
app.setSticky('')
#------

# SQLITE --
conn = sqlite3.connect('test.db')
c = conn.cursor()
#------


# GRID 2 UPDATE

def updatedg2(updg2):
    if updg2 == 'Get All':

        c.execute("SELECT * FROM items")
        rows =c.fetchall()
        for row in rows:
            rg1 = row[0]
            rg2 = row[1]
            rg3 = row[2]
            app.addGridRow('g2',[rg1, rg2, rg3])
        

    
#-----------------------------------------------------------------------------



# End Program Label #
app.addLabel('w','Welcome Program',8,0)
app.setLabelSticky('w','news')
app.setLabelBg('w','black')
app.setLabelFg('w','white')
app.getLabelWidget("w").config(font=("Comic Sans", "8", "normal"))
app.setLabelWidth('w','30')
app.setLabelHeight('w','1')
app.setLabelAnchor('w','sw')
app.addLabel('s',' ',8,1)
app.setLabelSticky('s','news')
app.setLabelBg('s','black')
app.setLabelPadding('w',[50,1])
app.addLabel('r',' ',8,3)
app.setLabelBg('r','black')
app.setLabelSticky('r','news')
# -----------------------

# SEARCH LABEL #
app.addLabel('lab','Search Items In DB',0,0)
app.addLabel('lab1','',0,1)
app.setLabelBg('lab1','green')
app.setLabelBg('lab','green')
app.setLabelSticky('lab','news')
app.setLabelSticky('lab1','news')
# -------------------

# SEARCH ENTRY #

app.addEntry('searche',1,0)
app.setEntryDefault('searche','Search Item')
searchi = app.getEntry('searche')
app.setEntryFg('searche','green')
app.setEntryBg('searche','honeydew')
app.setEntrySticky('searche','ew')

#----------------

# ADD ITEM LABEL #
app.addLabel('label3','Add Item To DB ',2,0)
app.setLabelSticky('label3','news')
app.addLabel('label4',' ',2,1)
app.setLabelBg('label4','green')
app.setLabelBg('label3','green')
app.setLabelSticky('label4','news')

# ------------------

# SEARCHED ITEMS LABEL
app.addLabel('l5','Searched Items',6,0)
app.addLabel('l6',' ',6,1)
app.addLabel('l7', ' ',7,1)
app.setLabelBg('l7','green')
app.setLabelBg('l6','green')
app.setLabelBg('l5','green')
app.setLabelSticky('l5','news')
app.setLabelSticky('l6','news')
# ----------------
def press2():
    print 'someting'

### GRID 1 ####

app.addGrid('g1',[['Name','Price','Qty']],7, 0, 2, 1)
app.setGridSticky('g1','news')
app.setGridBg('g1','mediumseagreen')
app.addLabel('123',' ',7,1)
app.setLabelBg('123','green')
app.setLabelSticky('123','news')
app.setGridFg('g1','yellow')
#----------------

def searchb(src):
    if src == 'Search':

        searchi = app.getEntry('searche')
        if not searchi == '':
            c.execute("SELECT * FROM items WHERE name=(?)",(searchi,))
            row = c.fetchone()
            if not row == None:
                r1=row[0]
                r2=row[1]
                r3=row[2] 
                app.addGridRow('g1',[r1,r2,r3],) 
                app.clearEntry('searche')
                app.warningBox('Searching','Items Added To Grid')
            else:
                app.warningBox('Searching','Nothing Found !!!')



            
             






# SEARCH BUTTON #
app.addButton('Search',searchb,1,1)
app.setButtonFg('Search','green')
app.setButtonSticky('Search','ew')
# -------------

# ENTRYIES 
app.addEntry('e2',3,0)
app.setEntrySticky('e2','ew')
app.addEntry('e3',4,0)
app.setEntrySticky('e3','ew')
app.addNumericEntry('e4',5,0)
app.setEntrySticky('e4','ew')
# -----------------------

app.setEntryDefault('e2','Isim')
app.setEntryDefault('e3','Fiyat')
app.setEntryDefault('e4','Adet')
#################################


def add(addb):
    if addb == 'Add':
        edb1=app.getEntry('e2')
        edb2=app.getEntry('e3')
        edb3=app.getEntry('e4')
        c.execute("INSERT INTO items VALUES(?,?,?)",(edb1,edb2,edb3))
        conn.commit()
        app.warningBox('Added','Name:' + str(edb1) + ' ' + 'Price:' + str(edb2) + ' ' + 'Qty:' + str(edb3) +' '+ 'Added !!!',parent=None)
        


        

               


def deleb(delb):
    searchd = app.getEntry('searche')
    if delb == 'Del':
        c.execute("DELETE FROM items WHERE name=(?)",(searchd,))
        app.warningBox('Delete',"".join(searchd) +' '+ 'Deleted !!!',parent=None)
        conn.commit()

        
        



def update(upd):
    if upd == 'Update':
        searchu = app.getEntry('searche')
        upde2 = app.getEntry('e2')
        upde3 = app.getEntry('e3')
        upde4 = app.getEntry('e4')
        c.execute('UPDATE items SET name = (?), price = (?), qty = (?) WHERE name =(?)',(upde2, upde3, upde4, searchu))
        conn.commit()

        

# BUTTONS #
app.addButton('Add',add,3,1)
app.setButtonSticky('Add','news')
app.addButton('Del',deleb,4,1)
app.setButtonSticky('Del','news')
app.addButton('Update',update,5,1)
app.setButtonSticky('Update','news')
app.addButton('Get All',updatedg2,5,3)
app.setButtonSticky('Get All','news')

#------------------------



app.addLabel('g2lab','All Items In Db',6,3)
app.setLabelBg('g2lab','green')
app.setLabelSticky('g2lab','news')


# GRID 2 
app.addGrid('g2',[['Name','Price','Qty']],7,3,2,0)
app.setGridBg('g2','mediumseagreen')
app.setGridSticky('g2','news')

#-----------------
app.go()

