# import all functions from the tkinter
from tkinter import *

from tkinter import ttk

#import Calendar module
import calendar

def showCal():
    
    #new calendar window
    new_window = Tk()

    #setting the background color of GUI application
    new_window.config(background = 'blue')

    #setting the title of the GUI application
    new_window.title("Calendar")

    #setting the geometry of the GUI application
    new_window.geometry('550x600')

    # get method returns current text as string 
    fetch_year = int(year_field.get()) 
  
    # calendar method of calendar module return 
    # the calendar of the given year . 
    cal_content = calendar.calendar(fetch_year) 
  
    # Create a label for showing the content of the calender 
    cal_year = Label(new_window, text = cal_content, font = "Consolas 8 bold") 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
    cal_year.grid(row = 5, column = 1, padx = 20) 
      
    # start the GUI  
    new_window.mainloop()


if __name__=='__main__':

    #Create the basic gui window
    root = Tk()

    #setting the background color of GUI application
    root.config(background = 'Blue')

    #setting the title of the GUI application
    root.title("HOME")

    #setting the geometry of the GUI application
    root.geometry('750x600')

    # Create a CALENDAR : label with specified font and size 
    cal = Label(root, text = "Calendar Application", 
                bg = "Red", 
                font = ("times", 25, "bold"),
                padx=15, pady=15) 
    cal.pack(pady=(40, 25)) 

    #Create a Year label : a label to ask the user for year
    year = Label(root, 
                 text = " Enter Year",
                 bg = "white",
                 font=("aeril", 15,))
    year.pack(pady=(10))

    #Create a Year Entry : Entry
    year_field = Entry(root, 
                       font=("aeril", 15),
                       justify="center",
                       width=20)
    year_field.pack(pady=(10))
    

    # Create a Show Calendar Button and attached to showCal function 
    Show = Button(root, 
                  text = "Show Calendar", 
                  fg = "Black", 
                  bg = "Light Green", 
                  command = showCal,
                  padx=15, pady=5,
                  font=('aeril', 12),
                  )
    Show.pack(pady=(15))

    # Create a Exit Button and attached to exit function 
    Exit = Button(root, 
                  text = "Exit", 
                  fg = "Black", 
                  bg = "Light Green", 
                  command = root.destroy,
                  padx=15, pady=5,
                  font=('aeril', 12)
                  )
    Exit.pack(pady=(10))
    
    # Developer signature
    signature = Label(
    root,
    text="Developed by Peter Githae © 2026",
    bg="white",  
    fg="gray",
    font=("Arial", 10, "italic")
)
 
    signature.pack(pady=(30, 10))

    # gri bd method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
     #cal.grid(row = 1, column = 1) 
  
    #year.grid(row = 2, column =  1) 
  
    #year_field.grid(row = 3, column = 1) 
  
    #Show.grid(row = 4, column = 1) 
  
    #Exit.grid(row = 6, column = 1) 
      
    # start the GUI  

    
    root.mainloop() 



