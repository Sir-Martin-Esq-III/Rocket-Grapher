"""TODO:
- Creater an event handler - May not need to if the only event is a mouse click and enter on the entries 
- Create the final GUI layout for the program
-- Fonts ect
- Import and configure MatplotLib (And maybe numpy)
- Import Threading? Would make it quicker and could do the calcs on one thred and draw the graph on the other
    
    Current Bugs:
- Functions
-- Can't find a reliable way of finding the widget an event has came from
"""
from tkinter import *

# Will also handle errors
def ExceptionHandler(value):
    if value==1:#Value Error
        errorText.config(text="Value Error: Please enter a number")
    if value==2:#Angle >360
        errorText.config(text="Angle Value Error: An angle must follow this rule:\n 0<= ANGLE <=360")
    
#Launch function- This is where the calculations will take place as well as makeing the user chose a number.
def launch(event):
    try:
        launchAngle=int(entry_LaunchAngle.get())
        resultantVelocity=int(entry_LaunchVel.get())
    except ValueError:
        ExceptionHandler(1)
    else:
        if int(launchAngle)>360:
            ExceptionHandler(2)
        else:
            errorText.config(text="")
            print("Launch angle:",launchAngle,"Resultant velocity:",resultantVelocity)


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
graphPos.place(x=0,y=0)
inputPos=Frame(root,height=height,width=width*0.33,bg ="White")
inputPos.place(x=width*0.66,y=0)

#Angle information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
angleValue=StringVar()
angleValue.set('Use values > 0')    
lable_LaunchAngle=Label(inputPos, text="Launch Angle: ",fg ="#0066ff",bg ="White")
lable_LaunchAngle.place(x=0,y=0)
entry_LaunchAngle=Entry(inputPos, textvariable=angleValue,fg ="#0066ff",bg ="#cce6ff",relief=FLAT)
entry_LaunchAngle.place(x=150,y=0)
entry_LaunchAngle.bind("<1>",clear1)

#Launch velocity information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
LaunchVel=StringVar()
LaunchVel.set('Use values > 0')
lable_LaunchVel=Label(inputPos, text="Resulatant Velocity: ",fg ="#0066ff",bg ="White")
lable_LaunchVel.place(x=2,y=50)
entry_LaunchVel=Entry(inputPos, textvariable=LaunchVel,fg ="#0066ff",bg ="#cce6ff",relief=FLAT)
entry_LaunchVel.place(x=150,y=50)
entry_LaunchVel.bind("<FocusIn>",clear2)

#Launch button- Creates a button which "launches" the rocket (goes to the launch Procedure)
launchButton=Button(inputPos,text="LAUNCH",fg ="#0066ff",relief=FLAT,bg="#cce6ff")
launchButton.place(x=0,y=100)
launchButton.bind("<1>",launch)

#Errors- Shows any errors to the user.
errorText=Label(inputPos, text="",fg ="Red",bg ="White")
errorText.place(x=0,y=150)

#Ouput Lables- Shows the maximum height of the projectile and the horizontal displacement
vDistance=Label(inputPos, text="",fg ="Red",bg ="White")
vDistance.place(x=0,y=200)
hDisplacement=Label(inputPos, text="",fg ="Red",bg ="White")
hDisplacement.place(x=0,y=250)

#Main loop
root.mainloop()
