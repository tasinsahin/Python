from numpy import linspace, sin, exp, pi
import matplotlib.pyplot as mp
# calculate 500 values for x and y without a for loop
x = linspace(0, 10*pi, 500)
y = sin(x) * exp(-x/10)
# make diagram
mp.plot(x,y)
mp.show()
