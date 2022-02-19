import tkinter as tk
from tkinter import ttk

import sqlite3

#Kevin Phan
#Michille Nguyen
#Angel Trujillo

def show_frame(frame):
    frame.tkraise()

#======================================================================= scrollbar function
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

#======================================================================= sql connections
#sqlite connect function
sqlite_connection = sqlite3.connect('Project2.db')

#creating cursor
sqlite_cursor = sqlite_connection.cursor()


#========================================================================= Requirement 1 submit function
def Q1_submit():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    '''
    submit_cursor.execute("INSERT INTO CUSTOMERS VALUES (:cust_id, :cust_name, :cust_phone)",
                           {
                               #'cust_id': frame2_CustID.get(),
                               'cust_id': submit_cursor.lastrowid,
                               'cust_name': frame2_Name.get(),
                               'cust_phone': frame2_Phone.get(),
                           })
    '''

    submit_cursor.execute("INSERT INTO CUSTOMERS VALUES (:cust_id, :cust_name, :cust_phone)",
                        {
                            'cust_id': None,
                            #'cust_id': submit_cursor.lastrowid,
                            'cust_name': frame2_Name.get(),
                            'cust_phone': frame2_Phone.get(),
                        })


    #commit changes
    submit_connection.commit()

    submit_cursor.execute("SELECT * FROM CUSTOMERS")
    output_records = submit_cursor.fetchall()

    submit_cursor.execute("SELECT COUNT(*) FROM CUSTOMERS")
    number_records = submit_cursor.fetchall()

    #print_records = 'CustID'


    #count for records
    number_query_label =  tk.Label(frame2, text = number_records)
    number_query_label.grid(row = 10, column = 0, columnspan = 2)

    #for output_record in output_records:
    #    print_records += str((str(output_record[0])) + "          " + output_record[1] + "                    " + output_record[2] + "\n")

    columns = ('custid','custname','phone')
    tree = ttk.Treeview(frame2, columns=columns, show='headings')

    tree.heading('custid', text='Customer ID')
    tree.heading('custname', text='Customer Name')
    tree.heading('phone', text='Phone')


    contacts = []
    for n in output_records:
        contacts.append((str(n[0]), n[1], n[2]))

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=20, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=20, column=2, sticky = 'ns')




    #close connection
    submit_connection.close()

#========================================================================= Requirement 2 submit function
'michelle code ======================================================================================='

def Q2_submit():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    submit_cursor.execute("INSERT INTO VEHICLE VALUES (:vehicleID, :vehicleDescription, :vehicleYear, :vehicleType, :category)",
                           {
                               'vehicleID': frame3_vID.get(),
                               'vehicleDescription': frame3_vDes.get(),
                               'vehicleYear': frame3_vYear.get(),
                               'vehicleType': frame3_vType.get(),
                               'category': frame3_vcat.get()
                           })

    #commit changes
    submit_connection.commit()

    submit_cursor.execute("SELECT * FROM VEHICLE")
    output_records_V = submit_cursor.fetchall()

    submit_cursor.execute("SELECT COUNT(*) FROM VEHICLE")
    number_records_V = submit_cursor.fetchall()



    #print(output_records)
    print_records_V = '{:>50} {:>50} {:>50} {:>50} {:>50}\n'.format('Vehicle ID', 'Description', 'Vehicle Year', 'Vehicle Type', 'Category')


    for output_record_V in output_records_V:
        print_records_V += '{:>50} {:>50} {:>50} {:>50} {:>50}\n'.format(str(output_record_V[0]), output_record_V[1], output_record_V[2],  output_record_V[3], output_record_V[4])


    number_query_label =  tk.Label(frame3, text = number_records_V)
    number_query_label.grid(row = 9, column = 0, columnspan = 2)

    '''**********************************************convert this to tree view
    input_query_label_V =  tk.Label(frame3, text = print_records_V)
    input_query_label_V.grid(row = 10, column = 0, columnspan = 2, sticky = 'S')
    '''

    columns = ('vehicle_id','vehicle_description','vehicle_year','vehicle_type','vehicle_category')
    tree = ttk.Treeview(frame3, columns=columns, show='headings')

    tree.heading('vehicle_id', text='VID')
    tree.heading('vehicle_description', text='Description')
    tree.heading('vehicle_year', text='Year')
    tree.heading('vehicle_type', text='Type')
    tree.heading('vehicle_category', text='Category')

    contacts = []
    for n in output_records_V:
        contacts.append((str(n[0]), n[1], n[2], n[3], n[4]))


    print(contacts)

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=10, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame3, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=10, column=2, sticky = 'ns')



    #canvas = tk.Canvas(frame3, width = 400, height = 200)
    #canvas.create_text(0,0, text = print_records_V, fill = 'black', font = 'Times 12')
    #canvas.grid(row = 9, column = 0, columnspan = 2)

    '''
    input_query_label_V =  tk.Label(frame3, text = number_records_V)
    input_query_label_V.grid(row = 7, column = 0, columnspan = 2)

    #additional here
    input_query_label_V =  tk.Label(frame3, text = print_records_V)
    input_query_label_V.grid(row = 8, column = 0, columnspan = 2)

    input_query_label_V =  tk.Label(frame3, text = number_records_V)
    input_query_label_V.grid(row = 9, column = 0, columnspan = 2)

    input_query_label_V =  tk.Label(frame3, text = print_records_V)
    input_query_label_V.grid(row = 10, column = 0, columnspan = 2)
    '''

    #close connection
    submit_connection.close()

