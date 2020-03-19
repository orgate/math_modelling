from numpy import *
from matplotlib.pyplot import *
import matplotlib.animation as animation
from scipy.integrate import odeint


fig, ax = subplots()

h = 0.001
k = 0.001
umax = 2.0
pmax = 1.0
v = arange(0,1,h)
t = arange(0,0.25,k)
H = len(v)
N = len(t)
a = 1
u0 = sin(2*pi*v)
# initial condition for single lane
u0[0:(H/2)] = 1.0
u0[(H/2):] = -0.0
# initial condition for single lane with traffic jam
#u0[0:(H/3)] = -0.0
#u0[(H/3):(2*H/3)] = 1.0
#u0[(2*H/3):] = -0.0
Un = u0
U = zeros([N,H])

diff = (u0[2:] - u0[0:-2])
summ = (u0[2:]+u0[0:-2])

#for i in range(N):
#	for j in range(H-1):
#		U[i][j] = Un[j] - umax*((Un[j+1] - Un[j-1])/(2*h))*(1 - ((Un[j-1]+Un[j+1])/pmax))*t[i]
##for i in range(N):
##    for j in range(H-1):
##        if(j!=0):
##            U[i][j] = ((Un[j-1]+Un[j+1])/2.0) - pmax*(diff[j-1]/(2*h))*(1 - (summ[j-1]/umax))*k
##            Un = U[i]
#plot(U.T)

ax.set_ylim([-1.5, 1.5])
line, = ax.plot(v,Un)

def animate(i):
#    temp1 = Un[1]
#    temp2 = Un[-2]
#    temp3 = Un[0]

    Un[1:-1] = ((1.0/2.0)*( Un[2:] + Un[0:-2] )) - ((a*k)/(2*h))*pmax*( 1 - (( Un[2:] + Un[0:-2] )/umax) )*( Un[2:] - Un[0:-2] )
#    Un[0] = ((1.0/2.0)*( temp1 + Un[-1] )) - ((a*k)/(2*h))*pmax*( 1 - (( temp1 + Un[-1] )/umax) )*( temp1 - Un[-1] )
#    Un[-1] = ((1.0/2.0)*( temp3 + temp2 )) - ((a*k)/(2*h))*pmax*( 1 - (( temp3 + temp2 )/umax) )*( temp3 - temp2 )
#    Un = u0
#    Un[:-1] = U[i][1:]
#    for j in  range(H-1):
#        Un[j] = U[i][j]
##    for j in range(H-1):
##        if(j!=0):
#            print i
##            Un[j] = (summ[j-1]/2.0) - pmax*(diff[j-1]/(2*h))*(1 - (summ[j-1]/umax))*i
#    diff = (Un[2:] - Un[0:-2])
#    summ = (Un[2:] + Un[0:-2])
#    Un[1:-1] = ((u0[0:-2]+u0[2:])/2.0)
#    Un[1:-1] = ((u0[0:-2]+u0[2:])/2.0) - pmax*((u0[2:] - u0[0:-2])/(2*h))*(1 - ((u0[0:-2]+u0[2:])/umax))*i*0.001
#    Un[0] = ((u0[-1]+u0[1])/2.0) - pmax*((u0[1] - u0[-1])/(2*h))*(1 - ((u0[-1]+u0[1])/umax))*i*0.001
#    Un[-1] = ((u0[-2]+u0[0])/2.0) - pmax*((u0[0] - u0[-2])/(2*h))*(1 - ((u0[-2]+u0[0])/umax))*i*0.001
##    for j in range(H-1):
##        Un[j] = u0[j] - umax*((u0[j+1] - u0[j-1])/(2*h))*(1 - ((u0[j-1]+u0[j+1])/pmax))*t[i]
#	Un = U[i][0:]
    line.set_ydata(Un)  # update the data
    return line,

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(ma.array(u0, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, t, init_func=init,
    interval=25, blit=True)

show()
