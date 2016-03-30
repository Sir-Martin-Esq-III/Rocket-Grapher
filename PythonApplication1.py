"""TODO:
- Creater an event handler - May not need to if the only event is a mouse click and enter on the entries 
- Create the final GUI layout for the program
- Import and configure MatplotLib (And maybe numpy)
- Import Threading? Would make it quicker and could do the calcs on one thred and draw the graph on the other
- Replace .Grid() with . Place()?
    
    Current Bugs:
- UI:
-- Error lable pushing other text away.
- Functions
-- Can't find a reliable way of finding the widget an event has came from
"""
from tkinter import *

# This may be redundant if the only exception it is going to throw is a VALUE ERROR (and I doubt that there will be enougth to justify a procedure)
def ExceptionHandler(value):
    if value==1:#Value Error
        Errors.config(text="Value Error: Please enter a number")
    
#Launch function- This is where the calculations will take place as well as makeing the user chose a number.
def launch(event):
    try:
        launchAngle=int(entry_LaunchAngle.get())
        resultantVelocity=int(entry_LaunchVel.get())
    except ValueError:
        ExceptionHandler(1)
    else:
        Errors.config(text="")
        print(launchAngle,resultantVelocity)
#Currently some of the worst code here(although most of it is bad)- These functions clear the Entry widgets
def clear1(event):
        print("Cleared Angle Input")
        angleValue.set("")
        event.widget.config(textvariable=angleValue)

def clear2(event):
    print("Cleared Resultant Velocity Input")
    LaunchVel.set("")
    event.widget.config(textvariable=LaunchVel)

#Window information
root = Tk()
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2
root.title("Temp")
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
root.config(bg="White")

#Creates 2 frames one for showing the graph and another for the user input.
graphPos=Frame(root,height=height,width=width*0.66,bg="Black")
graphPos.grid(row=0)
inputPos=Frame(root,height=height,width=width*0.33,bg ="White")
inputPos.grid(row=0,column=1)

#Angle information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
angleValue=StringVar()
angleValue.set('Use values > 0')    
lable_LaunchAngle=Label(inputPos, text="Launch Angle: ",fg ="#0066ff",bg ="White")
lable_LaunchAngle.grid(row=0,column=3)
entry_LaunchAngle=Entry(inputPos, textvariable=angleValue,fg ="#0066ff",bg ="#bfbfbf",relief=FLAT)
entry_LaunchAngle.grid(row=0,column=4)
entry_LaunchAngle.bind("<1>",clear1)

#Launch velocity information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
LaunchVel=StringVar()
LaunchVel.set('Use values > 0')
lable_LaunchVel=Label(inputPos, text="Resulatant Velocity: ",fg ="#0066ff",bg ="White")
lable_LaunchVel.grid(row=1,column=3)
entry_LaunchVel=Entry(inputPos, textvariable=LaunchVel,fg ="#0066ff",bg ="#bfbfbf",relief=FLAT)
entry_LaunchVel.grid(row=1,column=4)
entry_LaunchVel.bind("<FocusIn>",clear2)

#Launch button- Creates a button which "launches" the rocket (goes to the launch Procedure)
launchButton=Button(inputPos,text="LAUNCH",fg ="#0066ff",relief=FLAT)
launchButton.grid(row=2,columnspan=3)
launchButton.bind("<1>",launch)

#Errors- Shows any errors to the user.
errorText=Label(inputPos, text="",fg ="Red",bg ="White")
errorText.grid(row=30)

#Main loop
root.mainloop()
