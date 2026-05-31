import tkinter as tk

def createWindow():
    window = tk.Tk()
    window.title("Button you can Click")
    window.geometry = "1000x1000"

    label = tk.Label(window, text="Here is your button to click")
    label.grid(row=0, column=0)

    button = tk.Button(
        window,
        text = "Button To Click"
    )
    button.grid(row=1, column=0)

    window.mainloop() 