import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]         # x-axis represent no. of car years 
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]  # y-axis represent car's speed


slope,intercept,r,p,std_err=stats.linregress(x,y)

def myfunc(x):
    return slope*x + intercept
mymodel=list(map(myfunc,x))

prediction_1=myfunc(10)
print(prediction_1)
print(r)
'''
plt.scatter(x, y)
plt.plot(x,mymodel)
plt.show()
'''