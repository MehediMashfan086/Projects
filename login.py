from tkinter import *

root = Tk()
root.geometry("500x500")


def getvals():
    print("Accepted")


registration_form = Label(root, text="Registration Form", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name").grid(row=1, column=2)
mobile = Label(root, text="Mobile").grid(row=2, column=2)
gender = Label(root, text="Gender").grid(row=3, column=2)
emergency = Label(root, text="Emergency").grid(row=4, column=2)
payment_mood = Label(root, text="Payment Mood").grid(row=5, column=2)

name_value = StringVar
mobile_value = StringVar
gender_value = StringVar
emergency_value = StringVar
payment_mood_value = StringVar
check_value = IntVar

name_entry = Entry(root, textvariable=name_value).grid(row=1, column=3)
mobile_entry = Entry(root, textvariable=mobile_value).grid(row=2, column=3)
gender_entry = Entry(root, textvariable=gender_value).grid(row=3, column=3)
emergency_entry = Entry(root, textvariable=emergency_value).grid(row=4, column=3)
payment_mood_entry = Entry(root, textvariable=payment_mood_value).grid(row=5, column=3)

check_btn = Checkbutton(text="remember me?", variable=check_value).grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
