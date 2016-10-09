#Exercise 4 Double particle decay
##problem 1.5
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of typw A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are <br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/QQ%E5%9B%BE%E7%89%8720161009180342.png)<br>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant ![](http://latex.codecogs.com/gif.latex?%7B%5Ctau%20%7D). Solve the system of equations for the numbers of nuclei, ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D), as functions of time. Consider different initial confitions, such as ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D%3D100), ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D%3D0), etc., and take ![](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D1) s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) are constant. In such a steady state, the time derivatives ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) and ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) should vanish.<br>

==
##Abstract
  This is my first time using python to solve the easy Physics problem.And in the class,we have known that the easist situation of one particle decay.From the teacher's ppt , there is a standard python code about the decay,and it describe a decay by using "class".So i try
to use the same method to describe the double partical problem,and plot the picture.

===
##Background
### Radiation decay
For a large number of ![](http://latex.codecogs.com/gif.latex?%5E%7B235%7DU) nuclei,which would usually be the case if we were actually doing an experiment to study radioactive decay.If Nu（t） is the number of Uranium nuclei that are present in the sample at time t,the behavior is governed by the differential equation<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BN_%7BU%7D%7D%7B%5Ctau%7D)<br>
where τ is the "time constant" for the decay.You can show by direct substitution that the solution to this differential equation is<br>
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%3DN_%7BU%7D%280%29e%5E%7B-t/%7B%5Ctau%7D%7D)<br>
where Nu（0）is the number of nuclei present at t=0.This solution may be familiar to you;similar equations and similar solutions are found in many other contexts.We note that at time t=τ  a fraction e-1 of the nucler that were initially present has not yet decayed.It turns out that τ is the mean lifetime of a nucleus.

### A numerical approach
Basing on the Taylor expansion for ![](http://latex.codecogs.com/gif.latex?N_%7BU%7D)<br>
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28%5CDelta%20t%29%3DN_%7BU%7D%280%29&plus;%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%5CDelta%20t&plus;%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7B%5Cmathrm%7Bd%5E2%7D%20N_%7BU%7D%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%28%5CDelta%20t%29%5E2&plus;...)<br>
then ignore the terms that involves second and higher power of △t,leaving us with<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/1.4.gif)<br>
The same result can be obtained from the definition of a derivative.The derivative of N evaluated at time t can be written as<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/da%20shizi.gif)<br>
so from the physics of the problem we know the founctional form of the derivative ,wo obtain:<br>
![](http://latex.codecogs.com/gif.latex?N_%7BU%7D%28t&plus;%5CDelta%20t%29%5Capprox%20N_%7BU%7D%28t%29-%5Cfrac%7BN_%7BU%7D%28t%29%7D%7B%5Ctau%7D%5CDelta%20t)

                                
====
##content(solution)
####basic codes
```
import pylab as pl
class uranium_decay:
    """
    problem 1.5
    Simulation of radioactive decay
    Program to accompany 'Computational Physics' by David Yu
    """
    def __init__(self, number_of_nuclei_A = 100,number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.nA_uranium = [number_of_nuclei_A]
        self.nB_uranium = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.decayA=[-100]
        self.decayB=[100]
        print("Initial number of nuclei A ->", number_of_nuclei_A)
        print("Initial number of nuclei B ->", number_of_nuclei_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.nA_uranium[i] - self.nA_uranium[i] / self.tau * self.dt+self.nB_uranium[i] / self.tau * self.dt
            tmp_B = self.nB_uranium[i] - self.nB_uranium[i] / self.tau * self.dt+self.nA_uranium[i]/ self.tau * self.dt            
            self.nA_uranium.append(tmp_A)
            self.nB_uranium.append(tmp_B)
            changeA = -self.nA_uranium[i+1] / self.tau +self.nB_uranium[i+1] / self.tau
            changeB=  -self.nB_uranium[i+1] / self.tau +self.nA_uranium[i+1]/ self.tau
            self.decayA.append(changeA)
            self.decayB.append(changeB)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.subplot(211)
        plotA, = pl.plot(self.t, self.nA_uranium)
        plotB, = pl.plot(self.t, self.nB_uranium)        
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.subplot(212)
        plotA = pl.plot(self.t, self.decayA)
        plotB = pl.plot(self.t, self.decayB)
        pl.show()
        pl.xlabel('time ($s$)')
        pl.ylabel('dN/dt')
a = uranium_decay()
a.calculate()
a.show_results()
```
('Initial number of nuclei A ->', 100)<br>
('Initial number of nuclei B ->', 0)<br>
('Time constant ->', 1)<br>
('time step -> ', 0.05)<br>
('total time -> ', 5)<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-1.png)
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-2.png)
<br>
By calculating the equations of problem<br>
we can get a analytical solution<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/jiexijie.gif)<br>
the we put the calculated solution into python with numerical solution we got:
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-3.png)<br>
By changing different parameter we can get a lot of diferent situation,here we list these picture:<br>
#####total time is small for example
<br>
('Initial number of nuclei A ->', 100)
('Initial number of nuclei B ->', 0)
('Time constant ->', 0.1)
('time step -> ', 0.05)
('total time -> ', 0.1)<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-4.png)<br>
<br>
('Initial number of nuclei A ->', 100)
('Initial number of nuclei B ->', 0)
('Time constant ->', 0.1)
('time step -> ', 0.05)
('total time -> ', 0.25)<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-5.png)
#####number of B is not vanish at first
<br>
('Initial number of nuclei A ->', 100)
('Initial number of nuclei B ->', 50)
('Time constant ->', 0.1)
('time step -> ', 0.05)
('total time -> ', 1)<br>
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/exersice4/figure_1-6.png)

##conclusion
doing homework by myself is so great








 
