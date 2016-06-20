from tkinter import *
from math import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import animation


sideFrames=[None,None]
r0StagesList=list()#List of the stages for Rocket0
r1StagesList=list() #List of the stages for Rocket1

root = Tk()
#Gets the height and width of the monitor
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2
root.title("Rocket Science 9000")
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
#root.config(background = 'white')
root.resizable(False,False)

#StageFrame
class stageFrame:
    mainFont=("TkDefaultFont",10,"bold")
    titleFont=("TkDefaultFont",12,"bold")
    #Current stage numbers for each rocket
    r0currentStageNumber=0
    r1currentStageNumber=0
    #Frame
    newFrame=None
    #X/Y pos for frame
    x=None

    #Class which has all of the variables for each stage
    class Stages:
        mass=None
        angle=None
        thrust=None
        amountOfFuel=None
        burnTime=None
        stageColor=None

    def __init__(self,sideNumber):
    
        #This is so that there is a stage on INIT (so shit don't burn to the ground)
        if sideNumber==0:
            if len(r0StagesList)==0:
                startStage=self.Stages()
                r0StagesList.append(startStage)
        else:
           if len(r1StagesList)==0:
            startStage=self.Stages()
            r1StagesList.append(startStage)

        #Updates the color box 
        def updateColorBox(event):
            try:
                colorBox.config(bg=Entry_stageColor.get())
            except TclError:
                print("Error: %s is not a color. Please use the correct formatting: #000000"%(Entry_stageColor.get()))

        #Saves the current stage
        def saveStage(event):
            try:
                if sideNumber==0:
                    print("Saving stage%i from input field %i"%(self.r0currentStageNumber,sideNumber))
                    r0StagesList[self.r0currentStageNumber].mass=float(Entry_Mass.get())
                    r0StagesList[self.r0currentStageNumber].angle=float(Entry_Angle.get())
                    r0StagesList[self.r0currentStageNumber].amountOfFuel=float(Entry_Fuel.get())
                    r0StagesList[self.r0currentStageNumber].thrust=float(Entry_Thrust.get())
                    r0StagesList[self.r0currentStageNumber].burnTime=float(Entry_burnTime.get())
                    r0StagesList[self.r0currentStageNumber].stageColor=str(Entry_stageColor.get())
                else:
                    print("Saving stage%i from input field %i"%(self.r1currentStageNumber,sideNumber))
                    r1StagesList[self.r1currentStageNumber].mass=float(Entry_Mass.get())
                    r1StagesList[self.r1currentStageNumber].angle=float(Entry_Angle.get())
                    r1StagesList[self.r1currentStageNumber].amountOfFuel=float(Entry_Fuel.get())
                    r1StagesList[self.r1currentStageNumber].thrust=float(Entry_Thrust.get())
                    r1StagesList[self.r1currentStageNumber].burnTime=float(Entry_burnTime.get())
                    r1StagesList[self.r1currentStageNumber].stageColor=str(Entry_stageColor.get())
            except ValueError:
                print("An error occoured causing the stage not to save")
        #Changes the current stage
        def changeStageState(event,option):
             #Add a stage. Does this by increaseing the stageNumber, createing a class instance of "Stages" and then appending that instance to and array
            if option=="Add":
                if sideNumber==0:
                    self.r0currentStageNumber =len(r0StagesList)
                    currentStage=self.Stages()
                    r0StagesList.append(currentStage)
                    print("Last stage added %i to rocket%i" %(self.r0currentStageNumber,sideNumber))
                else:
                    self.r1currentStageNumber =len(r1StagesList)
                    currentStage=self.Stages()
                    r1StagesList.append(currentStage)
                    print("Last stage added %i to rocket%i" %(self.r1currentStageNumber,sideNumber))
                
            #Cycle left
            elif option=="Left":
                if sideNumber==0:
                    if self.r0currentStageNumber!=0:
                        self.r0currentStageNumber-=1
                else:
                    if self.r1currentStageNumber!=0:
                        self.r1currentStageNumber-=1
            #Cycle right
            elif option=="Right":
                if sideNumber==0:
                    if self.r0currentStageNumber<len(r0StagesList)-1:
                        self.r0currentStageNumber+=1
                else:
                    if self.r1currentStageNumber<len(r1StagesList)-1:
                        self.r1currentStageNumber+=1

            #Sets all of the entry widgets to the value of the currentStages class instance 
            if sideNumber==0:
                stageValue.set("Stage %i"%(self.r0currentStageNumber))
                currentStage=r0StagesList[self.r0currentStageNumber]
            else:
                stageValue.set("Stage %i"%(self.r1currentStageNumber))
                currentStage=r1StagesList[self.r1currentStageNumber]
            mass.set(str(currentStage.mass))
            angle.set(str(currentStage.angle))
            fuel.set(str(currentStage.amountOfFuel))
            thrust.set(str(currentStage.thrust))
            burnTime.set(str(currentStage.burnTime))
            colorBox.config(bg=currentStage.stageColor)
            stageColor.set(str(currentStage.stageColor))
        #Create a new frame
        self.newframe=Frame(height=height,width=width/2)
        self.newframe.config(bg ="white")
        #Get X coord
        if sideNumber==0:
            x=0
        else:
            x=width/2
        #Place the new frame
        self.newframe.place(x=x,y=0)
        """---BEGIN UI PLACEMENT---"""
        lable_rocketValue=Label(self.newframe,text="Rocket "+str(sideNumber),fg ="#8c8c8c",bg ="White",font=self.titleFont)
        lable_rocketValue.place(x=width/4,y=0)

        #Stage number
        stageValue=StringVar()
        stageValue.set("Stage 0")    
        lable_stageValue=Label(self.newframe, textvariable=stageValue,fg ="#8c8c8c",bg ="White",font=self.mainFont)
        lable_stageValue.place(x=width/4,y=20)
        
        #Mass widgets(Lable&Entry)
        mass=DoubleVar()
        lable_Mass=Label(self.newframe, text="Mass(KG)",fg ="#8c8c8c",bg ="White",font=self.mainFont)   
        lable_Mass.place(x=0,y=40)  
        Entry_Mass=Entry(self.newframe,textvariable=mass, fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Mass.place(x=0,y=60)
        
        #Angle widgets(Lable&Entry)
        angle=DoubleVar()
        lable_Angle=Label(self.newframe, text="Angle(°)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_Angle.place(x=0,y=80)
        Entry_Angle=Entry(self.newframe, textvariable=angle,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Angle.place(x=0,y=100)
        
        #Fuel widgets(Lable&Entry)
        fuel=DoubleVar()
        lable_Fuel=Label(self.newframe, text="Fuel(L)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_Fuel.place(x=0,y=120)
        Entry_Fuel=Entry(self.newframe, textvariable=fuel,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Fuel.place(x=0,y=140)
        
        #Thrust widgets(Lable&Entry)
        thrust=DoubleVar()
        lable_Thrust=Label(self.newframe, text="Engine thrust(KN)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_Thrust.place(x=0,y=160)
        Entry_Thrust=Entry(self.newframe, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Thrust.place(x=0,y=180)

        #Burn time widgets(Lable&Entry)
        burnTime=DoubleVar()
        lable_burnTime=Label(self.newframe, text="Burn Time(S)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_burnTime.place(x=0,y=200)
        Entry_burnTime=Entry(self.newframe, textvariable=burnTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_burnTime.place(x=0,y=220)    

        #Color widgets(canvas,Lable&Entry)
        stageColor=StringVar()
        stageColor.set("#")
        lable_stageColor=Label(self.newframe, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_stageColor.place(x=0,y=240)
        Entry_stageColor=Entry(self.newframe, textvariable=stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_stageColor.place(x=0,y=260)
        Entry_stageColor.bind("<FocusOut>",lambda event:updateColorBox(event))
        colorBox=Canvas(self.newframe, width=25, height=15)
        colorBox.place(x=100,y=260)

        #Adds a stage to the rocket
        addStageButton=Button(self.newframe,text="+ Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        addStageButton.place(x=(width/2)-100,y=20)
        addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=Button(self.newframe,text="Save Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        saveStageButton.place(x=240,y=260)
        saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=Button(self.newframe,text="<",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        cycleStageLeft.place(x=(width/4)-20,y=20)
        cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))

        #Cycles to the stage after the current one#current stage=max then don't show
        cycleStageRight=Button(self.newframe,text=">",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        cycleStageRight.place(x=(width/4)+60,y=20)
        cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))

        lable_graphOptions=Label(self.newframe, text="Graph type",fg ="#737373",bg ="White",font=self.mainFont)
        lable_graphOptions.place(x=0,y=330)
        #Graph widgets
        lable_graphType=Label(self.newframe, text="Graph type",fg ="#8c8c8c",bg ="White",font=self.mainFont)
        lable_graphType.place(x=0,y=350)
        
        currentGraphType=StringVar()
        currentGraphType.set("Displacement-Time") #default value
        graphTypes=["Displacement-Time",
                    "Velocity-Time",
                    "XDisplacement-YDisplacement",
                    "XVelocity-YVelocity"]
        w =  OptionMenu(self.newframe, currentGraphType , *graphTypes)
        w.place(x=0,y=350)

        #Launch button
        launchButton=Button(self.newframe,text="Launch",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        launchButton.place(x=0,y=height-50)
        launchButton.bind("<Button-1>",lambda event:launch(event))#Bind to the function "launch"

        def launch(event):
            graphType=str(currentGraphType.get())
            changeFrame(event,"Graph",sideNumber,graphType)
            
        #This is so when we graph->input it loads current stage
        changeStageState(None,"None")
 

    #Destroys the frame
    def destroy(self,sideNumber):
        sideFrames[sideNumber].newframe.destroy()
        
#GraphFrame        
class graphFrame:
    style.use('ggplot')
    newFrame=None
    canvas=None
    figure=None
    x=None
    vel=10 #temp
    xplot=0
    yplot=0
    stagesListUsed=None
    lastX=0
    lastY=0
    totalTime=0

    def getPlots(self,totalMass,angle,engineThrust,amountOfFuel,burnTime,graphType):
        xValues=list()
        yValues=list()
        xAxis=""
        yAxis=""
        g=9.81
        #print(self.lastY)
        #Resolving the vector into v/h components 
        verticalForce=engineThrust*(sin(radians(angle)))
        horizontalForce=engineThrust*(cos(radians(angle)))
        #Net Forces
        netVForce=verticalForce-(totalMass*g)#Upthrust-weight
        #Acceleration
        verticalAcc=(netVForce/totalMass)#A=F/M
        horizontalAcc=(horizontalForce/totalMass)
        for i in range(0,36):
            updateTime=(burnTime*(i/35))+self.totalTime
            amountOfFuel-=10
            if (amountOfFuel<0):
                #Burn stops              
                print("verticalVel<0 or (amountOfFuel<0)")
                #verticalVel+= g*(updateTime-burnTime*(i-1/35))/self.lastY V=(g*t)/u
                #self.lastX=horizontalVel
                #self.lastY=verticalVel
                #break
            #Velocity
            #print("Last y",self.lastY,"Last x",self.lastX)
            verticalVel=(verticalAcc*updateTime)# V=AT+u
            horizontalVel=(horizontalAcc*updateTime)
            #print(updateTime)
            print("Vv ",verticalVel,"Vh ",horizontalVel)
            #print(graphType)
            
            if graphType=="('Displacement-Time',)":
                yValues.append(((verticalVel**2)/(2*g))+self.lastY)#v^2=u^2+2as
                xValues.append(updateTime)
                xAxis="Time"
                yAxis="Vertical displacement"
            elif graphType=="('Velocity-Time',)":
                yValues.append(verticalVel+self.lastY)
                xValues.append(updateTime)
                xAxis="Time"
                yAxis="Vertical velocity"
            elif graphType=="('XDisplacement-YDisplacement',)":
                yValues.append((verticalVel**2)/(2*g))
                xValues.append(horizontalVel*updateTime)
                xAxis="Horizontal displacement"
                yAxis="Vertical displacement"
            elif graphType=="('XVelocity-YVelocity',)":
                yValues.append(verticalVel+self.lastY)
                xValues.append(horizontalVel+self.lastX)
                xAxis="Horizontal velocity"
                yAxis="Vertical velocity"
        self.lastY=verticalVel
        self.lastX=horizontalVel
        self.totalTime=updateTime
        print("LAST Y",self.lastY,"LAST X",self.lastX)
        return(xValues,yValues,xAxis,yAxis)
        
    def __init__(self,sideNumber,graphType):
        xAxisText=""
        yAxisText=""
        self.newFrame=Frame(height=height,width=width/2)
        self.newFrame.config(bg ="white")
        if sideNumber==0:
            x=0
        else:
            x=width/2
        #Create the frame
        self.newFrame.place(x=x,y=0)
        widthInches= root.winfo_screenwidth() / root.winfo_fpixels('1i')
        heightInches= root.winfo_screenheight() / root.winfo_fpixels('1i')
        #Begin graph creation
        figure = plt.figure(figsize=(((widthInches/4)-.2),(heightInches/2)-.2), dpi=100,frameon=False,tight_layout=True)        
        if sideNumber==0:
            stagesListUsed=r0StagesList
        else:
            stagesListUsed=r1StagesList
        for i in range(len(stagesListUsed)):
# should I move this get plots()?
            totalMass=0
            #Find the total mass of the rocket
            for Mass in range(i,len(stagesListUsed)):
                totalMass+=stagesListUsed[Mass].mass
            #Get all of the values for all of the inputs    
            angle=stagesListUsed[i].angle
            engineThrust=stagesListUsed[i].thrust
            amountOfFuel=stagesListUsed[i].amountOfFuel
            burnTime=stagesListUsed[i].burnTime
            #print("Mass",totalMass,"\n""angle",angle,"\n","EngineThrust",engineThrust,"\n","#Fuel",amountOfFuel,"\n","burnTime",burnTime,"\n")
            self.xplot,self.yplot,xAxisText,yAxisText= self.getPlots(totalMass,angle,engineThrust,amountOfFuel,burnTime,str(graphType))
            color=stagesListUsed[i].stageColor
            a0=plt.plot(self.xplot,self.yplot)
            plt.setp(a0, color=color, linewidth=2.0)

        plt.ylabel(yAxisText)
        plt.xlabel(xAxisText)
        canvas = FigureCanvasTkAgg(figure, self.newFrame)
        canvas._tkcanvas.config(highlightthickness=0,background="white")
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)
        

        launchButton3=Button(self.newFrame,text="Return to input",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
        launchButton3.place(x=(width/2)-125,y=0)
        launchButton3.bind("<1>",lambda event:changeFrame(event,"Input",sideNumber))
        
    #Destroys the frame
    def destroy(self,sideNumber):
        print(sideNumber)
        sideFrames[sideNumber].newFrame.destroy()
        sideFrames[sideNumber].newFrame.destroy()
       

"""ChangeFrame(Event: tkEvent-- Has to be passed when the user inputs something from a .bind function
               FrameType: String--"Input"= use instantiate inputStage,"Graph"= use instantiate graphStage,
               SideNumber: Integer--0=left, 1=right)  
Is called when the frame needs to be changed to show a graph/input field
"""
def changeFrame(event,Type,sideNumber,*args):
    Destroyer(event, sideNumber)
    if Type=="Input":
        sideFrames[sideNumber]=stageFrame(sideNumber)
    else:
        sideFrames[sideNumber]=graphFrame(sideNumber,args)
    print("Frame added: %s on side %i"%(str(sideFrames[sideNumber]),sideNumber))

"""Destroyer(Event: tkEvent-- Has to be passed when the user inputs something from a .bind function
            SideNumber: Integer--0=left, 1=right)  
Is called when a frame needs to be destroyed.
""" 
def Destroyer(event,sideNumber):
    try:
        sideFrames[sideNumber].destroy(sideNumber)
    except AttributeError:
        print("Tried to destroy a frame that is not there")
    else:
        print("Frame destroyed: %s on side %i"%(str(sideFrames[sideNumber]),sideNumber))
        sideFrames[sideNumber]=None
        


"""
This is called to show input fields when the program runs.
"""
def init():
    changeFrame(None,"Input",0)
    changeFrame(None,"Input",1)

init()
root.mainloop()