'michelle code ======================================================================================='
#===========================================================================Requirement 3 function
def Available_Cars():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    car_type = 0
    car_category = 0

    if frame4_car_type.get() == 'Compact':
        car_type = 1

    if frame4_car_type.get() == 'Medium':
        car_type = 2

    if frame4_car_type.get() == 'Large':
        car_type = 3

    if frame4_car_type.get() == 'SUV':
        car_type = 4

    if frame4_car_type.get() == 'Truck':
        car_type = 5

    if frame4_car_type.get() == 'VAN':
        car_type = 6

    if frame4_car_category.get() == 'Luxury':
        car_category = 1


    submit_cursor.execute("SELECT * FROM VEHICLE WHERE VehicleType = ? AND Category = ? AND VehicleID NOT IN (SELECT V.VehicleID FROM VEHICLE AS V NATURAL JOIN RENTAL AS R WHERE ? BETWEEN OrderDate AND ReturnDate)",
                                                    (frame4_car_type.get(), frame4_car_category.get(), frame4_date.get(), ))
    output_records = submit_cursor.fetchall()


    submit_cursor.execute("SELECT COUNT(*) FROM VEHICLE WHERE VehicleType = ? AND Category = ? AND VehicleID NOT IN (SELECT V.VehicleID FROM VEHICLE AS V NATURAL JOIN RENTAL AS R WHERE ? BETWEEN OrderDate AND ReturnDate)",
                                                    (frame4_rentaltype.get(), frame4_car_category.get(), frame4_date.get(), ))
    number_records = submit_cursor.fetchall()


    #count for records
    number_query_label =  tk.Label(frame4, text = number_records)
    number_query_label.grid(row = 5, column = 0, columnspan = 2)


    columns = ('vehicle_id','vehicle_description','vehicle_year','vehicle_type','vehicle_category')
    tree = ttk.Treeview(frame4, columns=columns, show='headings')

    tree.heading('vehicle_id', text='VID')
    tree.heading('vehicle_description', text='Description')
    tree.heading('vehicle_year', text='Year')
    tree.heading('vehicle_type', text='Type')
    tree.heading('vehicle_category', text='Category')

    contacts = []
    for n in output_records:
        contacts.append((str(n[0]), n[1], n[2], n[3], n[4]))

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame4, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=6, column=2, sticky = 'ns')



#===========================================================================Requirement 3 function SUBMIT NEW RENTAL

