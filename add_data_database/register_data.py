from tkinter import *
from add_data import *

def add():
    connection_mem = sqlite3.connect('python project/add_data_database/database.db')
    cr = connection_mem.cursor()
    cr.execute("INSERT INTO user_data VALUES (:f, :l, :pass)", {
        'f': f.get(),
        'l': l.get(),
        'pass': p.get()
    })
    cr.execute("SELECT * FROM user_data")
    record = cr.fetchall()
    print(record)
    connection_mem.commit()

    f.delete(0, END)
    l.delete(0, END)
    p.delete(0, END)
    cp.delete(0, END)
    

root = Tk()
root.geometry('520x450+500+250')
root.resizable(False, False)

# FIRST NAME
Label(root, text= 'Enter your first name:').pack(pady= 10)
f = Entry(root, width= 25)
f.pack(pady = 10)

# LAST NAME
Label(root, text= 'Enter your last name:').pack(pady= 10)
l = Entry(root, width= 25)
l.pack()

# PASSWORD
Label(root, text= 'Enter your password:').pack(pady= 10)
p = Entry(root, width= 25, show='*')
p.pack()


# CONFIRM PASSWORD
Label(root, text= 'Confirm your password:').pack(pady= 10)
cp= Entry(root, width= 25, show='*')
cp.pack()

# BUTTON
Button(root, text= 'Add to database', width= 23, command= add).pack(pady= 10)

root.mainloop()