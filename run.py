#import matplotlib.pyplot as plt 
#import numpy as np
from typing import Self

G = 6.67e-11

#define the body Class
class Body:
    def __init__(self:Self,mass:float,pos_x:float,pos_y:float,vel_x:float,vel_y:float):
        self.mass = mass
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
    
    def get_distance(self:Self,other_body:Self) -> float:
        dist_x2 = (self.pos_x - other_body.pos_x)**2
        dist_y2 = (self.pos_y - other_body.pos_y)**2
        return (dist_x2 + dist_y2)**0.5

    def get_acceleration(self:Self,other_body:Self) ->dict:
        acel_x = -(self.pos_x - other_body.pos_x) * G * other_body.mass /(self.get_distance(other_body)**3)
        acel_y = -(self.pos_y - other_body.pos_y) * G * other_body.mass /(self.get_distance(other_body)**3)
        return {"X": acel_x, "Y": acel_y}

    def update_velocity(self:Self,other_body:Self):
        Acel = self.get_acceleration(other_body)
        self.vel_x += Acel["X"]
        self.vel_y += Acel["Y"]
        
    def update_position(self:Self,TimeStep:float):
        self.pos_x += self.vel_x*TimeStep
        self.pos_y += self.vel_y*TimeStep



#Create the Bodies and a list of  them to loop over

time_step:float = 1
n_time_steps:int = 365 * 24 *60 * 60
check_in_time:int = 60*60*24  #How frequently to output progress in seconds

Sun = Body(2e30,0.,0.,0.,0.)
Mercury = Body(3.3e23,0,57e9,47.3e3 ,0)
Venus = Body(4.8e24,0,108e9,35e3 ,0)
Earth = Body(6e24,0,-150e9,-29.7e3 ,0)
Mars = Body(6.4e23,0,227e9,24e3 ,0)

Bodies:list[Body] = [Sun,Mercury,Venus,Earth,Mars]


for nT in range(n_time_steps):
    for body_primary in Bodies:
        for body_secondary in Bodies:
            if body_primary == body_secondary:
                continue
            else:
                body_primary.update_velocity(body_secondary)
                
        body_primary.update_position(time_step)
    if(nT % check_in_time == 0):
        print(f"Time Passed: {nT /check_in_time} Days") 