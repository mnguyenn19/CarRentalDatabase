from tkinter import *

import sqlite3

#create tkinter window

root = Tk()

#root title
root.title('Address Book')

root.geometry("400x400")


#sqlite connect function
sqlite_connection = sqlite3.connect('Experiment.db')


#creating cursor 
sqlite_cursor = sqlite_connection.cursor()


#sqlite_cursor.execute('''CREATE TABLE addresses(
#                         first_name text,
#                         last_name text,
#                         street text,
#                         city text,
#                         state text,
#                         zipcode integer)''')


#test submit function
def submit():
    submit_connection = sqlite3.connect('Experiment.db')
    submit_cursor = submit_connection.cursor()

    submit_cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :street, :city, :state, :zcode)",
                           {
                               'f_name': f_name.get(),
                               'l_name': l_name.get(),
                               'street': street.get(),
                               'city': city.get(),
                               'state': state.get(),
                               'zcode': zipcode.get()
                           })
                           
    #commit changes
    submit_connection.commit()

    #close connection
    submit_connection.close()



#building the gui components
    #pack | place | grid

    #create text boxes
f_name = Entry(root, width = 40)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 40)
l_name.grid(row = 1, column = 1)

street = Entry(root, width = 40)
street.grid(row = 2, column = 1)

city = Entry(root, width = 40)
city.grid(row = 3, column = 1)

state = Entry(root, width = 40)
state.grid(row = 4, column = 1)

zipcode = Entry(root, width = 40)
zipcode.grid(row = 5, column = 1)


f_name_label = Label(root, text = 'First Name: ')
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = 'Last Name: ')
l_name_label.grid(row = 1, column = 0)

street_label = Label(root, text = 'Street: ')
street_label.grid(row = 2, column = 0)

city_label = Label(root, text = 'City: ')
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = 'State: ')
state_label.grid(row = 4, column = 0)

zip_label = Label(root, text = 'Zipcode: ')
zip_label.grid(row = 5, column = 0)


#when submit button is clicked, call submit function
submit_btn = Button(root, text = 'Add Records to DB', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


#create query button




#execute your tkinter component
root.mainloop()



