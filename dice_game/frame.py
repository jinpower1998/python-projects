from tkinter import * 
from dicegame import *
        
master = Tk()  
master.geometry("800x600")  
frame = Frame(master)  
frame.pack()  


dice_button = Button(frame, text="dice !",  command=RollDice.rand_number).grid(column=600, row=600)
Label(frame, text="Input number").grid(column=100, row=200)

num_entry = Entry(frame).grid(column=200, row=200)
#get_num = master.getint(num_entry)



master.mainloop()  
