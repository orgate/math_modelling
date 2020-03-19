from numpy import *
from matplotlib.pyplot import *
import matplotlib.animation as animation

fig, ax = subplots()

h = 0.01
k = 0.001
v = arange(-1,2,h)
t = arange(0,0.25,k)
H = len(v)
N = len(t)
a = 1 #works only if it is 1
u0 = sin(2*pi*v)
u0[0:(H/2)] = 1 # should be commented for continuous case
u0[(H/2):] = arange(1,-1,-2.0/(H/2))

#u0[(H/2):] = -1 # should be commented for continuous case
Un = u0

ax.set_ylim([-1.5, 1.5])
line, = ax.plot(v,Un)

def animate(i):
    temp1 = Un[1] # should be commented for discontinuous case
    temp2 = Un[-2] # should be commented for discontinuous case
    temp3 = Un[0] # should be commented for discontinuous case
    Un[1:-1] = ((1.0/2.0)*( Un[2:] + Un[0:-2] )) - ((k)/(2*h))*( Un[2:]*Un[2:] - Un[0:-2]*Un[0:-2] )
    Un[0] = ((1.0/2.0)*( temp1 + Un[-1] )) - ((a*k)/(2*h))*( temp1 - Un[-1] ) # should be commented for discontinuous case
    Un[-1] = ((1.0/2.0)*( temp3 + temp2 )) - ((a*k)/(2*h))*( temp3 - temp2 ) # should be commented for discontinuous case

    line.set_ydata(Un)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(ma.array(u0, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, t, init_func=init,
    interval=25, blit=True)

show()
