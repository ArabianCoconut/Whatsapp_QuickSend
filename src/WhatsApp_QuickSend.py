import tkinter as tk
import modules.Messaging as Messaging


def open_link():
    Messaging.whatsapp_app_link(entry.get())


# GUI Code
# Window settings
window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("WhatsApp QuickSend")
window.geometry("200x200")
window.minsize(200, 200)
window.maxsize(350, 250)
window.config(bg="white")
# Widgets
# Label
label = tk.Label(window, text="Enter phone number", font=("Arial", 14), bg="white")
label.pack(pady=10)
# Entry
entry = tk.Entry(window, font=("Arial", 14), bg="#eaeaea", fg="#282828", justify="center")
entry.pack(pady=10)
entry.config(highlightbackground="white", highlightcolor="white", highlightthickness=10, bd=5)
# Button
button = tk.Button(window, text="Open WhatsApp", font=("Arial", 14), bg="#282828", fg="white")
button.config(command=open_link)
button.pack(pady=10)
# Mainloop
window.mainloop()
