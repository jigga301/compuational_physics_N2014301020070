```python
import matplotlib.pyplot as pl
import numpy as np
class billiard():
    def __init__(self, x_0, y_0, vx_0, vy_0, N, dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
    def calculate(self):
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1, self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1] * self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1] * self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (np.sqrt(self.x[i] ** 2 + self.y[i] ** 2) > 1.0): #boundory condition
                self.x[i], self.y[i] = self.correct('np.sqrt(x**2+(y)**2) < 1.0', self.x[i - 1], self.y[i - 1],
                                                    self.vx[i - 1], self.vy[i - 1])
                self.vx[i], self.vy[i] = self.reflect(self.x[i], self.y[i], self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
    #correction
    def correct(self, condition, x, y, vx, vy):
        vx_c = vx / 100.0
        vy_c = vy / 100.0
        while eval(condition):
            x = x + vx_c * self.dt
            y = y + vy_c * self.dt
        return x - vx_c * self.dt, y - vy_c * self.dt
    ##boundory reflection
    def reflect(self, x, y, vx, vy):
        R = np.sqrt(x ** 2 + y ** 2)
        x = x /R
        y = y /R
        v = np.sqrt(vx ** 2 + vy ** 2)
        vt = -v * (vx * x + vy * y) / v
        vc = v * (vx * y - vy * x) / v
        vx_2 = vt * x + vc * y
        vy_2 = vt * y - vc * x
        return vx_2, vy_2
    ##circle-table trajectory
    def plot(self):
        pl.figure(figsize=(8, 8))
        pl.xlim(-1, 1)
        pl.ylim(-1, 1)
        pl.xlabel('x')
        pl.ylabel('y')
        pl.title('trajectory of Circular Table ')
        pl.plot(self.x, self.y, 'g')

        theta = 0
        x = []
        y = []
        while theta < 2 * np.pi:
            x.append(np.cos(theta))
            y.append(np.sin(theta))
            theta += 0.02
        pl.plot(x, y, 'b')

        pl.show()
    ##phase-spase picture
    def phase_plot(self):
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0) < 0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        pl.xlabel('x')
        pl.ylabel(r'$v_x$')
        pl.plot(record_x, record_vx, 'r.')
        pl.show()

A = billiard(0.2, 0, 1, 0.6, 11000, 0.01)
A.calculate()
A.plot()
```
