from tkinter import *

def launch(event):
    launchAngle=launchAngleInput.get()
    resultantVelocity=resulatantVel.get()
    if (resultantVelocity=="0") or(launchAngle=="0"):
        print("Use bigger values")
    else:
        print(launchAngle,resultantVelocity)
#Exception should be moved from this function to "launch"    
def clear1(event):
    try:
        String=int(launchAngleInput.get())
    except ValueError:
        print("invalid")
    else:
        print(String)
        print(ord(STR(String)))
        print("Cleared Launch Angle Input ")
        angle.set("")
        event.widget.config(textvariable=angle)

def clear2(event):
    print("Cleared Resultant Velocity Input")
    resVel.set("")
    event.widget.config(textvariable=resVel)


root = Tk()
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
root.config(bg="White")

angle=IntVar()
angle.set('dsfg')           
resVel=IntVar()
resVel.set('Use values > 0')
#Gets the launch angle

graphPos=Frame(root,height=height,width=width*0.66,bg="Black")
graphPos.grid(row=0)
inputPos=Frame(root,height=height,width=width*0.33,bg ="White")
inputPos.grid(row=0,column=1)

launchAngleLable=Label(inputPos, text="Launch Angle: ",fg ="#0066ff",bg ="White")
launchAngleLable.grid(row=0,column=3)
launchAngleInput=Entry(inputPos, textvariable=angle,fg ="#0066ff",bg ="#bfbfbf",relief=FLAT)
launchAngleInput.grid(row=0,column=4)
launchAngleInput.bind("<1>",clear1)
#Gets the resultant velocity 
resulatantVelLable=Label(inputPos, text="Resulatant Velocity: ",fg ="#0066ff",bg ="White")
resulatantVelLable.grid(row=1,column=3)
resulatantVel=Entry(inputPos, textvariable=resVel,fg ="#0066ff",bg ="#bfbfbf",relief=FLAT)
resulatantVel.grid(row=1,column=4)
resulatantVel.bind("<FocusIn>",clear2)
#Launch button
launchButton=Button(inputPos,text="LAUNCH",fg ="#0066ff",relief=FLAT)
launchButton.grid(row=2,columnspan=3)
launchButton.bind("<1>",launch)
root.mainloop()
