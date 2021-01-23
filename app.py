import tkinter as tk
from tkinter import ttk
from random import sample,randint
from ctypes import windll
from twilio.rest import Client
from secure import acc,ph,tok
try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
k=["1","2","3","4",'5','6',"7",'8','9','0']
l=randint(3,6)
root = tk.Tk()
root.title("Otp Checker")
otp_value = tk.StringVar()
stat_value = tk.StringVar()
k=["1","2","3","4",'5','6',"7",'8','9','0']
l=randint(3,6)
otp=''.join(sample(k,l))
def sender():
    cli=Client(acc,tok)
    sms=cli.messages.create(
        body=otp,
        from_=ph,
        to='+919177410501')
    return otp
def check_stats():
    if otp_value.get()==otp:
        stat_value.set(f"Access Granted")
    else:
        stat_value.set('Wrong Otp,Please Check Again.')


main = ttk.Frame(root, padding=(30, 15))
main.grid()

root.columnconfigure(0, weight=1)
otp_label = ttk.Label(main, text="Enter Otp Here:")
otp_input = ttk.Entry(main, width=10, textvariable=otp_value)
stat_label = ttk.Label(main, text="Status")
stat_display = ttk.Label(main, textvariable=stat_value)
check_button = ttk.Button(main, text="Check", command=check_stats)
resend_button = ttk.Button(main, text="SendOtp", command=sender)
otp_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
otp_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
otp_input.focus()

stat_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
stat_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

check_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)
resend_button.grid(column=0, row=3, columnspan=2, sticky="EW", padx=5, pady=5)
root.geometry("500x200")
root.mainloop()