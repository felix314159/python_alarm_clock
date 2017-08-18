from datetime import datetime
import time
from tkinter import Tk, Label, Entry, Button, StringVar

import pause
import vlc

'''
Potential problems:

- quit button doesnt work while alarm is active
- numbers cant start with 0
'''


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")
        master.geometry('300x200')
        master.resizable(width=False, height=False)

        current_year, current_month, current_day = time.strftime("%Y,%m,%d").\
            split(',')

        self.label = Label(master, text="Wake Time (24 hour format)\n\
(Numbers can't start with 0)")
        self.label.grid(row=0, column=1)

        self.year_label = Label(master, text="     Year:")
        self.year_label.grid(row=1, column=0)
        temp = StringVar(master, value=current_year)
        self.year_entry = Entry(master, width=10, textvariable=temp)
        self.year_entry.grid(row=1, column=1)

        self.month_label = Label(master, text="  Month:")
        self.month_label.grid(row=2, column=0)
        temp = StringVar(master, value=current_month)
        self.month_entry = Entry(master, width=10, textvariable=temp)
        self.month_entry.grid(row=2, column=1)

        self.day_label = Label(master, text="      Day:")
        self.day_label.grid(row=3, column=0)
        temp = StringVar(master, value=current_day)
        self.day_entry = Entry(master, width=10, textvariable=temp)
        self.day_entry.grid(row=3, column=1)

        self.hour_label = Label(master, text="   Hours:")
        self.hour_label.grid(row=4, column=0)
        self.hour_entry = Entry(master, width=10)
        self.hour_entry.grid(row=4, column=1)

        self.minute_label = Label(master, text="Minutes:")
        self.minute_label.grid(row=5, column=0)
        self.minute_entry = Entry(master, width=10)
        self.minute_entry.grid(row=5, column=1)

        def button_click():

            # check if entered time is actually digits
            year = self.year_entry.get()
            month = self.month_entry.get()
            day = self.day_entry.get()
            hour = self.hour_entry.get()
            minute = self.minute_entry.get()
            if year.isdigit() and month.isdigit() \
                    and day.isdigit() and hour.isdigit() and minute.isdigit():
                # check if time entered are legal digits (0-12 and 0-59)
                year = int(year)
                month = int(month)
                day = int(day)
                hour = int(hour)
                minute = int(minute)
                if 2017 <= year \
                        and 1 <= month <= 12 \
                        and 1 <= day <= 31 and 0 <= hour <= 24 \
                        and 0 <= minute <= 59:
                        print("You will get an alarm at ", year, "-",
                              month, "-", day, "-", hour, "-", minute)
                        # datetime(year, month, day, hour, minute)
                        date = datetime(year, month, day, hour, minute)
                        pause.until(date)
                        p = vlc.MediaPlayer(
                            "file:///home/felix/Music/The_next_episode.mp3")
                        p.play()
                else:
                    print("Sorry, your input is not valid.")

        self.alarm_button = Button(master, text="Wake me",
                                   command=button_click)
        self.alarm_button.grid(row=6, column=1)

        self.quit_button = Button(master, text="Quit now", command=quit)
        self.quit_button.grid(row=7, column=1)

root = Tk()
my_gui = GUI(root)
root.mainloop()
