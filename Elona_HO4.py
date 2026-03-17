import tkinter as tk

window= tk.Tk()
window.geometry("500x300")
window.resizable(True,True)
window.title("Profile Builder")

frame =(window)
window.config(bg="lightgreen")

label1=tk.Label(window, text="Profile Builder", font=("Arial",14,"bold"), bg="lightgreen").pack(pady=5)
frame1 = tk.Frame(window, bg="lightgreen")
frame1.pack()

first_name=tk.Entry(frame1)
first_name.grid(row=0,column=0,padx=5)
middle_name=tk.Entry(frame1)
middle_name.grid(row=0,column=1,padx=5)
last_name=tk.Entry(frame1)
last_name.grid(row=0,column=2,padx=5)
birthyear=tk.Entry(frame1)
birthyear.grid(row=2,column=0,padx=5)


first_name=tk.Label(frame1,text="First Name",bg="lightgreen")
first_name.grid(row=1,column=0)
middle_name=tk.Label(frame1,text="Middle Name",bg="lightgreen")
middle_name.grid(row=1,column=1)
last_name=tk.Label(frame1,text="Last Name",bg="lightgreen")
last_name.grid(row=1,column=2)
birthyear=tk.Label(frame1,text="Birth year",bg="lightgreen")
birthyear.grid(row=3,column=0)
frame3 = tk.Frame(window, bg="lightgreen")
frame3.pack()







window.mainloop()