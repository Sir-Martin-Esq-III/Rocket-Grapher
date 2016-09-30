from tkinter import *
from math import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import style


sideFrames=[None,None]
r0StagesList=list()#List of the stages for Rocket0
r1StagesList=list() #List of the stages for Rocket1


root = Tk()
#Gets the height and width of the monitor
width=root.winfo_screenwidth()/2
height=root.winfo_screenheight()/2

root.title("Rocket Science 9000")
root.geometry("%dx%d+%d+%d" %(width,height,width/2,height/2))
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
    tempStageArray=list()
    tempStageNumber=None
    #Class which has all of the variables for each stage
    class Stages:
        mass=0
        angle=0
        thrust=0
        stageTime=0
        stageColor="#FFFFFF"
        
            
    def __init__(self,sideNumber):
        errors=[0,0]
        
        #Checks what rocket this frame is for and does the appropriate variable assignments
        if sideNumber==0:
            self.x=0
            self.tempStageArray=r0StagesList
            self.tempStageNumber=self.r0currentStageNumber

        else:
           self.x=width/2
           self.tempStageArray=r1StagesList
           self.tempStageNumber=self.r1currentStageNumber

        if len(self.tempStageArray)==0:
            startStage=self.Stages()
            self.tempStageArray.append(startStage)
    
        def checkErrors():
            if errors[0]==1 or errors[1]==1:
                launchButton.config(fg="#747e8b")
                return True
            else:
                launchButton.config(fg="#E24A33")
                errorText.set("")
                return False

        #Updates the widget which show the stage color 
        def updateColorBox(event):
            try:
                colorBox.config(bg=Entry_stageColor.get())
            except TclError:
                errors[1]=1
                checkErrors()
                errorText.set("Error: %s is not a color."%(Entry_stageColor.get()))
            else:
                errors[1]=0
                checkErrors()               

        #Saves the current stage
        def saveStage(event):
            try:
                    self.tempStageArray[self.tempStageNumber].mass=float(Entry_Mass.get())
                    self.tempStageArray[self.tempStageNumber].angle=float(Entry_Angle.get())
                    self.tempStageArray[self.tempStageNumber].thrust=float(Entry_Thrust.get())
                    self.tempStageArray[self.tempStageNumber].stageTime=float(Entry_stageTime.get())
                    self.tempStageArray[self.tempStageNumber].stageColor=str(Entry_stageColor.get())
            except ValueError:
                errors[0]=1
                checkErrors()
                errorText.set("An error occoured causing the stage not to save")
            else:
                errors[0]=0
                checkErrors()

        #Changes the current stage state
        def changeStageState(event,option):
            #Add a stage
            if option=="Add":
                self.tempStageNumber =len(self.tempStageArray)
                newStage=self.Stages()
                self.tempStageArray.append(newStage)
            #Cycle left
            elif option=="Left":
                if self.tempStageNumber!=0:
                    self.tempStageNumber-=1
            #Cycle right
            elif option=="Right":
                if self.tempStageNumber<len(self.tempStageArray)-1:
                    self.tempStageNumber+=1

            #Sets all of the entry widgets to the value of the currentStages class instance 
            stageValue.set("Stage %i"%(self.tempStageNumber))
            currentStage=self.tempStageArray[self.tempStageNumber]
            mass.set(str(currentStage.mass))
            angle.set(str(currentStage.angle))
            thrust.set(str(currentStage.thrust))
            stageTime.set(str(currentStage.stageTime))
            colorBox.config(bg=currentStage.stageColor)
            stageColor.set(str(currentStage.stageColor))
            
        #Create a new frame
        self.newframe=Frame(height=height,width=width/2)
        self.newframe.config(bg ="white")
     
        #Place the new frame at (x,0)
        self.newframe.place(x=self.x,y=0)
        
        """---BEGIN UI PLACEMENT---"""
        lable_rocketValue=Label(self.newframe,text="Rocket "+str(sideNumber),fg ="#8c8c8c",bg ="White",font=self.titleFont)
        lable_rocketValue.place(x=width/4,y=0)

        #Error text
        errorText=StringVar()
        errorText.set("")    
        lable_errorText=Label(self.newframe, textvariable=errorText,fg ="red",bg ="White",font=self.mainFont)
        lable_errorText.place(x=width/8,y=height-50)

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
        
        #Thrust widgets(Lable&Entry)
        thrust=DoubleVar()
        lable_Thrust=Label(self.newframe, text="Engine thrust(N)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_Thrust.place(x=0,y=120)
        Entry_Thrust=Entry(self.newframe, textvariable=thrust,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_Thrust.place(x=0,y=140)

        #Burn time widgets(Lable&Entry)
        stageTime=DoubleVar()
        lable_stageTime=Label(self.newframe, text="Time until next stage(S)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_stageTime.place(x=0,y=160)
        Entry_stageTime=Entry(self.newframe, textvariable=stageTime,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_stageTime.place(x=0,y=180)    

        #Color widgets(canvas,Lable&Entry)
        stageColor=StringVar()
        stageColor.set("#")
        lable_stageColor=Label(self.newframe, text="Stage color (Hex)",fg ="#8c8c8c",bg ="White",font=self.mainFont)     
        lable_stageColor.place(x=0,y=200)
        Entry_stageColor=Entry(self.newframe, textvariable=stageColor,fg ="#E24A33 ",bg ="#E5E5E5",relief=FLAT)
        Entry_stageColor.place(x=0,y=220)
        Entry_stageColor.bind("<FocusOut>",lambda event:updateColorBox(event))
        colorBox=Canvas(self.newframe, width=25, height=15)
        colorBox.place(x=100,y=220)

        #Adds a stage to the rocket
        addStageButton=Button(self.newframe,text="+ Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        addStageButton.place(x=(width/2)-100,y=20)
        addStageButton.bind("<Button-1>",lambda event:changeStageState(event,"Add"))
        #Save the values for the current stage
        saveStageButton=Button(self.newframe,text="Save Stage",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        saveStageButton.place(x=240,y=220)
        saveStageButton.bind("<Button-1>",lambda event:saveStage(event))
        
        #Cycles to the stage before the current one current stage=0 then don't show
        cycleStageLeft=Button(self.newframe,text="<",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        cycleStageLeft.place(x=(width/4)-20,y=20)
        cycleStageLeft.bind("<Button-1>",lambda event:changeStageState(event,"Left"))

        #Cycles to the stage after the current one#current stage=max then don't show
        cycleStageRight=Button(self.newframe,text=">",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5",font=self.mainFont)
        cycleStageRight.place(x=(width/4)+60,y=20)
        cycleStageRight.bind("<Button-1>",lambda event:changeStageState(event,"Right"))

        #Graph widgets
        lable_graphType=Label(self.newframe, text="Graph type",fg ="#8c8c8c",bg ="White",font=self.mainFont)
        lable_graphType.place(x=0,y=290)
        #Dropdown box
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
            if checkErrors()==False:
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
    xplot=0
    yplot=0
    currentRocketStages=None
    lastXVelocity=0
    lastYVelocity=0
    lastXDisplacement=0
    lastYDisplacement=0
    totalTime=0

    def getPlots(self,totalMass,angle,engineThrust,stageTime,graphType):
        xValues=list()
        yValues=list()
        xAxis=""
        yAxis=""
        g=-9.81

        #Resolving the engine thrust vector into its v/h components 
        verticalThrust=engineThrust*(sin(radians(angle)))
        horizontalThrust=engineThrust*(cos(radians(angle)))

        #Net Force
        netVForce=verticalThrust-(totalMass*g)#Upthrust-weight

        #Acceleration
        try:
            verticalAcc=(netVForce/totalMass)#A=F/M
            horizontalAcc=(horizontalThrust/totalMass)
        except ZeroDivisionError:
            return(0,0,"","")

        for i in range(0,36):
            dt=(stageTime*(i/35))
                   
            #Velocity
            verticalVel=(verticalAcc*dt)+self.lastYVelocity# V=AT+u
            horizontalVel=(horizontalAcc*dt)+self.lastXVelocity
           
            #Displacement
            verticalDisplacement=(0.5*(self.lastYVelocity+verticalVel)*dt)+self.lastYDisplacement
            horizDisplacement=(horizontalVel*dt)+self.lastXDisplacement
            if verticalDisplacement <0:
                verticalDisplacement=0
            
            if graphType=="('Displacement-Time',)":
                xValues.append(dt+self.totalTime)               
                yValues.append(verticalDisplacement)
                xAxis="Time (s)"
                yAxis="Vertical displacement (m)"

            elif graphType=="('Velocity-Time',)":
                yValues.append(verticalVel)
                xValues.append(dt+self.totalTime)
                xAxis="Time (s)"
                yAxis="Vertical velocity (m/s^-1)"
                
            elif graphType=="('XDisplacement-YDisplacement',)":
                yValues.append(verticalDisplacement)
                xValues.append(horizDisplacement)
                xAxis="Horizontal displacement (m)"
                yAxis="Vertical displacement (m)"
                
            elif graphType=="('XVelocity-YVelocity',)":
                yValues.append(verticalVel)
                xValues.append(horizontalVel)
                xAxis="Horizontal velocity (m/s^-1)"
                yAxis="Vertical velocity (m/s^-1)"
            

        self.totalTime+=stageTime
        self.lastYDisplacement=verticalDisplacement
        self.lastXDisplacement=horizDisplacement      
        self.lastYVelocity=verticalVel
        self.lastXVelocity=horizontalVel
        
        return(xValues,yValues,xAxis,yAxis)
        
    def __init__(self,sideNumber,graphType):
        xAxisText=""
        yAxisText=""
        self.newFrame=Frame(height=height,width=width/2)
        self.newFrame.config(bg ="white")
        if sideNumber==0:
            self.x=0
            self.currentRocketStages=r0StagesList
        else:
            self.currentRocketStages=r1StagesList
            self.x=width/2
        #Create the frame
        self.newFrame.place(x=self.x,y=0)
        widthInches= root.winfo_screenwidth() / root.winfo_fpixels('1i')
        heightInches= root.winfo_screenheight() / root.winfo_fpixels('1i')
        #Begin graph creation
        self.figure = plt.figure(figsize=(((widthInches/4)-.2),(heightInches/2)-.2), dpi=100,frameon=False,tight_layout=True)        

        for i in range(len(self.currentRocketStages)):
            totalMass=0
            #Find the total mass of the rocket
            for Mass in range(i,len(self.currentRocketStages)):
                totalMass+=self.currentRocketStages[Mass].mass
            #Get all of the values from all of the inputs    
            angle=self.currentRocketStages[i].angle
            engineThrust=self.currentRocketStages[i].thrust
            stageTime=self.currentRocketStages[i].stageTime
            self.xplot,self.yplot,xAxisText,yAxisText= self.getPlots(totalMass,angle,engineThrust,stageTime,str(graphType))
            color=self.currentRocketStages[i].stageColor
            a0=plt.plot(self.xplot,self.yplot)
            plt.setp(a0, color=color, linewidth=3.0)

        plt.ylabel(yAxisText)
        plt.xlabel(xAxisText)
        canvas = FigureCanvasTkAgg(self.figure, self.newFrame)
        canvas._tkcanvas.config(highlightthickness=0,background="white")
        canvas.show()
        canvas.get_tk_widget().place(x=0,y=0)
        
 
        returnButton=Button(self.newFrame,text="Return to input",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
        returnButton.place(x=(width/2)-125,y=0)
        returnButton.bind("<1>",lambda event:changeFrame(event,"Input",sideNumber))

        saveButton=Button(self.newFrame,text="Save",fg ="#E24A33 ",relief=FLAT,bg="#E5E5E5")
        saveButton.place(x=(width/2)-400,y=0)
        #Will need to choose a more suitable DIR for the picture
        saveButton.bind("<1>",plt.savefig(r"C:\Users\Thoma\Pictures\Test images\Image.png"))
        
    #Destroys the frame
    def destroy(self,sideNumber):
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

"""Destroyer(Event: tkEvent-- Has to be passed when the user inputs something from a .bind function
            SideNumber: Integer--0=left, 1=right)  
Is called when a frame needs to be destroyed.
""" 
def Destroyer(event,sideNumber):
    try:
        sideFrames[sideNumber].destroy(sideNumber)
    except AttributeError:
        pass
    else:
        sideFrames[sideNumber]=None
        
"""
This is called to show input fields when the program runs.
"""
def init():
    changeFrame(None,"Input",0)
    changeFrame(None,"Input",1)

init()
root.mainloop()
