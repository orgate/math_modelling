from numpy import *
from matplotlib.pyplot import *
import matplotlib.animation as animation

fig, ax = subplots()

h = 0.01
k = 0.001
v = arange(0,1,h)
t = arange(0,0.25,k)
H = len(v)
N = len(t)
a = 1
u0 = sin(2*pi*v)
u0[0:(H/2)] = 1 # should be commented for continuous case
u0[(H/2):] = -1 # should be commented for continuous case
u = zeros([N,H])
Un = u0
u[0,:] = u0


ax.set_ylim([-1.5, 1.5])
line, = ax.plot(v,Un)

def animate(i):
#    temp = Un[0] # should be commented for discontinuous case
#    Un[0:-1] = Un[0:-1] - ((a*k)/h)*( Un[1:] - Un[0:-1] ) # should be commented for discontinuous case
    Un[1:-1] = Un[1:-1] - ((a*k)/h)*( Un[2:] - Un[1:-1] ) # should be commented for continuous case
#    Un[-1] = Un[-1] - ((a*k)/h)*( 1 - Un[-1] ) # should be commented for discontinuous case
#    Un[-1] = Un[-1] - ((a*k)/h)*( 1 - Un[-1] ) # should be commented for discontinuous case

    line.set_ydata(Un)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(ma.array(u0, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, t, init_func=init,
    interval=25, blit=True)

show()
