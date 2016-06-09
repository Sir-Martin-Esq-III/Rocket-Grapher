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

StageFrames=[None,None]
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
    def __init__(self,number):
        self.create(number)
        
    def create(self,number):
        currentStageNumber=0
        print(number)
        stageFrame.newFrame=Frame(height=height,width=width/2)
        stageFrame.newFrame.config(bg ="White")
        if number==0:
            x=0
            y=0
        else:
            x=width/2
            y=0
        #Create the frame
        stageFrame.newFrame.place(x=x,y=y)
        #Begin UI placement
        lable_rocketValue=Label(stageFrame.newFrame,text="Rocket "+str(number),fg ="#8c8c8c",bg ="White")
        lable_rocketValue.place(x=width/4,y=0)

        #Stage number
        stageValue=StringVar()
        stageValue.set("Stage 0")    
        lable_stageValue=Label(stageFrame.newFrame, textvariable=stageValue,fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_stageValue.place(x=width/4,y=20)
        
        #Mass widgets(Lable&Entry)
        mass=DoubleVar()
        lable_Mass=Label(stageFrame.newFrame, text="Mass(KG)",fg ="#8c8c8c",bg ="White",font=MainFont)   
        lable_Mass.place(x=0,y=40)  
        Entry_Mass=Entry(stageFrame.newFrame,textvariable=mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Mass.place(x=0,y=60)
        
        #Angle widgets(Lable&Entry)
        angle=DoubleVar()
        lable_Angle=Label(stageFrame.newFrame, text="Angle(°)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Angle.place(x=0,y=80)
        Entry_Angle=Entry(stageFrame.newFrame, textvariable=angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Angle.place(x=0,y=100)
        
        #Fuel widgets(Lable&Entry)
        fuel=DoubleVar()
        lable_Fuel=Label(stageFrame.newFrame, text="Fuel(L)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Fuel.place(x=0,y=120)
        Entry_Fuel=Entry(stageFrame.newFrame, textvariable=fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Fuel.place(x=0,y=140)
        
        #Thrust widgets(Lable&Entry)
        thrust=DoubleVar()
        lable_Thrust=Label(stageFrame.newFrame, text="Engine thrust(KN)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_Thrust.place(x=0,y=160)
        Entry_Thrust=Entry(stageFrame.newFrame, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Thrust.place(x=0,y=180)

        #Burn time widgets(Lable&Entry)
        burnTime=DoubleVar()
        lable_burnTime=Label(stageFrame.newFrame, text="Burn Time(S)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_burnTime.place(x=0,y=200)
        Entry_burnTime=Entry(stageFrame.newFrame, textvariable=burnTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_burnTime.place(x=0,y=220)    

        stageColor=StringVar()
        stageColor.set("#")
        lable_stageColor=Label(stageFrame.newFrame, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=MainFont)     
        lable_stageColor.place(x=0,y=240)
        Entry_stageColor=Entry(stageFrame.newFrame, textvariable=stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_stageColor.place(x=0,y=260)
        #Entry_stageColor.bind("<FocusOut>",lambda event:saveColor(event))

        colorBox=Canvas(stageFrame.newFrame, width=25, height=15)
        colorBox.place(x=100,y=260)
        #colorBox.bind("<FocusOut>",lambda event:saveColor(event))

        #Adds a stage to the rocket
        addStageButton=Button(stageFrame.newFrame,text="+ Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        addStageButton.place(x=400,y=20)
        #addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=Button(stageFrame.newFrame,text="Save Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        saveStageButton.place(x=400,y=260)
       # saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=Button(stageFrame.newFrame,text="<",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageLeft.place(x=(width/4)-20,y=20)
        #cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))
        #Cycles to the stage after the current one# current stage=max then don't show
        cycleStageRight=Button(stageFrame.newFrame,text=">",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        cycleStageRight.place(x=(width/4)+60,y=20)
       # cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))

        lable_graphOptions=Label(stageFrame.newFrame, text="Graph config",fg ="#737373",bg ="White",font=headdingfont)
        lable_graphOptions.place(x=0,y=330)
        #Graph type lable
        lable_graphType=Label(stageFrame.newFrame, text="Graph type",fg ="#8c8c8c",bg ="White",font=MainFont)
        lable_graphType.place(x=0,y=350)
        #Save graph button
        launchButton=Button(stageFrame.newFrame,text="Launch",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=MainFont)
        launchButton.place(x=0,y=480)
        launchButton.bind("<Button-1>",lambda event:newFrame(event,"Graph",number))# Bind to the function "launch"

        currentGraphType=StringVar()
        currentGraphType.set("Graph type") # default value
        graphTypes=["Displacement-Time",
                    "Velocity-Time",
                    "XDisplacement-YDisplacement",
                    "XVelocity-YVelocity"]
        w =  OptionMenu(stageFrame.newFrame, currentGraphType , *graphTypes)
        w.place(x=0,y=350)

        

    # Destroys the frame
    def destroy(self,number):
        stageFrame.newFrame.destroy()
        
#GraphFrame        
class graphFrame:
    newFrame=None
    canvas=None
    figure=None
    x=None
    Y=None

    def __init__(self,number):
        self.create(number)
        
    def create(self,number):
        graphFrame.newFrame=Frame(height=height,width=width)
        if number==0:
            x=0
            y=0
        else:
            x=width/2
            y=0
        #Create the frame
        graphFrame.newFrame.place(x=x,y=y)
        #Begin graph creation
        figure = plt.figure(figsize=(4,5), dpi=100,frameon=False,tight_layout=True)
        plt.plot()
        canvas = FigureCanvasTkAgg(figure, graphFrame.newFrame)
       # canvas._tkcanvas.config(highlightthickness=0)
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)

        launchButton3=Button(graphFrame.newFrame,text="Return to input",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
        launchButton3.place(x=0,y=0)
        launchButton3.bind("<1>",lambda event:newFrame(event,"Input",number))
        
    # Destroys the frame
    def destroy(self,number):
        #canvas.get_tk_widget().destroy()
        StageFrames[number].newFrame.destroy()
       

        
def newFrame(event,Type,number):
    if StageFrames[number]!= None:
        Destroyer(event, number)
    if Type=="Input":
        StageFrames[number]=stageFrame(number)
    else:
        StageFrames[number]=graphFrame(number)
    print("New frame added",StageFrames)
    
def Destroyer(event,number):
    try:
        StageFrames[number].destroy(number)
    except AttributeError:
        print("There is nothing there")
    StageFrames[number]=None
    print("Frame destroyed",StageFrames)

#Input buttons
launchButton1=Button(root,text="ADD 1",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton1.place(x=0,y=150)
launchButton1.bind("<1>",lambda event:newFrame(event,"Input",0))

launchButton2=Button(root,text="ADD 2",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton2.place(x=0,y=250)
launchButton2.bind("<1>",lambda event:newFrame(event,"Input",1))

launchButton3=Button(root,text="DSET 1",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton3.place(x=0,y=200)
launchButton3.bind("<1>",lambda event:Destroyer(event,0))

launchButton4=Button(root,text="DSET 2",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton4.place(x=0,y=300)
launchButton4.bind("<1>",lambda event:Destroyer(event,1))

#Graph buttons
launchButton5=Button(root,text="ADD G 1",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton5.place(x=0,y=350)
launchButton5.bind("<1>",lambda event:newFrame(event,"Graph",0))

launchButton6=Button(root,text="ADD G 2",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton6.place(x=0,y=400)
launchButton6.bind("<1>",lambda event:newFrame(event,"Graph",1))

launchButton7=Button(root,text="DSET G 1",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton7.place(x=0,y=450)
launchButton7.bind("<1>",lambda event:Destroyer(event,0))

launchButton8=Button(root,text="DSET G 2",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
launchButton8.place(x=0,y=500)
launchButton8.bind("<1>",lambda event:Destroyer(event,1))

def init():
    newFrame(None,"Input",0)
    newFrame(None,"Input",1)

init()



root.mainloop()