def Submit_New_Rental():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    paydate = 0
    if len(frame4_paydate.get()) == 0:
        paydate = None
    else:
        paydate = frame4_paydate.get()

    submit_cursor.execute("INSERT INTO RENTAL VALUES (:cust_id, :vech_id, :startdate, :orderdate, :type, :quant, :return, :total, :payday, :return_status)",
                        {
                            'cust_id': frame4_custid.get(),
                            'vech_id': frame4_vehicleid.get(),
                            'startdate': frame4_startdate.get(),
                            'orderdate': frame4_orderdate.get(),
                            'type': frame4_rentaltype.get(),
                            'quant': frame4_rentalqty.get(),
                            'return': None,
                            'total': frame4_total.get(),
                            'payday': paydate,
                            'return_status': frame4_returned_status.get(),
                        })


    #commit changes
    submit_connection.commit()

    submit_cursor.execute("SELECT * FROM RENTAL")
    output_records_V = submit_cursor.fetchall()

    submit_cursor.execute("SELECT COUNT(*) FROM RENTAL")
    number_records_V = submit_cursor.fetchall()


    number_query_label =  tk.Label(frame4, text = number_records_V)
    number_query_label.grid(row = 19, column = 0, columnspan = 2)


    columns = ('cust_id','vehicle_id','startdate','orderdate','type','qty','returndate','total_amount','paymentdate','returned_status')
    tree = ttk.Treeview(frame4, columns=columns, show='headings')

    tree.heading('cust_id', text='Customer  ID')
    tree.heading('vehicle_id', text='Vehicle ID')
    tree.heading('startdate', text='Start Date')
    tree.heading('orderdate', text='Order Date')
    tree.heading('type', text='Type')
    tree.heading('qty', text='Quantity')
    tree.heading('returndate', text='Return Date'),
    tree.heading('total_amount', text='Total Amount'),
    tree.heading('paymentdate', text='Payment Date')
    tree.heading('returned_status', text='Returned')

    contacts = []
    for n in output_records_V:
        contacts.append((str(n[0]), n[1], n[2], n[3], str(n[4]), str(n[5]), n[6], str(n[7]), n[8], n[9]))

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=20, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame4, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=20, column=2, sticky = 'ns')

    #close connection
    submit_connection.close()



#===========================================================================Requirement 4 function find rental

def find_rental():

    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()


    submit_cursor.execute("SELECT * FROM vRentalInfo WHERE returnDate = ? AND CustomerName = ? AND VIN = ?",
                                                    (frame5_returndate.get(), frame5_name.get(), frame5_vin.get(), ))
    output_records = submit_cursor.fetchall()


    submit_cursor.execute("SELECT COUNT(*) FROM vRentalInfo WHERE returnDate = ? AND CustomerName = ? AND VIN = ?",
                                                    (frame5_returndate.get(), frame5_name.get(), frame5_vin.get(), ))
    number_records = submit_cursor.fetchall()


    #count for records
    number_query_label =  tk.Label(frame5, text = number_records)
    number_query_label.grid(row = 5, column = 0, columnspan = 2)


    columns = ('orderdate','startdate','returndate','totaldays','vin','vehicle','type','category','custid','custname','orderamount','balance')
    tree = ttk.Treeview(frame5, columns=columns, show='headings')

    tree.heading('orderdate', text='Order Date')
    tree.heading('startdate', text='Start Date')
    tree.heading('returndate', text='Return Date')
    tree.heading('totaldays', text='Total Days')
    tree.heading('vin', text='VIN')
    tree.heading('vehicle', text='Vehicle')
    tree.heading('type', text='Type')
    tree.heading('category', text='Category')
    tree.heading('custid', text='Customer ID')
    tree.heading('custname', text='Customer Name')
    tree.heading('orderamount', text='Order Amount')
    tree.heading('balance', text='Balance')

    contacts = []
    for n in output_records:
        contacts.append((str(n[0]), n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8],n[9],n[10],n[11]))

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame5, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=6, column=2, sticky = 'ns')


#===========================================================================Requirement 4 function return rental

def return_rental():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    submit_cursor.execute("UPDATE RENTAL SET PaymentDate = ?, Returned = 1 WHERE custID = ? AND VehicleID = ? AND StartDate = ?",
                         (frame5_payday.get(), frame5_custid.get(), frame5_vin.get(), frame5_start.get(), ))


    #commit changes
    submit_connection.commit()

    submit_cursor.execute("SELECT * FROM RENTAL")
    output_records_V = submit_cursor.fetchall()

    submit_cursor.execute("SELECT COUNT(*) FROM RENTAL")
    number_records_V = submit_cursor.fetchall()


    number_query_label =  tk.Label(frame5, text = number_records_V)
    number_query_label.grid(row = 19, column = 0, columnspan = 2)


    columns = ('cust_id','vehicle_id','startdate','orderdate','type','qty','returndate','total_amount','paymentdate','returned_status')
    tree = ttk.Treeview(frame5, columns=columns, show='headings')

    tree.heading('cust_id', text='Customer  ID')
    tree.heading('vehicle_id', text='Vehicle ID')
    tree.heading('startdate', text='Start Date')
    tree.heading('orderdate', text='Order Date')
    tree.heading('type', text='Type')
    tree.heading('qty', text='Quantity')
    tree.heading('returndate', text='Return Date'),
    tree.heading('total_amount', text='Total Amount'),
    tree.heading('paymentdate', text='Payment Date')
    tree.heading('returned_status', text='Returned')

    contacts = []
    for n in output_records_V:
        contacts.append((str(n[0]), n[1], n[2], n[3], str(n[4]), str(n[5]), n[6], str(n[7]), n[8], n[9]))

    for contact in contacts:
        tree.insert('', tk.END, values = contact)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=20, column=0, sticky='nsew', columnspan = 2)

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame5, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=20, column=2, sticky = 'ns')

    #close connection
    submit_connection.close()


