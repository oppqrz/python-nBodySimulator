import matplotlib.pyplot as plt 
import numpy as np


G = 6.67e-11

#define the body Class
class Body:
    def __init__(self,Mass,PosX,PosY,VelX,VelY):
        self.Mass = Mass
        self.PosX = PosX
        self.PosY = PosY
        self.VelX = VelX
        self.VelY = VelY

        self.Xarray = np.array([PosX])
        self.Yarray = np.array([PosY])
        
    
    def GetDistance(self,OtherBody):
        DisX2 = (self.PosX - OtherBody.PosX)**2
        DisY2 = (self.PosY - OtherBody.PosY)**2
        return (DisX2 + DisY2)**0.5

    def GetAcelleration(self,OtherBody):
        AceelerationX = -(self.PosX - OtherBody.PosX) * G * OtherBody.Mass /(self.GetDistance(OtherBody)**3)
        AceelerationY = -(self.PosY - OtherBody.PosY) * G * OtherBody.Mass /(self.GetDistance(OtherBody)**3)
        return {"X" : AceelerationX, "Y" : AceelerationY}

    def UpdateVelocity(self,OtherBody):
        Acel = self.GetAcelleration(OtherBody)
        self.VelX += Acel["X"]
        self.VelY += Acel["Y"]
        
    def UpdatePosition(self,TimeStep):
        self.PosX += self.VelX*TimeStep
        self.PosY += self.VelY*TimeStep
        self.Xarray = np.append(self.Xarray,[self.PosX])
        #print(self.Xarray)
        self.Yarray = np.append(self.Yarray,[self.PosY])
        #print(self.Yarray)



#Create the Bodies and a list of  them to loop over

TimeStep = 1
nTimeSteps = 10 * 24 *60 * 60
CheckInTime = 60*60*24  #How frequently to output progress in seconds

Sun = Body(2e30,0.,0.,0.,0.)
Mercury = Body(3.3e23,0,57e9,47.3e3 ,0)
Venus = Body(4.8e24,0,108e9,35e3 ,0)
Earth = Body(6e24,0,-150e9,-29.7e3 ,0)
Mars = Body(6.4e23,0,227e9,24e3 ,0)

Bodies = [Sun,Mercury,Venus,Earth,Mars]


for nT in range(nTimeSteps):
    for BodyPrimay in Bodies:
        for BodySecondary in Bodies:
            if BodyPrimay == BodySecondary:
                continue
            else:
                BodyPrimay.UpdateVelocity(BodySecondary)
                
        BodyPrimay.UpdatePosition(TimeStep)
    if(nT % CheckInTime == 0):
        print(f"Day: {nT /CheckInTime}") 

plt.plot(Bodies[0].Xarray,Bodies[0].Yarray,"o")
plt.plot(Bodies[1].Xarray,Bodies[1].Yarray,"o")
plt.plot(Bodies[2].Xarray,Bodies[2].Yarray,"o")
plt.plot(Bodies[3].Xarray,Bodies[3].Yarray,"o")
plt.plot(Bodies[4].Xarray,Bodies[4].Yarray,"o")

plt.show()