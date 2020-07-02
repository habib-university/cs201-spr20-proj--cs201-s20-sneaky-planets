from tkinter import *
from Node import HigherDeeNode
from RangeTree_3D import ThreeDeeRangeTree
from table import Table
from PIL import Image, ImageTk


class GUI:
    def __init__(self):
        self.range_tree = ThreeDeeRangeTree()

        self.display = Tk()
        self.display.geometry("460x460")
        self.display.title("Jamshoro Company ltd")
        self.display.grid_columnconfigure(0, minsize=20)
        Label(self.display, text="Jamshoro Company",  width=10, height=4).grid(
            row=0, column=1)

        self.name = Label(self.display, text="Name:")
        self.name.grid(row=3, column=0)
        self.name_ent = Entry(self.display, textvariable=StringVar())
        self.name_ent.grid(row=3, column=1)

        self.age = Label(self.display, text="Job Title:")
        self.age.grid(row=4, column=0)
        self.age_ent = Entry(self.display, textvariable=StringVar())
        self.age_ent.grid(row=4, column=1)

        self.display.grid_rowconfigure(0, minsize=20)
        
        self.salary = Label(self.display, text="Salary:")
        self.salary.grid(row=5, column=0)
        self.salary_ent = Entry(self.display, textvariable=StringVar())
        self.salary_ent.grid(row=5, column=1)

        self.rank = Label(self.display, text="Department:")
        self.rank.grid(row=6, column=0)
        self.rank_ent = Entry(self.display, textvariable=StringVar())
        self.rank_ent.grid(row=6, column=1)

        self.add_btn = Button(self.display, text="Add Employee", command = self.add_employee)
        self.add_btn.grid(row=7, column=2)

        ############
        self.error = Label(self.display, text="")
        self.error.grid(row=8, column=0)
        #########

        self.display.grid_rowconfigure(8, minsize=40)
        
        self.view_year = Label(self.display, text="Year:")
        self.view_year.grid(row=9, column=0)
        self.view_year_ent1 = Entry(self.display, textvariable=StringVar())
        self.view_year_ent1.grid(row=10, column=0)

        Label(self.display, text="--to--").grid(row=10, column=1)

        self.view_year_ent2 = Entry(self.display, textvariable=StringVar())
        self.view_year_ent2.grid(row=10, column=2, sticky=E)

        self.view_salary = Label(self.display, text="Salary:")
        self.view_salary.grid(row=11, column=0)
        self.view_salary_ent1 = Entry(self.display, textvariable=StringVar())
        self.view_salary_ent1.grid(row=12, column=0)

        Label(self.display, text="--to--").grid(row=12, column=1)

        self.view_salary_ent2 = Entry(self.display, textvariable=StringVar())
        self.view_salary_ent2.grid(row=12, column=2, sticky=W)

        self.view_incentives = Label(self.display, text="Bonus:")
        self.view_incentives.grid(row=13, column=0)
        self.view_incentives_ent1 = Entry(self.display, textvariable=StringVar())
        self.view_incentives_ent1.grid(row=14, column=0)

        Label(self.display, text="--to--").grid(row=14, column=1)

        self.view_incentives_ent2 = Entry(self.display, textvariable=StringVar())
        self.view_incentives_ent2.grid(row=14, column=2, sticky=E)


        self.display.grid_rowconfigure(13, minsize=5)

        self.srch_btn = Button(self.display, text="View Employees", command = self.show_employee)
        self.srch_btn.grid(row=16, column=2, sticky=W)

        self.error2 = Label(self.display, text="            ")
        self.error2.grid(row=15, column=0)

        self.load = Image.open('logo.png')
        self.resized = self.load.resize((160, 50), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(self.resized)

        self.logo = Label(self.display, image=render)
        self.logo.image = render
        self.logo.place(x=140, y=0)

        
    
    def add_employee(self):
        name = self.name_ent.get()
        age = self.age_ent.get()
        salary = self.salary_ent.get()
        rank = self.rank_ent.get()
        
        if rank == "" or age == "" or salary == "" or rank == "":
            self.error["text"] = "Please enter all the fields!"
        else:
            self.range_tree.add(HigherDeeNode([str(self.range_tree.n - 1), age, rank, salary, name]), self.range_tree.root)
            lines = open("data.txt", "a")
            lines.write(str(self.range_tree.n - 1) + " " + age + " " + rank + " " + salary + " " + name + "\n")
            lines.close()
            self.error["text"] = "Employee added!"

    def show_employee(self):
        year_start = self.view_year_ent1.get()
        year_end = self.view_year_ent2.get()

        salary_start = self.view_salary_ent1.get()
        salary_end = self.view_salary_ent2.get()

        incentive_start = self.view_incentives_ent1.get()
        incentive_end = self.view_incentives_ent2.get()

        if year_start == "":
            year_start = float('-inf')
        else:
            year_start = int(year_start)
        
        if year_end == "":
            year_end = float('inf')
        else:
            year_end = int(year_end)
        
        if salary_start == "":
            salary_start = float('-inf')
        else:
            salary_start = int(salary_start)

        if salary_end == "":
            salary_end = float('inf')
        else:
            salary_end = int(salary_end)

        if incentive_start == "":
            incentive_start = float('-inf')
        else:
            incentive_start = int(incentive_start)

        if incentive_end == "":
            incentive_end = float('inf')
        else:
            incentive_end = int(incentive_end)
        
        print(year_start, year_end)
        results = []
        self.range_tree.rangeSearch(incentive_start, incentive_end, salary_start, salary_end, year_start, year_end, results, self.range_tree.root)
        if len(results) != 0:
            newWindow = Toplevel(self.display)
            table = Table(newWindow, ['Year', 'Salary', 'Incentive', 'Name', 'Dept', 'Job Title'], column_minwidths=[20, 150, 150, 150, 150, 150])
            table.pack(padx=0,pady=0)
            table.set_data(results)
        else:
            self.error2["text"] = "No results found!"

    def run(self):
        self.display.mainloop()