#===========================================================================Requirement 5A function customer query

def customer_query():
    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()

    #filter by customer id
    if ((len(frame6_custid.get()) != 0) and (len(frame6_name.get()) == 0)):

        submit_cursor.execute("SELECT CustomerID, CustomerName, CASE WHEN SUM(RentalBalance) = 0 THEN '$0.00' WHEN SUM(RentalBalance) != 0 THEN '$' || CAST(SUM(RentalBalance) AS TEXT) || '.00' END AS balance FROM vRentalInfo WHERE CustomerID = ? GROUP BY CustomerID ORDER BY SUM(RentalBalance)",
                                        (frame6_custid.get(), ))

        output_records = submit_cursor.fetchall()


        columns = ('cust_id','cust_name','cust_balance')
        tree = ttk.Treeview(frame6, columns=columns, show='headings')

        tree.heading('cust_id', text='Customer ID')
        tree.heading('cust_name', text='Customer Name')
        tree.heading('cust_balance', text='Remaining Balance')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)


        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame6, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=2, sticky = 'ns')



    #filter by name or substring of name
    if ((len(frame6_custid.get()) == 0) and (len(frame6_name.get()) != 0)):

        submit_cursor.execute("SELECT CustomerID, CustomerName, CASE WHEN SUM(RentalBalance) = 0 THEN '$0.00' WHEN SUM(RentalBalance) != 0 THEN '$' || CAST(SUM(RentalBalance) AS TEXT) || '.00' END AS balance FROM vRentalInfo WHERE CustomerName LIKE ? GROUP BY CustomerName ORDER BY SUM(RentalBalance)",
                                        ('%' + frame6_name.get() + '%', ))

        output_records = submit_cursor.fetchall()


        columns = ('cust_id','cust_name','cust_balance')
        tree = ttk.Treeview(frame6, columns=columns, show='headings')

        tree.heading('cust_id', text='Customer ID')
        tree.heading('cust_name', text='Customer Name')
        tree.heading('cust_balance', text='Remaining Balance')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)



        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame6, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=2, sticky = 'ns')


    #if no input provided
    if ((len(frame6_custid.get()) == 0) and (len(frame6_name.get()) == 0)):

        submit_cursor.execute("SELECT CustomerID, CustomerName, CASE WHEN SUM(RentalBalance) = 0 THEN '$0.00' WHEN SUM(RentalBalance) != 0 THEN '$' || CAST(SUM(RentalBalance) AS TEXT) || '.00' END AS balance FROM vRentalInfo GROUP BY CustomerName ORDER BY SUM(RentalBalance)")

        output_records = submit_cursor.fetchall()



        columns = ('cust_id','cust_name','cust_balance')
        tree = ttk.Treeview(frame6, columns=columns, show='headings')

        tree.heading('cust_id', text='Customer ID')
        tree.heading('cust_name', text='Customer Name')
        tree.heading('cust_balance', text='Remaining Balance')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)



#===========================================================================Requirement 5B function vehicle query

