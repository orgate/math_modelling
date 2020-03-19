from numpy import *
from matplotlib.pyplot import *
import matplotlib.animation as animation

fig, ax = subplots()

h = 0.001 #could be made 0.001 for slow motion
k = 0.001 #could be made 0.001 for slow motion
umax = 1
pmax = 2
v = arange(0,1,h)
t = arange(0,0.25,k)
H = len(v)
N = len(t)
a = 1
u0 = sin(2*pi*v)
u0[0:(H/2)] = 1.0
u0[(H/2):] = -0.0
u = zeros([N,H])
Un = u0
u[0,:] = u0

ax.set_ylim([-1.5, 1.5])
line, = ax.plot(v,Un)

def animate(i):
    temp = Un[-1]
    Un[1:] = Un[1:] - (k/h)*umax*(1-(2*Un[1:]/pmax))*( Un[1:] - Un[0:-1] )
    Un[0] = Un[0] - (k/h)*umax*(1-(2*Un[0]/pmax))*Un[0]*( Un[0] - temp )

    line.set_ydata(Un)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(ma.array(u0, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, t, init_func=init,
    interval=25, blit=True)

show()
