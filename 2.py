import sqlite3
import string
import time
from  appJar import gui

## APP GUI
app = gui('400x300','1380x960')
app.setBg('ghostwhite')
#----------------

# SQLITE -----
conn = sqlite3.connect('test.db')
c = conn.cursor()
#----------------------------------

# ACTION BUTTON

def getgdata(appg):
    data = app.getGridEntries('g1')
    data2 = app.getGridEntries('g2')
    app.addGridRow('g3',data)
    app.addGridRow('g3',data2)
    print data


# GRID 2 ALL DATA IN DB

def updateg2(upg2):
    if upg2 == 'Get All':
        c.execute('SELECT * FROM items')
        rows = c.fetchall()
        for row in rows:
            rg1 = row[0]
            rg2 = row[1]
            rg3 = row[2]
            rg4 = row[3]
            app.addGridRow('g2',[rg1, rg2, rg3,rg4])
    app.warningBox('All Data','All Data Added to GRID 2')
#---------------------------------------------------------------------------


# SEARCH 


def searchb(src):
    if src == 'Search':
        searchi = app.getEntry('searche')
        if not searchi == '':
            c.execute('SELECT * FROM items WHERE name = (?)',(searchi,))
            row = c.fetchone()
            if not row == None:
                r1 = row[0]
                r2 = row[1]
                r3 = row[2]
                r4 = row[3]
                app.addGridRow('g1',[r1,r2,r3,r4])
                app.clearEntry('searche')
                app.warningBox('Searching','Items Added To Grid')
            else:
                app.warningBox('Searching', 'Nothing Found')

# ----------------------------------------------------------------------------

# ADD BUTTON 

def add(addb):
    if addb == 'Add':
        edb1 = app.getEntry('e2')
        edb2 = app.getEntry('e3')
        edb3 = app.getEntry('e4')
        edb4 = app.getEntry('e5')
        c.execute("SELECT * FROM items WHERE name = (?) ",(edb1,))
        lokn = c.fetchone()
        if not lokn ==  None:
        
            app.warningBox('Already Have','This already in table')
        else:
            c.execute("INSERT INTO items VALUES(?,?,?,?)",(edb1,edb2,edb3,edb4))
            conn.commit()
            app.warningBox('Added','Name:' + str(edb1) + ' ' + 'Price:' + str(edb2) + ' ' + 'Qty:' + str(edb3) + ' ' + 'Added !!!',parent=None)

#------------------------------------------------------------------------------------------------------------------------------------------------------


# DELETE BUTTON 

def deleb(delb):
    searchd = app.getEntry('searche')
    if delb == 'Delete':
        c.execute('DELETE FROM items WHERE name = (?)',(searchd,))
        app.warningBox('Delete',searchd + ' ' + 'Deleted !!!',parent=None)
        conn.commit()
    else:
        app.warningBox('?????','Something Went Wrong')
# ---------------------------------------------------------------------------


# UPDATE items IN DATABASE

def update(upd):
    if upd == 'Update':
        searchu = app.getEntry('searche')
        upde2 = app.getEntry('e2')
        upde3 = app.getEntry('e3')
        upde4 = app.getEntry('e4')
        upde5 = app.getEntry('e5')
        
        if upde2 == '' or upde3 == '' or upde4 == '' or upde5 == '':
            app.warningBox('Warning','You cant pass the entries empty')
        else:
            c.execute ('SELECT * FROM items WHERE name = (?)',(upde2,))
            loknup = c.fetchone()
            print loknup
            if loknup == None :
                app.warningBox('Warning','Specific item didnt found in db or entry was wrong anyway item added in db')
            else:
                c.execute('UPDATE items SET name = (?), price = (?), qty = (?), Date = (?) WHERE name = (?)',(upde2, upde3, upde4, upde5, upde2))
                conn.commit()


#------------------------------------------------------------------------------