def vehicle_query():

    submit_connection = sqlite3.connect('Project2.db')
    submit_cursor = submit_connection.cursor()


    #filter by customer id
    if ((len(frame7_vin.get()) != 0) and (len(frame7_vehicle_description.get()) == 0)):

        '''
        submit_cursor.execute("SELECT VIN, Vehicle, CASE WHEN ((SUM(OrderAmount))/TotalDays) = 0 THEN '$0.00' WHEN ((SUM(OrderAmount))/TotalDays) != 0 THEN '$' || CAST((SUM(RentalBalance)/TotalDays) AS TEXT) || '.00' END AS dailyAverage FROM vRentalInfo WHERE VIN = ? GROUP BY VIN",
                                        (frame7_vin.get(), ))
        '''

        submit_cursor.execute("SELECT VIN, Vehicle, CASE WHEN SUM(OrderAmount) = 0 THEN '$0.00' WHEN SUM(OrderAmount) != 0 THEN '$' || CAST(((SUM(OrderAmount))/TotalDays) AS TEXT) || '.00' END AS dailyAverage FROM vRentalInfo WHERE VIN = ? GROUP BY VIN ORDER BY SUM(OrderAmount)/TotalDays",
                                        (frame7_vin.get(), ))

        output_records = submit_cursor.fetchall()


        columns = ('vin_id','v_descr','daily_avg')
        tree = ttk.Treeview(frame7, columns=columns, show='headings')

        tree.heading('vin_id', text='VIN')
        tree.heading('v_descr', text='Vehicle Description')
        tree.heading('daily_avg', text='Daily Average')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)


        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame7, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=2, sticky = 'ns')



    #filter by customer vehicle description
    if ((len(frame7_vin.get()) == 0) and (len(frame7_vehicle_description.get()) != 0)):

        print("test print")

        submit_cursor.execute("SELECT VIN, Vehicle, CASE WHEN SUM(OrderAmount) = 0 THEN '$0.00' WHEN SUM(OrderAmount) != 0 THEN '$' || CAST(((SUM(OrderAmount))/TotalDays) AS TEXT) || '.00' END AS dailyAverage FROM vRentalInfo WHERE Vehicle LIKE ? GROUP BY Vehicle ORDER BY SUM(OrderAmount)/TotalDays",
                                            ('%' + frame7_vehicle_description.get() + '%', ))

        output_records = submit_cursor.fetchall()


        columns = ('vin_id','v_descr','daily_avg')
        tree = ttk.Treeview(frame7, columns=columns, show='headings')

        tree.heading('vin_id', text='VIN')
        tree.heading('v_descr', text='Vehicle Description')
        tree.heading('daily_avg', text='Daily Average')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)


        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame7, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=2, sticky = 'ns')



    #filter by no entry
    if ((len(frame7_vin.get()) == 0) and (len(frame7_vehicle_description.get()) == 0)):

        print("test print")

        submit_cursor.execute("SELECT VIN, Vehicle, CASE WHEN SUM(OrderAmount) = 0 THEN '$0.00' WHEN SUM(OrderAmount) != 0 THEN '$' || CAST(((SUM(OrderAmount))/TotalDays) AS TEXT) || '.00' END AS dailyAverage FROM vRentalInfo GROUP BY Vehicle ORDER BY SUM(OrderAmount)/TotalDays")

        output_records = submit_cursor.fetchall()


        columns = ('vin_id','v_descr','daily_avg')
        tree = ttk.Treeview(frame7, columns=columns, show='headings')

        tree.heading('vin_id', text='VIN')
        tree.heading('v_descr', text='Vehicle Description')
        tree.heading('daily_avg', text='Daily Average')


        contacts = []
        for n in output_records:
            contacts.append((str(n[0]), n[1], n[2]))

        for contact in contacts:
            tree.insert('', tk.END, values = contact)

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=6, column=0, sticky='nsew', columnspan = 2)


        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame7, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=2, sticky = 'ns')


#====================================================================== initializing frames
window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


#frame1 = tk.Frame(window,bg='blue')

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)
frame6 = tk.Frame(window)
frame7 = tk.Frame(window)


#scrollbar frame *

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7):
    frame.grid(row=0,column=0,sticky='nsew')

#========================================================================== frame 1 code (main menu)
frame1_title = tk.Label(frame1, text = 'Main Menu',font = ('Times 30'), bg='red')
frame1_title.pack(pady = 20)

frame1_btn1 = tk.Button(frame1, text='New Customer', command=lambda:show_frame(frame2), bg='pink', width = 36, font = ('Times 30'))
frame1_btn1.pack(pady = 20)

frame1_btn2 = tk.Button(frame1, text='New Vehicle', command=lambda:show_frame(frame3), bg='pink', width = 36, font = ('Times 30'))
frame1_btn2.pack(pady = 20)

