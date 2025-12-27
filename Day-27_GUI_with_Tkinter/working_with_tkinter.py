import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx= 20, pady= 50)

my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))

my_label["text"] = "New Text"
my_label.config(text="New Text") # iki şekilde de tamınlama yapabiliyoruz
# # Place ekranda spesifik koordinata araçları yerleştirir
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)


# Button

def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Button Clicked"
    my_label["text"] = input.get() # textbox içerisine yazılan değeri label a atıyoruz

button = tkinter.Button(text="Click Me", command=button_clicked)
# # pack belirtilen ya da default yönde eklenen araçları sırayla dizer
# button.pack()
button.grid(column=1,row=1)

button2 = tkinter.Button(text="Click Me2", command=button_clicked)
button2.grid(column=2,row=0)

#Entry

input = tkinter.Entry(width=15)
input.grid(column=3,row=2)



window.mainloop()