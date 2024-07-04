#import matplotlib.pyplot as plt 
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

        #self.x_array = [pos_x]
        #self.y_array = [pos_y]
        
    
    def get_distance(self,other_body):
        Dist_x2 = (self.pos_x - other_body.pos_x)**2
        Dist_y2 = (self.pos_y - other_body.pos_y)**2
        return (Dist_x2 + Dist_y2)**0.5

    def get_acceleration(self,other_body):
        acel_x = -(self.pos_x - other_body.pos_x) * G * other_body.mass /(self.get_distance(other_body)**3)
        acel_y = -(self.pos_y - other_body.pos_y) * G * other_body.mass /(self.get_distance(other_body)**3)
        return {"X" : acel_x, "Y" : acel_y}

    def update_velocity(self,other_body):
        Acel = self.GetAcelleration(other_body)
        self.vel_x += Acel["X"]
        self.vel_y += Acel["Y"]
        
    def update_position(self,TimeStep):
        self.pos_x += self.vel_x*TimeStep
        self.pos_y += self.vel_y*TimeStep
        #self.x_array.append(self.pos_x)
        #self.y_array.append(self.pos_y)



#Create the Bodies and a list of  them to loop over

time_step = 1
n_time_steps = 365 * 24 *60 * 60
check_in_time = 60*60*24  #How frequently to output progress in seconds

Sun = Body(2e30,0.,0.,0.,0.)
Mercury = Body(3.3e23,0,57e9,47.3e3 ,0)
Venus = Body(4.8e24,0,108e9,35e3 ,0)
Earth = Body(6e24,0,-150e9,-29.7e3 ,0)
Mars = Body(6.4e23,0,227e9,24e3 ,0)

Bodies = [Sun,Mercury,Venus,Earth,Mars]


for nT in range(n_time_steps):
    for BodyPrimay in Bodies:
        for BodySecondary in Bodies:
            if BodyPrimay == BodySecondary:
                continue
            else:
                BodyPrimay.update_velocity(BodySecondary)
                
        BodyPrimay.update_position(time_step)
    if(nT % check_in_time == 0):
        print(f"Time Passed: {nT /check_in_time} Days") 



#plt.plot(np.array(Bodies[0].x_array),np.array(Bodies[0].y_array),"o")
#plt.plot(np.array(Bodies[1].x_array),np.array(Bodies[1].y_array),"o")
#plt.plot(np.array(Bodies[2].x_array),np.array(Bodies[2].y_array),"o")
#plt.plot(np.array(Bodies[3].x_array),np.array(Bodies[3].y_array),"o")
#plt.plot(np.array(Bodies[4].x_array),np.array(Bodies[4].y_array),"o")

#plt.show()