frame1_btn3 = tk.Button(frame1, text='New Rental', command=lambda:show_frame(frame4), bg='pink', width = 36, font = ('Times 30'))
frame1_btn3.pack(pady = 20)

frame1_btn4 = tk.Button(frame1, text='Return Vehicle', command=lambda:show_frame(frame5), bg='pink', width = 36, font = ('Times 30'))
frame1_btn4.pack(pady = 20)

frame1_btn5 = tk.Button(frame1, text='Customer Search', command=lambda:show_frame(frame6), bg='pink', width = 36, font = ('Times 30'))
frame1_btn5.pack(pady = 20)

frame1_btn6 = tk.Button(frame1, text='Vehicle Search', command=lambda:show_frame(frame7), bg='pink', width = 36, font = ('Times 30'))
frame1_btn6.pack(pady = 20)



#=========================================================================== frame 2 code (Requirement 1)

frame2_title = tk.Label(frame2, text = 'Add New Customer',font = ('Times 30'), bg='red')
frame2_title.grid(row = 0, column = 0, columnspan = 2)



frame2_Name = tk.Entry(frame2, width = 36)
frame2_Name.grid(row = 2, column = 1)


frame2_Phone = tk.Entry(frame2, width = 36)
frame2_Phone.grid(row = 3, column = 1)




#CustID_label = tk.Label(frame2, text = 'Customer ID:')
#CustID_label.grid(row = 1, column = 0)


CustName_label = tk.Label(frame2, text = 'Customer Name:')
CustName_label.grid(row = 2, column = 0)


CustPhone_label = tk.Label(frame2, text = 'Phone Number:')
CustPhone_label.grid(row = 3, column = 0)



submit_btn = tk.Button(frame2, text = 'Submit',width = 30, command = Q1_submit)
submit_btn.grid(row = 4, column = 0, columnspan = 2, ipadx = 100)



MainMenu_btn = tk.Button(frame2, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 5, column = 0, columnspan = 2, ipadx = 100)



#================================================================================== frame 3 code (Requirement 2)
'michelle code ================================================================================================'

frame3_title = tk.Label(frame3, text = 'Add New Vehicle',font = ('Times 30'), bg='red')
frame3_title.grid(row = 0, column = 0, columnspan = 2)


frame3_vID = tk.Entry(frame3, width = 36)
frame3_vID.grid(row = 2, column = 1)

frame3_vDes = tk.Entry(frame3, width = 36)
frame3_vDes.grid(row = 3, column = 1)

frame3_vYear = tk.Entry(frame3, width = 36)
frame3_vYear.grid(row = 4, column = 1)

frame3_vType = tk.Entry(frame3, width = 36)
frame3_vType.grid(row = 5, column = 1)

frame3_vcat = tk.Entry(frame3, width = 36)
frame3_vcat.grid(row = 6, column = 1)



#CustID_label = tk.Label(frame2, text = 'Customer ID:')
#CustID_label.grid(row = 1, column = 0)

VehID_label = tk.Label(frame3, text = 'Vehicle ID:')
VehID_label.grid(row = 2, column = 0)

VehID_label = tk.Label(frame3, text = 'Vehicle Description:')
VehID_label.grid(row = 3, column = 0)

VehID_label = tk.Label(frame3, text = 'Vehicle Year:')
VehID_label.grid(row = 4, column = 0)

VehID_label = tk.Label(frame3, text = 'Vehicle Type:')
VehID_label.grid(row = 5, column = 0)

VehID_label = tk.Label(frame3, text = 'Vehicle Category:')
VehID_label.grid(row = 6, column = 0)



submit_btn = tk.Button(frame3, text = 'Submit',width = 30, command = Q2_submit)
submit_btn.grid(row = 7, column = 0, columnspan = 2, ipadx = 100)

MainMenu_btn = tk.Button(frame3, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 8, column = 0, columnspan = 2, ipadx = 100)



'michelle code ================================================================================================'
#================================================================================== frame 4 code (Requirement 3)

frame4_title = tk.Label(frame4, text = 'New Rental Reservation',font = ('Times 30'), bg='red')
frame4_title.grid(row = 0, column = 0, columnspan = 2)

frame4_car_type = tk.Entry(frame4, width = 36)
frame4_car_type.grid(row = 1, column = 1)

