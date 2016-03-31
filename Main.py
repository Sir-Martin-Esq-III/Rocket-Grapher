"""TODO:
- Creater an event handler - May not need to if the only event is a mouse click and enter on the entries 
- Create the final GUI layout for the program
-- Fonts ect
-- Have different lables for "Max height"(Example) and the "value" (Although if they are going to look the same I don't think it will )
- Import and configure MatplotLib (And maybe numpy)
- Import Threading? Would make it quicker and could do the calcs on one thred and draw the graph on the other
- Change the amount of sig figs that the values show? Perhaps get the user to give it...
    
    Current Bugs:
- Functions
-- Can't find a reliable way of finding the widget an event has came from
"""
from tkinter import *
from math import *
#Does all of the calculations 
def maths(angle,velocity):
    gravity=9.81
    #Resolving the vector into v/h components 
    verticalComponent=velocity*(sin(radians(angle)))
    horizontalComponent=velocity*(cos(radians(angle)))
    #Finds Time/max horizontal displacement/ max vertical displacement 
    time=(2*verticalComponent)/gravity # Max time would be used to help animate the graph
    maxHorizDisp=time*horizontalComponent
    maxVertDisp=(-(verticalComponent**2)/(2*-gravity))  
    return(maxVertDisp,maxHorizDisp,time)

# Will also handle errors
def ErrorHandler(value):
    vDisplacement.set("")
    hDisplacement.set("")
    Time.set("")
    if value==1:#Value Error
        errorText.config(text="Value Error: Please enter a number")
    if value==2:#Angle >360
        errorText.config(text="Angle Value Error: An angle must follow this rule:\n 0<= ANGLE <=360")
    if value==3:#Velocity<0
        errorText.config(text="Velocity Value Error: You can't have a negative velocity.")
    
#Launch function- This is where the calculations will take place as well as makeing the user chose a number.
def launch(event):
    try:
        launchAngle=int(entry_LaunchAngle.get())
        resultantVelocity=int(entry_LaunchVel.get())
    except ValueError:
        ErrorHandler(1)
    else:
        if launchAngle>360 or launchAngle<0:
            ErrorHandler(2)
        elif resultantVelocity<0:
            ErrorHandler(3)
            
            
        else:
            errorText.config(text="")
            print("Launch angle:",launchAngle,"Resultant velocity:",resultantVelocity)
            maxHeight,horizDisp,time=maths(launchAngle,resultantVelocity)
            vDisplacement.set("Max height: %s"%(maxHeight))
            hDisplacement.set("Horizontal displacement: %s"%(horizDisp))
            Time.set("Time in air: %s"%(str(time)))


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
root.title("Trajectory Grapher")
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
7
#Launch button- Creates a button which "launches" the rocket (goes to the launch Procedure)
launchButton=Button(inputPos,text="LAUNCH",fg ="#0066ff",relief=FLAT,bg="#cce6ff")
launchButton.place(x=0,y=100)
launchButton.bind("<1>",launch)

#Errors- Shows any errors to the user.
errorText=Label(inputPos, text="",fg ="Red",bg ="White")
errorText.place(x=0,y=150)

#Ouput Lables- Shows the maximum height, the horizontal displacement and Time in the air
vDisplacement=StringVar()
hDisplacement=StringVar()
Time=StringVar()
Lable_vDisplacement=Label(inputPos, textvariable=vDisplacement,fg ="Red",bg ="White")
Lable_vDisplacement.place(x=0,y=150)
Lable_hDisplacement=Label(inputPos, textvariable=hDisplacement,fg ="Red",bg ="White")
Lable_hDisplacement.place(x=0,y=200)
Lable_Time=Label(inputPos, textvariable=Time,fg ="Red",bg ="White")
Lable_Time.place(x=0,y=250)

#Main loop
root.mainloop()