# LABELS
app.addLabel('l1','Search',0,0)
app.addLabel('l1e','',0,1)
app.addLabel('l2','Searched Items',2,0)
app.addLabel('l2e','',2,1)
app.addLabel('l3','Add Items Database',4,0)
app.addLabel('l3e','',4,1)
app.addLabel('l4',' ',9,0)
app.addLabel('l4e',' ',9,1)
app.addLabel('l4e2',' ',9,2)
app.addLabel('l5','Get All Data In DB',0,2)
app.addLabel('l6','All Datas In DB',2,2)
app.addLabel('l7',' ',4,2)
app.addLabel('l8','Selected Items',10,0)
app.addLabel('l8e',' ',10,1)
app.addLabel('l8e2',' ',10,2)
# LABEL OPTIONS 
# 1 LABEL 
app.setLabelBg('l1','green')
app.setLabelSticky('l1','new')
# 1 ENDING
app.setLabelBg('l1e','green')
app.setLabelSticky('l1e','new')
# 2 LABEL SEARCHED ITEMS
app.setLabelBg('l2','forestgreen')
app.setLabelSticky('l2','news')
# 2 ENDING
app.setLabelBg('l2e','forestgreen')
app.setLabelSticky('l2e','news')
# 3 LABEL
app.setLabelBg('l3','aquamarine')
app.setLabelSticky('l3','new')
# 3 ENDING
app.setLabelBg('l3e','aquamarine')
app.setLabelSticky('l3e','new')
# 4 LABEL
app.setLabelBg('l4','aquamarine')
app.setLabelSticky('l4','new')
# 4 LABEL ENGING 
app.setLabelBg('l4e','aquamarine')
app.setLabelSticky('l4e','new')
app.setLabelBg('l4e2','aquamarine')
app.setLabelSticky('l4e2','new')
# 5 LABEL
app.setLabelBg('l5','slateblue')
app.setLabelSticky('l5','new')
# 6 LABEL
app.setLabelBg('l6','slateblue')
app.setLabelSticky('l6','news')
# 7 LABEL SELECTED ITEMS
app.setLabelBg('l7','aquamarine')
app.setLabelSticky('l7','new')
# 8 LABEL
app.setLabelBg('l8','red')
app.setLabelSticky('l8','news')
# 8 LABEL ENDING 
app.setLabelBg('l8e','red')
app.setLabelSticky('l8e','news')
app.setLabelBg('l8e2','red')
app.setLabelSticky('l8e2','news')
# ENTRIES ------

# SEARCH 

app.addEntry('searche',1,0)
app.setEntryDefault('searche', 'Search Item')
app.setEntryFg('searche','green')
app.setEntryBg('searche','honeydew')
app.setEntrySticky('searche','ew')

#-----------------------------------

# ADD ITEMS ENTRIES ---

app.addEntry('e2',5,0)
app.addEntry('e3',6,0)
app.addEntry('e4',7,0)
app.addEntry('e5',8,0)

# ---------------------

# ENTRIES OPTIONS

app.setEntryDefault('e2','Name:')
app.setEntryDefault('e3','Price:')
app.setEntryDefault('e4','Qty:')
app.setEntryDefault('e5','Date:')




# BUTTONS

# GET ALL BUTTON
app.addButton('Get All',updateg2,1,2)


# SEARCH ---------------------
app.addButton('Search',searchb,1,1)
app.setButtonFg('Search','green')
app.setButtonSticky('Search','ew')
#-----------------------------------

# ADD ITEM BUTTONS
app.addButton('Add',add,5,1)
app.addButton('Delete',deleb,6,1)
app.addButton('Update',update,7,1)

#-----------------------------

# BUTTON OPTIONS 
app.setButtonSticky('Add','ew')
app.setButtonSticky('Delete','ew')
app.setButtonSticky('Update','ew')
app.setButtonSticky('Get All','ew')

# GRIDS
app.addGrid('g1',[['Name: ','Price: ','Qty: ','Date: ']],3,0,3,1,action=getgdata)
app.addGrid('g2',[['Name: ','Price: ','Qty: ', 'Date: ']],3,2,4,1,action=getgdata)
app.addGrid('g3',[['Name: ', 'Price:', 'Qty: ', 'Date : ']],11,0,4,1)
# GRIDS OPTIONS

# 1
app.setGridSticky('g1','news')
app.setGridBg('g1','gold')
# 2
app.setGridSticky('g2','news')
app.setGridBg('g2','aqua')
# 3 
app.setGridBg('g3','honeydew')




app.go()
