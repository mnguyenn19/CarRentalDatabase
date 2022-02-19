import tkinter as tk

import sqlite3

def show_frame(frame):
    frame.tkraise()

def query1_submit():
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
    





#sqlite connect function
sqlite_connection = sqlite3.connect('Experiment.db')

#creating cursor 
sqlite_cursor = sqlite_connection.cursor()




window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#frame1 = tk.Frame(window,bg='blue')
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)


for frame in (frame1, frame2, frame3):
    frame.grid(row=0,column=0,sticky='nsew')

#==============================================================================================frame 1 code
'''
frame1_title = tk.Label(frame1, text = 'Main Menu', width = 60, height = 60, font = ('Times 20'))
frame1_title.grid(row = 0, column = 0, padx = 20)

frame1_btn = tk.Button(frame1, text='Enter', command=lambda:show_frame(frame2))
frame1_btn.grid(row = 1, column = 0, padx = 20)
'''

frame1_title = tk.Label(frame1, text = 'Main Menu',font = ('Times 20'), bg='red')
frame1_title.pack(pady=20)

frame1_entry = tk.Entry(frame1, width = 20)
frame1_entry.pack()

frame1_btn = tk.Button(frame1, text='Enter', command=lambda:show_frame(frame2))
frame1_btn.pack()

#================================================================================================frame 2 code
#frame1_title = tk.Label(frame2, text = 'Frame 2')
#frame1_title.grid(row = 0, column = 0)


#building the gui components
    #pack | place | grid

    #create text boxes
f_name = tk.Entry(frame2, width = 40)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = tk.Entry(frame2, width = 40)
l_name.grid(row = 1, column = 1)

street = tk.Entry(frame2, width = 40)
street.grid(row = 2, column = 1)

city = tk.Entry(frame2, width = 40)
city.grid(row = 3, column = 1)

state = tk.Entry(frame2, width = 40)
state.grid(row = 4, column = 1)

zipcode = tk.Entry(frame2, width = 40)
zipcode.grid(row = 5, column = 1)


f_name_label = tk.Label(frame2, text = 'First Name: ')
f_name_label.grid(row = 0, column = 0)

l_name_label = tk.Label(frame2, text = 'Last Name: ')
l_name_label.grid(row = 1, column = 0)

street_label = tk.Label(frame2, text = 'Street: ')
street_label.grid(row = 2, column = 0)

city_label = tk.Label(frame2, text = 'City: ')
city_label.grid(row = 3, column = 0)

state_label = tk.Label(frame2, text = 'State: ')
state_label.grid(row = 4, column = 0)

zip_label = tk.Label(frame2, text = 'Zipcode: ')
zip_label.grid(row = 5, column = 0)


frame1_btn = tk.Button(frame2, text='Submit', command = query1_submit)
frame1_btn.grid(row = 6, column = 0)

frame1_btn = tk.Button(frame2, text='Main Menu', command=lambda:show_frame(frame1))
frame1_btn.grid(row = 7, column = 0)





#show frame1 when we open project
show_frame(frame1)

window.mainloop()

