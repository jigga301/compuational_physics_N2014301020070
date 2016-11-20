```python
import pylab as pl
import math
class lorenz_model:
    def __init__(self,r):
        self.vx=[0]
        self.vy=[0]
        self.vz=[0]
        self.x=[1]
        self.y=[0]
        self.z=[0]
        self.t=[0]
        self.dt=0.0001
        self.sigma=10
        self.b=8/3
        self.r=r
        self.x2=[]
        self.y2 = []
        self.z2 = []
    def calculate(self):
        for i in range(600000):
            self.vx.append(self.sigma*(self.y[-1]-self.x[-1]))
            self.vy.append(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
            self.vz.append(self.x[-1]*self.y[-1]-self.b*self.z[-1])
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.z.append(self.z[-1]+self.vz[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)

    def show_results(self):
        pl.title('z versus x')
        pl.plot(self.x,self.z)
        pl.xlabel('x')
        pl.ylabel('z')
        pl.annotate('r',xy=(40,0),xytext=(0,0.04))
        pl.show()
    def show_results2(self):
        for i in range(600000):
            if self.t[i] > 30:
                if abs(self.y[i]) < 0.01:
                    self.z2.append(self.z[i])
                    self.x2.append(self.x[i])
        pl.plot(self.x2, self.z2,'.')
        pl.xlabel('y')
        pl.ylabel('z')
        pl.text(-10,10,'phase space plot:z versus x when y=0')
        pl.show()
    def show_results3(self):
        for i in range(6000000):
            if self.t[i] > 30:
                if abs(self.x[i]) < 0.01:
                    self.z2.append(self.z[i])
                    self.y2.append(self.y[i])
        pl.plot(self.y2, self.z2,'.')
        pl.xlabel('y')
        pl.ylabel('z')
        pl.text(-4,7,'phase space plot:z versus y when x=0')
        pl.show()
    def show_results4(self):
        pl.title('z versus t')
        pl.plot(self.t,self.z)
        pl.xlabel('t')
        pl.ylabel('z')
        pl.text(30, 500, 'r=163.8')
        pl.show()



A=lorenz_model(163.8)
A.calculate()
A.show_results4()
```
