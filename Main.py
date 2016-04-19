"""
This program plots the trajectory of a projectile using the SUVAT equations (That means no fancy physics, unfortunately).
"""
from tkinter import *
from math import *
#Matplotlib and its backend and other stuff.
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#Fonts/Styles
MainlableFont=("TkDefaultFont",15,"bold")
infoLableFont=("TkDefaultFont",10,"bold")
launchFont=("TkDefaultFont",15,"bold")
plt.style.use(['ggplot'])


#Window information (Window geometry, default bg color and title)
root = Tk()
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2
resolutionOffset=((100/(1920*1080))*((height*2)*(width*2))/100)
print(resolutionOffset)
root.title("Trajectory Grapher")
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
root.config(bg="White")
root.resizable(width=FALSE, height=FALSE)

#Creates 2 frames one for showing the graph and another for the user input.
graphPos=Frame(root,height=height,width=width*0.66,bg="White")
graphPos.place(x=0,y=0)
inputPos=Frame(root,height=height,width=width*0.33,bg ="White")
inputPos.place(x=width*0.66,y=0)

#This function gets an array of positions so that it can plot this coordinates on to a graph
def showGraph(xvals,yvals):
    figure = Figure(figsize=(((6.35*resolutionOffset)+0.5),5.1), dpi=99) 
    graph = figure.add_subplot(111)
    graph.plot(xvals,yvals)
    graph.set_xlabel("Horizontal displacement(M)")
    graph.set_ylabel("Vertical displacement(M)")
    canvas = FigureCanvasTkAgg(figure, graphPos)
    canvas.show()
    canvas.get_tk_widget().place(x=0,y=0)

#Does all of the calculations 
def maths(angle,velocity):
#Creates arrays for the x/y coordinates used to plot the graphs as well as defining gravity 
    xValues=list()
    yValues=list()
    gravity=9.81
    #Resolving the vector into v/h components 
    verticalComponent=velocity*(sin(radians(angle)))
    horizontalComponent=velocity*(cos(radians(angle)))
    #Finds Time/max horizontal displacement/ max vertical displacement 
    time=(2*verticalComponent)/gravity
    maxHorizDisp=time*horizontalComponent
    maxVertDisp=(-(verticalComponent**2)/(2*-gravity))
    for i in range(0,36):
        updateTime=(time*(i/35))
        yValues.append((verticalComponent*updateTime)+((-1/2*gravity)*(updateTime*updateTime)))
        xValues.append(updateTime*horizontalComponent) 
    showGraph(xValues,yValues)
    return(maxVertDisp,maxHorizDisp,time)

#Error handler- This function is called when an exception has been met or some arbitary rule that I have set has been broken also updates the error labeles to display to the user what they have done wrong.
def ErrorHandler(value):
    vDisplacement.set("")
    hDisplacement.set("")
    Time.set("")
    if value==1:#Value Error
        errorText.config(text=" Value Error: Please enter a number")
    if value==2:#Angle >360
        errorText.config(text=" Angle Value Error: An angle must follow this rule:\n 0<= ANGLE <=180")
    if value==3:#Velocity<0
        errorText.config(text=" Velocity Value Error: You can't have a negative velocity.")
    
#Launch function-input validation, updateing lables for Vdisp, hdisp and timer.
def launch(event):
    try:
        launchAngle=int(entry_LaunchAngle.get())
        resultantVelocity=int(entry_LaunchVel.get())
    except ValueError:
        ErrorHandler(1)
    else:
        if launchAngle>180 or launchAngle<0:
            ErrorHandler(2)
        elif resultantVelocity<0:
            ErrorHandler(3)         
        else:
            errorText.config(text="")
            print("Launch angle:",launchAngle,"Resultant velocity:",resultantVelocity)
            maxHeight,horizDisp,time=maths(launchAngle,resultantVelocity)
            vDisplacement.set("Max height (M):  %s" %float('%.3g' %maxHeight))
            hDisplacement.set("ΔDh(M): %s" %float('%.3g' %horizDisp))
            Time.set("Δt:  %s" %float('%.3g' %time))


#These functions clear the Entry widgets
def clear1(event):
        print("Cleared Angle Input")
        angleValue.set("")
        event.widget.config(textvariable=angleValue)

def clear2(event):
    print("Cleared Resultant Velocity Input")
    LaunchVel.set("")
    event.widget.config(textvariable=LaunchVel)


#Angle information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
angleValue=StringVar()
angleValue.set('Use values > 0')    
lable_LaunchAngle=Label(inputPos, text="Launchº ",fg ="#8c8c8c",bg ="White",font=MainlableFont)
lable_LaunchAngle.place(x=0,y=50)
entry_LaunchAngle=Entry(inputPos, textvariable=angleValue,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
entry_LaunchAngle.place(x=150*resolutionOffset,y=57)
entry_LaunchAngle.bind("<1>",clear1)

#Launch velocity information- Creates a lable and an entry box (Which can be cleared) as well as declares the variable for the value of launch velocity
LaunchVel=StringVar()
LaunchVel.set('Use values > 0')
lable_LaunchVel=Label(inputPos, text="Vr  ",fg ="#8c8c8c",bg ="White",font=MainlableFont)     
lable_LaunchVel.place(x=2,y=100)
entry_LaunchVel=Entry(inputPos, textvariable=LaunchVel,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
entry_LaunchVel.place(x=150*resolutionOffset,y=107)
entry_LaunchVel.bind("<FocusIn>",clear2)

#Launch button- Creates a button which "launches" the rocket (goes to the launch Procedure)
launchButton=Button(inputPos,text="LAUNCH",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainlableFont)
launchButton.place(x=100*resolutionOffset,y=150)
launchButton.bind("<1>",launch)

#Errors- Shows any errors to the user.
errorText=Label(inputPos, text="",fg ="#E24A33 ",bg ="White")

errorText.place(x=0,y=height-30)

#Ouput Lables- Shows the maximum height of the projectile and the horizontal displacement
vDisplacement=StringVar()
hDisplacement=StringVar()
Time=StringVar()
Lable_vDisplacement=Label(inputPos, textvariable=vDisplacement,fg ="#E24A33 ",bg ="White",font=infoLableFont)
Lable_vDisplacement.place(x=0,y=200)
Lable_hDisplacement=Label(inputPos, textvariable=hDisplacement,fg ="#E24A33 ",bg ="White",font=infoLableFont)
Lable_hDisplacement.place(x=0,y=250)
Lable_Time=Label(inputPos, textvariable=Time,fg ="#E24A33 ",bg ="White",font=infoLableFont)
Lable_Time.place(x=0,y=300)

#Main loop
root.mainloop()
