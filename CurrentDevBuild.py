import tkinter as tk
from math import *

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')





#Fonts/Styles
MainFont=("TkDefaultFont",8,"bold")
headdingfont=("TkDefaultFont",10,"bold")
# This is they array that will hold of all of the class instances of Stages
stagesList=list()
graphType=""
xvalues= [None] * 18
yvalues= [None] * 18
lastXVel=0
lastYVel=0
x_AxisLable=""
y_AxisLable=""

class TrajectoryGrapher(tk.Tk):
    def __init__(self,*args,**kwargs):
        #inits tk and other window geomerty
        tk.Tk.__init__(self,*args,**kwargs)
        width=self.winfo_screenwidth()/2
        height=self.winfo_screenheight()/2
        self.title("Rocket Science 9000")
        self.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
        self.resizable(False,False)
        container=tk.Frame(self,bg="#fff")
        container.pack(side="top",fill="both",expand=True)
        #Creates a dictonary for all of the frames 
        self.frames={}
        for F in (stageingFrame, graphFrame):
            page_name = F.__name__#Sets the page name as what is in 
            frame = F(container, self)
            self.frames[page_name] = frame
        frame = stageingFrame(container,self)# Change to graph frame when it is developed
        frame.grid(row=5,column=0,sticky="nsew")
        self.showFrame("stageingFrame")
        
        
    def showFrame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        
def math(angle,stageNumber,
         engineThrust,burnTime,
         mass,fuel,
         graphType):
    global x_AxisLable
    global y_AxisLable
    
    gravity=9.81
    TWR=(int(engineThrust/mass*gravity))
    resForce=(engineThrust-(mass*gravity))
    velocity=(resForce*burnTime)/mass
    global lastXVel
    global lastYVel
    Xcomp=velocity*(cos(radians(angle)))#cos
    Ycomp=velocity*(sin(radians(angle)))#sin
    time=(2*Ycomp)/gravity
    maxHorizDisp=time*Xcomp
    maxVertDisp=(-(Ycomp**2)/(2*-gravity))
    #TWR=engine thrust/mass*gravity
    print(stageNumber)                            
    if graphType=="Displacement-Time":
        x_AxisLable=""
        y_AxisLable=""
        print(graphType)
        #Do the math to plot all this graph
    elif graphType=="Velocity-Time":
        x_AxisLable=""
        y_AxisLable=""
        print(graphType)
        #Do the math to plot all this graph
    elif graphType=="XDisplacement-YDisplacement":
        x_AxisLable="X-Displacement(m)"
        y_AxisLable="y-Displacement(m)"
        for i in range(0,36):
         updateTime=(time*(i/35))
         if updateTime>time/2:
             lastXVel=xvalues[len(xvalues)-1]
             lastYVel=yvalues[len(yvalues)-1]
             break
         else:
             #Check for graph type
             if stageNumber!=0:
                 yvalues[i]=((lastYVel)+(Ycomp*updateTime)+((-1/2*gravity)*(updateTime*updateTime)))
                 xvalues[i]=((lastXVel)+(updateTime*Xcomp))
             else:
                 yvalues[i]=((Ycomp*updateTime)+((-1/2*gravity)*(updateTime*updateTime)))
                 xvalues[i]=(updateTime*Xcomp) 

         print(graphType)
        #Do the math to plot all this graph
    elif graphType=="XVelocity-YVelocity":
        #X v is constant
        #v=u+at
        x_AxisLable=""
        y_AxisLable=""
        
        

        
#Class which has all of the graph information
class graphFrame(tk.Frame):
    #Creates a graph on class init so that it displays it when the program runs
    def __init__(self,parent,controller):
        global Controller
        Controller=controller
        tk.Frame.__init__(self,parent)
        f = plt.figure(figsize=(4,5), dpi=100,frameon=False,tight_layout=True)
        plt.plot()
        canvas = FigureCanvasTkAgg(f, Controller)
        canvas._tkcanvas.config(highlightthickness=0)
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)

    def updateGraph(self,controller,graphType):
        f = plt.figure(figsize=(4,5), dpi=100,frameon=False,tight_layout=True)
        a = f.add_subplot(111)
        for i in range(len(stagesList)):
            math(stagesList[i].angle,stagesList[i].stageNumber,
                 stagesList[i].thrust,stagesList[i].burnTime,
                 stagesList[i].mass,stagesList[i].amountOfFuel,
                 graphType)
            
            color=stagesList[i].stageColor
            print(str(color))
            #Call the math function and return the plots
            a=plt.plot(xvalues,yvalues)
            plt.setp(a, color=color, linewidth=2.0)
        plt.ylabel(y_AxisLable)
        plt.xlabel(x_AxisLable)
        canvas = FigureCanvasTkAgg(f, Controller)
        canvas._tkcanvas.config(highlightthickness=0)
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)
            

