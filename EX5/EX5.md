#Exercise 5
==
##Abstract
 We gruadully learn how to solve the Realistic Projectile Motion.And in class , we have learnt that bicycle racing with the effect of air resistance.To analyse this problem, we need use the Newton’s second law and expression of Energy and Power.Eular method is still crucial to our solution.So when we met another physics problem with some easy ODE ,we can briefly use the same way to write python code to analyse.

##problem 2.6
Use the Eular method to calculate


##solution
###with no resistant
only consider the accelarate g.so we have such equation :<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX5/QQ%E6%88%AA%E5%9B%BE20161017003220.png)<br>
then decompose it so that it can be used by Eular method<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX5/QQ%E6%88%AA%E5%9B%BE20161017003231.png)<br>
therefore<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX5/QQ%E6%88%AA%E5%9B%BE20161017003244.png)<br>
so the code is below:
```
import pylab as pl
import math
class cannon_shell_trajextories(object):
    def __init__(self, v_0 = 0.7, time_step = 0.05, g = 0.0098): #the unit of length is "km"  time:"s"
        self.v_x = []
        self.v_y = []
        self.v_0 = v_0
        self.x = []
        self.y = []
        self.t = [0]
        self.g = g
        self.angle = [30, 35, 40, 45, 50, 55,60,65,70]
        self.dt = time_step
    def calculate(self):
        for i in self.angle:
            self.x.append([0])
            self.y.append([0])
            self.v_x.append([self.v_0 * math.cos((float(i) / 180) * math.pi)])
            self.v_y.append([self.v_0 * math.sin((float(i) / 180) * math.pi)])
            while (self.y[-1][-1] > 0) or (self.x[-1][-1] == 0):
                self.v_x[-1].append(self.v_x[-1][-1])
                self.v_y[-1].append(self.v_y[-1][-1] - self.g * self.dt)
                self.x[-1].append(self.x[-1][-1] + self.v_x[-1][-1] * self.dt)
                self.y[-1].append(self.y[-1][-1] + self.v_y[-1][-1] * self.dt)
            if self.y[-1][-1] < 0:
                r = - (self.y[-1][-2] / self.y[-1][-1])
                self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  
    def show_results(self):
        for i in range(len(self.angle)):
            pl.plot(self.x[i], self.y[i])
            pl.annotate('%d'%self.angle[i],xy=(25,6 + 2 * i))
        pl.title(' Cannon shell trajectory')
        pl.xlabel('x (km)')
        pl.ylabel('y (km)')
        pl.ylim(0,)
        pl.show()
        
a =  cannon_shell_trajextories()
a.calculate()
a.show_results()
```
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX5/figure_1.png)<br>
##conclude
Eular equation is vary perfect to solve many simple ODE problem
##Acknowledgement
Chapter 2 Realistic Projectile Motion
Chapter 1 A First Numerical Problem
Matplotlib Tutorial
