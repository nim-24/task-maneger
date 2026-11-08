# главный модуль

import tkinter as tk
from storage import load_tasks
from view import delete_task, add_task, edit_task, show_task, show_page, forget_page

root = tk.Tk()
root.title("task meneger")
root.geometry("450x300")
root.config(bg="grey")

tasks = load_tasks()

page_first = tk.Frame(root)
page_show = tk.Frame(root)
page_add = tk.Frame(root)
page_edit = tk.Frame(root)
page_del = tk.Frame(root)

# pages = [page_first, page_show, page_add_and_del, page_edit]

tx_list = tk.Label(page_add, text="введите задачу", width=50, bg="white", font=("Arial", 15))
tx_list.pack()

entry = tk.Entry(page_add, width=50, bg="white", fg="black", highlightthickness=2, 
highlightbackground="black", highlightcolor="blue")
entry.pack()
# entry.bind( "<Return>", add_task)

list3 = tk.Label(page_edit, text="введите задачу которую хотите поменять", width=50, bg="white", font=("Arial", 15))
list3.pack()

entry2 = tk.Entry(page_edit, width=50, bg="white", fg="black", highlightthickness=2, 
highlightbackground="black", highlightcolor="blue")
entry2.pack()

listbox = tk.Listbox(page_show, width=50, bg="white", fg="black",
                     highlightthickness=2, highlightbackground="black",
                     highlightcolor="blue")
listbox.pack()

list2 = tk.Label(page_edit, text="введите задачу на которую хотите поменять", width=50, bg="white", font=("Arial", 15))
list2.pack()

entry3 = tk.Entry(page_edit, width=50, bg="white", fg="black", highlightthickness=2, 
    highlightbackground="black", highlightcolor="blue")
entry3.pack()   

entry4 = tk.Entry(page_del, width=50, bg="white", fg="black", highlightthickness=2, 
    highlightbackground="black", highlightcolor="blue")
entry4.pack()


page_show_back = tk.Button(page_show, text="вернуться", font=("Arial", 15), 
                           command=lambda: (forget_page(page_show), show_page(page_first)))
page_show_back.pack()

page_add_back = tk.Button(page_add, text="вернуться", font=("Arial", 15), 
                           command=lambda: (forget_page(page_add), show_page(page_first)))
page_add_back.pack()

page_page_edit_back = tk.Button(page_edit, text="вернуться", font=("Arial", 15), 
                           command=lambda: (forget_page(page_edit), show_page(page_first)))
page_page_edit_back.pack()

page_del_back = tk.Button(page_del, text="вернуться", font=("Arial", 15), 
                           command=lambda: (forget_page(page_del), show_page(page_first)))
page_del_back.pack()


add_one_task = tk.Button(page_add, text="добавить задачу", font=("Arial", 15), 
                   command=lambda: (add_task(entry, tasks, listbox)))
add_one_task.pack()

edit_one_task = tk.Button(page_edit, text="редактировать задачу", font=("Arial", 15), 
                   command=lambda: (edit_task(entry2, entry3, tasks, listbox)))
edit_one_task.pack()

del_one_task = tk.Button(page_del, text="удалить задачу", font=("Arial", 15), 
                   command=lambda: (delete_task(entry4, tasks, listbox)))
del_one_task.pack()


show_bt = tk.Button(page_first, text="показать задачи", font=("Arial", 15), 
                    command=lambda: (forget_page(page_first), show_page(page_show), show_task(listbox, tasks)))
show_bt.pack()
add_bt = tk.Button(page_first, text="добавить задачи", font=("Arial", 15), 
                   command=lambda: (forget_page(page_first), show_page(page_add)))
add_bt.pack()
edit_bt = tk.Button(page_first, text="редактировать задачи", font=("Arial", 15), 
                    command=lambda: (forget_page(page_first), show_page(page_edit)))
edit_bt.pack()
del_bt = tk.Button(page_first, text="удалить задачи", font=("Arial", 15),
                   command=lambda: (forget_page(page_first), show_page(page_del)))
del_bt.pack()


page_first.pack()
root.mainloop()
