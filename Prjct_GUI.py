from tkinter import *
from Node import HigherDeeNode
from RangeTree_3D import ThreeDeeRangeTree
from table import Table


class GUI:
    def __init__(self):
        self.range_tree = ThreeDeeRangeTree()

        self.display = Tk()
        self.display.geometry("460x460")
        self.display.title("Jamshoro Company ltd")
        self.display.grid_columnconfigure(0, minsize=20)
        Label(self.display, text="Jamshoro Company ltd.", bg="grey", width=25, height=3).grid(
            row=0, column=1)

        self.name = Label(self.display, text="Name:")
        self.name.grid(row=3, column=0)
        self.name_ent = Entry(self.display, textvariable=StringVar())
        self.name_ent.grid(row=3, column=1)

        self.age = Label(self.display, text="Age:")
        self.age.grid(row=4, column=0)
        self.age_ent = Entry(self.display, textvariable=StringVar())
        self.age_ent.grid(row=4, column=1)

        self.display.grid_rowconfigure(0, minsize=20)
        
        self.salary = Label(self.display, text="Salary:")
        self.salary.grid(row=5, column=0)
        self.salary_ent = Entry(self.display, textvariable=StringVar())
        self.salary_ent.grid(row=5, column=1)

        self.rank = Label(self.display, text="Rank:")
        self.rank.grid(row=6, column=0)
        self.rank_ent = Entry(self.display, textvariable=StringVar())
        self.rank_ent.grid(row=6, column=1)

        self.add_btn = Button(self.display, text="Add Employee", command = self.add_employee)
        self.add_btn.grid(row=7, column=2)

        ############
        self.error = Label(self.display, text="            ")
        self.error.grid(row=8, column=0)
        #########

        self.display.grid_rowconfigure(8, minsize=40)
        
        self.view_age = Label(self.display, text="Age:")
        self.view_age.grid(row=9, column=0)
        self.view_age_ent1 = Entry(self.display, textvariable=StringVar())
        self.view_age_ent1.grid(row=10, column=0)

        Label(self.display, text="--to--").grid(row=10, column=1)

        self.view_age_ent2 = Entry(self.display, textvariable=StringVar())
        self.view_age_ent2.grid(row=10, column=2, sticky=E)

        self.id = Label(self.display, text="Id:")
        self.id.grid(row=11, column=0)
        self.id_ent1 = Entry(self.display, textvariable=StringVar())
        self.id_ent1.grid(row=12, column=0)

        Label(self.display, text="--to--").grid(row=12, column=1)

        self.id_ent2 = Entry(self.display, textvariable=StringVar())
        self.id_ent2.grid(row=12, column=2, sticky=W)

        self.display.grid_rowconfigure(13, minsize=5)


        self.srch_btn = Button(self.display, text="View Employees", command = self.show_employee)
        self.srch_btn.grid(row=14, column=2, sticky=W)

    
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
            lines.write(str(range_tree.n - 1) + " " + age + " " + rank + " " + salary + " " + name)
            lines.close()
            self.error["text"] = "Employee added!"

    
    def show_employee(self):
        age_start = self.view_age_ent1.get()
        age_end = self.view_age_ent2.get()

        id_start = self.id_ent1.get()
        id_end = self.id_ent2.get()

        if id_start == "":
            id_start = float('-inf')
        else:
            id_start = int(id_start)
        
        if id_end == "":
            id_end = float('inf')
        else:
            id_end = int(id_end)
        
        if age_start == "":
            age_start = float('-inf')
        else:
            age_start = int(age_start)

        if age_end == "":
            age_end = float('inf')
        else:
            age_end = int(age_end)

        results = []
        self.range_tree.rangeSearch(age_start, age_end, id_start, id_end, results, self.range_tree.root)
        newWindow = Toplevel(self.display)
        table = Table(newWindow, ['ID', 'Age', 'Rank', 'Salary', 'Name'], column_minwidths=[20, 100, 100, 100, 100])
        table.pack(padx=0,pady=0)
        table.set_data(results)

    def run(self):
        self.display.mainloop()




