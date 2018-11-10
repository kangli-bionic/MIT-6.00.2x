"""PyLab samples."""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


plt.figure('linear')
plt.clf()
plt.plot(mySamples, myLinear)

plt.figure('quadratic')
plt.clf()
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.clf()
plt.plot(mySamples, myCubic)

plt.figure('exponential')
plt.clf()
plt.plot(mySamples, myExponential)

plt.figure('linear')
plt.title('Linear')

plt.figure('quadratic')
plt.title('Quadratic')

plt.figure('cubic')
plt.title('Cubic')

plt.figure('exponential')
plt.title('Exponential')

plt.show()
