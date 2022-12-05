import tkinter as tk
import functions as fnc

root = tk.Tk()
root.geometry("400x400")
root.title("Derivative Calculator")

label = tk.Label(root, text="Derivative Calculator", font=('Arial', 18))
label.pack(padx=20, pady=20)

label2 = tk.Label(root, text="Function:", font=('Arieal', 19))
label2.pack()

input = tk.StringVar()

entry = tk.Entry(root, textvariable=input)
entry.pack()

#calls simpleconversion with entry value and sets label4 to the output
def userinput():
    current = entry.get()
    try:
        newcurrent = fnc.simpleconversion(current)
        label4.config(text=newcurrent)
    except:
        label4.config(text="Invalid Input")
    

button = tk.Button(root, text='Enter', width=10, font=('Arial', 18), command=userinput)
button.pack(pady=10)

label3 = tk.Label(root, text='Derivative:', pady=10, font=('Arial', 18))
label3.pack()

label4 = tk.Label(root, text="", pady=20, font=('Arial', 14))
label4.pack()

root.mainloop()


