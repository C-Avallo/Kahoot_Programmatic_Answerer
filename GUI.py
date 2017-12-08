
from tkinter import *


class Gui:

    def createScroll(self, list):

        master = Tk()
        master.geometry('%dx%d+%d+%d' % (500, master.winfo_screenheight()+400, master.winfo_screenwidth(), master.winfo_screenheight()+400))

        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y, expand = False)

        listbox = Listbox(master, yscrollcommand=scrollbar.set)

        for i in range(len(list)):

            try:
                if("red" in str(list[i])):
                    listbox.insert(END, str(list[i]))
                    listbox.itemconfig(i, bg='red')
                if ("blue" in str(list[i])):
                    listbox.insert(END, str(list[i]))
                    listbox.itemconfig(i, bg='blue')
                if ("yellow" in str(list[i])):
                    listbox.insert(END, str(list[i]))
                    listbox.itemconfig(i, bg='yellow')
                if ("green" in str(list[i])):
                    listbox.insert(END, str(list[i]))
                    listbox.itemconfig(i, bg='green')

            except Exception as e:
                print("Error")
                listbox.pack(side=LEFT, fill=BOTH, expand=True)


        listbox.pack(side=LEFT, fill=BOTH, expand = True)

        scrollbar.config(command=listbox.yview)

        mainloop()