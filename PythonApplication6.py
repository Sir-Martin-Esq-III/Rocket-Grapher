"""
import tkinter as tk   # python3
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label = tk.tk.Label(self, text="This is the start page", font=TITLE_FONT)
        tk.Label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label = tk.tk.Label(self, text="This is page 1", font=TITLE_FONT)
        tk.Label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label = tk.tk.Label(self, text="This is page 2", font=TITLE_FONT)
        tk.Label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
"""

"""
This program plots the trajectory of a projectile using the SUVAT equations (That means no fancy physics, unfortunately).
"""
import tkinter as tk
from math import *
#Fonts/Styles
MainFont=("TkDefaultFont",15,"bold")
infoLableFont=("TkDefaultFont",10,"bold")
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
        for F in (stageingFrame, graphFrame):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

       # frame = stageingFrame(container,self)# Change to graph frame when it is developed
        frame.grid(row=5,column=0,sticky="nsew")
        self.showFrame("stageingFrame")

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
class stageingFrame(tk.Frame):
    currentStageNumber=0
  
    class Stages:
        stageNumber=None
        mass=None
        angle=None
        thrust=None
        amountOfFuel=None
        def __init__(self,number):
           self.stageNumber=number
           print("Last stage added %i" %(self.stageNumber))   

    startStage=Stages(0)
    stagesList.append(startStage)

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #Creates the menu bar   
        self.controller = controller
        stageValue=tk.StringVar()
        stageValue.set("Stage 0")    
        lable_stageValue=tk.Label(controller, textvariable=stageValue,fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_stageValue.place(x=(controller.winfo_screenwidth()/4)-22,y=0)
        
        #Mass widgets(Lable&Entry)
        mass=tk.StringVar()
        lable_Mass=tk.Label(controller, text="Mass",fg ="#8c8c8c",bg ="White",font=MainFont)   
        lable_Mass.place(y=150)  
        Entry_Mass=tk.Entry(controller,textvariable=mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Mass.place(y=200)
        
        #Angle widgets(Lable&Entry)
        angle=tk.StringVar()
        lable_Angle=tk.Label(controller, text="Angle",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Angle.place(x=(controller.winfo_screenwidth()/4)-22,y=150)
        Entry_Angle=tk.Entry(controller, textvariable=angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Angle.place(x=(controller.winfo_screenwidth()/4)-22,y=200)
        
        #Fuel widgets(Lable&Entry)
        fuel=tk.StringVar()
        lable_Fuel=tk.Label(controller, text="Fuel",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Fuel.place(x=(controller.winfo_screenwidth()/2)-100,y=150)
        Entry_Fuel=tk.Entry(controller, textvariable=fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Fuel.place(x=(controller.winfo_screenwidth()/2)-100,y=200)
        
        #Thrust widgets(Lable&Entry)
        thrust=tk.StringVar()
        lable_Thrust=tk.Label(controller, text="Engine thrust",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Thrust.place(y=300)
        Entry_Thrust=tk.Entry(controller, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=tk.FLAT)
        Entry_Thrust.place(y=350)
        #Creates the start stage(stage 0) and appends it to the list 

 
        #(TODO:)Remove the tk.Entry assignments on both left and right (they are redundant)
        #This function is called when a button is pressed which chaneges the current state(works like a queue)
        def changeStageState(event,option,):
            self.currentStageNumber
            #Add a stage
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
            stageValue.set("Stage %i"%(self.currentStageNumber))
            currentStage=stagesList[self.currentStageNumber]
            mass.set(str(currentStage.mass))
            angle.set(str(currentStage.angle))
            fuel.set(str(currentStage.amountOfFuel))
            thrust.set(str(currentStage.thrust))
        
        def saveStage(event):
            print("Saving stage%i"%(self.currentStageNumber))
            stagesList[self.currentStageNumber].mass=Entry_Mass.get()
            stagesList[self.currentStageNumber].angle=Entry_Angle.get()
            stagesList[self.currentStageNumber].amountOfFuel=Entry_Fuel.get()
            stagesList[self.currentStageNumber].thrust=Entry_Thrust.get()
            print(stagesList[self.currentStageNumber].mass,stagesList[self.currentStageNumber].angle,stagesList[self.currentStageNumber].amountOfFuel,stagesList[self.currentStageNumber].thrust)
        
        #Adds a stage to the rocket
        addStageButton=tk.Button(controller,text="   + Stage    ",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        addStageButton.place(x=(controller.winfo_screenwidth()/2)-125)
        addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=tk.Button(controller,text="Save Stage",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        saveStageButton.place(x=(controller.winfo_screenwidth()/2)-125,y=(parent.winfo_screenheight()/2)-45)
        saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=tk.Button(controller,text="<",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageLeft.place(x=(controller.winfo_screenwidth()/4)-100)
        cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))
        #Cycles to the stage after the current one# current stage=max then don't show
        cycleStageRight=tk.Button(controller,text=">",fg ="#E24A33 ",relief=tk.FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageRight.place(x=(controller.winfo_screenwidth()/4)+100)
        cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))
#Main loop
program=TrajectoryGrapher()
program.mainloop()

