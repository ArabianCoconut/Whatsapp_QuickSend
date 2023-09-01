import tkinter as tk
import modules.Messaging as Messaging
import modules.assets as assets

# Variables
qr_image_path = assets.resource_path("py_assets\\bmc_qr.png")
icon_path = assets.resource_path("py_assets\\icon.ico")


def open_link():
    Messaging.whatsapp_app_link(entry.get())


# GUI Code
# Window settings
window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.title("WhatsApp QuickSend")
window.minsize(350, 350)
window.config(bg="white")
# Icon
window.iconbitmap(icon_path)
# Frame
frame = tk.Frame(window, bg="white")
frame.pack(pady=10)
# Widgets
# Label
label = tk.Label(frame, text="Enter phone number", font=("Arial", 14), bg="white")
label.pack(pady=10)
# Entry
entry = tk.Entry(frame, font=("Arial", 14), bg="#eaeaea", fg="#282828", justify="center")
entry.pack(pady=10)
entry.config(highlightbackground="white", highlightcolor="white", highlightthickness=10, bd=5)
# Button
button = tk.Button(frame, text="Open WhatsApp", font=("Arial", 14), bg="#282828", fg="white")
button.config(command=open_link)
button.pack(pady=10)
# QR Code
tk.Label(window, text="Support me on Buy Me a Coffee", font=("Arial", 10), bg="white").pack(pady=10)
qr_code = tk.PhotoImage(file=qr_image_path)
qr_code_label = tk.Label(window, image=qr_code, bg="white")
qr_code_label.pack(pady=5)
tk.Label(window, text="Thank you for your support!\nFrom Arabian Coconut", font=("Arial", 10), bg="white").pack(pady=10)
# Mainloop
window.mainloop()
