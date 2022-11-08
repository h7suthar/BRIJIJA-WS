import tkinter as tk
from tkinter import ttk


food_Items = {
  "Bhavnagari Gathiya - 1.5 Lbs": True,
  "Kachori Khasta-30 pcs": True,
  "Mathiya Jada-50 pcs": True,
  "Badam Puri-30 pcs": True,
  "Modak Ladu-30 pcs": True,
  "Dryfruit Chikki-2 Lbs": True,
  "Tiranga Barfi-30 pcs": True,
  "Kalajamun-30 pcs": True,
  "Kopra Paak Yellow White-30 pcs": True,
  "Khamman Dhokla-30 pcs": True
}


def person_Info():
    root = tk.Tk()
    root.geometry("300x200")


    root.title('Summer Picnic Food Signup Form')
    root.resizable(0,0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    # First name...
    FirstName_label = ttk.Label(root, text="First Name: ")
    FirstName_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
    FirstName_entry = ttk.Entry(root)
    FirstName_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)
    # Last name...
    LastName_label = ttk.Label(root, text="Last Name: ")
    LastName_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
    LastName_entry = ttk.Entry(root)
    LastName_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

    # City name...
    cityName_label = ttk.Label(root, text="City Name: ")
    cityName_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)
    cityName_entry = ttk.Entry(root)
    cityName_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

    # Phone number...
    phone_label = ttk.Label(root, text="Phone: ")
    phone_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)
    phone_entry = ttk.Entry(root)
    phone_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

    # Email address...
    Email_label = ttk.Label(root, text="Email: ")
    Email_label.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)
    Email_entry = ttk.Entry(root)
    Email_entry.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

    # Button to Submit...
    exitButton = ttk.Button(root,text='Submit',command=lambda: root.quit())
    exitButton.grid(columnspan=2, row=5, sticky=tk.S, padx=5, pady=5)

    root.mainloop()


def select_Item():
    global food_Items
    root = tk.Tk()
    root.geometry("500x500")
    root.title('New Participant!..Select from the Item below!')
    root.resizable(0,0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    selected_Items = []
    key_list = list(food_Items.keys())
    val_list = list(food_Items.values())
    button_list = []
    
    def select_Callback(argkey,keyButton,argKey):
        if food_Items[argkey] == False:
            keyButton['state'] = 'disabled'
            return
        if keyButton['text'] == "Remove":
            keyButton['text'] = "Select"
            selected_Items.remove(argkey)
        elif keyButton['text'] == "Select":
            keyButton['text'] = "Remove"
            selected_Items.append(argkey)

    def update_foodList(argList):
        print("Selection made this Participant: ")
        for x in argList:
            print(x)
            food_Items[x] = False
        print('\n')
        root.destroy()
    

    def update_Buttons(button_list):
        keyList1 = list(food_Items.keys())
        for x in range(len(keyList1)):
            i = x
            if food_Items[keyList1[i]] == False:
                button = button_list[i]
                button['state'] = 'disabled' 
            else:
                button = button_list[i]
                button['state'] = '!disabled'

    def clear_Select(argList,buttonList):
        key_list2 = list(food_Items.keys())
        for x in range(len(argList)):
            i = 0
            for y in key_list2:
                if argList[x] == y:
                    buttonList[i]['text'] = "Select"
                else:
                    pass
                i += 1
        selected_Items = []
        

    # Key1/Item1 label....
    key1_label = ttk.Label(root, text = key_list[0])
    key1_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)
    key1_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[0],key1_button,val_list[0]))
    key1_button.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    button_list.append(key1_button)

    # Key2/Item2 label....
    key2_label = ttk.Label(root, text = key_list[1])
    key2_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
    key2_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[1],key2_button,val_list[1]))
    key2_button.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    button_list.append(key2_button)

    # Key3/Item3 label....
    key3_label = ttk.Label(root, text = key_list[2])
    key3_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)
    key3_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[2],key3_button,val_list[2]))
    key3_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    button_list.append(key3_button)

    # Key4/Item4 label....
    key4_label = ttk.Label(root, text = key_list[3])
    key4_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)
    key4_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[3],key4_button,val_list[3]))
    key4_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    button_list.append(key4_button)

    # Key5/Item5 label....
    key5_label = ttk.Label(root, text = key_list[4])
    key5_label.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)
    key5_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[4],key5_button,val_list[4]))
    key5_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
    button_list.append(key5_button)

    # Key6/Item6 label....
    key6_label = ttk.Label(root, text = key_list[5])
    key6_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)
    key6_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[5],key6_button,val_list[5]))
    key6_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
    button_list.append(key6_button)

    # Key8/Item8 label....
    key7_label = ttk.Label(root, text = key_list[6])
    key7_label.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)
    key7_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[6],key7_button,val_list[6]))
    key7_button.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
    button_list.append(key7_button)

    # Key9/Item9 label....
    key8_label = ttk.Label(root, text = key_list[7])
    key8_label.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=5)
    key8_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[7],key8_button,val_list[7]))
    key8_button.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
    button_list.append(key8_button)

    # Key10/Item10 label....
    key9_label = ttk.Label(root, text = key_list[8])
    key9_label.grid(column=0, row=8, sticky=tk.EW, padx=5, pady=5)
    key9_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[8],key9_button,val_list[8]))
    key9_button.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)
    button_list.append(key9_button)

    # Key11/Item11 label....
    key10_label = ttk.Label(root, text = key_list[9])
    key10_label.grid(column=0, row=9, sticky=tk.EW, padx=5, pady=5)
    key10_button = ttk.Button(root,text='Select',command=lambda:select_Callback(key_list[9],key10_button,val_list[9]))
    key10_button.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)
    button_list.append(key10_button)

    update_Buttons(button_list)

    # Button to Clear current selection...
    clearButton = ttk.Button(root,text='Clear',command=lambda:clear_Select(selected_Items,button_list))
    clearButton.grid(column=1, row=12,sticky=tk.E, padx=5, pady=5)
    
    # Button to Submit...
    selectButton = ttk.Button(root,text='Submit',command=lambda:update_foodList(selected_Items))
    selectButton.grid(column=0, row=12,sticky=tk.W, padx=5, pady=5)
    
    root.mainloop()

if __name__ == '__main__':
    count = 3
    while count > 0:
     select_Item()
     count -= 1