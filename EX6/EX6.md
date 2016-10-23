#EX6. PROBLEM2.10升级版
------
##摘要
我们在之前的课上学习过处理简单的常微分方程，运用欧拉方程可以轻松的简化。现在对一个受到风阻，重力，空气密度阻力的影响下的加农炮。意味着要处理多个微分项。用python的对象语言‘class’，可以较简便的模拟出非常简易的炮弹并且很愚蠢的击打在制定位置。

------
##problem2.10
>PROBLEM2.10 :Gerneralize the Progame developed for the previous problem so that it can deal with situation in which the target is at a different altitude than the cannon.
Consider cases in which the target is higher and lower thwn the cannon.Also investigate how the minimum firing velocity required to hit the target varies as the altitude of the target is varied.

##解决办法
从互联网得知炮弹的速度大致在2km/s,风速大约为30m/s(假令风向水平)，现在只需要控制角度就能将炮弹打击到制定位置
(下面公式是先在作业部落上用latex编辑再截图)
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX6/QQ%E6%88%AA%E5%9B%BE20161024004807.png)

####编出来的关于相关常微分方程的主要程序是这样的：
```python
    def calculate(self):
        for i in numpy.arange(91):
            self.x.append([0])
            self.y.append([0])
            self.vx.append([self.v_0 * numpy.cos((float(i) / 180) * numpy.pi)])
            self.vy.append([self.v_0 * numpy.sin((float(i) / 180) * numpy.pi)])
            while (self.y[-1][-1] > 0) or (self.x[-1][-1] == 0):
                v = numpy.sqrt(abs(self.vx[-1][-1] - self.v_wind) ** 2 + (self.vy[-1][-1]) ** 2)
                self.x[-1].append(self.x[-1][-1] + self.vx[-1][-1] * self.dt)
                self.y[-1].append(self.y[-1][-1] + self.vy[-1][-1] * self.dt)
                self.vx[-1].append(self.vx[-1][-1] - ((1 - a * self.y[-1][-1] / T0) ** alpha) * B2 * v * (self.vx[-1][-1] - self.v_wind) * self.dt)
                self.vy[-1].append(self.vy[-1][-1] - (self.g * ((float(R) / (R + self.y[-1][-1])) ** 2) + ((1 - a * self.y[-1][-1] / T0) ** alpha) * B2 * v * self.vy[-1][-1]) * self.dt)
            if self.y[-1][-1] < 0:
                r = - (self.y[-1][-2] / self.y[-1][-1])
                self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  

```
####作图
> * 先利用‘for i in numpy.arange(91)’画出角度从1到90度
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX6/1%E5%88%B090%E5%BA%A6%E9%A3%9E%E8%A1%8C%E7%82%AE%E5%BC%B9.png)<br>
观察所有大致角度规律，当然肉眼看是毫无作用的。<br>
* 接下来用一个循环确定设计的准确值
```python
 if self.y[-1][-1] < 0:
    r = - (self.y[-1][-2] / self.y[-1][-1])
    self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  
    self.distance.append(abs(self.target-self.x[-1][-1]))   
        for i in numpy.arange(0,90,1):
            if self.distance[int(i*10)] == min(self.distance):
                print i
                print self.x[int(i*10)][-1]
```
在0到90度之间每隔一度找到与x轴交点，并求得距离目标最近的角度，print出来。
那么大致在44度离目标是最近的，炮弹水平射击的距离是99.9045234383
![](https://github.com/jigga301/compuational_physics_N2014301020070/blob/master/EX6/figure_1.png)<br>
*找到不算是精确的角度后，给予其误差
关键用到```random.uniform(0.95,1.05)```
就是在原先的代码中引入这个量，使得有误差的数据都变成在误差范围内的随机数。<br>
那么引入随机变量，在风速，初速度后面都*random.uniform(1-a,1+a)再打出50个这样的炮弹
！[]()

