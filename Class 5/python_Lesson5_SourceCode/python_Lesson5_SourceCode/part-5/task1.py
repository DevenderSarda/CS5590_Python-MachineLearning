import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])

xMean=x.mean()
yMean=y.mean()
print('mean X',xMean)
print('mean Y',yMean)

a=np.sum((x-xMean)*(y-yMean))
b=np.sum(np.power((x-xMean),2))
print('numerator for B1',a)
print('denominator for B2',b)

B1=a/b
print('B1 value',B1)

B0=yMean-(B1*xMean)
print('B0 value',B0)

print(np.mean(x)*np.mean(y))
plt.scatter(x,y)
Y=B0+(B1*x)
plt.plot(x,Y)
plt.show()