[10:31] Eduardo Brito
import tkinter as tk
 
def was_clicked():

    print("a button was clicked.")
 
def change_color(color):

    root.configure(bg=color)

    label.configure(text=f"A cor mudou para {color}")
 
root = tk.Tk()

root.title("Janela")

root.geometry("500x300+200+200")

root.wm_resizable(width=False, height=False)
 
label = tk.Label(root, text="clica para mudar a cor", font=("Arial", 16))

label.pack(pady=20)
 
button1 = tk.Button(root, text="Red", command=lambda:change_color("Red"))

button1.pack(pady=10)
 
button2 = tk.Button(root, text="Blue", command=lambda:change_color("Blue"))

button2.pack(pady=10)
 
button3 = tk.Button(root, text="Green", command=lambda:change_color("Green"))

button3.pack(pady=10)
 
button4 = tk.Button(root, text="Black", command=lambda:change_color("Black"))

button4.pack(pady=10)
 
root.mainloop()
