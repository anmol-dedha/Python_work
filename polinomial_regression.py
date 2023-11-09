import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
x=[1,2,3,4,5,6,7,8,9,10]
y=[100,90,80,60,55,60,65,70,70,75]

mymodel =np.poly1d(np.polyfit(x,y,3))
myline = np.linspace(1,10)

print(r2_score(y,mymodel(x)))
plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()