frame4_car_category = tk.Entry(frame4, width = 36)
frame4_car_category.grid(row = 2, column = 1)

frame4_date = tk.Entry(frame4, width = 36)
frame4_date.grid(row = 3, column = 1)



car_type_label = tk.Label(frame4, text = 'Car Type:')
car_type_label.grid(row = 1, column = 0)

car_category_label = tk.Label(frame4, text = 'Car Category:')
car_category_label.grid(row = 2, column = 0)

date_label = tk.Label(frame4, text = 'Order Date:')
date_label.grid(row = 3, column = 0)


new_rental_btn = tk.Button(frame4, text = 'Find Available Cars',width = 30, command = Available_Cars)
new_rental_btn.grid(row = 4, column = 0, columnspan = 2, ipadx = 100)


frame4_enterinfo = tk.Label(frame4, text = "Enter New Rental Info")
frame4_enterinfo.grid(row = 8, column = 0, columnspan = 2)


#new rental submit part
frame4_custid = tk.Entry(frame4, width = 36)
frame4_custid.grid(row = 9, column = 1)

frame4_vehicleid = tk.Entry(frame4, width = 36)
frame4_vehicleid.grid(row = 10, column = 1)

frame4_startdate = tk.Entry(frame4, width = 36)
frame4_startdate.grid(row = 11, column = 1)

frame4_orderdate = tk.Entry(frame4, width = 36)
frame4_orderdate.grid(row = 12, column = 1)

frame4_rentaltype = tk.Entry(frame4, width = 36)
frame4_rentaltype.grid(row = 13, column = 1)

frame4_rentalqty = tk.Entry(frame4, width = 36)
frame4_rentalqty.grid(row = 14, column = 1)

frame4_total = tk.Entry(frame4, width = 36)
frame4_total.grid(row = 15, column = 1)

frame4_paydate = tk.Entry(frame4, width = 36)
frame4_paydate.grid(row = 16, column = 1)

frame4_returned_status = tk.Entry(frame4, width = 36)
frame4_returned_status.grid(row = 17, column = 1)

#labels
custid_label = tk.Label(frame4, text = 'Customer ID:')
custid_label.grid(row = 9, column = 0)

vehicleid_label = tk.Label(frame4, text = 'Vehicle ID:')
vehicleid_label.grid(row = 10, column = 0)

startdate_label = tk.Label(frame4, text = 'Start Date:')
startdate_label.grid(row = 11, column = 0)

orderdate_label = tk.Label(frame4, text = 'Order Date:')
orderdate_label.grid(row = 12, column = 0)

rentaltype_label = tk.Label(frame4, text = 'Rental Type:')
rentaltype_label.grid(row = 13, column = 0)

qty_label = tk.Label(frame4, text = 'Quantity:')
qty_label.grid(row = 14, column = 0)

total_label = tk.Label(frame4, text = 'Rental Total:')
total_label.grid(row = 15, column = 0)

paydate_label = tk.Label(frame4, text = 'Payment Date:')
paydate_label.grid(row = 16, column = 0)

returned_status_label = tk.Label(frame4, text = 'Returned Status:')
returned_status_label.grid(row = 17, column = 0)




create_new_rental_btn = tk.Button(frame4, text = 'Create New Rental',width = 30, command = Submit_New_Rental)
create_new_rental_btn.grid(row = 18, column = 0, columnspan = 2, ipadx = 100, pady = 20)


MainMenu_btn = tk.Button(frame4, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 22, column = 0, columnspan = 2, ipadx = 100, pady = 20)




#================================================================================== frame 5 code (Requirement 4) Return Vehicle

frame5_title = tk.Label(frame5, text = 'Return Vehicle',font = ('Times 30'), bg='red')
frame5_title.grid(row = 0, column = 0, columnspan = 2)

frame5_returndate = tk.Entry(frame5, width = 36)
frame5_returndate.grid(row = 1, column = 1)

frame5_name = tk.Entry(frame5, width = 36)
frame5_name.grid(row = 2, column = 1)

frame5_vin = tk.Entry(frame5, width = 36)
frame5_vin.grid(row = 3, column = 1)


returndate_label = tk.Label(frame5, text = 'Return Date:')
returndate_label.grid(row = 1, column = 0)

name_label = tk.Label(frame5, text = 'Customer Name:')
name_label.grid(row = 2, column = 0)