#Class which has all of the stageing information
#TODO: Add validation to the enrties
class stageingFrame(tk.Frame):
    currentStageNumber=0
    
    class Stages:
        stageNumber=None
        mass=None
        angle=None
        thrust=None
        amountOfFuel=None
        burnTime=None
        stageColor=None
        def __init__(self,number):
           self.stageNumber=number
           print("Last stage added %i" %(self.stageNumber))
        
    def __init__(self,parent,controller):
        if len(stagesList)==0:
            startStage=self.Stages(0)
            stagesList.append(startStage)
        tk.Frame.__init__(self,parent) 
        self.controller = controller
        #Rocket config
        
        #Rocket config heading
        lable_rocketOptions=tk.Label(controller, text="Rocket config",fg ="#737373",bg ="White",font=headdingfont)
        lable_rocketOptions.place(x=(controller.winfo_screenwidth()/2)-150)
        
        #Stage value
        stageValue=tk.StringVar()
        stageValue.set("Stage 0")    
        lable_stageValue=tk.Label(controller, textvariable=stageValue,fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_stageValue.place(x=(controller.winfo_screenwidth()/2)-150,y=30)
        
        #Mass widgets(Lable&Entry)
        mass=tk.DoubleVar()
        lable_Mass=tk.Label(controller, text="Mass(KG)",fg ="#8c8c8c",bg ="White",font=MainFont)   
        lable_Mass.place(x=controller.winfo_screenwidth()/4+150,y=50)  
        Entry_Mass=tk.Entry(controller,textvariable=mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Mass.place(x=controller.winfo_screenwidth()/4+150,y=70)
        
        #Angle widgets(Lable&Entry)
        angle=tk.DoubleVar()
        lable_Angle=tk.Label(controller, text="Angle(°)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Angle.place(x=controller.winfo_screenwidth()/4+150,y=90)
        Entry_Angle=tk.Entry(controller, textvariable=angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Angle.place(x=controller.winfo_screenwidth()/4+150,y=110)
        
        #Fuel widgets(Lable&Entry)
        fuel=tk.DoubleVar()
        lable_Fuel=tk.Label(controller, text="Fuel(L)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Fuel.place(x=controller.winfo_screenwidth()/4+150,y=130)
        Entry_Fuel=tk.Entry(controller, textvariable=fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Fuel.place(x=controller.winfo_screenwidth()/4+150,y=150)
        
        #Thrust widgets(Lable&Entry)
        thrust=tk.DoubleVar()
        lable_Thrust=tk.Label(controller, text="Engine thrust(KN)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Thrust.place(x=controller.winfo_screenwidth()/4+150,y=170)
        Entry_Thrust=tk.Entry(controller, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Thrust.place(x=controller.winfo_screenwidth()/4+150,y=190)

        #Burn time widgets(Lable&Entry)
        burnTime=tk.DoubleVar()
        lable_burnTime=tk.Label(controller, text="Burn Time(S)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_burnTime.place(x=controller.winfo_screenwidth()/4+150,y=210)
        Entry_burnTime=tk.Entry(controller, textvariable=burnTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_burnTime.place(x=controller.winfo_screenwidth()/4+150,y=230)
        
        #Color widgets(canvas,lable&Entry)
        stageColor=tk.StringVar()
        stageColor.set("#")
        lable_stageColor=tk.Label(controller, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_stageColor.place(x=controller.winfo_screenwidth()/4+150,y=250)
        Entry_stageColor=tk.Entry(controller, textvariable=stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_stageColor.place(x=controller.winfo_screenwidth()/4+150,y=270)
        Entry_stageColor.bind("<FocusOut>",lambda event:saveColor(event))
        colorBox=tk.Canvas(controller, width=25, height=15)
        colorBox.place(x=(controller.winfo_screenwidth()/2-70),y=270)
        colorBox.bind("<FocusOut>",lambda event:saveColor(event))

        #Adds a stage to the rocket
        addStageButton=tk.Button(controller,text="   + Stage    ",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        addStageButton.place(x=(controller.winfo_screenwidth()/2-60),y=30)
        addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=tk.Button(controller,text="Save Stage",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        saveStageButton.place(x=(controller.winfo_screenwidth()/2-70),y=300)
        saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=tk.Button(controller,text="<",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageLeft.place(x=(controller.winfo_screenwidth()/4)+150,y=30)
        cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))
        #Cycles to the stage after the current one# current stage=max then don't show
        cycleStageRight=tk.Button(controller,text=">",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageRight.place(x=(controller.winfo_screenwidth()/4)+220,y=30)
        cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))

        #Graph config TODO: add a drop down box with the graph types, add a function to save the current graph
        
        #Graph config headding
        lable_graphOptions=tk.Label(controller, text="Graph config",fg ="#737373",bg ="White",font=headdingfont)
        lable_graphOptions.place(x=(controller.winfo_screenwidth()/2)-150,y=330)
        #Graph type labe
        lable_graphType=tk.Label(controller, text="Graph type",fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_graphType.place(x=controller.winfo_screenwidth()/4+150,y=350)
        #Save graph button
        launchButton=tk.Button(controller,text="Launch",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        launchButton.place(x=controller.winfo_screenwidth()/2-70,y=480)
        launchButton.bind("<Button-1>",lambda event:launch(event))# Bind to the function "launch"

        currentGraphType=tk.StringVar()
        currentGraphType.set("Graph type") # default value
        graphTypes=["Displacement-Time",
                    "Velocity-Time",
                    "XDisplacement-YDisplacement",
                    "XVelocity-YVelocity"]
        w =  tk.OptionMenu(controller, currentGraphType , *graphTypes)
        w.place(x=controller.winfo_screenwidth()/4+125,y=350)

#I need to remove the functions from the INIT 
        
        #Changes the color of the canvas when the keyboard leaves the colorBox entry widget
        def saveColor(event):
            colorBox.config(bg=Entry_stageColor.get())
            
        def launch(event):
            graphType=currentGraphType.get()
            print(graphType)
            graphFrame.updateGraph(TrajectoryGrapher,controller,graphType)
            
            
       
        #This function is called when a button is pressed which chaneges the current state(works like a queue)
        def changeStageState(event,option,):
            self.currentStageNumber
            #Add a stage. Does this by increaseing the stageNumber, createing a class instance of "Stages" and then appending that instance to and array
            if option=="Add":
                self.currentStageNumber=len(stagesList)
                currentStage=self.Stages(self.currentStageNumber)
                stagesList.append(currentStage)
            #Cycle left
            elif option=="Left":
                if self.currentStageNumber!=0:
                    self.currentStageNumber-=1
            #Cycle right
            elif option=="Right":
                if self.currentStageNumber<len(stagesList)-1:
                    self.currentStageNumber+=1
            #Sets all of the entry widgets to the value of the currentStages class instance 
            stageValue.set("Stage %i"%(self.currentStageNumber))
            currentStage=stagesList[self.currentStageNumber]
            mass.set(str(currentStage.mass))
            angle.set(str(currentStage.angle))
            fuel.set(str(currentStage.amountOfFuel))
            thrust.set(str(currentStage.thrust))
            burnTime.set(str(currentStage.burnTime))
            colorBox.config(bg=currentStage.stageColor)
            stageColor.set(str(currentStage.stageColor))
            
        #Saves all of the enties as the variable in the current class instance
        def saveStage(event):
            print("Saving stage%i"%(self.currentStageNumber))
            stagesList[self.currentStageNumber].mass=int(Entry_Mass.get())
            stagesList[self.currentStageNumber].angle=int(Entry_Angle.get())
            stagesList[self.currentStageNumber].amountOfFuel=int(Entry_Fuel.get())
            stagesList[self.currentStageNumber].thrust=int(Entry_Thrust.get())
            stagesList[self.currentStageNumber].burnTime=int(Entry_burnTime.get())
            stagesList[self.currentStageNumber].stageColor=str(Entry_stageColor.get())
                        
            
#Main loop
program=TrajectoryGrapher()
program.mainloop()

