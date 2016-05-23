import tkinter as tk
from math import *
#Fonts/Styles
MainFont=("TkDefaultFont",8,"bold")
headdingfont=("TkDefaultFont",10,"bold")
# This is they array that will hold of all of the class instances of Stages
stagesList=list()


class TrajectoryGrapher(tk.Tk):
    def __init__(self,*args,**kwargs):
        #inits tk and other window geomerty
        tk.Tk.__init__(self,*args,**kwargs)
        width=self.winfo_screenwidth()/2
        height=self.winfo_screenheight()/2
        self.title("Trajectory Grapher")
        self.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
        self.resizable(False,False)
        container=tk.Frame(self,bg="#fff")
        container.pack(side="top",fill="both",expand=True)
        #Creates a dictonary for all of the frames 
        self.frames={}
        for F in (setupFrame, graphFrame):
            page_name = F.__name__#Sets the page name as what is in 
            frame = F(container, self)
            self.frames[page_name] = frame
       # frame = stageingFrame(container,self)# Change to graph frame when it is developed
        frame.grid(row=5,column=0,sticky="nsew")
        self.showFrame("setupFrame")
        
    def showFrame(self,page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        
        
#Class which has all of the graph information
class graphFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        print("hello")
        
#Class which has all of help information
class helpFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

     
#Class which has all of the stageing information
#TODO: Add validation to the enrties
class setupFrame(tk.Frame):
    currentStageNumber=0
    #Contains all of the stageing vars for each stage
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
        
    #Changes the color of the canvas "colorBox" when the keyboard leaves the stage_color entry widget
    def saveColor(self,event):
        try:
            self.colorBox.config(bg=self.Entry_stageColor.get())
        except tk.TclError :
            print("Minor Error, color not defined, program will function as normal")
    
    #Changes the current state(and the widgets to match it)
    def changeStageState(self,event,
                         option,):
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
        self.stageValue.set("Stage %i"%(self.currentStageNumber))
        currentStage=stagesList[self.currentStageNumber]
        self.mass.set(str(currentStage.mass))
        self.angle.set(str(currentStage.angle))
        self.fuel.set(str(currentStage.amountOfFuel))
        self.thrust.set(str(currentStage.thrust))
        self.burnTime.set(str(currentStage.burnTime))
        try:
            self.colorBox.config(bg=currentStage.stageColor)
            self.stageColor.set(str(currentStage.stageColor))
        except tk.TclError:
            print("Minor Error, color not defined, program will function as normal")
        
    #Saves all of the enties as the variable in the current class instance
    def saveStage(self,event):
        print("Saving stage%i"%(self.currentStageNumber))
        stagesList[self.currentStageNumber].mass=self.Entry_Mass.get()
        stagesList[self.currentStageNumber].angle=self.Entry_Angle.get()
        stagesList[self.currentStageNumber].amountOfFuel=self.Entry_Fuel.get()
        stagesList[self.currentStageNumber].thrust=self.Entry_Thrust.get()
        stagesList[self.currentStageNumber].burnTime=self.Entry_burnTime.get()
        stagesList[self.currentStageNumber].stageColor=self.Entry_stageColor.get()  
    
    
    def __init__(self,parent,
                 controller):
        if len(stagesList)==0:
            startStage=self.Stages(0)
            stagesList.append(startStage)
        tk.Frame.__init__(self,parent) 
        self.controller = controller
        #Rocket config
        
        #Rocket config heading
        lable_rocketOptions=tk.Label(controller, text="Rocket config",fg ="#737373",bg ="White",font=headdingfont)
        lable_rocketOptions.place(x=controller.winfo_screenwidth()/4+300)
        
        #Stage value
        self.stageValue=tk.StringVar()
        self.stageValue.set("Stage 0")    
        self.lable_stageValue=tk.Label(controller, textvariable=self.stageValue,fg ="#8c8c8c",bg ="White",font=MainFont)
        self.lable_stageValue.place(x=controller.winfo_screenwidth()/4+330,y=30)
        
        #Mass widgets(Lable&Entry)
        self.mass=tk.DoubleVar()
        self.lable_Mass=tk.Label(controller, text="Mass(KG)",fg ="#8c8c8c",bg ="White",font=MainFont)   
        self.lable_Mass.place(x=controller.winfo_screenwidth()/4+290,y=50)  
        self.Entry_Mass=tk.Entry(controller,textvariable=self.mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_Mass.place(x=controller.winfo_screenwidth()/4+290,y=70)
        
        #Angle widgets(Lable&Entry)
        self.angle=tk.DoubleVar()
        self.lable_Angle=tk.Label(controller, text="Angle(°)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        self.lable_Angle.place(x=controller.winfo_screenwidth()/4+290,y=90)
        self.Entry_Angle=tk.Entry(controller, textvariable=self.angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_Angle.place(x=controller.winfo_screenwidth()/4+290,y=110)

       #Fuel widgets(Lable&Entry)
        self.fuel=tk.DoubleVar()
        self.lable_Fuel=tk.Label(controller, text="Fuel(L)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        self.lable_Fuel.place(x=controller.winfo_screenwidth()/4+290,y=130)
        self.Entry_Fuel=tk.Entry(controller, textvariable=self.fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_Fuel.place(x=controller.winfo_screenwidth()/4+290,y=150)
     
       #Thrust widgets(Lable&Entry)
        self.thrust=tk.DoubleVar()
        self.lable_Thrust=tk.Label(controller, text="Engine thrust(KN)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        self.lable_Thrust.place(x=controller.winfo_screenwidth()/4+290,y=170)
        self.Entry_Thrust=tk.Entry(controller, textvariable=self.thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_Thrust.place(x=controller.winfo_screenwidth()/4+290,y=190)
       
       #Burn time widgets(Lable&Entry)
        self.burnTime=tk.DoubleVar()
        self.lable_burnTime=tk.Label(controller, text="Burn Time(S)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        self.lable_burnTime.place(x=controller.winfo_screenwidth()/4+290,y=210)
        self.Entry_burnTime=tk.Entry(controller, textvariable=self.burnTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_burnTime.place(x=controller.winfo_screenwidth()/4+290,y=230)
       
       #Color widgets(canvas,lable&Entry)
        self.stageColor=tk.StringVar()
        self.stageColor.set("#")
        self.lable_stageColor=tk.Label(controller, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        self.lable_stageColor.place(x=controller.winfo_screenwidth()/4+290,y=250)
        self.Entry_stageColor=tk.Entry(controller, textvariable=self.stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        self.Entry_stageColor.place(x=controller.winfo_screenwidth()/4+290,y=270)
        self.Entry_stageColor.bind("<FocusOut>",lambda event:self.saveColor(event))
        self.colorBox=tk.Canvas(controller, width=25, height=15)
        self.colorBox.place(x=(controller.winfo_screenwidth()/2-70),y=270)

        
        #Adds a stage to the rocket
        self.addStageButton=tk.Button(controller,text="   + Stage    ",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        self.addStageButton.place(x=(controller.winfo_screenwidth()/2-60),y=30)
        self.addStageButton.bind("<Button-1>",lambda event:self.changeStageState(event,"Add"))
       #Save the values for the current stage
        self.saveStageButton=tk.Button(controller,text="Save Stage",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        self.saveStageButton.place(x=(controller.winfo_screenwidth()/2-70),y=300)
        self.saveStageButton.bind("<Button-1>",lambda event:self.saveStage(event))
       #Cycles to the stage before the current one current stage=0 then don't show
        self.cycleStageLeft=tk.Button(controller,text="<",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        self.cycleStageLeft.place(x=controller.winfo_screenwidth()/4+290,y=30)
        self.cycleStageLeft.bind("<Button-1>",lambda event:self.changeStageState(event,"Left"))
       #Cycles to the stage after the current one# current stage=max then don't show
        self.cycleStageRight=tk.Button(controller,text=">",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        self.cycleStageRight.place(x=controller.winfo_screenwidth()/4+400,y=30)
        self.cycleStageRight.bind("<Button-1>",lambda event:self.changeStageState(event,"Right"))
       
      #Graph config TODO: add a drop down box with the graph types, add a function to save the current graph
       
        #Graph config headding
        self.lable_graphOptions=tk.Label(controller, text="Graph config",fg ="#737373",bg ="White",font=headdingfont)
        self.lable_graphOptions.place(x=(controller.winfo_screenwidth()/2)-150,y=330)
       #Graph type label
        self.lable_graphType=tk.Label(controller, text="Graph type",fg ="#8c8c8c",bg ="White",font=MainFont)
        self.lable_graphType.place(x=controller.winfo_screenwidth()/4+150,y=350)
       #Save graph button
        self.saveGraphButton=tk.Button(controller,text="Save Graph",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        self.saveGraphButton.place(x=controller.winfo_screenwidth()/2-70,y=380)
        
            
#Main loop
program=TrajectoryGrapher()
program.mainloop()
