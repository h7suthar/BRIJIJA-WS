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
    root.geometry("400x200")


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


def select_Callback():
    pass

def select_Item():
    global food_Items
    root = tk.Tk()
    root.geometry("400x400")
    root.title('Select from the Item below!')
    root.resizable(0,0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    selected_keys = []
    count  = 0
    
    for key, values in food_Items.items():
        key_label = ttk.Label(root, text = key)
        key_label.grid(column=0, row=count, sticky=tk.EW, padx=5, pady=5)
        key_button = ttk.Button(root,text='Select',command=lambda: selected_keys.append(key))
        key_button.grid(columns=2, row=count, sticky=tk.E, padx=5, pady=5)
        count += 1

    # Button to Clear current selection...
    clearButton = ttk.Button(root,text='Clear',command=lambda: root.quit())
    clearButton.grid(columns=2, row=count,sticky=tk.E, padx=5, pady=5)

    # Button to Submit...
    
    selectButton = ttk.Button(root,text='Submit',command=lambda: root.quit())
    selectButton.grid(columns=1, row=count,sticky=tk.W, padx=5, pady=5)
    
    root.mainloop()

if __name__ == '__main__':
    #person_Info()
    select_Item()