# def add_employee():
#     name = name_ent.get()
#     age = age_ent.get()
#     salary = salary_ent.get()
#     rank = rank_ent.get()
    
#     if rank == "" or age == "" or salary == "" or rank == "":
#         error["text"] = "Please enter all the fields!"
#     else:
#         range_tree.add(HigherDeeNode([str(range_tree.n - 1), age, rank, salary, name]), range_tree.root)
#         lines = open("data.txt", "a")
#         lines.write(str(range_tree.n - 1) + " " + age + " " + rank + " " + salary + " " + name)
#         lines.close()
#         error["text"] = "Employee added!"


# display = Tk()
# display.geometry("460x460")
# display.title("Jamshoro Company ltd")
# display.grid_columnconfigure(0, minsize=20)
# Label(display, text="Jamshoro Company ltd.", bg="grey", width=25, height=3).grid(
#     row=0, column=1)

# display.grid_rowconfigure(1, minsize=20)

# name = Label(display, text="Name:")
# name.grid(row=3, column=0)
# name_ent = Entry(display, textvariable=StringVar())
# name_ent.grid(row=3, column=1)

# age = Label(display, text="Age:")
# age.grid(row=4, column=0)
# age_ent = Entry(display, textvariable=StringVar())
# age_ent.grid(row=4, column=1)

# display.grid_rowconfigure(0, minsize=20)

# salary = Label(display, text="Salary:")
# salary.grid(row=5, column=0)
# salary_ent = Entry(display, textvariable=StringVar())
# salary_ent.grid(row=5, column=1)

# rank = Label(display, text="Rank:")
# rank.grid(row=6, column=0)
# rank_ent = Entry(display, textvariable=StringVar())
# rank_ent.grid(row=6, column=1)

# add_btn = Button(display, text="Add Employee", command = add_employee)
# add_btn.grid(row=7, column=2)

# ############
# error = Label(display, text="            ")
# error.grid(row=8, column=0)
# #########

# display.grid_rowconfigure(8, minsize=40)

# view_age = Label(display, text="Age:")
# view_age.grid(row=9, column=0)
# view_age_ent1 = Entry(display, textvariable=StringVar())
# view_age_ent1.grid(row=10, column=0)

# Label(display, text="--to--").grid(row=10, column=1)

# view_age_ent2 = Entry(display, textvariable=StringVar())
# view_age_ent2.grid(row=10, column=2, sticky=E)

# id = Label(display, text="Id:")
# id.grid(row=11, column=0)
# id_ent1 = Entry(display, textvariable=StringVar())
# id_ent1.grid(row=12, column=0)

# Label(display, text="--to--").grid(row=12, column=1)

# id_ent2 = Entry(display, textvariable=StringVar())
# id_ent2.grid(row=12, column=2, sticky=W)

# display.grid_rowconfigure(13, minsize=5)


# srch_btn = Button(display, text="View Employees", command = show_employee)
# srch_btn.grid(row=14, column=2, sticky=W)

# display.mainloop()




# def show_employee():
#     age_start = view_age_ent1.get()
#     age_end = view_age_ent2.get()

#     id_start = id_ent1.get()
#     id_end = id_ent2.get()

#     if id_start == "":
#         id_start = float('-inf')
#     else:
#         id_start = int(id_start)
    
#     if id_end == "":
#         id_end = float('inf')
#     else:
#         id_end = int(id_end)
    
#     if age_start == "":
#         age_start = float('-inf')
#     else:
#         age_start = int(age_start)

#     if age_end == "":
#         age_end = float('inf')
#     else:
#         age_end = int(age_end)
#     results = []
#     range_tree.rangeSearch(age_start, age_end, id_start, id_end, results, range_tree.root)
#     newWindow = Toplevel(display)
#     table = Table(newWindow, ['ID', 'Age', 'Rank', 'Salary', 'Name'], column_minwidths=[20, 100, 100, 100, 100])
#     table.pack(padx=0,pady=0)
#     table.set_data(results)


# range_tree = ThreeDeeRangeTree()
