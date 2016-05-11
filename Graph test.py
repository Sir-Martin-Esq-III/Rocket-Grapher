#This is a test of how the graph will work with default values
import matplotlib.pyplot as plt
from math import *
stages=list()
xvalues= [None] * 18
yvalues= [None] * 18
lastXVel=0
lastYVel=0
colors={0:"#0099cc",1:"#bb4477",2:"#ff3300",3:"#33cc33"}#Dict of colors
def plotCalc(angle,velocity,stageNumber):
    print(stageNumber)
    gravity=9.81
    global lastXVel
    global lastYVel
    Xcomp=velocity*(cos(radians(angle)))#cos
    Ycomp=velocity*(sin(radians(angle)))#sin
    time=(2*Ycomp)/gravity
    maxHorizDisp=time*Xcomp
    maxVertDisp=(-(Ycomp**2)/(2*-gravity))
    for i in range(0,36):
        updateTime=(time*(i/35))
        if updateTime>time/2:
            lastXVel=xvalues[len(xvalues)-1]
            lastYVel=yvalues[len(yvalues)-1]
            break
        else:
            if stageNumber!=0:
                yvalues[i]=((lastYVel)+(Ycomp*updateTime)+((-1/2*gravity)*(updateTime*updateTime)))
                xvalues[i]=((lastXVel)+(updateTime*Xcomp))
            else:
                yvalues[i]=((Ycomp*updateTime)+((-1/2*gravity)*(updateTime*updateTime)))
                xvalues[i]=(updateTime*Xcomp) 
    
class Stage:
    def __init__(self,number):
        self.stageNumber=number  
    currentAngle =None
    currentVelocity =None
    

amountOfStages=int(input("How many stages do you want"))
for h in range(amountOfStages):
    print("Stage%i" %(h))
    currentStage=Stage(h)
    currentStage.currentAngle=int(input("Current Angle"))
    currentStage.currentVelocity=int(input("Current Velocity"))
    stages.append(currentStage)
        
for k in range(len(stages)):
    print("Stage: %i"%(stages[k].stageNumber))
    print(" Angle: %i"%(stages[k].currentAngle))
    print(" Velocity: %i"%(stages[k].currentVelocity))
    

for j in range(len(stages)):#Number of stages
    color=j
    print(len(colors))
    plotCalc(stages[j].currentAngle,stages[j].currentVelocity,stages[j].stageNumber)
    while color>len(colors)-1:
        color-=4
        print(color)
    currentColor=colors[color]#Setting the color of the plot
    plt.plot(xvalues,yvalues,currentColor)#Plot the values for the current stages plots
   
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()
