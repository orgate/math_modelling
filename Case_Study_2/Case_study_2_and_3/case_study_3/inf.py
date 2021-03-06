from numpy import *
from matplotlib.pyplot import *

alf = 0.5	# the rate of antigen multiplication
p = 0.5		# the rate of contact between antigen and antibodies
bet = 0.5	# the rate of antibody production by plasma cell
gam = 2.	# amount of antibodies necessary for the neutralization of the antigens.
a = 0.5		# mean lifetime of antibodies
mu = 0.5	# mean lifetime of plasma cells
k = 0.5		# the coefficient of immune system response
sig = 0.5	# the rate of injury by antigen
eta = 0.5	# the rate of regeneration of the mass of the damaged organ
T = 10.		# time taken for antigens to show response and die
C0 = 0.5	# normal level of plasma cells

V = 0.1		# antigen count
F = bet*C0	# antibody count
C = C0		# plasma cells
m = 0.		# relative characteristic of the organ

dt = 0.01	# time step
t = arange(0,0.25,dt)

g = t*0		# describes dysfunction of immune system due to substantial organ damage
g[0:(len(t)/2)] = 1.
g[(len(t)/2):] = arange(1.,0.,-(2./len(t)))
Vt = t*0	# stores V for all t
Ft = t*0	# stores F for all t
Ct = t*0	# stores C for all t
mt = t*0	# stores m for all t

for i in range(len(t)):
	Vt[i] = V
	Ft[i] = F
	Ct[i] = C
	mt[i] = m
	V = V + dt*( alf*V - p*V*F )
	F = F + dt*( bet*C - gam*p*V*F - a*F )
	if(i>=T):
		C = C + dt*( -mu*(C-C0) + g[m]*k*Vt[i-T]*Ft[i-T] )
	else:
		C = C + dt*( -mu*(C-C0) )
	m = m + dt*( sig*V - eta*m )
	print "V is ",V, "	F is ",F, "	C is ",C,"	m is ",m

plot(Vt)
plot(Ft)
plot(Ct)
plot(mt)
#plot(g)
show()
