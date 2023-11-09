# fitting the line as liner regresion model

import matplotlib.pyplot as plt
from scipy import stats

x = [1,2,3,5] # x-axis represent no. of car years 
y = [100,200,300,500] # y-axis represent car's speed

slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x + intercept
mymodel=list(map(myfunc,x))


plt.scatter(x, y)
plt.plot(x,mymodel)
plt.show()