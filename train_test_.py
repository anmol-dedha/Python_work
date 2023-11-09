# 80% for training and 20% for testing

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x=np.random.normal(3,1,100)
y=np.random.normal(150,40,100)/x

train_x=x[:80]
train_y=y[:80]

test_x=x[80:]
test_y=y[80:]

mymodel = np.poly1d(np.polyfit(train_x,train_y,4))
myline = np.linspace(0,6,100)

r2=r2_score(test_y,mymodel(test_x))

plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()

print(r2) #  r squared score to tell the strength of relationship between x axis and y axis

print(mymodel(5)) # use to predict new values through our model

