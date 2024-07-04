import matplotlib.pyplot as plt 
import numpy as np


G = 6.67e-11

#define the body Class
class Body:
    def __init__(self,mass,pos_x,pos_y,vel_x,vel_y):
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

        self.x_array = [pos_x]
        self.y_array = [pos_y]
        
    
    def get_distance(self,OtherBody):
        DisX2 = (self.pos_x - OtherBody.pos_x)**2
        DisY2 = (self.pos_y - OtherBody.pos_y)**2
        return (DisX2 + DisY2)**0.5

    def get_acceleration(self,OtherBody):
        AceelerationX = -(self.pos_x - OtherBody.pos_x) * G * OtherBody.mass /(self.GetDistance(OtherBody)**3)
        AceelerationY = -(self.pos_y - OtherBody.pos_y) * G * OtherBody.mass /(self.GetDistance(OtherBody)**3)
        return {"X" : AceelerationX, "Y" : AceelerationY}

    def update_velocity(self,OtherBody):
        Acel = self.GetAcelleration(OtherBody)
        self.vel_x += Acel["X"]
        self.vel_y += Acel["Y"]
        
    def update_position(self,TimeStep):
        self.pos_x += self.vel_x*TimeStep
        self.pos_y += self.vel_y*TimeStep
        self.x_array.append(self.pos_x)
        self.y_array.append(self.pos_y)



#Create the Bodies and a list of  them to loop over

TimeStep = 1
nTimeSteps = 365 * 24 *60 * 60
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
        print(f"Time Passed: {nT /CheckInTime} Days") 



#plt.plot(np.array(Bodies[0].x_array),np.array(Bodies[0].y_array),"o")
#plt.plot(np.array(Bodies[1].x_array),np.array(Bodies[1].y_array),"o")
#plt.plot(np.array(Bodies[2].x_array),np.array(Bodies[2].y_array),"o")
#plt.plot(np.array(Bodies[3].x_array),np.array(Bodies[3].y_array),"o")
#plt.plot(np.array(Bodies[4].x_array),np.array(Bodies[4].y_array),"o")

#plt.show()