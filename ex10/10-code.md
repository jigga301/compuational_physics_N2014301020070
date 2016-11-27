```python
import pylab as pl
import math
class xingxing(object):
    def __init__(self,x0,y0,vx0,a,e,dt,b):
        vy0 = math.sqrt(4 * (1 - e) * math.pi ** 2 / ((1+e) * a) )
        self.x= [x0]
        self.y= [y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt = dt
        self.time =[0]
        self.r=[math.sqrt(x0**2+ y0**2)]
        self.b=b
    def calculate(self):
        for i in range(5000):
            self.vx.append(self.vx[-1]-4*self.x[-1]*self.dt*math.pi**2  / self.r[-1]**(self.b+1) )
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.vy.append(self.vy[-1]-4*self.y[-1]*self.dt*math.pi**2  / self.r[-1]**(self.b+1))
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.time.append(self.time[-1]+self.dt)
            self.r.append(math.sqrt(self.x[-1] ** 2 + self.y[-1]** 2))
    def plot1(self):
        pl.title(r'earth around sun $\beta=2.4$')
        pl.plot(self.x, self.y,'b.')
        pl.xlabel('x$AU$')
        pl.ylabel('y$AU$')
        pl.xlim(-1,1)
        pl.ylim(-1,1)

        x1=[0]
        y1=[0]
        pl.plot(x1,y1,'r*')

        pl.show()


a=xingxing(1,0,0,5.0/9 ,4.0/9,0.001,2.4)
a.calculate()
a.plot1()
```
