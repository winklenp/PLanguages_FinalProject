from tkinter import *


def export_info():
    form_info = open("info.csv", "w")
    form_info.write(
        firstname.get() + " " + lastname.get() + " " + age.get() + " " + residence_hall.get() + " " + floor.get() + " " + date_of_pos_test.get() + " " + "0")
    form_info.close()
    exit()


screen = Tk()
screen.geometry("500x550")
screen.title("Covid Self Reporting Service")
heading = Label(text="Covid Self Reporting Service", bg="white", fg="black", height="3", width="500")
heading.pack()

firstname_text = Label(text="First Name")
lastname_text = Label(text="Last Name")
age_text = Label(text="Age")
residence_hall_text = Label(text="Residence Hall")
floor_text = Label(text="Floor of Residence Hall")
date_of_pos_test_text = Label(text="Date of Positive Test (mm/dd/yy)")

firstname_text.place(x=10, y=65)
lastname_text.place(x=10, y=135)
age_text.place(x=10, y=205)
residence_hall_text.place(x=10, y=275)
floor_text.place(x=10, y=345)
date_of_pos_test_text.place(x=10, y=415)


firstname = StringVar()
lastname = StringVar()
age = StringVar()
residence_hall = StringVar()
floor = StringVar()
date_of_pos_test = StringVar()


firstname_entry = Entry(textvariable=firstname, width="30")
firstname_entry.place(x=30, y=100)
lastname_entry = Entry(textvariable=lastname, width="30")
lastname_entry.place(x=30, y=170)
age_entry = Entry(textvariable=age, width="30")
age_entry.place(x=30, y=240)
residence_hall_entry = Entry(textvariable=residence_hall, width="30")
residence_hall_entry.place(x=30, y=310)
floor_entry = Entry(textvariable=floor, width="30")
floor_entry.place(x=30, y=380)
date_of_pos_test_entry = Entry(textvariable=date_of_pos_test, width="30")
date_of_pos_test_entry.place(x=30, y=450)


submit = Button(screen, text="submit", width="50", command=export_info)
submit.place(x=75, y=520)

input()
