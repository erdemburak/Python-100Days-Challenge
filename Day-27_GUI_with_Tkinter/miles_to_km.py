import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=350,height=150)
window.config(padx= 20, pady= 50)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1,column=0)

value_label = tkinter.Label()
value_label.grid(row=1,column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1,column=2)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)


miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)


def convert_miles_to_km():
    miles = float(miles_input.get())
    miles_to_km = round(miles * 1.6, 1)
    value_label.config(text=f"{miles_to_km}")
    
button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
button.grid(row=2, column=1)

window.mainloop()