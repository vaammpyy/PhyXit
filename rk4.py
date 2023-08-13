import numpy as np
import matplotlib.pyplot as plt


s0_1 = np.array( [  0, 5 ] ) #initial conditions y = [ y, y' ]
s0_2 = np.array( [  0, 9 ] )

s0_3 = np.array( [  5, 5, 9 ] )


t = np.linspace(1,10 ,100) 

def deriv1(s, t, a, b, c): #define the derivative in coupled form
    #x = s[0]
    #vx = s[1]
    #z = y[2]
    x = s[0]
    y = s[1]
    z = s[2]
    #return np.array([ -y-z , x + a*x, b*z*(x-c) ])
    return np.array( [a*(y-x), x*(b-z)-y, x*y - c*z] )
    #return np.array([ vx, 0 ])

def deriv2(s, t, a, b, c): #define the derivative in coupled form
    y = s[0] #here a,b,c are dummy arguments
    vy = s[1] 
    #z = y[2]
    #return np.array([ -y-z , x + a*x, b*z*(x-c) ])
    return np.array([ vy, -9.8 ])

def rungekutta4(f, s0, t, args=()):
    N = len(t)
    s = np.zeros((N, len(s0)))
    s[0] = s0
    for i in range(N - 1):
        h = t[i+1] - t[i]
        k1 = f(s[i], t[i], *args)
        k2 = f(s[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(s[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(s[i] + k3 * h, t[i] + h, *args)
        s[i+1] = s[i] + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
    return s

#sol1 = rungekutta4(deriv1, s0_1, t, args=(1,2,3))
#sol2 = rungekutta4(deriv2, s0_2, t, args=(1,2,3))

sol3 = rungekutta4(deriv1, s0_3, t, args=(10,28,8.0/3))


fig = plt.figure()
ax = plt.axes(projection='3d')

#fig = plt.figure()

#plt.plot(sol1[:,0], sol2[:,0])
#plt.plot(t, sol3[:,0])
plt.plot(sol3[:,0], sol3[:,1],sol3[:,2])
plt.grid()
plt.show()