vin_label = tk.Label(frame5, text = 'VIN:')
vin_label.grid(row = 3, column = 0)


search_rental_btn = tk.Button(frame5, text = 'Find Rental',width = 30, command = find_rental)
search_rental_btn.grid(row = 4, column = 0, columnspan = 2, ipadx = 100, pady = 20)


frame5_custid = tk.Entry(frame5, width = 36)
frame5_custid.grid(row = 10, column = 1)

frame5_vin_return = tk.Entry(frame5, width = 36)
frame5_vin_return.grid(row = 11, column = 1)

frame5_start = tk.Entry(frame5, width = 36)
frame5_start.grid(row = 12, column = 1)

frame5_payday = tk.Entry(frame5, width = 36)
frame5_payday.grid(row = 13, column = 1)


custid_label = tk.Label(frame5, text = 'Customer ID:')
custid_label.grid(row = 10, column = 0)

vin2_label = tk.Label(frame5, text = 'VIN:')
vin2_label.grid(row = 11, column = 0)

start_label = tk.Label(frame5, text = 'Start Date:')
start_label.grid(row = 12, column = 0)

payday_label = tk.Label(frame5, text = 'Payment Date:')
payday_label.grid(row = 13, column = 0)


return_rental_btn = tk.Button(frame5, text = 'Return Rental',width = 30, command = return_rental)
return_rental_btn.grid(row = 14, column = 0, columnspan = 2, ipadx = 100, pady = 20)

MainMenu_btn = tk.Button(frame5, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 22, column = 0, columnspan = 2, ipadx = 100, pady = 20)


#================================================================================== frame 6 code (Requirement 5A)

frame6_title = tk.Label(frame6, text = 'Customer Search',font = ('Times 30'), bg='red')
frame6_title.grid(row = 0, column = 0, columnspan = 2)

frame6_instructions = tk.Label(frame6, text = 'Only fill one entry or leave blank for no filter search. You can also search part of a name in name entry.')
frame6_instructions.grid(row = 1, column = 0, columnspan = 2)

frame6_custid = tk.Entry(frame6, width = 36)
frame6_custid.grid(row = 2, column = 1)

frame6_name = tk.Entry(frame6, width = 36)
frame6_name.grid(row = 3, column = 1)

frame6_search_btn = tk.Button(frame6, text = 'Customer Query',width = 30, command = customer_query)
frame6_search_btn.grid(row = 4, column = 0, columnspan = 2, ipadx = 100)


frame6_custid_label = tk.Label(frame6, text = 'Customer ID:')
frame6_custid_label.grid(row = 2, column = 0)

frame6_name_label = tk.Label(frame6, text = 'Customer Name:')
frame6_name_label.grid(row = 3, column = 0)



MainMenu_btn = tk.Button(frame6, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 22, column = 0, columnspan = 2, ipadx = 100, pady = 20)



#================================================================================== frame 7 code (Requirement 5B)

frame7_title = tk.Label(frame7, text = 'Vehicle Search',font = ('Times 30'), bg='red')
frame7_title.grid(row = 0, column = 0, columnspan = 2)

frame7_instructions = tk.Label(frame7, text = 'Only fill one entry or leave blank for no filter search. You can also search part of a vehicle description in description entry.')
frame7_instructions.grid(row = 1, column = 0, columnspan = 2)

frame7_vin = tk.Entry(frame7, width = 36)
frame7_vin.grid(row = 2, column = 1)

frame7_vehicle_description = tk.Entry(frame7, width = 36)
frame7_vehicle_description.grid(row = 3, column = 1)

frame7_search_btn = tk.Button(frame7, text = 'Vehicle Query',width = 30, command = vehicle_query)
frame7_search_btn.grid(row = 4, column = 0, columnspan = 2, ipadx = 100)


frame7_vin_label = tk.Label(frame7, text = 'VIN:')
frame7_vin_label.grid(row = 2, column = 0)

frame7_description_label = tk.Label(frame7, text = 'Vehicle Description:')
frame7_description_label.grid(row = 3, column = 0)

MainMenu_btn = tk.Button(frame7, text = 'Main Menu',width = 30, command=lambda:show_frame(frame1))
MainMenu_btn.grid(row = 22, column = 0, columnspan = 2, ipadx = 100, pady = 20)


show_frame(frame1)

window.mainloop()
