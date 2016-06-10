from tkinter import *
from math import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#Fonts/Styles
MainFont=("TkDefaultFont",10,"bold")
headdingfont=("TkDefaultFont",10,"bold")

sideFrames=[None,None]
root = Tk()
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2
root.title("Rocket Science 9000")
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
root.config(background = 'white')
root.resizable(False,False)
#StageFrame
class stageFrame:
    #Class which has all of the variables for each stage
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

    newFrame=None
    x=None
    y=None
       
    def __init__(self,sideNumber):
        self.newframe=Frame(height=height,width=width/2)
        self.newframe.config(bg ="white")
        if sideNumber==0:
            x=0
            y=0
        else:
            x=width/2
            y=0
        #Create the frame
        self.newframe.place(x=x,y=y)
        #Begin UI placement
        lable_rocketValue=Label(self.newframe,text="Rocket "+str(sideNumber),fg ="#8c8c8c",bg ="White")
        lable_rocketValue.place(x=width/4,y=0)

        #Stage number
        stageValue=StringVar()
        stageValue.set("Stage 0")    
        lable_stageValue=Label(self.newframe, textvariable=stageValue,fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_stageValue.place(x=width/4,y=20)
        
        #Mass widgets(Lable&Entry)
        mass=DoubleVar()
        lable_Mass=Label(self.newframe, text="Mass(KG)",fg ="#8c8c8c",bg ="White",font=MainFont)   
        lable_Mass.place(x=0,y=40)  
        Entry_Mass=Entry(self.newframe,textvariable=mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Mass.place(x=0,y=60)
        
        #Angle widgets(Lable&Entry)
        angle=DoubleVar()
        lable_Angle=Label(self.newframe, text="Angle(°)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Angle.place(x=0,y=80)
        Entry_Angle=Entry(self.newframe, textvariable=angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Angle.place(x=0,y=100)
        
        #Fuel widgets(Lable&Entry)
        fuel=DoubleVar()
        lable_Fuel=Label(self.newframe, text="Fuel(L)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Fuel.place(x=0,y=120)
        Entry_Fuel=Entry(self.newframe, textvariable=fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Fuel.place(x=0,y=140)
        
        #Thrust widgets(Lable&Entry)
        thrust=DoubleVar()
        lable_Thrust=Label(self.newframe, text="Engine thrust(KN)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Thrust.place(x=0,y=160)
        Entry_Thrust=Entry(self.newframe, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Thrust.place(x=0,y=180)

        #Burn time widgets(Lable&Entry)
        burnTime=DoubleVar()
        lable_burnTime=Label(self.newframe, text="Burn Time(S)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_burnTime.place(x=0,y=200)
        Entry_burnTime=Entry(self.newframe, textvariable=burnTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_burnTime.place(x=0,y=220)    

        stageColor=StringVar()
        stageColor.set("#")
        lable_stageColor=Label(self.newframe, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_stageColor.place(x=0,y=240)
        Entry_stageColor=Entry(self.newframe, textvariable=stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_stageColor.place(x=0,y=260)
        #Entry_stageColor.bind("<FocusOut>",lambda event:saveColor(event))

        colorBox=Canvas(self.newframe, width=25, height=15)
        colorBox.place(x=100,y=260)
        colorBox.bind("<FocusOut>",lambda event:saveColor(event))

        #Adds a stage to the rocket
        addStageButton=Button(self.newframe,text="+ Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        addStageButton.place(x=(width/2)-100,y=20)
        #addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=Button(self.newframe,text="Save Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        saveStageButton.place(x=240,y=260)
       # saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=Button(self.newframe,text="<",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageLeft.place(x=(width/4)-20,y=20)
        #cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))
        #Cycles to the stage after the current one# current stage=max then don't show
        cycleStageRight=Button(self.newframe,text=">",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageRight.place(x=(width/4)+60,y=20)
       # cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))

        lable_graphOptions=Label(self.newframe, text="Graph config",fg ="#737373",bg ="White",font=headdingfont)
        lable_graphOptions.place(x=0,y=330)
        #Graph type lable
        lable_graphType=Label(self.newframe, text="Graph type",fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_graphType.place(x=0,y=350)
        #Save graph button
        launchButton=Button(self.newframe,text="Launch",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        launchButton.place(x=0,y=480)
        launchButton.bind("<Button-1>",lambda event:changeFrame(event,"Graph",sideNumber))# Bind to the function "launch"

        currentGraphType=StringVar()
        currentGraphType.set("Graph type") # default value
        graphTypes=["Displacement-Time",
                    "Velocity-Time",
                    "XDisplacement-YDisplacement",
                    "XVelocity-YVelocity"]
        w =  OptionMenu(self.newframe, currentGraphType , *graphTypes)
        w.place(x=0,y=350)

        

    # Destroys the frame
    def destroy(self,sideNumber):
        sideFrames[sideNumber].newframe.destroy()
        
#GraphFrame        
class graphFrame:
    newFrame=None
    canvas=None
    figure=None
    x=None

    def __init__(self,sideNumber):
        self.create(sideNumber)
        
    def create(self,sideNumber):
        self.newFrame=Frame(height=height,width=width/2)
        self.newFrame.config(bg ="white")
        if sideNumber==0:
            x=0
        else:
            x=width/2
        #Create the frame
        self.newFrame.place(x=x,y=0)
        #Begin graph creation
        figure = plt.figure(figsize=(2,2), dpi=100,frameon=False,tight_layout=True)
        plt.plot()
        canvas = FigureCanvasTkAgg(figure, self.newFrame)
        canvas._tkcanvas.config(highlightthickness=0,background="white")
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)

        launchButton3=Button(self.newFrame,text="Return to input",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
        launchButton3.place(x=0,y=0)
        launchButton3.bind("<1>",lambda event:changeFrame(event,"Input",sideNumber))
        
    # Destroys the frame
    def destroy(self,sideNumber):
        print(sideNumber)
        sideFrames[sideNumber].newFrame.destroy()
        sideFrames[sideNumber].newFrame.destroy()
       

        
def changeFrame(event,Type,sideNumber):
    Destroyer(event, sideNumber)
    if Type=="Input":
        sideFrames[sideNumber]=stageFrame(sideNumber)
    else:
        sideFrames[sideNumber]=graphFrame(sideNumber)
    print("Frame added: %s on side %i"%(str(sideFrames[sideNumber]),sideNumber))
    
def Destroyer(event,sideNumber):
    try:
        sideFrames[sideNumber].destroy(sideNumber)
    except AttributeError:
        print("Tried to destroy a frame that is not there")
    else:
        print("Frame destroyed: %s on side %i"%(str(sideFrames[sideNumber]),sideNumber))
        sideFrames[sideNumber]=None
        



def init():
    changeFrame(None,"Input",0)
    changeFrame(None,"Input",1)

init()
root.mainloop()
